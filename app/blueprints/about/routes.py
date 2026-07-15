from flask import render_template

from app.blueprints.about import about_bp
from app.services.catalog import VALUES


@about_bp.route("/")
def index():
    return render_template(
        "about/index.html",
        values=VALUES,
        meta={
            "title": "Sobre — All We Core",
            "description": (
                "Empresa de tecnologia que une software, IA, automações e marketing "
                "para transformar tecnologia em vantagem competitiva para o seu negócio."
            ),
        },
    )
