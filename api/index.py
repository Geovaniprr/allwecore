"""Ponto de entrada para a Vercel (Python Serverless Function).

A Vercel procura um objeto WSGI chamado `app` neste arquivo.
Todo o tráfego é roteado para cá pelo vercel.json.
"""
import sys
from pathlib import Path

# Garante que a raiz do projeto está no path para importar o pacote `app`.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402

app = create_app()
