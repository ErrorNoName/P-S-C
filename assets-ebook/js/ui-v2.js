/* ==========================================================================
   PSYCLOPÉDIA — Interface v2
   Barre de progression de lecture · sommaire latéral actif · cartes de
   références dépliables · filtres de listes · ancrage des titres.
   ========================================================================== */

(function () {
  "use strict";

  /* ------------------ Barre de progression de lecture ---------------------- */

  function initReadProgress() {
    if (!document.querySelector(".content, .ref-list")) return;
    var bar = document.createElement("div");
    bar.id = "read-progress";
    document.body.appendChild(bar);
    function update() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var pct = h > 0 ? (window.scrollY / h) * 100 : 0;
      bar.style.width = Math.min(100, Math.max(0, pct)) + "%";
    }
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  /* -------------------- Sommaire latéral : titre actif --------------------- */

  function initToc() {
    var toc = document.querySelector(".toc-side");
    if (!toc) return;
    var links = Array.prototype.slice.call(toc.querySelectorAll("a[href^='#']"));
    if (!links.length) return;
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); });

    function update() {
      var best = 0;
      for (var i = 0; i < targets.length; i++) {
        if (targets[i] && targets[i].getBoundingClientRect().top <= 140) best = i;
      }
      links.forEach(function (a, i) { a.classList.toggle("active", i === best); });
    }
    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  /* ----------------- Cartes de références dépliables ----------------------- */

  function initRefCards() {
    document.addEventListener("click", function (e) {
      var head = e.target.closest(".ref-card-head");
      if (!head) return;
      var card = head.parentElement;
      var wasOpen = card.classList.contains("open");
      card.classList.toggle("open", !wasOpen);
      if (!wasOpen) {
        var id = card.getAttribute("data-ref-id");
        if (id) history.replaceState(null, "", "#" + id);
      }
    });

    // Ouverture directe via l'ancre de l'URL.
    if (location.hash.length > 1) {
      var target = document.querySelector('[data-ref-id="' + CSS.escape(location.hash.slice(1)) + '"]');
      if (target) {
        target.classList.add("open");
        setTimeout(function () { target.scrollIntoView({ behavior: "smooth", block: "center" }); }, 120);
      }
    }
  }

  /* ------------------- Filtre texte + famille des listes ------------------- */

  function normalize(s) {
    return (s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  }

  function initRefFilter() {
    var toolbar = document.querySelector("[data-ref-filter]");
    if (!toolbar) return;
    var input = toolbar.querySelector("input");
    var countEl = toolbar.querySelector(".ref-count");
    var chips = Array.prototype.slice.call(toolbar.querySelectorAll(".search-filter"));
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-ref-id]"));
    var famille = "all";

    function apply() {
      var q = normalize(input ? input.value.trim() : "");
      var shown = 0;
      cards.forEach(function (c) {
        var okFam = famille === "all" || c.getAttribute("data-famille") === famille;
        var okTxt = !q || normalize(c.getAttribute("data-search") || c.textContent).indexOf(q) !== -1;
        var visible = okFam && okTxt;
        c.style.display = visible ? "" : "none";
        if (visible) shown++;
      });
      if (countEl) countEl.textContent = shown + (shown > 1 ? " fiches" : " fiche");
    }

    if (input) input.addEventListener("input", apply);
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        chips.forEach(function (c) { c.classList.remove("active"); });
        chip.classList.add("active");
        famille = chip.getAttribute("data-famille") || "all";
        apply();
      });
    });
    apply();
  }

  /* ------------------------ Filtre alphabétique ---------------------------- */

  function initAlphaFilter() {
    var nav = document.querySelector(".alpha-nav");
    if (!nav) return;
    nav.addEventListener("click", function (e) {
      var btn = e.target.closest("button");
      if (!btn) return;
      nav.querySelectorAll("button").forEach(function (b) { b.classList.remove("active"); });
      btn.classList.add("active");
      var letter = btn.getAttribute("data-letter");
      document.querySelectorAll("[data-letter-key]").forEach(function (entry) {
        entry.style.display = (letter === "all" || entry.getAttribute("data-letter-key") === letter) ? "" : "none";
      });
      var countEl = document.querySelector("[data-alpha-count]");
      if (countEl) {
        var n = document.querySelectorAll("[data-letter-key]:not([style*='display: none'])").length;
        countEl.textContent = n + (n > 1 ? " entrées" : " entrée");
      }
    });
  }

  /* ------------------ Ancres cliquables sur les titres --------------------- */

  function initHeadingAnchors() {
    document.querySelectorAll(".content h2[id]").forEach(function (h) {
      h.style.scrollMarginTop = "6rem";
    });
  }

  function init() {
    initReadProgress();
    initToc();
    initRefCards();
    initRefFilter();
    initAlphaFilter();
    initHeadingAnchors();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
