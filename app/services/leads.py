"""Persistência de leads.

MVP: grava em CSV local + registra no log (PRD: sem painel admin próprio).
Fase 2: trocar `save_lead` por envio a serviço externo / CRM (webhook, e-mail).
A interface pública (`save_lead`) permanece a mesma — os templates/rotas não mudam.
"""
import csv
import logging
from datetime import datetime, timezone

from flask import current_app

logger = logging.getLogger(__name__)

FIELDNAMES = ["timestamp", "name", "contact", "service", "message", "source"]


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

    path = current_app.config["LEADS_FILE"]
    write_header = not path.exists()
    try:
        with open(path, "a", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
            if write_header:
                writer.writeheader()
            writer.writerow(lead)
    except OSError:
        # Nunca perder o lead: se o arquivo falhar, ao menos fica no log.
        logger.exception("Falha ao gravar lead em arquivo")

    logger.info("Novo lead recebido: %s (%s)", lead["name"], lead["contact"])
    # TODO(Fase 2): notificar o time (e-mail/WhatsApp) e enviar ao CRM.
    return lead
