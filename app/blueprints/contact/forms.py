"""Formulário de contato (RF-13/14/17)."""
import re

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Optional, ValidationError
from email_validator import validate_email, EmailNotValidError


class ContactForm(FlaskForm):
    name = StringField(
        "Nome",
        validators=[DataRequired("Informe seu nome."), Length(min=2, max=80)],
    )
    # Aceita e-mail OU WhatsApp num único campo, reduzindo atrito (RNF-07).
    contact = StringField(
        "E-mail ou WhatsApp",
        validators=[DataRequired("Informe um e-mail ou WhatsApp."), Length(max=120)],
    )
    service = SelectField("Serviço de interesse", validators=[Optional()])
    message = TextAreaField(
        "Mensagem",
        validators=[Optional(), Length(max=1000)],
    )
    # Honeypot invisível — deve permanecer vazio (bots costumam preencher).
    website = StringField("Não preencha este campo")

    def validate_contact(self, field):
        """Se for e-mail, valida formato + domínio (MX). Se for telefone, valida dígitos."""
        value = (field.data or "").strip()
        if "@" in value:
            try:
                # check_deliverability=True consulta o DNS (MX) do domínio.
                validate_email(value, check_deliverability=True)
            except EmailNotValidError:
                raise ValidationError(
                    "Esse e-mail não parece válido. Confira o endereço e tente de novo."
                )
        else:
            digits = re.sub(r"\D", "", value)
            if len(digits) < 10:
                raise ValidationError(
                    "Informe um e-mail válido ou um WhatsApp com DDD (ex.: 11 91234-5678)."
                )
