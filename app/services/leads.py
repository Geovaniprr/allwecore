"""Persistência de leads.

- Local: grava em CSV (abre no Excel) + log.
- Serverless (Vercel): não há disco persistente — o CSV é pulado e o lead
  fica registrado no log (recuperável) além do e-mail enviado pelo mailer.
"""
import csv
import os
import logging
from datetime import datetime, timezone

from flask import current_app

logger = logging.getLogger(__name__)

FIELDNAMES = ["timestamp", "name", "contact", "service", "message", "source"]

# Vercel/Lambda expõem esta variável e têm sistema de arquivos somente-leitura.
IS_SERVERLESS = bool(os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"))


def _append_csv(lead):
    path = current_app.config["LEADS_FILE"]
    write_header = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(lead)


def save_lead(name, contact, service, message, source="site"):
    """Registra um novo lead. Retorna o dicionário salvo."""
    lead = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "name": name.strip(),
        "contact": contact.strip(),
        "service": service or "",
        "message": (message or "").strip(),
        "source": source,
    }

    if not IS_SERVERLESS:
        try:
            _append_csv(lead)
        except OSError:
            # Nunca perder o lead: se o arquivo falhar, ao menos fica no log.
            logger.exception("Falha ao gravar lead em arquivo")

    # Sempre registra: é a rede de segurança quando não há disco (serverless).
    logger.info(
        "NOVO LEAD | nome=%s | contato=%s | servico=%s | origem=%s",
        lead["name"], lead["contact"], lead["service"], lead["source"],
    )
    return lead
