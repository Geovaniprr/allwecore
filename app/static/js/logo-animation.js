/* All We Core — animação cinematográfica da teia.
   Uma corrente de energia percorre os fios reais do SVG (getPointAtLength) e os
   "tece": cada fio só aparece depois que a energia passa. SVG + CSS + JS puro.
   Duração alvo ~2.4s. Sem bibliotecas. Respeita prefers-reduced-motion. */
(function () {
  "use strict";
  var svg = document.getElementById("awc-web");
  if (!svg) return;

  var NS = "http://www.w3.org/2000/svg";
  var CX = 100, CY = 100;
  var ANG = [-90, -45, 0, 45, 90, 135, 180, 225].map(function (d) { return d * Math.PI / 180; });
  var RADII = [30, 58, 86];          // dois anéis internos + pontas
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- nós ---------- */
  var nodes = { c: { x: CX, y: CY } };
  function nid(r, a) { return r + "_" + a; }
  for (var r = 0; r < 3; r++) for (var a = 0; a < 8; a++) {
    nodes[nid(r, a)] = { x: CX + RADII[r] * Math.cos(ANG[a]), y: CY + RADII[r] * Math.sin(ANG[a]) };
  }

  /* ---------- arestas (fios) ---------- */
  function line(f, t) { var A = nodes[f], B = nodes[t]; return "M" + A.x.toFixed(2) + " " + A.y.toFixed(2) + " L" + B.x.toFixed(2) + " " + B.y.toFixed(2); }
  function arc(f, t, rad) {
    var A = nodes[f], B = nodes[t];
    var mx = (A.x + B.x) / 2, my = (A.y + B.y) / 2;
    var ang = Math.atan2(my - CY, mx - CX);
    var cr = rad * 0.86;                       // controle puxado para dentro (barriga da teia)
    var cx = CX + cr * Math.cos(ang), cy = CY + cr * Math.sin(ang);
    return "M" + A.x.toFixed(2) + " " + A.y.toFixed(2) + " Q" + cx.toFixed(2) + " " + cy.toFixed(2) + " " + B.x.toFixed(2) + " " + B.y.toFixed(2);
  }

  var edges = [];
  for (a = 0; a < 8; a++) {                    // raios (3 segmentos cada)
    edges.push({ from: "c", to: nid(0, a), curve: false, d: line("c", nid(0, a)) });
    edges.push({ from: nid(0, a), to: nid(1, a), curve: false, d: line(nid(0, a), nid(1, a)) });
    edges.push({ from: nid(1, a), to: nid(2, a), curve: false, d: line(nid(1, a), nid(2, a)) });
  }
  for (r = 0; r < 3; r++) for (a = 0; a < 8; a++) {   // anéis (arcos)
    var b = (a + 1) % 8;
    edges.push({ from: nid(r, a), to: nid(r, b), curve: true, d: arc(nid(r, a), nid(r, b), RADII[r]) });
  }

  /* ---------- elementos ---------- */
  var wiresG = document.createElementNS(NS, "g");
  wiresG.setAttribute("class", "aw-wires");
  svg.appendChild(wiresG);

  edges.forEach(function (e) {
    var p = document.createElementNS(NS, "path");
    p.setAttribute("d", e.d);
    p.setAttribute("class", "aw-wire");
    wiresG.appendChild(p);
    e.el = p;
    e.len = p.getTotalLength();
    p.style.strokeDasharray = e.len;
    p.style.strokeDashoffset = e.len;          // começa invisível
  });

  var hub = document.createElementNS(NS, "circle");
  hub.setAttribute("cx", CX); hub.setAttribute("cy", CY); hub.setAttribute("r", 7);
  hub.setAttribute("class", "aw-hub");
  svg.appendChild(hub);

  var ghosts = [];                              // rastro curto (fibra óptica)
  for (var g = 4; g >= 1; g--) {
    var gc = document.createElementNS(NS, "circle");
    gc.setAttribute("r", 1.2 + g * 0.35);
    gc.setAttribute("fill", "#d9ff7a");
    gc.setAttribute("opacity", (0.10 * g).toFixed(2));
    gc.style.filter = "url(#aw-bloom)";
    svg.appendChild(gc);
    ghosts.push(gc);
  }

  var spark = document.createElementNS(NS, "circle");
  spark.setAttribute("r", 3.1);
  spark.setAttribute("class", "aw-spark");
  spark.setAttribute("cx", CX); spark.setAttribute("cy", CY);
  svg.appendChild(spark);

  /* ---------- reduced motion: mostra pronto ---------- */
  if (reduce) {
    edges.forEach(function (e) { e.el.style.strokeDashoffset = 0; e.el.classList.add("lit"); });
    hub.classList.add("lit");
    return;
  }

  /* ---------- adjacência ---------- */
  var adj = {};
  Object.keys(nodes).forEach(function (n) { adj[n] = []; });
  edges.forEach(function (e, i) {
    adj[e.from].push({ i: i, to: e.to, dir: 1 });
    adj[e.to].push({ i: i, to: e.from, dir: -1 });
  });
  function radiusOf(id) { return id === "c" ? -1 : parseInt(id.split("_")[0], 10); }

  /* ---------- rota contínua (guloso, reutiliza fios já traçados) ---------- */
  var visited = new Array(edges.length).fill(false);
  var route = [], cur = "c", guard = 0;

  function nextFrom(node) {
    var opts = adj[node].filter(function (o) { return !visited[o.i]; });
    if (!opts.length) return null;
    opts.sort(function (A, B) {                 // preferir sair para fora (tecendo em espiral)
      var oa = radiusOf(A.to) > radiusOf(node) ? 0 : 1;
      var ob = radiusOf(B.to) > radiusOf(node) ? 0 : 1;
      if (oa !== ob) return oa - ob;
      return A.i - B.i;
    });
    return opts[0];
  }
  function bfsToUnvisited(from) {               // caminho por fios já existentes até um nó com fio pendente
    var q = [[from]], seen = {}; seen[from] = 1;
    while (q.length) {
      var path = q.shift(), node = path[path.length - 1];
      if (node !== from && adj[node].some(function (o) { return !visited[o.i]; })) return path;
      adj[node].forEach(function (o) { if (!seen[o.to]) { seen[o.to] = 1; q.push(path.concat(o.to)); } });
    }
    return null;
  }

  while (visited.indexOf(false) !== -1 && guard++ < 600) {
    var nx = nextFrom(cur);
    if (nx) { visited[nx.i] = true; route.push({ i: nx.i, dir: nx.dir, draw: true }); cur = nx.to; }
    else {
      var path = bfsToUnvisited(cur);
      if (!path) break;
      for (var k = 1; k < path.length; k++) {
        var mv = adj[path[k - 1]].find(function (o) { return o.to === path[k]; });
        route.push({ i: mv.i, dir: mv.dir, draw: false });
      }
      cur = path[path.length - 1];
    }
  }

  /* ---------- durações (curva mais lenta; reposicionamento rápido) ---------- */
  var totalBase = 0;
  route.forEach(function (m) {
    m.dur = m.draw ? (edges[m.i].curve ? 150 : 92) : 40;
    totalBase += m.dur;
  });
  var TARGET = 2400, scale = TARGET / totalBase;
  route.forEach(function (m) { m.dur *= scale; });
  // partida mais lenta (primeiros movimentos), reforça o "surgir do centro"
  for (var s = 0; s < Math.min(3, route.length); s++) route[s].dur *= 1.6;

  /* ---------- easing ---------- */
  function easeInOut(t) { return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; }   // retas: acelera no meio
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }                                     // curvas: desacelera

  /* ---------- execução ---------- */
  var ri = 0, segStart = null, history = [], safety = null;
  function frame(ts) {
    if (segStart === null) segStart = ts;
    var m = route[ri], e = edges[m.i];
    var raw = Math.min(1, (ts - segStart) / m.dur);
    var t = e.curve ? easeOut(raw) : easeInOut(raw);
    var prog = m.dir === 1 ? t : (1 - t);
    var pt = e.el.getPointAtLength(e.len * prog);

    spark.setAttribute("cx", pt.x.toFixed(2));
    spark.setAttribute("cy", pt.y.toFixed(2));

    // rastro
    history.unshift({ x: pt.x, y: pt.y });
    if (history.length > 14) history.pop();
    ghosts.forEach(function (gc, idx) {
      var h = history[(idx + 1) * 3];
      if (h) { gc.setAttribute("cx", h.x.toFixed(2)); gc.setAttribute("cy", h.y.toFixed(2)); }
    });

    if (m.draw) {                               // desenha o fio conforme a energia avança
      spark.classList.remove("dim");
      e.el.style.strokeDashoffset = (m.dir === 1 ? 1 : -1) * (e.len * (1 - t));
    } else {
      spark.classList.add("dim");               // apenas reposiciona sobre fio já traçado
    }

    if (raw >= 1) {
      if (m.draw) { e.el.style.strokeDashoffset = 0; e.el.classList.add("lit"); }
      ri++; segStart = ts;
      if (ri >= route.length) { finish(); return; }
    }
    requestAnimationFrame(frame);
  }

  function finish() {
    if (safety) { clearTimeout(safety); safety = null; }
    ri = route.length;
    spark.style.opacity = "0";
    ghosts.forEach(function (gc) { gc.setAttribute("opacity", "0"); });
    hub.classList.add("pulse");                 // pulso no núcleo
    svg.classList.add("aw-flash");              // glow forte ~500ms
    setTimeout(function () {
      svg.classList.remove("aw-flash");
      svg.classList.add("aw-done");             // assenta em brilho discreto
      hub.classList.add("lit");
    }, 520);
  }

  // Segurança: garante a teia visível mesmo se o rAF for estrangulado
  // (ex.: aba em segundo plano) e a animação não completar.
  function revealAll() {
    if (ri >= route.length) return;
    edges.forEach(function (e) { e.el.style.strokeDashoffset = 0; e.el.classList.add("lit"); });
    ri = route.length;
    spark.style.opacity = "0";
    ghosts.forEach(function (gc) { gc.setAttribute("opacity", "0"); });
    hub.classList.add("lit");
    svg.classList.add("aw-done");
  }

  function begin() {
    if (ri >= route.length || segStart !== null) return;   // já começou/terminou
    requestAnimationFrame(frame);
    var budget = route.reduce(function (s, m) { return s + m.dur; }, 0) + 2500;
    safety = setTimeout(revealAll, budget);
  }

  // Só anima quando a aba está visível — se carregou em segundo plano,
  // espera o usuário focar para causar a primeira impressão (e não ficar invisível).
  if (document.hidden) {
    document.addEventListener("visibilitychange", function onVis() {
      if (!document.hidden) { document.removeEventListener("visibilitychange", onVis); begin(); }
    });
    // rede de segurança final caso o evento nunca ocorra
    safety = setTimeout(revealAll, 8000);
  } else {
    begin();
  }
})();
