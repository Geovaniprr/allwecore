from flask import render_template, redirect, url_for, flash, request

from app.blueprints.contact import contact_bp
from app.blueprints.contact.forms import ContactForm
from app.services.leads import save_lead
from app.services.mailer import send_lead_email
from app.services.catalog import SERVICES


@contact_bp.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()
    # Popula o select de serviços a partir do catálogo (fonte única de verdade).
    form.service.choices = [("", "Selecione um serviço")] + [
        (s["slug"], s["name"]) for s in SERVICES
    ]

    if form.validate_on_submit():
        # Honeypot (RF-17): campo oculto preenchido = bot -> descarta silenciosamente.
        if form.website.data:
            return redirect(url_for("contact.success"))

        lead = save_lead(
            name=form.name.data,
            contact=form.contact.data,
            service=form.service.data,
            message=form.message.data,
            source=request.args.get("utm_source", "site"),
        )
        send_lead_email(lead)   # notifica por e-mail; se falhar, o lead já está no CSV
        return redirect(url_for("contact.success"))

    return render_template(
        "contact/index.html",
        form=form,
        meta={
            "title": "Contato — All We Core",
            "description": "Fale com um especialista da All We Core e receba um diagnóstico gratuito do seu negócio.",
        },
    )


@contact_bp.route("/sucesso")
def success():
    return render_template(
        "contact/success.html",
        meta={"title": "Mensagem enviada — All We Core", "description": ""},
    )
