"""Envio de e-mail de notificação de lead (Gmail SMTP).

Falha de e-mail NUNCA quebra o formulário: o lead já foi gravado no CSV antes.
Se o SMTP não estiver configurado (sem senha de app), apenas registra aviso.
"""
import smtplib
import logging
from email.message import EmailMessage

from flask import current_app

logger = logging.getLogger(__name__)


def send_lead_email(lead):
    """Envia o lead para o e-mail configurado (LEAD_TO). Retorna True se enviou."""
    cfg = current_app.config
    user = cfg.get("SMTP_USER")
    password = cfg.get("SMTP_PASS")
    to_addr = cfg.get("LEAD_TO")

    if not (user and password and to_addr):
        logger.warning("SMTP não configurado — e-mail de lead não enviado (lead salvo no CSV).")
        return False

    msg = EmailMessage()
    msg["Subject"] = "Novo lead: {} — {}".format(lead["name"], lead.get("service") or "sem serviço")
    msg["From"] = user
    msg["To"] = to_addr
    # Permite responder direto ao cliente, se ele deixou um e-mail.
    if "@" in lead.get("contact", ""):
        msg["Reply-To"] = lead["contact"]

    msg.set_content(
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

    try:
        with smtplib.SMTP(cfg["SMTP_HOST"], cfg["SMTP_PORT"], timeout=15) as server:
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
        logger.info("E-mail de lead enviado para %s", to_addr)
        return True
    except Exception:
        logger.exception("Falha ao enviar e-mail de lead (lead permanece salvo no CSV).")
        return False
