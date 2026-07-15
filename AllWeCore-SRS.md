# SRS — Software Requirements Specification
## Site Institucional All We Core

| Campo | Valor |
|-------|-------|
| Sistema | Site institucional All We Core (MVP) |
| Versão do documento | 1.0 |
| Data | 2026-07-03 |
| Padrão de referência | IEEE 830 (adaptado) |
| Status | Aprovado para desenvolvimento |

---

## 1. Introdução

### 1.1 Propósito
Este documento especifica os requisitos funcionais e não-funcionais do site institucional da All We Core (MVP), servindo de base para o desenvolvimento, testes e homologação.

### 1.2 Escopo
O sistema é um site institucional público, majoritariamente estático, com formulário de captação de leads e integrações de rastreamento e comunicação. Não contempla, nesta versão, área administrativa própria, autenticação, blog ou portal de cliente.

### 1.3 Definições e siglas
| Sigla | Significado |
|-------|-------------|
| MVP | Minimum Viable Product |
| CTA | Call to Action (chamada para ação) |
| GA4 | Google Analytics 4 |
| GTM | Google Tag Manager |
| LGPD | Lei Geral de Proteção de Dados |
| SEO | Search Engine Optimization |
| Lead | Contato comercial captado pelo site |
| SSG | Static Site Generation |
| CWV | Core Web Vitals |

### 1.4 Referências
- PRD — Site Institucional All We Core v1.0.
- Diretrizes LGPD (Lei nº 13.709/2018).
- Google Core Web Vitals.

---

## 2. Descrição geral

### 2.1 Perspectiva do produto
Aplicação web front-end, responsiva, servida preferencialmente como site estático (SSG) para máxima performance e SEO. Integra serviços de terceiros para envio de leads, analytics e comunicação. Não possui backend próprio de dados no MVP.

### 2.2 Funções principais
- Apresentação institucional e de serviços.
- Captação de leads via formulário e WhatsApp.
- Rastreamento de conversões (GA4, Meta Pixel).
- Conformidade LGPD (consentimento de cookies e páginas legais).

### 2.3 Perfis de usuário
| Perfil | Descrição | Acesso |
|--------|-----------|--------|
| Visitante | Potencial cliente navegando no site | Público |
| Time comercial All We Core | Recebe e trata os leads | Via e-mail/planilha externa (não no site) |

### 2.4 Restrições
- Sem autenticação/back-office no MVP.
- Dados de leads processados por serviços externos (não há banco de dados próprio).
- Deve operar sob HTTPS.

### 2.5 Premissas e dependências
- Serviço externo de envio de formulário disponível (endpoint de e-mail/planilha/automação).
- Contas GA4, GTM, Meta Business e WhatsApp Business ativas.
- Conteúdo e identidade visual fornecidos pela All We Core.

---

## 3. Requisitos funcionais

Convenção: **RF-xx** = requisito funcional.

### 3.1 Navegação e estrutura
- **RF-01** O sistema deve exibir um cabeçalho fixo com logotipo, menu de navegação e CTA de contato em todas as páginas.
- **RF-02** O sistema deve exibir um rodapé com links institucionais, legais, redes sociais e dados de contato em todas as páginas.
- **RF-03** O sistema deve prover as páginas: Home, Serviços, Página de serviço (2–3), Sobre, Contato, Política de Privacidade, Termos de Uso e 404.
- **RF-04** O sistema deve exibir a página 404 personalizada, com CTAs de retorno, para qualquer rota inexistente.

### 3.2 Home
- **RF-05** A Home deve conter as seções: Hero, prova de credibilidade, serviços, processo de trabalho, diferenciais, prova social, FAQ e CTA final.
- **RF-06** O Hero deve conter headline, subheadline, CTA primário ("Falar com especialista") e CTA secundário ("Ver serviços").
- **RF-07** A seção de serviços deve listar os 9 serviços com ícone, título e descrição curta, cada um com link para detalhe/seção.
- **RF-08** A seção de FAQ deve ser exibida em formato acordeão (expandir/recolher).

### 3.3 Serviços
- **RF-09** A página Serviços deve agrupar os 9 serviços em 3 categorias.
- **RF-10** Cada card de serviço deve direcionar à página de serviço correspondente ou à sua seção.

### 3.4 Página de serviço
- **RF-11** Cada página de serviço deve apresentar: problema resolvido, entrega da All We Core, benefícios/resultados, mini-processo, exemplos, FAQ específica e CTA.
- **RF-12** No MVP, apenas 2–3 páginas de serviço prioritárias devem existir.

### 3.5 Contato e captação de leads
- **RF-13** O sistema deve prover um formulário de contato com os campos: nome, e-mail e/ou WhatsApp, serviço de interesse e mensagem.
- **RF-14** O sistema deve validar os campos obrigatórios e o formato de e-mail/telefone antes do envio.
- **RF-15** Ao enviar, o sistema deve transmitir os dados a um serviço externo que os registre (e-mail e/ou planilha) e notifique o time comercial.
- **RF-16** O sistema deve exibir mensagem de sucesso após envio e mensagem de erro em caso de falha.
- **RF-17** O sistema deve aplicar mecanismo anti-spam (honeypot e/ou captcha invisível) no formulário.
- **RF-18** O sistema deve exibir um botão flutuante de WhatsApp em todas as páginas, abrindo conversa via link `wa.me` com mensagem pré-preenchida.
- **RF-19** O sistema deve disparar evento de conversão no GA4 e no Meta Pixel a cada envio de formulário bem-sucedido.

### 3.6 Conformidade e legal
- **RF-20** O sistema deve exibir um banner de consentimento de cookies no primeiro acesso, com opções de aceitar/recusar.
- **RF-21** Scripts de rastreamento (GA4, Pixel) só devem ser ativados após consentimento, quando aplicável.
- **RF-22** O sistema deve disponibilizar as páginas de Política de Privacidade e Termos de Uso, linkadas no rodapé e no banner de cookies.

### 3.7 Rastreamento e SEO
- **RF-23** O sistema deve integrar GA4 (via GTM, quando disponível) para métricas de navegação e conversão.
- **RF-24** O sistema deve integrar o Meta Pixel para rastreio de conversão e remarketing.
- **RF-25** Cada página deve possuir meta title, meta description e URL semântica próprias.
- **RF-26** O sistema deve gerar sitemap.xml e robots.txt.
- **RF-27** Cada página deve incluir metadados Open Graph (título, descrição, imagem) para compartilhamento.
- **RF-28** O sistema deve incluir dados estruturados (schema.org: Organization e Service).
- **RF-29 (condicional)** Caso haja endereço físico relevante, a página de Contato deve exibir Google Maps.

---

## 4. Requisitos não-funcionais

Convenção: **RNF-xx**.

### 4.1 Performance
- **RNF-01** LCP deve ser inferior a 2,5s em conexão 4G típica.
- **RNF-02** Todos os Core Web Vitals devem ficar na faixa "bom" (verde).
- **RNF-03** Imagens devem ser otimizadas (formatos modernos, lazy loading).
- **RNF-04** Scripts de terceiros devem ser carregados de forma assíncrona/diferida.

### 4.2 Usabilidade e responsividade
- **RNF-05** O layout deve ser responsivo mobile-first, funcionando de 320px a desktop.
- **RNF-06** CTAs devem estar sempre visíveis ou de fácil acesso em cada tela.
- **RNF-07** O formulário não deve exceder 4 campos no MVP.

### 4.3 Acessibilidade
- **RNF-08** Contraste de cores conforme WCAG AA.
- **RNF-09** Navegação completa por teclado.
- **RNF-10** Textos alternativos em imagens significativas e uma única H1 por página.

### 4.4 Segurança e privacidade
- **RNF-11** Todo o tráfego deve ocorrer sob HTTPS.
- **RNF-12** Dados do formulário devem trafegar de forma criptografada ao serviço externo.
- **RNF-13** O tratamento de dados pessoais deve estar em conformidade com a LGPD.

### 4.5 Compatibilidade
- **RNF-14** Suporte às versões atuais de Chrome, Edge, Firefox e Safari (desktop e mobile).

### 4.6 Manutenibilidade e escalabilidade
- **RNF-15** Conteúdo textual deve ser separado da estrutura de código para edição facilitada.
- **RNF-16** A arquitetura deve permitir adicionar novas páginas de serviço e integrar um CMS headless futuramente sem retrabalho estrutural.
- **RNF-17** O código deve seguir padrão consistente e ser versionado.

### 4.7 Disponibilidade
- **RNF-18** O site deve ter disponibilidade ≥ 99,9% (hospedagem estática/CDN).

---

## 5. Interfaces externas

### 5.1 Integrações
| Integração | Finalidade | Requisito relacionado |
|------------|-----------|-----------------------|
| Serviço de formulário (e-mail/planilha/automação) | Registro e notificação de leads | RF-15 |
| Google Analytics 4 | Métricas e conversões | RF-23 |
| Google Tag Manager | Gestão de tags | RF-23 |
| Meta Pixel | Conversão e remarketing | RF-24 |
| WhatsApp (wa.me) | Contato direto | RF-18 |
| Google Maps (condicional) | Localização | RF-29 |

### 5.2 Interfaces de usuário
- Interface web responsiva conforme identidade visual premium da All We Core.

### 5.3 Interfaces de hardware/software
- Navegadores modernos; hospedagem estática com CDN e HTTPS.

---

## 6. Modelo de dados (MVP)

O MVP não possui banco de dados próprio. O único dado transacionado é a submissão do formulário:

| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| nome | texto | Sim |
| email | e-mail | Condicional (e-mail ou WhatsApp) |
| whatsapp | telefone | Condicional |
| servico_interesse | seleção | Não |
| mensagem | texto longo | Não |
| origem/UTM | texto | Não (capturado automaticamente) |
| timestamp | data/hora | Sim (gerado) |

---

## 7. Critérios de aceitação (resumo)
- Todas as páginas RF-03 acessíveis e responsivas.
- Formulário envia, registra, notifica e dispara eventos de conversão (RF-13 a RF-19).
- Botão de WhatsApp funcional em todas as páginas (RF-18).
- Banner de cookies e páginas legais presentes e funcionais (RF-20 a RF-22).
- GA4 e Meta Pixel registrando dados (RF-23, RF-24).
- Metadados de SEO e Open Graph presentes em todas as páginas (RF-25 a RF-28).
- Core Web Vitals verdes e LCP < 2,5s (RNF-01, RNF-02).
- HTTPS ativo e conformidade LGPD (RNF-11 a RNF-13).

---

## 8. Rastreabilidade (PRD → SRS)
| Item PRD | Requisitos SRS |
|----------|----------------|
| Telas T-1 a T-9 | RF-03 a RF-12, RF-22 |
| F-1 Formulário | RF-13 a RF-17, RF-19 |
| F-2 WhatsApp | RF-18 |
| F-3 GA4 / F-4 Pixel | RF-19, RF-23, RF-24 |
| F-5 SEO | RF-25 a RF-28 |
| F-6 Cookies / LGPD | RF-20 a RF-22, RNF-13 |
| F-7 Open Graph | RF-27 |
| F-8 Notificação de lead | RF-15 |
| F-9 Anti-spam | RF-17 |
| RNF (performance/SEO/etc.) | RNF-01 a RNF-18 |
