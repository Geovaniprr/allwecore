from flask import render_template, abort

from app.blueprints.services import services_bp
from app.services.catalog import SERVICES, SERVICE_CATEGORIES, get_service


@services_bp.route("/")
def index():
    return render_template(
        "services/index.html",
        categories=SERVICE_CATEGORIES,
        services=SERVICES,
        meta={
            "title": "Serviços — All We Core",
            "description": (
                "IA, desenvolvimento de software, automações, BI, marketing e "
                "tráfego pago: soluções para empresas que querem crescer."
            ),
        },
    )


@services_bp.route("/<slug>")
def detail(slug):
    service = get_service(slug)
    if service is None or not service.get("has_page"):
        abort(404)
    return render_template(
        "services/detail.html",
        service=service,
        meta={
            "title": f"{service['name']} — All We Core",
            "description": service["short"],
        },
    )
