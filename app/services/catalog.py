"""Conteúdo estruturado do site (fonte única de verdade).

No MVP o conteúdo vive em Python — simples, versionável e rápido (sem banco).
Na Fase 2 pode migrar para um CMS headless sem alterar os templates.
"""

# --- Categorias (Design System: 3 grupos para não parecer genérico) ---
SERVICE_CATEGORIES = [
    {"key": "build", "title": "Construção Digital"},
    {"key": "data", "title": "Inteligência & Dados"},
    {"key": "growth", "title": "Crescimento"},
]

# has_page=True -> possui página individual no MVP (2–3 prioritárias / PRD RF-12).
SERVICES = [
    {
        "slug": "desenvolvimento-de-software",
        "name": "Desenvolvimento de Software",
        "icon": "code",
        "category": "build",
        "short": "Sistemas sob medida, escaláveis e seguros — feitos para o jeito que a sua empresa trabalha.",
        "has_page": True,
    },
    {
        "slug": "desenvolvimento-de-sites",
        "name": "Desenvolvimento de Sites",
        "icon": "browser",
        "category": "build",
        "short": "Sites rápidos, modernos e otimizados para transformar visitantes em clientes.",
        "has_page": False,
    },
    {
        "slug": "integracoes",
        "name": "Integrações entre Sistemas",
        "icon": "nodes",
        "category": "build",
        "short": "Conecte seus sistemas, elimine trabalho manual e acabe com o retrabalho.",
        "has_page": False,
    },
    {
        "slug": "inteligencia-artificial",
        "name": "Inteligência Artificial",
        "icon": "ai",
        "category": "data",
        "short": "Inteligência artificial aplicada ao seu negócio para automatizar tarefas e decidir melhor.",
        "has_page": True,
    },
    {
        "slug": "automacoes",
        "name": "Automações",
        "icon": "automation",
        "category": "data",
        "short": "Automatize tarefas repetitivas e libere seu time para o que realmente gera valor.",
        "has_page": False,
    },
    {
        "slug": "dashboards-bi",
        "name": "Dashboards & BI",
        "icon": "chart",
        "category": "data",
        "short": "Seus dados reunidos em painéis claros e em tempo real, para decidir com segurança.",
        "has_page": False,
    },
    {
        "slug": "trafego-pago",
        "name": "Tráfego Pago",
        "icon": "target",
        "category": "growth",
        "short": "Campanhas orientadas a ROI para atrair os clientes certos e vender mais.",
        "has_page": True,
    },
    {
        "slug": "marketing-digital",
        "name": "Marketing Digital",
        "icon": "megaphone",
        "category": "growth",
        "short": "Presença digital estratégica para atrair, engajar e converter o público certo.",
        "has_page": False,
    },
    {
        "slug": "consultoria-estrategica",
        "name": "Consultoria Estratégica",
        "icon": "compass",
        "category": "growth",
        "short": "Direção clara para transformar tecnologia em vantagem competitiva real.",
        "has_page": False,
    },
]

PROCESS_STEPS = [
    {"n": "01", "title": "Diagnóstico", "text": "Mergulhamos no seu negócio para entender o problema real — não só o aparente."},
    {"n": "02", "title": "Proposta", "text": "Você recebe um plano claro: escopo, prazo e o resultado que vamos entregar."},
    {"n": "03", "title": "Execução", "text": "Construímos com tecnologia de ponta, agilidade e total transparência."},
    {"n": "04", "title": "Resultado", "text": "Entregamos, medimos o impacto e evoluímos com base em dados."},
]

DIFFERENTIALS = [
    {"icon": "target", "title": "Tecnologia com propósito", "text": "Cada solução mira um resultado de negócio — não entrega técnica pela metade."},
    {"icon": "layers", "title": "Estratégia + execução", "text": "Do plano à implementação, sem terceirizar o que importa."},
    {"icon": "nodes", "title": "Conexão que gera resultado", "text": "Tecnologia, dados e marketing trabalhando juntos, em um só time."},
    {"icon": "people", "title": "Parceria de verdade", "text": "Comunicação clara e acompanhamento próximo, do início ao resultado."},
]

VALUES = [
    {"icon": "bulb", "title": "Inovadora", "text": "Buscamos sempre a melhor tecnologia para o problema certo — não a mais chamativa."},
    {"icon": "target", "title": "Estratégica", "text": "Pensamos no resultado de negócio antes de escrever a primeira linha de código."},
    {"icon": "shield", "title": "Confiável", "text": "Transparência e compromisso do primeiro contato à entrega final."},
    {"icon": "nodes", "title": "Conectada", "text": "Unimos áreas, sistemas e pessoas em torno de um mesmo objetivo."},
    {"icon": "people", "title": "Acessível", "text": "Tecnologia de ponta explicada em linguagem simples, sem jargão."},
]

FAQ = [
    {"q": "Como funciona o orçamento?", "a": "Começa com um diagnóstico gratuito. A partir dele, você recebe uma proposta transparente com escopo, prazo e investimento — sem surpresas depois."},
    {"q": "Qual o prazo de um projeto?", "a": "Depende do escopo. Após o diagnóstico, apresentamos um cronograma realista antes de qualquer início — você sempre sabe o que esperar."},
    {"q": "Preciso entender de tecnologia para trabalhar com vocês?", "a": "Não. Traduzimos tudo em linguagem simples e cuidamos da parte técnica por você — do começo ao fim."},
    {"q": "Vocês atendem empresas de qualquer segmento?", "a": "Sim. Adaptamos cada solução ao contexto, ao tamanho e ao momento do seu negócio."},
    {"q": "Como é o suporte depois da entrega?", "a": "Continuamos ao seu lado. Oferecemos acompanhamento e evolução contínua conforme a necessidade do projeto."},
]

TESTIMONIALS = [
    # Preencher com depoimentos reais (prova social — Design System / PRD).
    # {"name": "", "role": "", "company": "", "text": ""},
]


def get_service(slug):
    return next((s for s in SERVICES if s["slug"] == slug), None)


def services_by_category(key):
    return [s for s in SERVICES if s["category"] == key]
