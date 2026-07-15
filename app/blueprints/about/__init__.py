from flask import Blueprint

about_bp = Blueprint("about", __name__, url_prefix="/sobre")

from app.blueprints.about import routes  # noqa: E402,F401
