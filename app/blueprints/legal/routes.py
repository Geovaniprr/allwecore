from flask import render_template, Response, url_for, request

from app.blueprints.legal import legal_bp


@legal_bp.route("/politica-de-privacidade")
def privacy():
    return render_template(
        "legal/privacy.html",
        meta={"title": "Política de Privacidade — All We Core", "description": ""},
    )


@legal_bp.route("/termos-de-uso")
def terms():
    return render_template(
        "legal/terms.html",
        meta={"title": "Termos de Uso — All We Core", "description": ""},
    )


@legal_bp.route("/robots.txt")
def robots():
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {request.url_root.rstrip('/')}{url_for('legal.sitemap')}",
    ]
    return Response("\n".join(lines), mimetype="text/plain")


@legal_bp.route("/sitemap.xml")
def sitemap():
    from app.services.catalog import SERVICES

    urls = [
        url_for("home.index"),
        url_for("services.index"),
        url_for("about.index"),
        url_for("contact.index"),
        url_for("legal.privacy"),
        url_for("legal.terms"),
    ]
    urls += [url_for("services.detail", slug=s["slug"]) for s in SERVICES if s["has_page"]]

    root = request.url_root.rstrip("/")
    items = "".join(f"<url><loc>{root}{u}</loc></url>" for u in urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{items}</urlset>"
    )
    return Response(xml, mimetype="application/xml")
