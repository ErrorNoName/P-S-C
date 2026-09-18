/* ==========================================================================
   PSYCLOPÉDIA — Lecteur de livres intégré
   Rendu PDF.js · extraction du texte natif · OCR Tesseract.js (français)
   pour les scans sans couche texte · modernisation du français du XIXe
   siècle · traduction optionnelle vers d'autres langues.
   ========================================================================== */

(function () {
  "use strict";

  var PDFJS_SRC = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js";
  var PDFJS_WORKER = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
  var TESSERACT_SRC = "https://cdn.jsdelivr.net/npm/tesseract.js@5.1.0/dist/tesseract.min.js";

  var state = {
    doc: null,
    page: 1,
    pages: 0,
    scale: 1.3,
    rendering: false,
    pending: null,
    mode: "page",          // "page" | "split"
    modernize: true,
    lang: "fr",
    book: null,
    rawText: "",
    ocrWorker: null,
  };

  var el = {};

  /* --------------------- Glossaire de modernisation XIXe ------------------- */
  // Formes anciennes fréquentes dans les traités de psychologie 1850-1920.
  var LEXIQUE = [
    ["aliéné", "personne atteinte de troubles psychiques"],
    ["aliénés", "personnes atteintes de troubles psychiques"],
    ["aliénation mentale", "trouble psychique"],
    ["aliéniste", "psychiatre"],
    ["aliénistes", "psychiatres"],
    ["idiotie", "déficience intellectuelle profonde (terme obsolète)"],
    ["imbécillité", "déficience intellectuelle moyenne (terme obsolète)"],
    ["débilité mentale", "déficience intellectuelle légère (terme obsolète)"],
    ["arriération", "retard de développement (terme obsolète)"],
    ["dégénérescence", "dégénérescence (théorie abandonnée)"],
    ["monomanie", "idée fixe / trouble délirant circonscrit"],
    ["hystérie", "hystérie (concept historique, éclaté aujourd'hui en troubles dissociatifs et somatoformes)"],
    ["neurasthénie", "épuisement nerveux (proche du burn-out)"],
    ["psychasthénie", "trouble anxieux avec doute et inhibition (Janet)"],
    ["automatisme psychologique", "fonctionnement psychique automatique, hors contrôle volontaire"],
    ["idéation", "production d'idées"],
    ["cénesthésie", "sensation globale du corps"],
    ["sensorium", "ensemble des fonctions sensorielles"],
    ["âme", "esprit / vie psychique"],
    ["esprits animaux", "influx nerveux (modèle ancien)"],
    ["faculté", "fonction mentale"],
    ["facultés", "fonctions mentales"],
    ["entendement", "compréhension / intelligence"],
    ["concupiscence", "désir intense"],
    ["volonté", "volonté (capacité de décision et d'action)"],
    ["abulie", "perte de la capacité à décider et à agir"],
    ["aboulie", "perte de la capacité à décider et à agir"],
    ["idée fixe", "pensée obsédante"],
    ["suggestion", "influence induite chez un sujet"],
    ["magnétisme animal", "hypnose (théorie ancienne de Mesmer)"],
    ["somnambulisme provoqué", "état hypnotique"],
    ["catalepsie", "rigidité musculaire avec maintien des postures"],
    ["névrose", "névrose (catégorie historique, remplacée par les troubles anxieux et dépressifs)"],
    ["névropathe", "personne souffrant de troubles nerveux"],
    ["moral", "psychologique"],
    ["physique", "corporel"],
    ["sujet", "participant / patient"],
    ["observation", "étude de cas"],
    ["expérimentateur", "chercheur"],
    ["fonctions cérébrales", "fonctions cognitives"],
    ["localisations cérébrales", "cartographie fonctionnelle du cerveau"],
    ["ataxie", "trouble de la coordination des mouvements"],
    ["aphasie", "trouble du langage d'origine cérébrale"],
    ["amnésie rétrograde", "amnésie des souvenirs antérieurs à l'événement"],
    ["amnésie antérograde", "incapacité à former de nouveaux souvenirs"],
    ["atavisme", "réapparition de caractères ancestraux (théorie abandonnée)"],
    ["criminel-né", "criminel-né (théorie de Lombroso, scientifiquement invalidée)"],
    ["anthropométrie", "mesure des dimensions du corps"],
    ["craniométrie", "mesure du crâne (méthode invalidée)"],
    ["phrénologie", "phrénologie (pseudoscience des bosses du crâne)"],
    ["tempérament", "tempérament (base biologique de la personnalité)"],
    ["humeurs", "humeurs corporelles (théorie hippocratique abandonnée)"],
    ["bile noire", "bile noire (humeur supposée de la mélancolie)"],
    ["mélancolie", "dépression (terme historique)"],
    ["manie", "état d'excitation pathologique"],
    ["délire des grandeurs", "idées de grandeur"],
    ["persécution", "idées de persécution"],
    ["obnubilation", "confusion / conscience altérée"],
    ["prostration", "abattement extrême"],
    ["asthénie", "fatigue pathologique"],
    ["céphalalgie", "mal de tête"],
    ["céphalée", "mal de tête"],
    ["inanition", "épuisement par privation de nourriture"],
    ["commotion", "choc / traumatisme"],
    ["ébranlement", "perturbation"],
    ["disposition", "prédisposition"],
    ["accoutumance", "habituation"],
    ["association des idées", "association d'idées (mécanisme d'apprentissage)"],
    ["réminiscence", "souvenir qui revient spontanément"],
    ["aperception", "perception consciente et intégrée (Wundt)"],
    ["introspection", "observation de sa propre expérience consciente"],
    ["psychophysique", "étude des relations entre stimulus physique et sensation"],
    ["vésanie", "folie (terme obsolète)"],
    ["démence précoce", "schizophrénie (nom historique)"],
    ["confusion mentale", "état confusionnel"],
    ["stupeur", "immobilité avec absence de réaction"],
    ["hébétude", "engourdissement mental"],
    ["éréthisme", "excitation excessive"],
    ["torpeur", "engourdissement"],
    ["impulsion", "impulsion (passage à l'acte non contrôlé)"],
    ["obsession", "pensée intrusive récurrente"],
    ["phobie", "peur intense et irrationnelle"],
    ["agoraphobie", "peur des espaces ouverts et des lieux publics"],
    ["claustration", "enfermement"],
    ["asile", "hôpital psychiatrique (terme historique)"],
    ["hospice", "établissement d'accueil"],
    ["traitement moral", "psychothérapie (approche de Pinel)"],
    ["isolement", "isolement thérapeutique (pratique historique)"],
    ["hydrothérapie", "traitement par l'eau (pratique historique)"],
    ["électrisation", "stimulation électrique (pratique historique)"],
  ];

  // Réécritures orthographiques et typographiques anciennes → modernes.
  var REGLES = [
    [/\boit\b/g, "ait"],
    [/\bétoit\b/gi, "était"],
    [/\bavoit\b/gi, "avait"],
    [/\bétoient\b/gi, "étaient"],
    [/\bavoient\b/gi, "avaient"],
    [/\bfaisoit\b/gi, "faisait"],
    [/\bpouvoit\b/gi, "pouvait"],
    [/\bdevoit\b/gi, "devait"],
    [/\bconnoissance\b/gi, "connaissance"],
    [/\bfoible\b/gi, "faible"],
    [/\bfoiblesse\b/gi, "faiblesse"],
    [/\bparoît\b/gi, "paraît"],
    [/\bparoissent\b/gi, "paraissent"],
    [/\bcroyoit\b/gi, "croyait"],
    [/\benfans\b/gi, "enfants"],
    [/\bparens\b/gi, "parents"],
    [/\bsavans\b/gi, "savants"],
    [/\bdifférens\b/gi, "différents"],
    [/\bsentimens\b/gi, "sentiments"],
    [/\bmouvemens\b/gi, "mouvements"],
    [/\bévénemens\b/gi, "événements"],
    [/\bphénomènes?\s+moraux\b/gi, "phénomènes psychologiques"],
    [/\btrès-([a-zàâçéèêëîïôûùüÿñæœ])/gi, "très $1"],
    [/\bpar-tout\b/gi, "partout"],
    [/\baujourd'-hui\b/gi, "aujourd'hui"],
    [/\blong-temps\b/gi, "longtemps"],
    [/\bpoëte\b/gi, "poète"],
    [/\bpoësie\b/gi, "poésie"],
    [/ſ/g, "s"],
  ];

  /* ------------------------------ Utilitaires ------------------------------ */

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      if (document.querySelector('script[src="' + src + '"]')) { resolve(); return; }
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = function () { reject(new Error("Impossible de charger " + src)); };
      document.head.appendChild(s);
    });
  }

  function status(html, busy) {
    el.status.innerHTML = (busy ? '<span class="spin"></span> ' : "") + html;
  }

  function escHtml(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  /* --------------------- Nettoyage et modernisation du texte ---------------- */

  function cleanRaw(txt) {
    return txt
      .replace(/\r/g, "")
      .replace(/([a-zàâçéèêëîïôûùüÿñæœ])-\n([a-zàâçéèêëîïôûùüÿñæœ])/gi, "$1$2") // césures
      .replace(/[ \t]+/g, " ")
      .replace(/\n{3,}/g, "\n\n")
      .replace(/ +\n/g, "\n")
      .trim();
  }

  function modernize(txt) {
    var out = escHtml(txt);
    REGLES.forEach(function (r) { out = out.replace(r[0], r[1]); });
    // Glossaire : du terme le plus long au plus court pour éviter les collisions.
    var sorted = LEXIQUE.slice().sort(function (a, b) { return b[0].length - a[0].length; });
    sorted.forEach(function (pair) {
      var re = new RegExp("\\b(" + pair[0].replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")\\b", "gi");
      out = out.replace(re, function (m) {
        return '<span class="modern" data-gloss="' + pair[1].replace(/"/g, "&quot;") + '">' + m + "</span>";
      });
    });
    return out;
  }

  /* ------------------------------- Rendu PDF ------------------------------- */

  function renderPage(num) {
    if (!state.doc) return;
    if (state.rendering) { state.pending = num; return; }
    state.rendering = true;
    state.doc.getPage(num).then(function (page) {
      var viewport = page.getViewport({ scale: state.scale });
      var canvas = el.canvas;
      var ctx = canvas.getContext("2d");
      var ratio = window.devicePixelRatio || 1;
      canvas.width = Math.floor(viewport.width * ratio);
      canvas.height = Math.floor(viewport.height * ratio);
      canvas.style.width = Math.floor(viewport.width) + "px";
      canvas.style.height = Math.floor(viewport.height) + "px";
      ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
      return page.render({ canvasContext: ctx, viewport: viewport }).promise.then(function () {
        state.rendering = false;
        if (state.pending !== null) { var p = state.pending; state.pending = null; renderPage(p); }
      });
    }).catch(function (err) {
      state.rendering = false;
      status("Erreur de rendu : " + err.message);
    });
    el.pageInput.value = num;
    el.pageTotal.textContent = "/ " + state.pages;
    saveBookmark();
    if (state.mode === "split") extractText(num);
  }

  function gotoPage(num) {
    num = Math.max(1, Math.min(state.pages || 1, num));
    state.page = num;
    renderPage(num);
  }

  /* ---------------------- Extraction du texte (natif / OCR) ---------------- */

  function extractText(num) {
    if (!state.doc) return;
    el.text.innerHTML = '<p class="ocr-note">Extraction du texte…</p>';
    el.badge.textContent = "…";
    el.badge.className = "pane-badge";
    state.doc.getPage(num).then(function (page) {
      return page.getTextContent();
    }).then(function (content) {
      var txt = "";
      var lastY = null;
      content.items.forEach(function (item) {
        if (lastY !== null && Math.abs(item.transform[5] - lastY) > 4) txt += "\n";
        txt += item.str;
        lastY = item.transform[5];
      });
      txt = cleanRaw(txt);
      if (txt.replace(/\s/g, "").length < 40) {
        el.badge.textContent = "Page image";
        el.badge.className = "pane-badge warn";
        el.text.innerHTML =
          '<p class="ocr-note">Cette page ne contient pas de couche texte : c\'est une <strong>image</strong> ' +
          '(planche gravée, page de titre, tableau, ou page restée blanche). ' +
          'Lance la reconnaissance optique pour en extraire le texte français, puis le moderniser ou le traduire.</p>';
        el.ocrBtn.disabled = false;
        el.ocrBtn.classList.add("primary");
        state.rawText = "";
      } else {
        el.badge.textContent = "Texte natif";
        el.badge.className = "pane-badge";
        state.rawText = txt;
        paintText();
        el.ocrBtn.disabled = false;
        el.ocrBtn.classList.remove("primary");
      }
    }).catch(function (err) {
      el.text.innerHTML = '<p class="ocr-note">Extraction impossible : ' + escHtml(err.message) + "</p>";
    });
  }

  function paintText() {
    if (!state.rawText) { el.text.innerHTML = '<p class="ocr-note">Aucun texte pour cette page.</p>'; return; }
    el.text.innerHTML = state.modernize ? modernize(state.rawText) : escHtml(state.rawText);
  }

  function runOCR() {
    if (!state.doc) return;
    el.ocrBtn.disabled = true;
    status("Chargement du moteur de reconnaissance optique (≈ 3 Mo, une seule fois)…", true);
    loadScript(TESSERACT_SRC).then(function () {
      status("Reconnaissance du texte en cours…", true);
      el.badge.textContent = "OCR en cours";
      el.badge.className = "pane-badge warn";
      el.text.innerHTML = '<p class="ocr-note">Analyse de l\'image page ' + state.page + "…</p>";
      return window.Tesseract.recognize(el.canvas, "fra", {
        logger: function (m) {
          if (m.status === "recognizing text") {
            var pct = Math.round(m.progress * 100);
            el.progFill.style.width = pct + "%";
            status("Reconnaissance du texte : " + pct + " %", true);
          } else if (m.status) {
            status(m.status + "…", true);
          }
        },
      });
    }).then(function (res) {
      el.progFill.style.width = "100%";
      state.rawText = cleanRaw(res.data.text || "");
      el.badge.textContent = "Texte reconnu (OCR)";
      el.badge.className = "pane-badge";
      paintText();
      status("Texte reconnu — " + state.rawText.split(/\s+/).filter(Boolean).length + " mots extraits de la page " + state.page + ".");
      el.ocrBtn.disabled = false;
      el.ocrBtn.classList.remove("primary");
      setTimeout(function () { el.progFill.style.width = "0"; }, 1200);
    }).catch(function (err) {
      status("Reconnaissance impossible : " + escHtml(err.message) + ". Vérifie ta connexion internet.");
      el.ocrBtn.disabled = false;
    });
  }

  /* -------------------------------- Traduction ----------------------------- */

  var LANGS = { fr: "français", en: "anglais", es: "espagnol", de: "allemand", it: "italien", pt: "portugais", ar: "arabe" };

  function translate() {
    if (!state.rawText) { status("Extrais d'abord le texte de la page (bouton OCR si c'est un scan)."); return; }
    var target = el.langSel.value;
    if (target === "fr") { paintText(); status("Le texte d'origine est déjà en français."); return; }

    var chunks = splitChunks(state.rawText, 480);
    status("Traduction vers " + LANGS[target] + " (" + chunks.length + " segments)…", true);
    var done = [];
    var i = 0;

    function next() {
      if (i >= chunks.length) {
        el.text.innerHTML = escHtml(done.join(" "));
        el.badge.textContent = "Traduit en " + LANGS[target];
        el.badge.className = "pane-badge warn";
        status("Traduction terminée. Traduction automatique : à vérifier pour un usage rigoureux.");
        el.progFill.style.width = "0";
        return;
      }
      el.progFill.style.width = Math.round((i / chunks.length) * 100) + "%";
      var url = "https://api.mymemory.translated.net/get?q=" + encodeURIComponent(chunks[i]) + "&langpair=fr|" + target;
      fetch(url)
        .then(function (r) { return r.json(); })
        .then(function (d) {
          var t = d && d.responseData && d.responseData.translatedText;
          done.push(t && !/MYMEMORY WARNING/i.test(t) ? t : chunks[i]);
          i++; next();
        })
        .catch(function () {
          status("Service de traduction indisponible. Le texte français d'origine reste affiché.");
          el.progFill.style.width = "0";
          paintText();
        });
    }
    next();
  }

  function splitChunks(txt, size) {
    var sentences = txt.split(/(?<=[.!?])\s+/);
    var chunks = [], buf = "";
    sentences.forEach(function (s) {
      if ((buf + " " + s).length > size && buf) { chunks.push(buf.trim()); buf = s; }
      else buf += " " + s;
    });
    if (buf.trim()) chunks.push(buf.trim());
    return chunks;
  }

  /* --------------------------- Marque-page local --------------------------- */

  function saveBookmark() {
    if (!state.book) return;
    try {
      var all = JSON.parse(localStorage.getItem("psy-bookmarks") || "{}");
      all[state.book] = state.page;
      localStorage.setItem("psy-bookmarks", JSON.stringify(all));
    } catch (e) { /* stockage indisponible */ }
  }

  function readBookmark(book) {
    try {
      var all = JSON.parse(localStorage.getItem("psy-bookmarks") || "{}");
      return all[book] || 1;
    } catch (e) { return 1; }
  }

  /* ------------------------------ Chargement ------------------------------- */

  function loadBook(path, label) {
    state.book = path;
    status("Ouverture de « " + label + " »…", true);
    el.text.innerHTML = '<p class="ocr-note">Chargement du livre…</p>';
    loadScript(PDFJS_SRC).then(function () {
      window.pdfjsLib.GlobalWorkerOptions.workerSrc = PDFJS_WORKER;
      return window.pdfjsLib.getDocument(path).promise;
    }).then(function (doc) {
      state.doc = doc;
      state.pages = doc.numPages;
      state.page = Math.min(readBookmark(path), doc.numPages);
      el.pageTotal.textContent = "/ " + state.pages;
      [el.prev, el.next, el.zoomIn, el.zoomOut, el.pageInput, el.splitBtn, el.ocrBtn].forEach(function (b) { b.disabled = false; });
      renderPage(state.page);
      status("« " + label + " » — " + state.pages + " pages. Tu peux tourner les pages, zoomer, extraire et moderniser le texte.");
      if (state.mode === "split") extractText(state.page);
    }).catch(function (err) {
      status("Impossible d'ouvrir ce livre : " + escHtml(err.message));
      el.text.innerHTML = '<p class="ocr-note">Le fichier est peut-être trop volumineux pour ta connexion, ou introuvable. ' +
        'Tu peux aussi le <a href="' + path + '" target="_blank" rel="noopener">télécharger directement</a>.</p>';
    });
  }

  /* -------------------------------- Init ----------------------------------- */

  function init() {
    var root = document.getElementById("reader-root");
    if (!root) return;

    el.canvas = document.getElementById("pdf-canvas");
    el.text = document.getElementById("reader-text");
    el.badge = document.getElementById("reader-badge");
    el.status = document.getElementById("reader-status");
    el.progFill = document.getElementById("reader-prog-fill");
    el.grid = document.getElementById("reader-grid");
    el.bookSel = document.getElementById("book-select");
    el.langSel = document.getElementById("lang-select");
    el.pageInput = document.getElementById("page-input");
    el.pageTotal = document.getElementById("page-total");
    el.prev = document.getElementById("btn-prev");
    el.next = document.getElementById("btn-next");
    el.zoomIn = document.getElementById("btn-zoom-in");
    el.zoomOut = document.getElementById("btn-zoom-out");
    el.splitBtn = document.getElementById("btn-split");
    el.ocrBtn = document.getElementById("btn-ocr");
    el.modernBtn = document.getElementById("btn-modern");
    el.transBtn = document.getElementById("btn-translate");
    el.dlBtn = document.getElementById("btn-download");

    el.prev.addEventListener("click", function () { gotoPage(state.page - 1); });
    el.next.addEventListener("click", function () { gotoPage(state.page + 1); });
    el.pageInput.addEventListener("change", function () { gotoPage(parseInt(el.pageInput.value, 10) || 1); });
    el.zoomIn.addEventListener("click", function () { state.scale = Math.min(3, state.scale + 0.2); renderPage(state.page); });
    el.zoomOut.addEventListener("click", function () { state.scale = Math.max(0.5, state.scale - 0.2); renderPage(state.page); });

    el.splitBtn.addEventListener("click", function () {
      state.mode = state.mode === "split" ? "page" : "split";
      el.grid.classList.toggle("split", state.mode === "split");
      el.splitBtn.classList.toggle("active", state.mode === "split");
      el.splitBtn.textContent = state.mode === "split" ? "📖 Masquer le texte" : "📖 Afficher le texte";
      if (state.mode === "split") extractText(state.page);
    });

    el.ocrBtn.addEventListener("click", runOCR);
    el.transBtn.addEventListener("click", translate);

    el.modernBtn.addEventListener("click", function () {
      state.modernize = !state.modernize;
      el.modernBtn.classList.toggle("active", state.modernize);
      el.modernBtn.textContent = state.modernize ? "✨ Français modernisé" : "✨ Moderniser le français";
      paintText();
    });

    el.bookSel.addEventListener("change", function () {
      var opt = el.bookSel.selectedOptions[0];
      if (!opt || !opt.value) return;
      el.dlBtn.href = opt.value;
      var url = new URL(window.location);
      url.searchParams.set("livre", opt.value);
      history.replaceState(null, "", url);
      loadBook(opt.value, opt.textContent);
    });

    // Info-bulle du glossaire de modernisation.
    var pop = null;
    el.text.addEventListener("mouseover", function (e) {
      var m = e.target.closest(".modern");
      if (!m) return;
      pop = document.createElement("div");
      pop.className = "lexique-pop";
      pop.textContent = m.dataset.gloss;
      document.body.appendChild(pop);
      var r = m.getBoundingClientRect();
      pop.style.left = Math.min(r.left, window.innerWidth - 300) + "px";
      pop.style.top = (r.bottom + 6) + "px";
    });
    el.text.addEventListener("mouseout", function (e) {
      if (e.target.closest(".modern") && pop) { pop.remove(); pop = null; }
    });

    document.addEventListener("keydown", function (e) {
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) return;
      if (document.querySelector(".search-overlay.open")) return;
      if (e.key === "ArrowRight") gotoPage(state.page + 1);
      else if (e.key === "ArrowLeft") gotoPage(state.page - 1);
    });

    // Ouverture directe via ?livre=chemin.pdf
    var wanted = new URLSearchParams(window.location.search).get("livre");
    if (wanted) {
      for (var i = 0; i < el.bookSel.options.length; i++) {
        if (el.bookSel.options[i].value === wanted) { el.bookSel.selectedIndex = i; break; }
      }
    }
    var sel = el.bookSel.selectedOptions[0];
    if (sel && sel.value) {
      el.dlBtn.href = sel.value;
      loadBook(sel.value, sel.textContent);
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
