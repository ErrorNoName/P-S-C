/* ==========================================================================
   PSYCLOPÉDIA — Moteur de recherche intelligent
   Index JSON chargé à la demande, normalisation des accents, recherche
   par mots multiples, tolérance aux fautes de frappe (distance de Levenshtein
   bornée), scoring par champ, surlignage et navigation clavier.
   ========================================================================== */

(function () {
  "use strict";

  var ROOT = document.body.getAttribute("data-root") || "./";
  var INDEX_URL = ROOT + "livres-psychologie/07-ebook-final/search-index.json";

  var KIND_LABEL = {
    categorie: "Catégorie",
    section: "Section",
    notion: "Notion",
    experience: "Expérience",
    auteur: "Auteur",
    theorie: "Théorie",
    trouble: "Trouble",
    biais: "Biais",
    test: "Test",
    cas: "Cas clinique",
    debat: "Débat",
    pratique: "Fiche pratique",
    metier: "Métier",
    labo: "Laboratoire",
    anglais: "Anglais",
    date: "Chronologie",
    livre: "Livre",
    quiz: "Quiz",
    page: "Page",
  };

  var KIND_ICON = {
    categorie: "📂", section: "📄", notion: "📖", experience: "🔬", auteur: "👤",
    theorie: "🧩", trouble: "🩺", biais: "🌀", test: "📊", cas: "🗃️", debat: "⚖️",
    pratique: "🧰", metier: "💼", labo: "🧪", anglais: "🌍",
    date: "🗓️", livre: "📕", quiz: "🎮", page: "🧭",
  };

  var FILTERS = [
    ["all", "Tout"],
    ["categorie", "Catégories"],
    ["section", "Sections"],
    ["notion", "Notions"],
    ["experience", "Expériences"],
    ["auteur", "Auteurs"],
    ["theorie", "Théories"],
    ["trouble", "Troubles"],
    ["biais", "Biais"],
    ["test", "Tests"],
    ["cas", "Cas cliniques"],
    ["debat", "Débats"],
    ["pratique", "Pratique"],
    ["metier", "Métiers"],
    ["labo", "Laboratoire"],
    ["anglais", "Anglais"],
    ["date", "Chronologie"],
    ["livre", "Livres"],
    ["quiz", "Quiz"],
  ];

  var index = null;
  var loading = false;
  var activeFilter = "all";
  var selIdx = 0;
  var currentHits = [];

  /* ----------------------- Normalisation & similarité ---------------------- */

  function norm(s) {
    return (s || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[''`]/g, "'")
      .replace(/[^a-z0-9' ]+/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  // Distance de Levenshtein bornée : abandonne dès que le seuil est dépassé.
  function editDistance(a, b, max) {
    if (a === b) return 0;
    if (Math.abs(a.length - b.length) > max) return max + 1;
    var prev = new Array(b.length + 1);
    var cur = new Array(b.length + 1);
    for (var j = 0; j <= b.length; j++) prev[j] = j;
    for (var i = 1; i <= a.length; i++) {
      cur[0] = i;
      var best = cur[0];
      for (var k = 1; k <= b.length; k++) {
        var cost = a.charCodeAt(i - 1) === b.charCodeAt(k - 1) ? 0 : 1;
        cur[k] = Math.min(cur[k - 1] + 1, prev[k] + 1, prev[k - 1] + cost);
        if (cur[k] < best) best = cur[k];
      }
      if (best > max) return max + 1;
      var tmp = prev; prev = cur; cur = tmp;
    }
    return prev[b.length];
  }

  // Tolérance : 0 faute sous 4 lettres, 1 faute jusqu'à 7, 2 au-delà.
  function tolerance(len) {
    if (len < 4) return 0;
    if (len < 8) return 1;
    return 2;
  }

  /* --------------------------- Scoring d'une entrée ------------------------ */

  // Chaque entrée de l'index : {t: titre, d: description, k: kind, u: url, g: mots-clés}
  function scoreEntry(entry, terms) {
    var title = entry._nt || (entry._nt = norm(entry.t));
    var desc = entry._nd || (entry._nd = norm(entry.d));
    var keys = entry._nk || (entry._nk = norm(entry.g || ""));
    var haystack = title + " " + keys + " " + desc;
    var total = 0;

    for (var i = 0; i < terms.length; i++) {
      var term = terms[i];
      var best = 0;

      if (title === term) best = 120;
      else if (title.indexOf(term) === 0) best = 90;
      else if (new RegExp("\\b" + escapeRe(term)).test(title)) best = 72;
      else if (title.indexOf(term) !== -1) best = 52;
      else if (new RegExp("\\b" + escapeRe(term)).test(keys)) best = 44;
      else if (keys.indexOf(term) !== -1) best = 30;
      else if (new RegExp("\\b" + escapeRe(term)).test(desc)) best = 22;
      else if (desc.indexOf(term) !== -1) best = 14;

      // Repli tolérant aux fautes sur les mots du titre uniquement.
      if (best === 0 && term.length >= 4) {
        var tol = tolerance(term.length);
        if (tol > 0) {
          var words = title.split(" ");
          for (var w = 0; w < words.length; w++) {
            if (Math.abs(words[w].length - term.length) > tol) continue;
            if (editDistance(words[w], term, tol) <= tol) { best = 34; break; }
          }
        }
      }

      if (best === 0 && haystack.indexOf(term) === -1) return 0; // terme absent → rejet
      total += best;
    }

    // Bonus : titres courts (plus spécifiques) et types prioritaires.
    if (title.length < 30) total += 5;
    if (entry.k === "categorie" || entry.k === "notion") total += 6;
    return total;
  }

  function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

  function search(query) {
    var terms = norm(query).split(" ").filter(function (t) { return t.length > 0; });
    if (!terms.length || !index) return [];
    var out = [];
    for (var i = 0; i < index.length; i++) {
      if (activeFilter !== "all" && index[i].k !== activeFilter) continue;
      var sc = scoreEntry(index[i], terms);
      if (sc > 0) out.push({ e: index[i], s: sc });
    }
    out.sort(function (a, b) { return b.s - a.s; });
    return out.slice(0, 40);
  }

  /* ------------------------------ Surlignage ------------------------------- */

  function highlight(text, terms) {
    if (!text) return "";
    var esc = text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    var normText = norm(text);
    var ranges = [];
    terms.forEach(function (term) {
      if (term.length < 2) return;
      var from = 0, pos;
      while ((pos = normText.indexOf(term, from)) !== -1) {
        ranges.push([pos, pos + term.length]);
        from = pos + term.length;
      }
    });
    if (!ranges.length) return esc;
    // La normalisation conserve la longueur caractère par caractère (NFD retiré
    // uniquement sur les diacritiques combinants), on peut mapper 1:1 en repli simple.
    if (normText.length !== text.length) return esc;
    ranges.sort(function (a, b) { return a[0] - b[0]; });
    var merged = [ranges[0]];
    for (var i = 1; i < ranges.length; i++) {
      var last = merged[merged.length - 1];
      if (ranges[i][0] <= last[1]) last[1] = Math.max(last[1], ranges[i][1]);
      else merged.push(ranges[i]);
    }
    var res = "", cursor = 0;
    merged.forEach(function (r) {
      res += escHtml(text.slice(cursor, r[0])) + "<mark>" + escHtml(text.slice(r[0], r[1])) + "</mark>";
      cursor = r[1];
    });
    res += escHtml(text.slice(cursor));
    return res;
  }

  function escHtml(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  function snippet(text, terms, len) {
    if (!text) return "";
    var n = norm(text);
    var pos = -1;
    for (var i = 0; i < terms.length; i++) {
      var p = n.indexOf(terms[i]);
      if (p !== -1 && (pos === -1 || p < pos)) pos = p;
    }
    if (pos === -1 || pos < len / 2) return text.slice(0, len);
    var start = Math.max(0, pos - Math.floor(len / 3));
    return (start > 0 ? "…" : "") + text.slice(start, start + len);
  }

  /* -------------------------------- Interface ------------------------------ */

  var overlay, input, resultsEl, countEl;

  function buildUI() {
    overlay = document.createElement("div");
    overlay.className = "search-overlay";
    overlay.innerHTML =
      '<div class="search-modal" role="dialog" aria-label="Recherche dans Psyclopédia">' +
        '<div class="search-input-row">' +
          '<span class="ico">🔍</span>' +
          '<input type="search" id="psy-search-input" placeholder="Rechercher une notion, un auteur, une expérience, un trouble…" autocomplete="off" spellcheck="false">' +
          '<span class="search-esc">Échap</span>' +
        '</div>' +
        '<div class="search-filters">' +
          FILTERS.map(function (f, i) {
            return '<button class="search-filter' + (i === 0 ? " active" : "") + '" data-kind="' + f[0] + '">' + f[1] + "</button>";
          }).join("") +
        '</div>' +
        '<div class="search-results" id="psy-search-results"></div>' +
        '<div class="search-foot">' +
          '<span><kbd>↑</kbd><kbd>↓</kbd> naviguer</span>' +
          '<span><kbd>↵</kbd> ouvrir</span>' +
          '<span><kbd>Échap</kbd> fermer</span>' +
          '<span id="psy-search-count"></span>' +
        '</div>' +
      "</div>";
    document.body.appendChild(overlay);

    input = overlay.querySelector("#psy-search-input");
    resultsEl = overlay.querySelector("#psy-search-results");
    countEl = overlay.querySelector("#psy-search-count");

    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    input.addEventListener("input", function () { render(input.value); });

    overlay.querySelectorAll(".search-filter").forEach(function (btn) {
      btn.addEventListener("click", function () {
        overlay.querySelectorAll(".search-filter").forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        activeFilter = btn.dataset.kind;
        render(input.value);
        input.focus();
      });
    });

    resultsEl.addEventListener("mousemove", function (e) {
      var hit = e.target.closest(".search-hit");
      if (!hit) return;
      var i = parseInt(hit.dataset.i, 10);
      if (i !== selIdx) { selIdx = i; paintSelection(); }
    });
  }

  function open(prefill) {
    if (!overlay) buildUI();
    overlay.classList.add("open");
    document.body.style.overflow = "hidden";
    if (prefill) input.value = prefill;
    input.focus();
    input.select();
    ensureIndex(function () { render(input.value); });
  }

  function close() {
    if (!overlay) return;
    overlay.classList.remove("open");
    document.body.style.overflow = "";
  }

  function ensureIndex(cb) {
    if (index) { cb(); return; }
    if (loading) return;
    loading = true;
    resultsEl.innerHTML = '<div class="search-empty"><span class="spin"></span> Chargement de l\'index…</div>';
    fetch(INDEX_URL)
      .then(function (r) { return r.json(); })
      .then(function (data) { index = data; loading = false; cb(); })
      .catch(function () {
        loading = false;
        resultsEl.innerHTML = '<div class="search-empty">Index de recherche indisponible.<br>Ouvre le site via un serveur web (ou GitHub Pages) pour activer la recherche.</div>';
      });
  }

  function render(query) {
    if (!index) return;
    var q = (query || "").trim();
    if (!q) {
      currentHits = [];
      countEl.textContent = index.length + " entrées indexées";
      resultsEl.innerHTML =
        '<div class="search-group-label">Suggestions</div>' +
        ["conditionnement", "dissonance cognitive", "Milgram", "biais de confirmation", "attachement", "TCC", "mémoire de travail", "burnout"]
          .map(function (s) {
            return '<div class="search-hit" data-suggest="' + s + '"><span class="search-hit-ico">💡</span>' +
              '<div class="search-hit-body"><div class="search-hit-title">' + s + "</div></div></div>";
          }).join("");
      resultsEl.querySelectorAll("[data-suggest]").forEach(function (el) {
        el.addEventListener("click", function () { input.value = el.dataset.suggest; render(input.value); input.focus(); });
      });
      return;
    }

    var terms = norm(q).split(" ").filter(Boolean);
    var hits = search(q);
    currentHits = hits;
    selIdx = 0;
    countEl.textContent = hits.length + (hits.length > 1 ? " résultats" : " résultat");

    if (!hits.length) {
      resultsEl.innerHTML = '<div class="search-empty">Aucun résultat pour « ' + escHtml(q) + ' ».<br>Essaie un synonyme, un nom d\'auteur, ou retire un mot.</div>';
      return;
    }

    var html = "";
    var lastKind = null;
    hits.forEach(function (h, i) {
      if (h.e.k !== lastKind) {
        html += '<div class="search-group-label">' + (KIND_LABEL[h.e.k] || h.e.k) + "</div>";
        lastKind = h.e.k;
      }
      html +=
        '<a class="search-hit' + (i === 0 ? " sel" : "") + '" data-i="' + i + '" href="' + ROOT + h.e.u + '">' +
          '<span class="search-hit-ico">' + (KIND_ICON[h.e.k] || "•") + "</span>" +
          '<div class="search-hit-body">' +
            '<div class="search-hit-title">' + highlight(h.e.t, terms) + "</div>" +
            '<div class="search-hit-desc">' + highlight(snippet(h.e.d, terms, 165), terms) + "</div>" +
          "</div>" +
          '<span class="search-hit-kind">' + (KIND_LABEL[h.e.k] || h.e.k) + "</span>" +
        "</a>";
    });
    resultsEl.innerHTML = html;
    resultsEl.scrollTop = 0;
  }

  function paintSelection() {
    var nodes = resultsEl.querySelectorAll(".search-hit");
    nodes.forEach(function (n, i) { n.classList.toggle("sel", i === selIdx); });
    var active = nodes[selIdx];
    if (active) {
      var top = active.offsetTop, bottom = top + active.offsetHeight;
      if (top < resultsEl.scrollTop) resultsEl.scrollTop = top - 8;
      else if (bottom > resultsEl.scrollTop + resultsEl.clientHeight) resultsEl.scrollTop = bottom - resultsEl.clientHeight + 8;
    }
  }

  // Phase de capture : Chrome réserve Ctrl+K pour sa barre d'adresse, il faut
  // intercepter l'événement avant qu'il ne remonte jusqu'au navigateur.
  window.addEventListener("keydown", function (e) {
    var openNow = overlay && overlay.classList.contains("open");

    var isK = e.key === "k" || e.key === "K" || e.code === "KeyK";
    if ((e.ctrlKey || e.metaKey) && isK && !e.altKey) {
      e.preventDefault();
      e.stopPropagation();
      openNow ? close() : open();
      return;
    }
    if (!openNow) {
      // « / » ouvre la recherche hors champ de saisie.
      if (e.key === "/" && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
        e.preventDefault(); open();
      }
      return;
    }
    if (e.key === "Escape") { e.preventDefault(); close(); return; }
    if (!currentHits.length) return;
    if (e.key === "ArrowDown") { e.preventDefault(); selIdx = Math.min(selIdx + 1, currentHits.length - 1); paintSelection(); }
    else if (e.key === "ArrowUp") { e.preventDefault(); selIdx = Math.max(selIdx - 1, 0); paintSelection(); }
    else if (e.key === "Enter") {
      var node = resultsEl.querySelectorAll(".search-hit")[selIdx];
      if (node && node.href) { e.preventDefault(); window.location.href = node.href; }
    }
  }, true);

  document.addEventListener("click", function (e) {
    var trigger = e.target.closest("[data-search-open]");
    if (trigger) { e.preventDefault(); open(trigger.getAttribute("data-search-open") || ""); }
  });

  window.PsySearch = { open: open, close: close };
})();
