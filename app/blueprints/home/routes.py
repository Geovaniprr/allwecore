from flask import render_template

from app.blueprints.home import home_bp
from app.services.catalog import SERVICES, PROCESS_STEPS, DIFFERENTIALS, FAQ, TESTIMONIALS


@home_bp.route("/")
def index():
    return render_template(
        "home/index.html",
        services=SERVICES,
        process=PROCESS_STEPS,
        differentials=DIFFERENTIALS,
        faq=FAQ,
        testimonials=TESTIMONIALS,
        meta={
            "title": "All We Core — Tecnologia e IA para sua empresa crescer",
            "description": (
                "Software, IA, automações, dashboards e marketing integrados para "
                "otimizar processos e gerar resultados reais. Fale com um especialista."
            ),
        },
    )
