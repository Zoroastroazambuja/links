from pathlib import Path
import re
from datetime import date

DOMAIN = "https://www.capetaazul.com.br"

PAGES = [
    {
        "slug": "curso-colegio-naval",
        "title": "Curso de Matemática para Colégio Naval | Bruno Pedra",
        "h1": "Curso de Matemática para o Colégio Naval",
        "description": "Preparação completa de matemática para o Colégio Naval com teoria, exercícios, simulados e método de alto rendimento com Bruno Pedra.",
        "cta_text": "Quero conhecer o curso completo",
        "cta_link": "https://deusdamatematica.com.br/pt/cursos/curso-completo-para-colegio-naval-e-epcar",
        "sections": [
            ("O que você vai encontrar", [
                "Teoria completa e objetiva",
                "Questões selecionadas e comentadas",
                "Simulados para treinar no estilo da prova",
                "Método pensado para concursos militares",
                "Linha de estudo eficiente e organizada",
            ]),
            ("Para quem é este curso", "Para alunos que querem sair da base fraca, organizar o estudo e alcançar nível competitivo para o Colégio Naval."),
            ("Por que estudar com Bruno Pedra", "Bruno Pedra é professor, autor e especialista em matemática para concursos militares, com foco em desempenho real em prova."),
        ],
    },
    {
        "slug": "curso-epcar",
        "title": "Curso de Matemática para EPCAr | Bruno Pedra",
        "h1": "Curso de Matemática para EPCAr",
        "description": "Prepare-se para a EPCAr com um curso completo de matemática: teoria, exercícios, estratégia e treinamento direcionado.",
        "cta_text": "Quero acessar o curso da EPCAr",
        "cta_link": "https://deusdamatematica.com.br/pt/cursos/curso-completo-para-epcar",
        "sections": [
            ("Diferenciais do curso", [
                "Conteúdo estruturado por assunto",
                "Foco total na matemática cobrada na EPCAr",
                "Exercícios comentados",
                "Simulados para consolidar aprendizado",
                "Treinamento voltado para aprovação",
            ]),
            ("O objetivo", "Levar o aluno do estudo disperso para uma preparação consistente, com base sólida e rendimento crescente."),
        ],
    },
    {
        "slug": "capeta-azul",
        "title": "Capeta Azul: Tópicos de Álgebra Elementar | Bruno Pedra",
        "h1": "Capeta Azul: Tópicos de Álgebra Elementar",
        "description": "Conheça o Capeta Azul, o famoso livro Tópicos de Álgebra Elementar, referência para estudantes de concursos militares.",
        "cta_text": "Quero ver o livro",
        "cta_link": "https://www.mercadolivre.com.br/livro-topicos-de-algebra-elementar-capeta-azul-bruno-pedra/p/MLB67997287",
        "sections": [
            ("Por que o Capeta Azul se destaca", [
                "Conteúdo denso e bem selecionado",
                "Foco em desenvolvimento real do aluno",
                "Excelente para concursos militares e provas fortes",
                "Material reconhecido entre estudantes e professores",
            ]),
            ("Para quem é indicado", "Para alunos que querem sair do básico, ganhar profundidade em álgebra e ter contato com um material realmente forte."),
        ],
    },
    {
        "slug": "matematica-militar",
        "title": "Matemática para Concursos Militares | Bruno Pedra",
        "h1": "Matemática para Concursos Militares",
        "description": "Curso e materiais de matemática para Colégio Naval, EPCAr, AFA, EEAr, EsPCEx, EFOMM e outros concursos militares.",
        "cta_text": "Quero ver todos os cursos",
        "cta_link": "https://deusdamatematica.com.br/pt/cursos",
        "sections": [
            ("Concursos atendidos", [
                "Colégio Naval",
                "EPCAr",
                "AFA",
                "EEAr",
                "EsPCEx",
                "EFOMM",
                "Outras provas de alto nível",
            ]),
            ("Como funciona a preparação", "O estudo é organizado para atacar os temas essenciais, consolidar teoria e desenvolver segurança por meio da resolução de exercícios e simulados."),
        ],
    },
    {
        "slug": "simulados-matematica",
        "title": "Simulados de Matemática para Concursos Militares | Bruno Pedra",
        "h1": "Simulados de Matemática",
        "description": "Treine com simulados de matemática voltados para concursos militares e eleve seu nível de preparação.",
        "cta_text": "Quero acessar o banco de questões",
        "cta_link": "https://deusdamatematica.com.br/pt/comprar/plano/mensal-50pct-off-banco-10k-questoes",
        "sections": [
            ("Benefícios dos simulados", [
                "Treino de resistência e ritmo de prova",
                "Identificação de pontos fracos",
                "Melhora na administração do tempo",
                "Mais segurança no dia do concurso",
            ]),
            ("Por que isso importa", "Simulado é diagnóstico, ajuste de rota e preparação mental para a prova."),
        ],
    },
]


def read_root_index() -> str:
    path = Path("index.html")
    if not path.exists():
        raise FileNotFoundError("Não encontrei o arquivo index.html na raiz do repositório.")
    return path.read_text(encoding="utf-8")


def extract_style_block(html: str) -> str:
    match = re.search(r"(<style>.*?</style>)", html, flags=re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)
    return """
<style>
body{background:#080808;color:#F2EDE4;font-family:Georgia,serif;margin:0;padding:0}
.wrap{max-width:860px;margin:0 auto;padding:40px 20px}
h1,h2{font-family:Arial,sans-serif}
a{color:#C9A84C}
.card{background:#101010;border:1px solid rgba(201,168,76,.25);padding:24px;border-radius:8px}
.btn{display:inline-block;background:#C9A84C;color:#000;text-decoration:none;padding:14px 24px;border-radius:4px;font-weight:bold}
.topnav{margin-bottom:24px}
.topnav a{margin-right:14px;text-decoration:none}
ul{line-height:1.8}
p{line-height:1.8}
</style>
"""


def build_nav():
    links = ['<a href="/">Início</a>']
    for p in PAGES:
        links.append(f'<a href="/{p["slug"]}/">{p["h1"]}</a>')
    return '<div class="topnav">' + " | ".join(links) + "</div>"


def render_section(title, content):
    if isinstance(content, list):
        items = "\n".join(f"<li>{item}</li>" for item in content)
        body = f"<ul>{items}</ul>"
    else:
        body = f"<p>{content}</p>"
    return f"<section><h2>{title}</h2>{body}</section>"


def build_page_html(style_block: str, page: dict) -> str:
    sections_html = "\n".join(
        render_section(section_title, section_content)
        for section_title, section_content in page["sections"]
    )
    canonical = f"{DOMAIN}/{page['slug']}/"

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{page["title"]}</title>
<meta name="description" content="{page["description"]}"/>
<link rel="canonical" href="{canonical}"/>
{style_block}
</head>
<body>
  <div class="wrap">
    {build_nav()}
    <div class="card">
      <h1>{page["h1"]}</h1>
      <p>{page["description"]}</p>
      {sections_html}
      <p style="margin-top:28px;">
        <a class="btn" href="{page["cta_link"]}" target="_blank" rel="noopener noreferrer">{page["cta_text"]}</a>
      </p>
    </div>
  </div>
</body>
</html>
"""


def write_pages(style_block: str):
    for page in PAGES:
        folder = Path(page["slug"])
        folder.mkdir(parents=True, exist_ok=True)
        output = folder / "index.html"
        output.write_text(build_page_html(style_block, page), encoding="utf-8")
        print(f"OK: {output}")


def write_sitemap():
    today = date.today().isoformat()
    urls = [f"{DOMAIN}/"] + [f"{DOMAIN}/{p['slug']}/" for p in PAGES]

    body = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for url in urls:
        body.extend([
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{today}</lastmod>",
            "    <changefreq>weekly</changefreq>",
            "    <priority>0.8</priority>",
            "  </url>",
        ])

    body.append("</urlset>")
    Path("sitemap.xml").write_text("\n".join(body), encoding="utf-8")
    print("OK: sitemap.xml")


def write_robots():
    content = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    Path("robots.txt").write_text(content, encoding="utf-8")
    print("OK: robots.txt")


def main():
    root_html = read_root_index()
    style_block = extract_style_block(root_html)
    write_pages(style_block)
    write_sitemap()
    write_robots()
    print("\\nPronto. Agora faça commit e push para o GitHub.")


if __name__ == "__main__":
    main()
