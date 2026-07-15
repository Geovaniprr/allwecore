# All We Core — Site Institucional

Site institucional (MVP) construído em Flask, seguindo o PRD, SRS e Design System da pasta do projeto.

## Stack
- **Flask** (app factory + blueprints por página)
- **Flask-WTF** (formulário com CSRF + honeypot anti-spam)
- Front-end estático: HTML (Jinja) + CSS por camadas (tokens → base → layout → components → pages) + JS vanilla
- Fontes: Sora + Inter (marca) · JetBrains Mono (utilitário)

## Estrutura
```
app/
├── __init__.py        # application factory
├── config.py          # config por ambiente
├── blueprints/        # home, about, services, contact, legal, errors
├── services/          # catalog.py (conteúdo) + leads.py (persistência)
├── models/            # reservado p/ Fase 2 (CMS/CRM)
├── utils/             # seo.py
├── templates/         # base + partials + páginas
└── static/            # css/ js/ images/ icons/
```

## Rodar localmente
```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env       # e preencha SECRET_KEY etc.
python run.py
```
Acesse http://127.0.0.1:5000

## Onde editar
- **Conteúdo (serviços, FAQ, processo, valores):** `app/services/catalog.py` — fonte única de verdade.
- **Cores/tipografia/espaçamento:** `app/static/css/tokens.css` (derivado do manual de marca).
- **Leads:** `app/services/leads.py` — MVP grava em `leads.csv`; trocar por CRM/webhook na Fase 2.
- **Rastreamento (GA4/Pixel/GTM):** IDs via `.env`, injetados no `base.html`.

## Pendências antes do lançamento
- [ ] Substituir o símbolo placeholder (`partials/symbol.html`) pelo SVG oficial da marca.
- [ ] Adicionar `static/images/og-default.png` (preview de compartilhamento).
- [ ] Revisar textos legais (Privacidade/Termos) com jurídico.
- [ ] Preencher depoimentos reais em `catalog.py` (TESTIMONIALS).
- [ ] Configurar envio real de leads (e-mail/CRM) e carregamento condicional de GA4/Pixel após consentimento.
```
