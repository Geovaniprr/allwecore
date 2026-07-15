from flask import Blueprint

legal_bp = Blueprint("legal", __name__)

from app.blueprints.legal import routes  # noqa: E402,F401
