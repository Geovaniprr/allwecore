"""Helpers de SEO (dados estruturados — SRS RF-28)."""
import json


def organization_schema(brand, base_url=""):
    """Retorna o JSON-LD schema.org/Organization como string pronta p/ template."""
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": brand["name"],
        "slogan": brand["tagline"],
        "url": base_url or None,
        "email": brand["email"],
        "sameAs": [],
    }
    data = {k: v for k, v in data.items() if v is not None}
    return json.dumps(data, ensure_ascii=False)
