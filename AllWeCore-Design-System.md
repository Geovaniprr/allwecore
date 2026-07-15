# Design System — All We Core
### Documento 1 · Fundação Visual do Produto

| Campo | Valor |
|-------|-------|
| Versão | 1.0 |
| Data | 2026-07-03 |
| Base | Manual de marca oficial All We Core |
| Marca | "Tecnologia, IA e Marketing para impulsionar negócios." |
| Tema base | Dark-first (fundo preto profundo) |

> Este documento é a **fonte da verdade visual** do site. Todos os valores derivam diretamente do manual de marca fornecido. Os tokens estão implementados em [`awc-tokens.css`](awc-tokens.css) para uso imediato no desenvolvimento — garantindo consistência, manutenção fácil e escalabilidade (requisitos RNF-15/16 do SRS).

---

## 1. Fundamentos da marca

### 1.1 Personalidade
Inovadora · Estratégica · Confiável · Conectada · Acessível

### 1.2 O que a marca transmite
Conexão que gera resultados · Tecnologia com propósito · Estratégia que impulsiona · Crescimento que se conecta.

### 1.3 Como isso vira decisão de design
| Traço da marca | Tradução visual |
|----------------|-----------------|
| Conectada | O símbolo (teia/rede) e o motivo de "nós conectados" aparecem como textura e detalhe estrutural. |
| Inovadora / Tecnológica | Base dark, verde neon com **glow**, gradiente energético. |
| Confiável | Alto contraste, hierarquia clara, espaçamento generoso, nada poluído. |
| Acessível | Tipografia legível (Inter), contraste WCAG AA, foco visível. |
| Crescimento | Uso do verde (evolução/resultado) como cor de ação principal. |

**Por quê dark-first:** o manual define o preto profundo como base e o verde neon como destaque luminoso. Em fundo escuro, o neon "acende" e cria a assinatura tecnológica premium da marca — impossível de reproduzir em fundo claro sem perder identidade.

---

## 2. Tokens de cor

### 2.1 Cores primárias (estrutura / neutros)
| Token | Nome | Hex | Uso |
|-------|------|-----|-----|
| `--color-black` | Preto Profundo | `#0A0A0A` | Fundo base do site |
| `--color-graphite` | Grafite | `#121417` | Superfícies / seções |
| `--color-gray-dark` | Cinza Escuro | `#1E2126` | Cards, bordas, inputs |
| `--color-gray-light` | Cinza Claro | `#E5E7EB` | Texto principal sobre fundo escuro |

### 2.2 Cores secundárias (verde — evolução e resultado)
| Token | Nome | Hex | Uso |
|-------|------|-----|-----|
| `--color-green-dark` | Verde Escuro | `#16A34A` | Estados, ícones, gradiente |
| `--color-green-light` | Verde Claro | `#A3E635` | Hover, realces suaves |

### 2.3 Cores de destaque
| Token | Nome | Hex | Uso |
|-------|------|-----|-----|
| `--color-green-neon` | Verde Neon | `#C6FF00` | **Cor de ação principal (CTAs), palavras-chave, glow** |
| `--color-purple` | Roxo Profundo | `#6D28D9` | Contraponto de inovação/tecnologia, acentos, badges |

### 2.4 Gradiente da marca
```
Verde Escuro (#16A34A) → Verde Neon (#C6FF00) → Roxo Profundo (#6D28D9)
```
- **Uso:** destaques, botões especiais, elementos interativos e gráficos.
- **Regra:** é um recurso de **assinatura** — usar com moderação (hero, um card de destaque, divisórias). Nunca em blocos grandes de texto nem em vários elementos concorrendo na mesma tela.
- **Por quê:** o gradiente une "crescimento" (verde) a "tecnologia/inovação" (roxo) numa única transição — resume a proposta da empresa. Repetido demais, perde o impacto.

### 2.5 Tokens semânticos (mapeamento de uso)
Trabalhe sempre por **função**, não por cor bruta — assim o tema é fácil de manter.

| Token semântico | Valor | Função |
|-----------------|-------|--------|
| `--bg-base` | `#0A0A0A` | Fundo da página |
| `--bg-surface` | `#121417` | Seções alternadas |
| `--bg-elevated` | `#1E2126` | Cards, inputs, menus |
| `--border-subtle` | `rgba(255,255,255,.08)` | Bordas discretas |
| `--border-strong` | `#1E2126` | Bordas de card/input |
| `--text-primary` | `#E5E7EB` | Texto principal |
| `--text-heading` | `#FFFFFF` | Títulos de maior peso |
| `--text-muted` | `#8A93A3` | Texto secundário/legendas |
| `--action` | `#C6FF00` | Cor de CTA principal |
| `--action-hover` | `#A3E635` | CTA em hover |
| `--action-text` | `#0A0A0A` | Texto **sobre** o neon (nunca branco) |
| `--accent` | `#6D28D9` | Destaque secundário |
| `--focus-ring` | `#C6FF00` | Anel de foco (acessibilidade) |
| `--success` | `#16A34A` | Feedback positivo |
| `--danger` | `#F04438` | Erros de formulário |

**Regra de contraste crítica:** o Verde Neon é claríssimo. Texto **sobre** neon é sempre `#0A0A0A` (preto). Neon como **texto** só sobre fundo escuro. Nunca neon sobre branco (ilegível) nem branco sobre neon.

---

## 3. Tipografia

### 3.1 Famílias
| Papel | Fonte | Peso base | Por quê |
|-------|-------|-----------|---------|
| Títulos / Destaques | **Sora** | SemiBold (600) | Geométrica, moderna, "engenheirada" — carrega a personalidade tecnológica. |
| Texto / Parágrafos | **Inter** | Regular (400) | Neutra, altamente legível em qualquer tamanho — reforça acessibilidade. |
| Utilitário / Dados | **JetBrains Mono** (opcional) | Regular | Números, tags técnicas, code snippets, métricas de dashboard. Nod à área de BI/dev. |

> Sora + Inter vêm direto do manual. O mono é uma extensão opcional coerente para telas de dados — não substitui nada.

### 3.2 Escala tipográfica (modular ~1.25)
| Token | Tamanho | Uso | Fonte / peso |
|-------|---------|-----|--------------|
| `--fs-display` | 60–72px | Headline do Hero | Sora 600, tracking -0.02em |
| `--fs-h1` | 44–48px | Título de página | Sora 600 |
| `--fs-h2` | 32–36px | Título de seção | Sora 600 |
| `--fs-h3` | 24px | Subtítulo | Sora 600 |
| `--fs-h4` | 20px | Card / bloco | Sora 600 |
| `--fs-lg` | 18px | Lead / intro | Inter 400 |
| `--fs-base` | 16px | Corpo | Inter 400 |
| `--fs-sm` | 14px | Auxiliar | Inter 400 |
| `--fs-xs` | 12px | Legenda / eyebrow | Inter 500, uppercase, tracking +0.08em |

### 3.3 Regras de uso
- **Line-height:** títulos 1.1–1.15; corpo 1.6.
- **Letter-spacing:** títulos grandes negativos (-0.02em) para densidade premium; eyebrows/labels positivos (+0.08em) em caixa alta.
- **Medida de linha:** máx. ~70 caracteres em blocos de texto.
- **Realce de palavra-chave:** dentro de um título, destacar 1 palavra em Verde Neon (ex.: "empresas que querem **crescer**") — técnica direta do manual. Nunca mais de uma cor de realce por título.

---

## 4. Grid e layout

| Item | Valor | Por quê |
|------|-------|---------|
| Container máx. | 1200px (conteúdo) / 1280px (full) | Confortável em desktop sem esticar linhas de texto. |
| Colunas | 12 | Padrão flexível para qualquer composição. |
| Gutter | 24px | Respiro entre colunas. |
| Margem lateral | 24px (mobile) → 48px+ (desktop) | Mobile-first (RNF-05). |
| Ritmo vertical | Seções com 96–128px de padding vertical no desktop | Espaço = percepção premium. |

**Breakpoints:**
| Nome | Largura | Alvo |
|------|---------|------|
| `sm` | ≥ 640px | Celular grande |
| `md` | ≥ 768px | Tablet |
| `lg` | ≥ 1024px | Desktop |
| `xl` | ≥ 1280px | Desktop amplo |

---

## 5. Espaçamento

Escala base **8px** (com meio-passo de 4px). Consistência de espaçamento é o que faz o layout parecer "caro".

| Token | px |
|-------|----|
| `--space-1` | 4 |
| `--space-2` | 8 |
| `--space-3` | 12 |
| `--space-4` | 16 |
| `--space-5` | 24 |
| `--space-6` | 32 |
| `--space-8` | 48 |
| `--space-10` | 64 |
| `--space-12` | 80 |
| `--space-16` | 128 |

---

## 6. Border radius

| Token | Valor | Uso | Por quê |
|-------|-------|-----|---------|
| `--radius-sm` | 8px | Inputs, tags | Suave, moderno. |
| `--radius-md` | 12px | Cards internos | Padrão. |
| `--radius-lg` | 16px | Cards principais | Coincide com o manual (cards/app arredondados). |
| `--radius-xl` | 24px | Blocos de destaque, hero container | Premium. |
| `--radius-pill` | 9999px | Botões, chips | Botões do manual são pill. |

**Por quê pill nos botões:** o manual mostra botões totalmente arredondados ("Fale conosco"). O formato pill combina com a estética conectada/orgânica da teia.

---

## 7. Sombras e glow

Dois sistemas: **elevação** (profundidade neutra) e **glow** (assinatura neon).

| Token | Valor | Uso |
|-------|-------|-----|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,.4)` | Elementos rasos |
| `--shadow-md` | `0 8px 24px rgba(0,0,0,.45)` | Cards |
| `--shadow-lg` | `0 20px 50px rgba(0,0,0,.55)` | Modais, hero |
| `--glow-green` | `0 0 24px rgba(198,255,0,.35)` | CTA em hover, símbolo, destaques |
| `--glow-purple` | `0 0 24px rgba(109,40,217,.40)` | Acentos roxos |

**Por quê o glow:** no manual, o símbolo da teia emite luz verde. O glow é a assinatura da marca — reservado a poucos elementos (CTA principal, símbolo, 1 card em destaque). Usado em tudo, vira ruído.

---

## 8. Glassmorphism

Faz sentido **com moderação**, porque combina com o dark-first tecnológico.

- **Onde usar:** navbar ao rolar, cards flutuantes sobre o gradiente/hero, overlays.
- **Onde NÃO usar:** blocos de texto longo, cards em massa (prejudica contraste e performance).
- **Receita padrão:**
```
background: rgba(18,20,23,.60);
backdrop-filter: blur(16px);
border: 1px solid rgba(255,255,255,.08);
border-radius: var(--radius-lg);
```
- **Por quê com cautela:** `backdrop-filter` custa performance (RNF-01/02) e reduz contraste. Limitar a 1–2 superfícies por tela preserva velocidade e legibilidade.

---

## 9. Componentes

Cada componente lista **variantes + estados (hover, active, disabled, loading, focus)**.

### 9.1 Botões
| Variante | Fundo | Texto | Uso |
|----------|-------|-------|-----|
| **Primary** | `#C6FF00` (neon) | `#0A0A0A` | CTA principal ("Fale conosco") |
| **Secondary** | Transparente, borda `#1E2126` | `#E5E7EB` | Ação secundária ("Ver soluções") |
| **Ghost** | Transparente | `#A3E635` | Links de ação discretos |
| **Accent** | `#6D28D9` (roxo) | `#FFFFFF` | Destaque alternativo pontual |

**Estados (Primary):**
- Hover: fundo `#A3E635` + `--glow-green` + leve `translateY(-1px)`.
- Active: `scale(.98)`, glow reduzido.
- Focus: `--focus-ring` (anel neon 2px, offset 2px).
- Disabled: fundo `#1E2126`, texto `#8A93A3`, sem glow, `cursor: not-allowed`.
- Loading: texto substituído por spinner; largura mantida (evita "pulo" de layout).

Padding: `14px 28px` (base). Radius: `--radius-pill`. Fonte: Sora 600 / 16px.

### 9.2 Inputs e campos
- Fundo `#1E2126`, borda `1px #2A2F37`, radius `--radius-sm`, texto `#E5E7EB`, placeholder `#8A93A3`.
- **Estados:** Focus → borda `#C6FF00` + glow verde sutil. Erro → borda `#F04438` + mensagem abaixo. Disabled → opacidade 0.5. Sucesso → borda `#16A34A`.
- Label acima do campo (Inter 500, 14px). Mensagem de erro clara e específica ("Informe um e-mail válido"), nunca genérica.

### 9.3 Cards
- Base: fundo `#121417`, borda `1px rgba(255,255,255,.06)`, radius `--radius-lg`, padding `--space-6`, `--shadow-md`.
- **Card de serviço** (como no manual): ícone neon no topo, título Sora, descrição Inter, link. Hover → borda passa a verde sutil + `translateY(-4px)` + `--shadow-lg`.
- **Card destaque:** borda em gradiente da marca ou `--glow-green`. Máximo 1 por seção.
- **Estados:** hover (elevar), focus-within (anel neon se clicável), loading (skeleton em `#1E2126`).

### 9.4 Navbar
- Topo: logo à esquerda, links centrais (Soluções, Sobre, Cases, Blog), CTA neon à direita — exatamente como o mockup do manual.
- **Repouso:** fundo transparente sobre o hero.
- **Ao rolar:** vira glass (`rgba(10,10,10,.7)` + blur) com borda inferior sutil — mantém legibilidade sobre qualquer conteúdo.
- **Mobile:** menu hambúrguer → drawer full-screen escuro com links grandes e CTA no fim.
- **Estados de link:** hover → `#C6FF00`; ativo → underline neon curto; focus → anel.

### 9.5 Footer
- Fundo `#0A0A0A`, borda superior sutil.
- Colunas: marca + slogan · navegação · serviços · contato/redes · links legais (Privacidade, Termos).
- Assinatura horizontal da marca (logo + símbolo). Ícones de rede em linha, hover neon.
- **Por quê:** consolida confiança e conformidade (LGPD) no fim de cada página.

### 9.6 Formulários
- Layout de 1 coluna (mobile) / 2 colunas para campos curtos (desktop).
- Máx. 4 campos no MVP (SRS RF-13/RNF-07): Nome · E-mail/WhatsApp · Serviço de interesse (select) · Mensagem.
- Botão de envio Primary, largura total no mobile.
- Feedback: sucesso (banner verde `#16A34A` + ícone check), erro por campo, estado loading no botão.
- Honeypot invisível anti-spam (RF-17).

### 9.7 FAQ (acordeão)
- Item: pergunta (Sora 600, 18px) + ícone chevron/“+”. Resposta (Inter, `--text-muted`) revelada com transição de altura.
- **Estados:** fechado (chevron ↓), aberto (chevron ↑ + item com leve realce de borda esquerda neon), hover (pergunta em `#FFFFFF`), focus (anel).
- Um item aberto por vez (opcional). Animação suave de expand/collapse.

### 9.8 Hero Section (assinatura da página)
- Estrutura: eyebrow → headline (Sora, com 1 palavra em neon) → subheadline (Inter) → CTAs (Primary + Secondary) → **símbolo da teia com glow** à direita/fundo.
- Fundo: preto profundo com **glow verde radial** atrás do símbolo + toque do gradiente da marca.
- **Por quê:** o hero abre com o elemento mais característico da marca (a teia luminosa) — é a "tese" visual da página e o que ela será lembrada.
- Motion sugerido: símbolo com leve respiração/parallax; nós da teia acendendo em sequência no load (respeitar `prefers-reduced-motion`).

---

## 10. Ícones e elementos gráficos

- **Estilo:** linha (outline), traço médio, cantos levemente arredondados, cor `#A3E635`/`#C6FF00` — igual ao manual (IA, chip, gráfico, alvo, chat, rede de nós).
- **Grid do ícone:** 24×24, traço 1.5–2px.
- **Elemento de marca recorrente:** a **teia/rede de nós** e o padrão de **pontos** (dot grid) como textura de fundo sutil em seções — reforça "conectada".
- **Regra:** ícones nunca preenchidos em cores concorrentes; um só peso de traço em toda a interface.

---

## 11. Estados globais (resumo)
| Estado | Tratamento padrão |
|--------|-------------------|
| Hover | Elevar (`translateY`), acender (glow/cor), transição 150–200ms. |
| Active | `scale(.98)`, feedback imediato. |
| Focus | Anel neon `--focus-ring`, 2px, offset 2px — **sempre visível** (acessibilidade). |
| Disabled | Opacidade/cinza, sem glow, `cursor: not-allowed`. |
| Loading | Spinner ou skeleton em `#1E2126`; nunca deixar a UI "morta" sem feedback. |
| Empty | Mensagem com direção + CTA, nunca tela vazia sem saída. |

---

## 12. Responsividade
- **Mobile-first** obrigatório (maior parte do tráfego, sobretudo tráfego pago).
- Tipografia fluida: display escala de ~36px (mobile) a ~72px (desktop).
- Navbar → hambúrguer abaixo de `lg`.
- Grids de card: 1 col (mobile) → 2 (md) → 3 (lg).
- Touch targets mínimos 44×44px.
- Padding de seção reduz de 128px (desktop) para 64px (mobile).

---

## 13. Animações e motion
| Princípio | Regra |
|-----------|-------|
| Propósito | Motion serve à compreensão/energia da marca, não é enfeite. |
| Duração | Micro-interações 150–250ms; reveals 400–600ms. |
| Easing | `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out suave) como padrão. |
| Momento orquestrado | 1 sequência marcante no load do hero (teia acendendo) vale mais que efeitos espalhados. |
| Scroll reveal | Fade + subida sutil (16–24px) ao entrar na viewport. |
| Acessibilidade | `prefers-reduced-motion` desliga parallax e sequências. |
| Performance | Animar apenas `transform` e `opacity` (RNF-01/02). |

---

## 14. Uso correto da marca
**Fazer:**
- Fundo escuro como base; neon com moderação, sempre com respiro.
- Símbolo da teia com espaço de proteção ao redor.
- Uma palavra-chave em neon por título; um destaque de glow por tela.
- Preto sobre neon; neon/branco sobre escuro.

**Não fazer:**
- Neon sobre fundo claro ou branco sobre neon (ilegível).
- Gradiente da marca em áreas grandes ou em blocos de texto.
- Múltiplos elementos com glow competindo na mesma seção.
- Esticar/distorcer o símbolo, mudar suas cores fora da paleta, aplicar sombra dura.
- Misturar outras fontes fora de Sora/Inter (+ mono utilitário).

---

## 15. Entregáveis
| Arquivo | Conteúdo |
|---------|----------|
| `All We Core-Design-System.md` | Este documento (fundamentos + regras). |
| `awc-tokens.css` | Todos os tokens como CSS Custom Properties, prontos para importar. |

**Próximos passos sugeridos:** (a) versão dos tokens em JSON/Tailwind config; (b) biblioteca de componentes (Storybook) na Fase 2; (c) protótipo do Hero para validar a assinatura visual antes do desenvolvimento.
