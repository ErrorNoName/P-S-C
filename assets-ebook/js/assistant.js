/* ==========================================================================
   PSYCLOPÉDIA — Assistant ancré dans le corpus du site
   Recherche + synthèse en français. Aucun diagnostic. Aucune source inventée.
   ========================================================================== */

(function () {
  "use strict";

  var ROOT = document.body.getAttribute("data-root") || "./";
  var CORPUS_URL = ROOT + "livres-psychologie/07-ebook-final/ai-corpus.json";
  var INDEX_URL = ROOT + "livres-psychologie/07-ebook-final/search-index.json";
  var ASSIST_PAGE = ROOT + "livres-psychologie/07-ebook-final/assistant.html";

  var KIND_LABEL = {
    categorie: "Catégorie", section: "Section", notion: "Notion",
    experience: "Expérience", auteur: "Auteur", theorie: "Théorie",
    trouble: "Trouble", biais: "Biais", cas: "Cas", faq: "FAQ",
    mythe: "Idée reçue", metier: "Métier", lycee: "Lycée",
    branche: "Branche", oral: "Grand oral", page: "Page", quiz: "Quiz",
  };

  var STOP = {
    le:1, la:1, les:1, un:1, une:1, des:1, du:1, de:1, d:1, au:1, aux:1,
    et:1, ou:1, en:1, dans:1, sur:1, pour:1, par:1, avec:1, sans:1, que:1,
    qui:1, quoi:1, dont:1, est:1, sont:1, a:1, ont:1, ce:1, cet:1, cette:1,
    ces:1, ne:1, pas:1, plus:1, tres:1, comme:1, mais:1, donc:1, alors:1,
    comment:1, pourquoi:1, quel:1, quelle:1, quels:1, quelles:1, cest:1,
    qu:1, se:1, sa:1, son:1, ses:1, leur:1, leurs:1, je:1, tu:1, il:1,
    elle:1, on:1, nous:1, vous:1, ils:1, elles:1, y:1, ca:1, cela:1,
    etre:1, avoir:1, faire:1, peut:1, peuton:1,
  };

  var corpus = null;
  var loading = false;
  var history = [];

  function isAbs(url) { return /^https?:\/\//i.test(url || ""); }
  function hrefOf(url) { return isAbs(url) ? url : ROOT + url; }

  function norm(s) {
    return (s || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[''`]/g, " ")
      .replace(/[^a-z0-9 ]+/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function tokens(s) {
    return norm(s).split(" ").filter(function (w) {
      return w.length > 1 && !STOP[w];
    });
  }

  function esc(s) {
    return (s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function intentOf(q) {
    var n = norm(q);
    if (/(diagnost|trouble chez moi|suis-je|ai-je un|soigner|traitement|medicament|ordonnance)/.test(n)) {
      return "sante";
    }
    if (/(difference|vs|versus|ou bien|distinguer|comparer|plutot)/.test(n)) return "compare";
    if (/(specialite|parcoursup|grand oral|cio|licence de psycho|licence psycho)/.test(n)) {
      return "lycee";
    }
    if (/(c est quoi|cest quoi|qu est-ce|quest-ce|definir|definition|signifie)/.test(n)) {
      return "define";
    }
    if (/(qui est|qui a|quel auteur)/.test(n)) return "who";
    if (/(experience|experience de|protocole|milgram|asch|stroop)/.test(n)) return "xp";
    if (/(liste|quoi lire|par ou|par ou commencer|planning|semaine)/.test(n)) return "list";
    return "explain";
  }

  function scoreDoc(doc, terms) {
    var title = doc._nt || (doc._nt = norm(doc.t));
    var body = doc._nx || (doc._nx = norm((doc.x || doc.d || "") + " " + (doc.g || "")));
    var total = 0;
    for (var i = 0; i < terms.length; i++) {
      var t = terms[i];
      var best = 0;
      if (title === t) best = 130;
      else if (title.indexOf(t) === 0) best = 95;
      else if (title.indexOf(t) !== -1) best = 70;
      else if (body.indexOf(t) !== -1) best = 22;
      if (best === 0) return 0;
      total += best;
    }
    if (doc.k === "notion" || doc.k === "branche" || doc.k === "categorie") total += 8;
    if (doc.k === "lycee") total += 6;
    return total;
  }

  function search(query, limit) {
    var terms = tokens(query);
    if (!terms.length || !corpus) return [];
    var out = [];
    for (var i = 0; i < corpus.length; i++) {
      var sc = scoreDoc(corpus[i], terms);
      if (sc > 0) out.push({ e: corpus[i], s: sc });
    }
    out.sort(function (a, b) { return b.s - a.s; });
    return out.slice(0, limit || 8);
  }

  function firstSentences(text, n) {
    var parts = (text || "").replace(/([.!?])\s+/g, "$1|").split("|");
    return parts.slice(0, n || 2).join(" ");
  }

  function uniqueByTitle(hits) {
    var seen = {};
    var out = [];
    hits.forEach(function (h) {
      var k = norm(h.e.t);
      if (seen[k]) return;
      seen[k] = 1;
      out.push(h);
    });
    return out;
  }

  function synthesize(query, hits) {
    var intent = intentOf(query);
    if (intent === "sante") {
      return {
        lead: "Je ne peux pas poser de diagnostic ni conseiller un traitement.",
        parts: [
          "Psyclopédia est une encyclopédie pédagogique. Un quiz, une fiche ou une réponse d'assistant ne remplacent pas un professionnel.",
          "Si tu vas mal, ou si tu t'inquiètes pour quelqu'un : écoute sans étiqueter, ne reste pas seul, oriente vers un adulte et les numéros d'aide.",
        ],
        recap: ["Page Aide du site", "3114 (prévention suicide)", "15 / 112 en urgence"],
        follow: ["Qu'est-ce qu'un CMP ?", "Différence psychologue et psychiatre ?", "C'est quoi l'alliance thérapeutique ?"],
        extraHref: ROOT + "livres-psychologie/07-ebook-final/aide.html",
        extraLabel: "Ouvrir Aide et ressources",
      };
    }

    if (!hits.length) {
      return {
        lead: "Je n'ai pas trouvé cette notion dans le site.",
        parts: [
          "Essaie un synonyme, un nom d'auteur (Piaget, Milgram, Loftus) ou le nom d'une branche (clinique, sociale, développement, cognitive).",
          "La recherche classique (Ctrl + K) parcourt le même corpus, fiche par fiche.",
        ],
        recap: [],
        follow: ["Quelles spécialités préparent une licence de psychologie ?", "C'est quoi la psychologie cognitive ?", "Différence des quatre branches"],
      };
    }

    hits = uniqueByTitle(hits);
    var top = hits[0].e;
    var lead = firstSentences(top.x || top.d, 2);
    if (intent === "define") {
      lead = top.t + " — " + firstSentences(top.x || top.d, 2);
    }
    if (intent === "compare" && hits.length > 1) {
      lead = "Pour distinguer clairement : " + hits[0].e.t + " n'est pas " + hits[1].e.t + ".";
    }

    var parts = [];
    var used = {};
    hits.slice(0, 5).forEach(function (h) {
      var key = norm(h.e.t);
      if (used[key]) return;
      used[key] = 1;
      var bit = firstSentences(h.e.x || h.e.d, 2);
      if (bit && bit !== lead) {
        parts.push(h.e.t + ". " + bit);
      }
    });
    if (!parts.length) parts.push(firstSentences(top.x || top.d, 3));

    if (intent === "lycee") {
      parts.push("Il n'y a pas de spécialité Psychologie au bac. On prépare via SES, HLP, SVT, maths, HGGSP et la philo de Terminale ; le CIO et les PsyEN orientent vers une licence.");
    }

    var recap = hits.slice(0, 4).map(function (h) {
      return h.e.t;
    });

    var follow = [];
    if (hits[1]) follow.push("Approfondir : " + hits[1].e.t);
    if (hits[2]) follow.push("Lien : " + hits[2].e.t);
    follow.push("Ouvre Métiers et études");
    follow.push("Compare les quatre branches");

    return { lead: lead, parts: parts.slice(0, 4), recap: recap, follow: follow.slice(0, 4) };
  }

  function renderAnswer(box, query, hits, syn) {
    var sources = uniqueByTitle(hits).slice(0, 6).map(function (h) {
      return '<a class="ai-src" href="' + hrefOf(h.e.u) + '"' +
        (isAbs(h.e.u) ? ' target="_blank" rel="noopener"' : "") + ">" +
        "<strong>" + esc(h.e.t) + "</strong>" +
        "<span>" + esc(KIND_LABEL[h.e.k] || h.e.k) + "</span></a>";
    }).join("");

    var recap = syn.recap.length
      ? "<ul>" + syn.recap.map(function (r) { return "<li>" + esc(r) + "</li>"; }).join("") + "</ul>"
      : "";

    var follow = syn.follow.map(function (f) {
      return '<button type="button" class="ai-chip" data-ai-q="' + esc(f.replace(/^Approfondir : |^Lien : /, "")) + '">' + esc(f) + "</button>";
    }).join("");

    var extra = syn.extraHref
      ? '<p><a class="btn btn-primary" href="' + syn.extraHref + '">' + esc(syn.extraLabel) + "</a></p>"
      : "";

    box.innerHTML =
      '<article class="ai-answer">' +
        "<p class=\"ai-q\">« " + esc(query) + " »</p>" +
        "<h3>Réponse</h3>" +
        "<p class=\"ai-lead\">" + esc(syn.lead) + "</p>" +
        syn.parts.map(function (p) { return "<p>" + esc(p) + "</p>"; }).join("") +
        (recap ? "<h4>À retenir</h4>" + recap : "") +
        extra +
        "<h4>Pages du site</h4>" +
        "<div class=\"ai-sources\">" + (sources || "<p>Aucune source interne.</p>") + "</div>" +
        "<h4>Continuer</h4>" +
        "<div class=\"ai-chips\">" + follow + "</div>" +
      "</article>";
    bindChips(box);
  }

  function ensureCorpus(cb) {
    if (corpus) { cb(); return; }
    if (loading) return;
    loading = true;
    Promise.all([
      fetch(CORPUS_URL).then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; }),
      fetch(INDEX_URL).then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; }),
    ]).then(function (pair) {
      var rich = pair[0] || [];
      var idx = (pair[1] || []).map(function (e) {
        return { t: e.t, k: e.k, u: e.u, x: e.d, g: e.g || "" };
      });
      corpus = rich.concat(idx);
      loading = false;
      cb();
    }).catch(function () {
      loading = false;
      cb();
    });
  }

  function ask(box, query) {
    query = (query || "").trim();
    if (!query) return;
    var out = box.querySelector("[data-ai-out]");
    out.innerHTML = '<div class="ai-empty"><span class="spin"></span> Lecture du site…</div>';
    ensureCorpus(function () {
      if (!corpus || !corpus.length) {
        out.innerHTML = '<div class="ai-empty">Corpus indisponible. Ouvre le site via GitHub Pages ou un serveur local.</div>';
        return;
      }
      var hits = search(query, 10);
      var syn = synthesize(query, hits);
      history.push(query);
      renderAnswer(out, query, hits, syn);
    });
  }

  function bindChips(root) {
    root.querySelectorAll("[data-ai-q]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var q = btn.getAttribute("data-ai-q");
        var box = btn.closest("[data-ai-root]") || document.querySelector("[data-ai-root]");
        var input = box && box.querySelector("[data-ai-input]");
        if (input) input.value = q;
        if (box) ask(box, q);
      });
    });
  }

  function mountPage() {
    var box = document.querySelector("[data-ai-root]");
    if (!box) return;
    var form = box.querySelector("[data-ai-form]");
    var input = box.querySelector("[data-ai-input]");
    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        ask(box, input.value);
      });
    }
    bindChips(box);
    var pre = new URLSearchParams(location.search).get("q");
    if (pre) {
      if (input) input.value = pre;
      ask(box, pre);
    }
  }

  function openOverlay(prefill) {
    var ov = document.querySelector(".ai-overlay");
    if (!ov) {
      ov = document.createElement("div");
      ov.className = "ai-overlay";
      ov.innerHTML =
        '<div class="ai-modal" role="dialog" aria-label="Assistant Psyclopédia" data-ai-root>' +
          '<div class="ai-modal-head">' +
            "<strong>Assistant du site</strong>" +
            '<a href="' + ASSIST_PAGE + '">Plein écran</a>' +
            '<button type="button" class="ai-close" data-ai-close>Fermer</button>' +
          "</div>" +
          '<form class="ai-form" data-ai-form>' +
            '<textarea data-ai-input rows="2" placeholder="Une question sur tout le site…"></textarea>' +
            '<button type="submit" class="btn btn-primary">Répondre</button>' +
          "</form>" +
          '<div class="ai-out" data-ai-out><div class="ai-empty">Réponse sourcée à partir de Psyclopédia uniquement.</div></div>' +
        "</div>";
      document.body.appendChild(ov);
      ov.addEventListener("click", function (e) {
        if (e.target === ov || e.target.closest("[data-ai-close]")) ov.classList.remove("open");
      });
      ov.querySelector("[data-ai-form]").addEventListener("submit", function (e) {
        e.preventDefault();
        ask(ov.querySelector("[data-ai-root]"), ov.querySelector("[data-ai-input]").value);
      });
    }
    ov.classList.add("open");
    var input = ov.querySelector("[data-ai-input]");
    if (prefill) input.value = prefill;
    input.focus();
    if (prefill) ask(ov.querySelector("[data-ai-root]"), prefill);
  }

  function injectFab() {
    if (document.querySelector(".ai-fab")) return;
    var a = document.createElement("a");
    a.className = "ai-fab";
    a.href = ASSIST_PAGE;
    a.setAttribute("aria-label", "Assistant IA du site");
    a.innerHTML = "<span aria-hidden=\"true\">🤖</span><span>IA</span>";
    a.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey) return;
      e.preventDefault();
      openOverlay("");
    });
    document.body.appendChild(a);
  }

  window.addEventListener("keydown", function (e) {
    var isJ = e.key === "j" || e.key === "J" || e.code === "KeyJ";
    if ((e.ctrlKey || e.metaKey) && isJ && !e.altKey) {
      e.preventDefault();
      e.stopPropagation();
      openOverlay("");
    }
  }, true);

  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-ai-open]");
    if (t) {
      e.preventDefault();
      openOverlay(t.getAttribute("data-ai-open") || "");
    }
  });

  injectFab();
  mountPage();
  window.PsyAssistant = { ask: function (q) { openOverlay(q || ""); }, open: openOverlay };
})();
