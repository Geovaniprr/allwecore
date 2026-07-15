/* Interações do site (Design System §13) — vanilla JS, sem dependências. */
(function () {
  "use strict";

  // Navbar: vira "glass" ao rolar
  var navbar = document.querySelector(".navbar");
  if (navbar) {
    var onScroll = function () {
      navbar.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Menu mobile (drawer)
  var toggle = document.querySelector(".navbar__toggle");
  var drawer = document.querySelector(".drawer");
  var closeBtn = document.querySelector(".drawer__close");
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("is-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (toggle) toggle.setAttribute("aria-expanded", String(open));
  }
  if (toggle) toggle.addEventListener("click", function () { setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setDrawer(false); });
  if (drawer) drawer.querySelectorAll("a").forEach(function (a) {
    a.addEventListener("click", function () { setDrawer(false); });
  });

  // FAQ (acordeão)
  document.querySelectorAll(".faq__q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq__item");
      var answer = item.querySelector(".faq__a");
      var open = item.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
      answer.style.maxHeight = open ? answer.scrollHeight + "px" : null;
    });
  });

  // Scroll reveal
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        // Stagger: atraso proporcional à posição entre os irmãos .reveal (cascata)
        var idx = 0, sib = el;
        while ((sib = sib.previousElementSibling) && idx < 5) {
          if (sib.classList.contains("reveal")) idx++;
        }
        el.style.transitionDelay = (idx * 70) + "ms";
        el.classList.add("is-visible");
        setTimeout(function () { el.style.transitionDelay = ""; }, 900);
        io.unobserve(el);
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  // Banner de cookies (consentimento — RF-20/21)
  var banner = document.querySelector(".cookie-banner");
  if (banner) {
    var KEY = "awc_cookie_consent";
    if (!localStorage.getItem(KEY)) banner.hidden = false;
    banner.querySelectorAll("[data-consent]").forEach(function (b) {
      b.addEventListener("click", function () {
        localStorage.setItem(KEY, b.getAttribute("data-consent"));
        banner.hidden = true;
        // TODO: carregar GA4/Pixel apenas se data-consent === "accept".
      });
    });
  }

  // Evita envio duplicado: no 1º submit trava o botão e mostra spinner.
  document.querySelectorAll("form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      if (form.dataset.submitting === "1") { e.preventDefault(); return; }
      form.dataset.submitting = "1";
      var btn = form.querySelector('[type="submit"], button:not([type])');
      if (btn) { btn.classList.add("is-loading"); btn.setAttribute("aria-busy", "true"); }
    });
  });
})();
