#!/usr/bin/env python3
"""Validate the hand-maintained static site.

This filename is kept for compatibility with the existing manual GitHub Actions
workflow. The site is no longer generated from an embedded HTML snapshot: the
HTML, CSS and sitemap in the repository are the source of truth.
"""

from __future__ import annotations

import sys
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = (
    "index.html",
    "capeta-azul/index.html",
    "consultor.html",
    "curso-colegio-naval/index.html",
    "curso-colegio-naval/styles.css",
    "escola-naval/index.html",
    "sitemap.xml",
)

PUBLIC_HTML = (
    "index.html",
    "capeta-azul/index.html",
    "capeta-azul/Consultor.html",
    "capetaazul.com.br/consultor.html",
    "consultor.html",
    "curso-colegio-naval/index.html",
)

STALE_COPY = (
    "curso-completo-para-colegio-naval-e-epcar",
    "+1000 aprovados",
    "100% risco zero",
    "garantia incondicional",
    "sem perguntas",
    "12 medalhas internacionais",
    "focado exclusivamente no epcar",
)


def fail(message: str) -> None:
    print(f"ERRO: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        fail("arquivos obrigatórios ausentes: " + ", ".join(missing))


def validate_sitemap() -> None:
    try:
        ElementTree.parse(ROOT / "sitemap.xml")
    except ElementTree.ParseError as exc:
        fail(f"sitemap.xml inválido: {exc}")


def validate_copy() -> None:
    for relative_path in PUBLIC_HTML:
        text = (ROOT / relative_path).read_text(encoding="utf-8").casefold()
        for stale_text in STALE_COPY:
            if stale_text in text:
                fail(f"copy obsoleta em {relative_path}: {stale_text!r}")


def validate_college_naval_landing() -> None:
    landing = (ROOT / "curso-colegio-naval/index.html").read_text(encoding="utf-8")
    required_markers = (
        'role="tablist"',
        'role="tabpanel"',
        "matematica-cnepcar-topicos-de-algebra-topicos-de-geometria-resolvidos",
        "solucionario-capeta-azul",
        "utm_content",
    )
    missing = [marker for marker in required_markers if marker not in landing]
    if missing:
        fail("landing do Colégio Naval incompleta: " + ", ".join(missing))


def main() -> None:
    validate_required_files()
    validate_sitemap()
    validate_copy()
    validate_college_naval_landing()
    print("Site estático validado; nenhum arquivo foi gerado ou publicado.")


if __name__ == "__main__":
    main()
