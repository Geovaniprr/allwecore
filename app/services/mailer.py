"""Envio de e-mail de notificação de lead.

Estratégia (nesta ordem):
  1. Resend (API HTTP) — usado em produção/serverless (Vercel). Confiável e rápido.
  2. Gmail SMTP — fallback para desenvolvimento local.
  3. Só log — se nada estiver configurado.

Falha de e-mail NUNCA quebra o formulário: a rota já respondeu ao usuário e o
lead é sempre registrado no log (recuperável), além do CSV quando há disco.
"""
import json
import smtplib
import logging
import urllib.request
import urllib.error
from email.message import EmailMessage

from flask import current_app

logger = logging.getLogger(__name__)

RESEND_ENDPOINT = "https://api.resend.com/emails"


def _subject(lead):
    return "Novo lead: {} — {}".format(lead["name"], lead.get("service") or "sem serviço")


def _body(lead):
    return (
        "Novo contato pelo site All We Core\n\n"
        "Nome: {name}\n"
        "E-mail/WhatsApp: {contact}\n"
        "Serviço de interesse: {service}\n"
        "Mensagem:\n{message}\n\n"
        "Recebido em: {timestamp}\n"
        "Origem: {source}\n".format(
            name=lead["name"],
            contact=lead["contact"],
            service=lead.get("service") or "-",
            message=lead.get("message") or "-",
            timestamp=lead.get("timestamp", "-"),
            source=lead.get("source", "site"),
        )
    )


def _send_via_resend(lead, cfg):
    payload = {
        "from": cfg["LEAD_FROM"],
        "to": [cfg["LEAD_TO"]],
        "subject": _subject(lead),
        "text": _body(lead),
    }
    # Permite responder direto ao cliente, se ele deixou um e-mail.
    if "@" in lead.get("contact", ""):
        payload["reply_to"] = lead["contact"]

    req = urllib.request.Request(
        RESEND_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + cfg["RESEND_API_KEY"],
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        if 200 <= resp.status < 300:
            logger.info("Lead enviado via Resend para %s", cfg["LEAD_TO"])
            return True
    return False


def _send_via_smtp(lead, cfg):
    msg = EmailMessage()
    msg["Subject"] = _subject(lead)
    msg["From"] = cfg["SMTP_USER"]
    msg["To"] = cfg["LEAD_TO"]
    if "@" in lead.get("contact", ""):
        msg["Reply-To"] = lead["contact"]
    msg.set_content(_body(lead))

    with smtplib.SMTP(cfg["SMTP_HOST"], cfg["SMTP_PORT"], timeout=15) as server:
        server.starttls()
        server.login(cfg["SMTP_USER"], cfg["SMTP_PASS"])
        server.send_message(msg)
    logger.info("Lead enviado via SMTP para %s", cfg["LEAD_TO"])
    return True


def send_lead_email(lead):
    """Envia o lead para o e-mail configurado. Retorna True se enviou."""
    cfg = current_app.config
    to_addr = cfg.get("LEAD_TO")

    if not to_addr:
        logger.warning("LEAD_TO não configurado — e-mail não enviado.")
        return False

    try:
        if cfg.get("RESEND_API_KEY"):
            return _send_via_resend(lead, cfg)
        if cfg.get("SMTP_USER") and cfg.get("SMTP_PASS"):
            return _send_via_smtp(lead, cfg)
        logger.warning("Nenhum provedor de e-mail configurado (Resend/SMTP).")
        return False
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        logger.error("Resend recusou o envio (%s): %s", e.code, detail)
    except Exception:
        logger.exception("Falha ao enviar e-mail de lead.")

    # Rede de segurança: o lead nunca se perde — fica registrado no log.
    logger.error("LEAD NÃO ENVIADO POR E-MAIL — dados: %s", json.dumps(lead, ensure_ascii=False))
    return False
