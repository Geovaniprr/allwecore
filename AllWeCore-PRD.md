# PRD — Product Requirements Document
## Site Institucional All We Core

| Campo | Valor |
|-------|-------|
| Produto | Site institucional All We Core (MVP) |
| Versão do documento | 1.0 |
| Data | 2026-07-03 |
| Autor | Product Management |
| Status | Aprovado para desenvolvimento |
| Fase alvo | Fase 1 (MVP) |

---

## 1. Visão geral do produto

### 1.1 Resumo
O site institucional da All We Core é a principal ferramenta comercial da empresa. Seu papel é gerar **autoridade**, **captar leads** e **converter visitantes em clientes**, transmitindo uma imagem moderna, premium, confiável e altamente tecnológica.

A All We Core é uma empresa nova que ajuda outras empresas a crescer através da tecnologia, com serviços de: Inteligência Artificial, Desenvolvimento de Software, Automações, Dashboards & BI, Marketing Digital, Tráfego Pago, Desenvolvimento de Sites, Consultoria Estratégica e Integrações entre sistemas.

### 1.2 Problema que o produto resolve
- A empresa não tem presença digital nem prova de credibilidade online.
- Não há canal estruturado para captar e qualificar leads.
- Não há ativo comercial para sustentar campanhas de tráfego pago e SEO.

### 1.3 Proposta de valor
Um site enxuto, rápido, de alto impacto visual, que comunica a oferta em segundos e conduz o visitante à conversão pelo canal de sua preferência (WhatsApp ou formulário).

### 1.4 Princípios de produto
1. Simplicidade acima de completude — nada entra sem justificativa de valor.
2. Toda tela tem um caminho claro para a conversão.
3. Conteúdo concreto, não clichê.
4. Performance e SEO como requisitos de primeira classe.
5. Escalável: fácil adicionar páginas e um CMS no futuro sem retrabalho.

---

## 2. Objetivos e métricas de sucesso

### 2.1 Objetivos de negócio
| ID | Objetivo |
|----|----------|
| OBJ-1 | Estabelecer presença digital profissional e premium. |
| OBJ-2 | Gerar leads qualificados de forma contínua. |
| OBJ-3 | Servir como destino de campanhas de tráfego pago. |
| OBJ-4 | Construir base de SEO orgânico de longo prazo. |

### 2.2 Métricas (KPIs)
| Métrica | Meta inicial de referência |
|---------|----------------------------|
| Taxa de conversão de visitante em lead | ≥ 2–4% |
| Tempo de carregamento (LCP) | < 2,5s |
| Core Web Vitals | Todos "verdes" |
| Leads/mês | Crescente mês a mês |
| Taxa de rejeição da Home | < 55% |
| Origem dos leads rastreada | 100% (GA4 + Pixel) |

### 2.3 Não-objetivos (fora de escopo do MVP)
- Blog / produção de conteúdo recorrente.
- Área de cliente / portal / login de terceiros.
- Painel administrativo próprio.
- Página de preços pública.
- E-commerce ou pagamentos.
- Multilíngue.

---

## 3. Público-alvo e personas

### 3.1 Persona primária — "Decisor Ocupado"
- Dono de empresa ou gestor (marketing, operações, TI).
- Busca um parceiro de tecnologia confiável.
- Chega por anúncio, indicação ou busca no Google.
- Decide rápido, majoritariamente pelo celular.
- Objeção principal: "posso confiar meu dinheiro/projeto a uma empresa nova?"

### 3.2 Persona secundária — "Pesquisador Técnico"
- Analista/gestor comparando fornecedores.
- Quer detalhe de serviço, processo e prova de resultado.
- Alta intenção; converte via formulário.

---

## 4. Escopo funcional (Fase 1 — MVP)

### 4.1 Telas incluídas
| ID | Tela | Prioridade |
|----|------|-----------|
| T-1 | Home (landing longa) | Must |
| T-2 | Serviços (visão geral, 9 serviços agrupados) | Must |
| T-3 | Página individual de serviço (2–3 prioritárias) | Must |
| T-4 | Sobre | Must |
| T-5 | Contato | Must |
| T-6 | FAQ (seção na Home e serviços) | Must |
| T-7 | Política de Privacidade | Must |
| T-8 | Termos de Uso | Should |
| T-9 | Página 404 | Must |

### 4.2 Funcionalidades incluídas
| ID | Funcionalidade | Prioridade | Justificativa |
|----|----------------|-----------|---------------|
| F-1 | Formulário de contato | Must | Principal captação de lead. |
| F-2 | Botão flutuante de WhatsApp | Must | Canal preferido no Brasil; reduz atrito. |
| F-3 | Google Analytics 4 | Must | Medir para otimizar investimento. |
| F-4 | Meta Pixel | Must | Rastreio de conversão e remarketing para tráfego pago. |
| F-5 | SEO on-page + técnico | Must | Tráfego orgânico sustentável. |
| F-6 | Banner de consentimento de cookies (LGPD) | Must | Conformidade legal. |
| F-7 | Open Graph / preview de links | Must | Credibilidade ao compartilhar. |
| F-8 | Notificação de novo lead (e-mail/planilha) | Must | Operação de vendas sem painel próprio. |
| F-9 | Anti-spam no formulário (honeypot/captcha invisível) | Must | Qualidade dos leads. |
| F-10 | Google Tag Manager | Should | Gestão de tags sem alterar código. |
| F-11 | Google Maps | Could (condicional) | Só se houver endereço relevante. |

### 4.3 Fora do MVP (fases futuras)
- Painel administrativo / CMS headless → Fase 2 (se necessário).
- Página de Cases dedicada → Fase 2.
- Blog + Newsletter → Fase 3.
- Portal do cliente, multilíngue, CRM próprio → Fase 4.

---

## 5. Requisitos funcionais por tela

### 5.1 Home (T-1)
- **Objetivo:** comunicar valor em segundos e conduzir à conversão.
- **Seções:** Hero (headline, subheadline, CTA primário/secundário) → Prova de credibilidade → Serviços (grid) → Como trabalhamos (processo 3–4 passos) → Diferenciais → Prova social → FAQ → CTA final → Rodapé.
- **Ações:** CTAs, navegar para serviços, abrir WhatsApp, enviar formulário, expandir FAQ.
- **Contribuição para conversão:** concentra a jornada inteira; destino ideal para tráfego pago.

### 5.2 Serviços (T-2)
- Introdução + 9 serviços agrupados em 3 categorias (Construção Digital / Inteligência & Dados / Crescimento).
- Cada card leva ao detalhe ou seção. CTA de contato ao final.

### 5.3 Página de serviço (T-3)
- Problema que resolve, como a All We Core entrega, benefícios/resultados, mini-processo, exemplos, FAQ específica, CTA.
- MVP: 2–3 serviços prioritários (ex.: Desenvolvimento de Software, IA/Automações, Tráfego Pago).

### 5.4 Sobre (T-4)
- Propósito/missão, história curta e honesta, valores, diferenciais, time/stack.
- Reduz risco percebido de contratar empresa nova.

### 5.5 Contato (T-5)
- Formulário curto (nome, e-mail/WhatsApp, serviço de interesse, mensagem), canais diretos, horário.
- Múltiplos canais respeitam preferência do usuário.

### 5.6 FAQ (T-6)
- Prazos, orçamento, forma de trabalho, tecnologias, suporte. Remove objeções silenciosas.

### 5.7 Legais (T-7, T-8) e 404 (T-9)
- Privacidade e Termos: conformidade e profissionalismo.
- 404: mensagem na identidade da marca + CTAs de retorno.

---

## 6. Jornada do usuário
1. Chegada (Hero) → entende o quê/para quem em ~5s.
2. Interesse → reconhece o próprio problema nos serviços.
3. Confiança → processo + diferenciais + prova social.
4. Aprofundamento → página de serviço específica.
5. Objeções → FAQ.
6. Conversão → WhatsApp ou formulário.
7. Pós-clique → lead notificado + registrado; GA4/Pixel registram conversão.
8. Retorno → remarketing reimpacta quem não converteu.

---

## 7. Requisitos não-funcionais
| Categoria | Requisito |
|-----------|-----------|
| Performance | LCP < 2,5s; Core Web Vitals verdes; site majoritariamente estático. |
| Responsividade | Mobile-first. |
| SEO | Meta tags por página, dados estruturados, sitemap, robots.txt, 1 H1/página. |
| Acessibilidade | Contraste, navegação por teclado, textos alternativos. |
| Segurança/LGPD | HTTPS, consentimento de cookies, anti-spam. |
| Manutenibilidade | Conteúdo separado da estrutura. |
| Escalabilidade | Arquitetura pronta para novas páginas e CMS futuro. |

---

## 8. Roadmap
- **Fase 1 (MVP):** telas T-1 a T-9 + funcionalidades F-1 a F-9 (F-10/F-11 conforme necessidade).
- **Fase 2:** páginas de serviço restantes, Cases, GTM, testes A/B, CMS headless simples se necessário.
- **Fase 3:** Blog, Newsletter, materiais ricos, automação de marketing/CRM.
- **Fase 4:** portal do cliente, multilíngue, CRM próprio, personalização.

---

## 9. Dependências e premissas
- Domínio, hospedagem e conta de e-mail corporativo disponíveis.
- Contas GA4, Meta Business e número de WhatsApp Business ativos.
- Conteúdo (textos, logotipo, identidade visual, depoimentos) fornecido pela All We Core.
- Serviço de envio de formulário / automação de leads definido.

---

## 10. Riscos
| Risco | Mitigação |
|-------|-----------|
| Conteúdo raso por falta de cases | Prova social como seção na Home; página de Cases só na Fase 2. |
| Excesso de páginas de serviço vazias | Apenas 2–3 páginas no MVP. |
| Atraso por escopo inflado | Congelar escopo do MVP neste PRD. |
| Baixa conversão | CTAs claros, formulário curto, WhatsApp, testes A/B na Fase 2. |
