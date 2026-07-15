"""Application factory da All We Core."""
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

# Carrega o .env ANTES de importar a config (a classe Config lê as variáveis
# de ambiente no momento do import; sem isso, os valores do .env são ignorados).
load_dotenv()

from app.config import get_config  # noqa: E402

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    csrf.init_app(app)

    register_blueprints(app)
    register_error_handlers(app)
    register_context(app)

    return app


def register_blueprints(app):
    from app.blueprints.home import home_bp
    from app.blueprints.about import about_bp
    from app.blueprints.services import services_bp
    from app.blueprints.contact import contact_bp
    from app.blueprints.legal import legal_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(legal_bp)


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("errors/500.html"), 500


def register_context(app):
    """Injeta variáveis globais em todos os templates."""

    @app.context_processor
    def inject_globals():
        from datetime import datetime
        return {
            "brand": {
                "name": "All We Core",
                "tagline": "Tecnologia, IA e Marketing para impulsionar negócios.",
                "whatsapp": app.config["WHATSAPP_NUMBER"],
                "email": app.config["CONTACT_EMAIL"],
            },
            "tracking": {
                "ga4": app.config["GA4_ID"],
                "pixel": app.config["META_PIXEL_ID"],
                "gtm": app.config["GTM_ID"],
            },
            "current_year": datetime.now().year,
        }
