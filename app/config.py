"""Configuração da aplicação por ambiente."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """Configuração base compartilhada."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-insecure-change-me")

    # Marca / contato
    WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER", "5583900000000")
    CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "allwecore@gmail.com")

    # Rastreamento (injetado nos templates)
    GA4_ID = os.environ.get("GA4_ID", "")
    META_PIXEL_ID = os.environ.get("META_PIXEL_ID", "")
    GTM_ID = os.environ.get("GTM_ID", "")

    # Leads (MVP: CSV local — mantido como backup mesmo com e-mail)
    LEADS_FILE = BASE_DIR / os.environ.get("LEADS_FILE", "leads.csv")

    # Destino dos leads
    LEAD_TO = os.environ.get("LEAD_TO", "allwecore@gmail.com")

    # Envio via Resend (API HTTP) — usado em produção/serverless. Tem prioridade.
    RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
    LEAD_FROM = os.environ.get("LEAD_FROM", "All We Core <onboarding@resend.dev>")

    # Envio via Gmail SMTP — fallback para desenvolvimento local.
    SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
    SMTP_USER = os.environ.get("SMTP_USER", "")            # ex.: allwecore@gmail.com
    SMTP_PASS = os.environ.get("SMTP_PASS", "")            # senha de app do Gmail (16 dígitos)

    WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}


def get_config():
    env = os.environ.get("FLASK_ENV", "development")
    return config_by_name.get(env, DevelopmentConfig)
