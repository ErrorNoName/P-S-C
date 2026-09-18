/* =============================================================================
   PSYCLOPÉDIA — Révision espacée
   Implémentation légère inspirée de SM-2 : chaque carte porte un intervalle
   (en jours), un facteur de facilité et une date de prochaine présentation.
   Tout est stocké dans localStorage, uniquement sur cet appareil.
   ============================================================================= */

(function () {
  "use strict";

  var shell = document.getElementById("rev-shell");
  if (!shell) return;

  var ROOT = document.body.getAttribute("data-root") || "./";
  var EBOOK = ROOT + "livres-psychologie/07-ebook-final/";
  var CARDS_URL = EBOOK + "revision-cards.json";
  var STORE = "psyclo-revision-v1";
  var JOUR = 24 * 60 * 60 * 1000;

  var cards = [];
  var state = {};
  var queue = [];
  var current = null;
  var revealed = false;
  var sessionDone = 0;

  var deckSelect = document.getElementById("rev-deck");
  var resetBtn = document.getElementById("rev-reset");

  // ------------------------------------------------------------- persistance

  function loadState() {
    try {
      state = JSON.parse(localStorage.getItem(STORE) || "{}");
    } catch (e) {
      state = {};
    }
  }

  function saveState() {
    try {
      localStorage.setItem(STORE, JSON.stringify(state));
    } catch (e) {
      /* quota dépassé ou stockage désactivé : la session reste utilisable */
    }
  }

  function cardState(id) {
    return state[id] || { n: 0, i: 0, ef: 2.5, due: 0 };
  }

  /* Grade 0 = oublié, 1 = hésitant, 2 = facile. */
  function schedule(id, grade) {
    var s = cardState(id);
    if (grade === 0) {
      s.n = 0;
      s.i = 1;
      s.ef = Math.max(1.3, s.ef - 0.2);
    } else {
      s.n += 1;
      s.ef = Math.max(1.3, s.ef + (grade === 2 ? 0.1 : -0.05));
      if (s.n === 1) s.i = grade === 2 ? 3 : 1;
      else if (s.n === 2) s.i = grade === 2 ? 7 : 3;
      else s.i = Math.round(s.i * s.ef * (grade === 2 ? 1 : 0.7));
      s.i = Math.max(1, Math.min(s.i, 365));
    }
    s.due = Date.now() + s.i * JOUR;
    state[id] = s;
    saveState();
  }

  // ------------------------------------------------------------------- files

  function selectedDeck() {
    return deckSelect ? deckSelect.value : "all";
  }

  function deckCards() {
    var deck = selectedDeck();
    return deck === "all" ? cards : cards.filter(function (c) { return c.c === deck; });
  }

  function buildQueue() {
    var now = Date.now();
    var pool = deckCards();
    var due = [];
    var fresh = [];

    pool.forEach(function (c) {
      var s = state[c.id];
      if (!s) fresh.push(c);
      else if (s.due <= now) due.push(c);
    });

    shuffle(due);
    shuffle(fresh);
    // On mélange les cartes dues et un contingent de nouvelles, pour éviter
    // d'enchaîner vingt découvertes d'affilée.
    queue = due.concat(fresh.slice(0, 20));
    updateStats();
  }

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function updateStats() {
    var now = Date.now();
    var pool = deckCards();
    var due = 0, fresh = 0, known = 0;
    pool.forEach(function (c) {
      var s = state[c.id];
      if (!s) fresh++;
      else if (s.due <= now) due++;
      else if (s.i >= 7) known++;
    });
    setText("rev-n-due", due);
    setText("rev-n-new", fresh);
    setText("rev-n-known", known);
    setText("rev-n-total", pool.length);
  }

  function setText(id, value) {
    var n = document.getElementById(id);
    if (n) n.textContent = value;
  }

  // ---------------------------------------------------------------- affichage

  function escapeAttr(s) {
    return String(s).replace(/"/g, "&quot;");
  }

  function render() {
    if (!queue.length) return renderDone();
    current = queue[0];
    revealed = false;
    shell.innerHTML =
      '<p class="rev-tag">' + current.t + " · " + current.c + " · " + queue.length + " restantes</p>" +
      '<div class="rev-q">' + current.q + "</div>" +
      '<div><button class="btn btn-primary" id="rev-show">Afficher la réponse <span style="opacity:0.6">(Espace)</span></button></div>';
    var btn = document.getElementById("rev-show");
    if (btn) btn.addEventListener("click", reveal);
  }

  function reveal() {
    if (!current || revealed) return;
    revealed = true;
    shell.innerHTML =
      '<p class="rev-tag">' + current.t + " · " + current.c + " · " + queue.length + " restantes</p>" +
      '<div class="rev-q">' + current.q + "</div>" +
      '<div class="rev-a">' + current.a + "</div>" +
      '<div class="rev-grades">' +
      '<button class="rev-grade g0" data-grade="0">Je ne savais pas<small>revoir demain (1)</small></button>' +
      '<button class="rev-grade g1" data-grade="1">Hésitant<small>bientôt (2)</small></button>' +
      '<button class="rev-grade g2" data-grade="2">Facile<small>plus tard (3)</small></button>' +
      "</div>" +
      '<p style="font-size:0.76rem;color:var(--gris)"><a href="' + EBOOK + escapeAttr(current.p) +
      '" style="color:var(--vert)">→ Voir la fiche complète</a></p>';

    Array.prototype.forEach.call(shell.querySelectorAll(".rev-grade"), function (b) {
      b.addEventListener("click", function () {
        grade(parseInt(b.getAttribute("data-grade"), 10));
      });
    });
  }

  function grade(g) {
    if (!current || !revealed) return;
    schedule(current.id, g);
    sessionDone++;
    if (g === 0) {
      // Une carte oubliée revient en fin de session, pas seulement demain.
      var again = queue.shift();
      queue.push(again);
    } else {
      queue.shift();
    }
    updateStats();
    render();
  }

  function renderDone() {
    shell.innerHTML =
      '<p class="rev-tag">Session terminée</p>' +
      '<div class="rev-q">🎉 Plus rien à réviser pour l\'instant</div>' +
      '<p class="lab-prompt">Vous avez traité <strong>' + sessionDone + "</strong> carte" +
      (sessionDone > 1 ? "s" : "") + " dans cette session. Les cartes reviendront à l'échéance calculée " +
      "pour chacune : c'est l'espacement qui fait le travail, pas le volume d'une seule séance.</p>" +
      '<div class="rev-grades"><button class="btn btn-secondary" id="rev-more">Réviser un autre paquet</button></div>';
    var b = document.getElementById("rev-more");
    if (b && deckSelect) {
      b.addEventListener("click", function () {
        deckSelect.focus();
      });
    }
  }

  // -------------------------------------------------------------- événements

  document.addEventListener("keydown", function (e) {
    if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
    if (e.key === " " || e.key === "Enter") {
      if (!revealed && current) { e.preventDefault(); reveal(); }
      return;
    }
    if (revealed && (e.key === "1" || e.key === "2" || e.key === "3")) {
      e.preventDefault();
      grade(parseInt(e.key, 10) - 1);
    }
  });

  if (deckSelect) {
    deckSelect.addEventListener("change", function () {
      sessionDone = 0;
      buildQueue();
      render();
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      if (!window.confirm("Effacer toute votre progression de révision sur cet appareil ?")) return;
      state = {};
      saveState();
      sessionDone = 0;
      buildQueue();
      render();
    });
  }

  // ------------------------------------------------------------------ amorçage

  loadState();
  fetch(CARDS_URL)
    .then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    })
    .then(function (data) {
      cards = data;
      buildQueue();
      render();
    })
    .catch(function () {
      shell.innerHTML =
        '<p class="rev-tag">Chargement impossible</p>' +
        '<div class="rev-q">Les cartes n\'ont pas pu être chargées</div>' +
        '<p class="lab-prompt">Ce module lit un fichier JSON, ce que les navigateurs bloquent quand la page ' +
        "est ouverte directement depuis le disque (protocole <code>file://</code>). Ouvrez le site via " +
        "GitHub Pages, ou lancez un serveur local :<br><code>python3 -m http.server 8000</code></p>";
    });
})();
