/* ==========================================================================
   PSYCLOPÉDIA — Assistant ancré dans le corpus du site
   Recherche + synthèse en français. Aucun diagnostic. Aucune source inventée.
   ========================================================================== */

(function () {
  "use strict";

  var hasDom = typeof document !== "undefined" && document.body;
  var ROOT = hasDom ? (document.body.getAttribute("data-root") || "./") : "./";
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
    etre:1, avoir:1, faire:1, peut:1, peuton:1, veux:1, veut:1, voulais:1,
    voudrais:1, savoir:1, sais:1, cherche:1, chercher:1, trouve:1, trouver:1,
    donne:1, donner:1, explique:1, expliquer:1, parle:1, parler:1, dis:1,
    dire:1, montre:1, montrer:1, besoin:1, aimerais:1, peux:1, pourrais:1,
    merci:1, bonjour:1, salut:1, stp:1, svp:1, juste:1, vraiment:1, aussi:1,
    bien:1, mal:1, fait:1, suis:1, vais:1, aller:1, moi:1, me:1, te:1,
    concernant:1, propos:1, sujet:1, info:1, infos:1, resultat:1, resultats:1,
    contenu:1, page:1, pages:1, site:1, encyclopedie:1, psyclopedia:1,
    psychopedia:1, sil:1, plait:1, tout:1, toute:1, toutes:1, tous:1,
    quelque:1, quelques:1, chose:1, choses:1, c:1, j:1, l:1, n:1, m:1, t:1,
    ai:1, as:1, es:1, ouvrir:1, voir:1, dit:1, rien:1, vrai:1, faux:1,
    entre:1, selon:1, chez:1, apres:1, avant:1, sous:1, vers:1, lors:1,
    quand:1, lorsque:1, afin:1, ainsi:1, puis:1, encore:1, seulement:1,
    depuis:1, pendant:1, chaque:1, autre:1, autres:1, meme:1, ici:1,
  };

  var WEAK = { psychologie:1, psycho:1, psychologique:1, humain:1, humaine:1, personne:1, gens:1 };

  var SYN = {
    memoire: ["souvenir", "rappel", "oubli", "mnesique", "empan"],
    souvenir: ["memoire", "rappel"],
    oubli: ["memoire", "ebbinghaus"],
    attention: ["selective", "cocktail", "dichotique"],
    bebe: ["nourrisson", "enfant"],
    nourrisson: ["bebe", "enfant"],
    enfant: ["developpement", "piaget", "bebe"],
    piaget: ["stade", "developpement", "conservation"],
    stade: ["piaget", "developpement"],
    milgram: ["obeissance", "autorite"],
    obeissance: ["milgram", "autorite"],
    asch: ["conformite", "conformisme"],
    conformite: ["asch"],
    freud: ["psychanalyse", "inconscient", "reve"],
    psychanalyse: ["freud", "inconscient"],
    inconscient: ["freud", "psychanalyse"],
    bowlby: ["attachement", "ainsworth"],
    ainsworth: ["attachement", "bowlby"],
    attachement: ["bowlby", "ainsworth"],
    baddeley: ["memoire", "empan", "travail"],
    empan: ["memoire", "miller", "baddeley"],
    miller: ["empan", "memoire"],
    biais: ["heuristique", "kahneman"],
    heuristique: ["biais", "kahneman"],
    kahneman: ["biais", "heuristique"],
    cerveau: ["neurone", "lobe", "hippocampe"],
    emotion: ["sentiment", "peur"],
    personnalite: ["ocean", "trait"],
    clinique: ["entretien", "psychologue"],
    psychologue: ["clinique", "titre"],
    therapie: ["tcc", "beck", "rogers"],
    tcc: ["beck", "therapie", "cognitif"],
    variable: ["independante", "dependante", "hypothese"],
    hypothese: ["methode", "variable", "scientifique"],
    scientifique: ["methode", "experience", "protocole"],
    sommeil: ["reve"],
    reve: ["freud", "sommeil"],
    langage: ["broca", "wernicke"],
    intelligence: ["binet", "qi"],
    stress: ["anxiete", "yerkes"],
    anxiete: ["stress", "peur"],
    groupe: ["social", "foule", "conformite"],
    apprentissage: ["conditionnement", "skinner", "pavlov"],
    conditionnement: ["pavlov", "skinner"],
    pavlov: ["conditionnement", "chien"],
    skinner: ["conditionnement", "renforcement"],
    cours: ["seance", "cm", "td"],
    notification: ["rappel", "alerte"],
    discord: ["communaute"],
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
    var seen = {};
    return norm(s).split(" ").filter(function (w) {
      if (w.length < 2 || STOP[w] || seen[w]) return false;
      seen[w] = 1;
      return true;
    });
  }

  function editDistance(a, b, max) {
    if (a === b) return 0;
    if (Math.abs(a.length - b.length) > max) return max + 1;
    var prev = new Array(b.length + 1);
    var cur = new Array(b.length + 1);
    var j, i, k;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur[0] = i;
      var best = cur[0];
      for (k = 1; k <= b.length; k++) {
        var cost = a.charCodeAt(i - 1) === b.charCodeAt(k - 1) ? 0 : 1;
        cur[k] = Math.min(cur[k - 1] + 1, prev[k] + 1, prev[k - 1] + cost);
        if (cur[k] < best) best = cur[k];
      }
      if (best > max) return max + 1;
      var tmp = prev; prev = cur; cur = tmp;
    }
    return prev[b.length];
  }

  function tolerance(len) {
    if (len < 5) return 0;
    if (len < 8) return 1;
    return 2;
  }

  function prefixHit(word, term) {
    if (WEAK[word] || WEAK[term]) return false;
    var n = 0;
    var m = Math.min(word.length, term.length);
    var longer = Math.max(word.length, term.length);
    for (var i = 0; i < m; i++) {
      if (word.charCodeAt(i) !== term.charCodeAt(i)) break;
      n++;
    }
    if (n < 5) return false;
    return n / longer >= 0.8;
  }

  function wordHit(words, term) {
    var tol = tolerance(term.length);
    for (var i = 0; i < words.length; i++) {
      var w = words[i];
      if (!w || w.length < 3 || WEAK[w]) continue;
      if (w === term) return 40;
      if (term.length >= 5 && (w.indexOf(term) === 0 || (term.indexOf(w) === 0 && w.length >= 5))) return 28;
      if (prefixHit(w, term)) return 24;
      if (tol > 0 && Math.abs(w.length - term.length) <= tol && editDistance(w, term, tol) <= tol) return 22;
    }
    return 0;
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

  function fieldWords(doc) {
    if (doc._words) return doc._words;
    var title = doc._nt || (doc._nt = norm(doc.t));
    var keys = doc._nk || (doc._nk = norm(doc.g || ""));
    doc._words = (title + " " + keys).split(" ").filter(Boolean);
    return doc._words;
  }

  function hasWord(hay, term) {
    if (!hay || !term) return false;
    if (term.length >= 6) return hay.indexOf(term) !== -1;
    return (" " + hay + " ").indexOf(" " + term + " ") !== -1;
  }

  function termScore(doc, term) {
    var title = doc._nt || (doc._nt = norm(doc.t));
    var body = doc._nx || (doc._nx = norm((doc.x || doc.d || "") + " " + (doc.g || "")));
    var best = 0;
    if (title === term) best = 140;
    else if (hasWord(title, term) && title.indexOf(term) === 0) best = 100;
    else if (hasWord(title, term)) best = 78;
    else if (hasWord(body, term)) best = 26;
    if (best < 40) {
      var fuzzy = wordHit(fieldWords(doc), term);
      if (fuzzy > best) best = fuzzy;
    }
    var alts = SYN[term] || [];
    for (var i = 0; i < alts.length && best < 70; i++) {
      var alt = alts[i];
      var altScore = 0;
      if (hasWord(title, alt)) altScore = 48;
      else if (hasWord(body, alt)) altScore = 18;
      if (altScore > best) best = altScore;
    }
    if (WEAK[term]) best = Math.min(best, 12);
    return best;
  }

  function scoreDoc(doc, terms) {
    var total = 0;
    var matched = 0;
    for (var j = 0; j < terms.length; j++) {
      var sc = termScore(doc, terms[j]);
      if (sc > 0) matched += 1;
      total += sc;
    }
    if (!matched) return 0;
    var coverage = matched / terms.length;
    total = total * coverage;
    if (coverage === 1) total += 28;
    if (doc.k === "notion" || doc.k === "experience" || doc.k === "mythe" || doc.k === "branche") total += 6;
    if (doc.k === "categorie" || doc.k === "section") total += 4;
    var phrase = terms.join(" ");
    var title = doc._nt || "";
    if (phrase.length > 6 && title.indexOf(phrase) !== -1) total += 36;
    for (var k = 0; k < terms.length; k++) {
      if (title === terms[k]) total += 48;
    }
    return total;
  }

  function search(query, limit) {
    var terms = tokens(query);
    if (!terms.length || !corpus) return [];
    var out = [];
    var seen = {};
    for (var i = 0; i < corpus.length; i++) {
      var sc = scoreDoc(corpus[i], terms);
      if (sc < 18) continue;
      var key = norm(corpus[i].t) || corpus[i].u;
      if (seen[key] && seen[key] >= sc) continue;
      seen[key] = sc;
      out.push({ e: corpus[i], s: sc });
    }
    var bestBy = {};
    out.forEach(function (h) {
      var key = norm(h.e.t) || h.e.u;
      if (!bestBy[key] || bestBy[key].s < h.s) bestBy[key] = h;
    });
    var uniq = [];
    Object.keys(bestBy).forEach(function (k) { uniq.push(bestBy[k]); });
    uniq.sort(function (a, b) { return b.s - a.s; });
    return uniq.slice(0, limit || 8);
  }

  function sentences(text) {
    return (text || "").replace(/([.!?])\s+/g, "$1|").split("|").map(function (s) {
      return s.trim();
    }).filter(Boolean);
  }

  function firstSentences(text, n) {
    return sentences(text).slice(0, n || 2).join(" ");
  }

  function bestSentence(doc, terms) {
    var parts = sentences(doc.x || doc.d || "");
    if (!parts.length) return firstSentences(doc.x || doc.d || "", 2);
    var best = parts[0];
    var bestSc = -1;
    parts.forEach(function (p) {
      var n = norm(p);
      var sc = 0;
      terms.forEach(function (t) {
        if (n.indexOf(t) !== -1) sc += 3;
        var alts = SYN[t] || [];
        for (var i = 0; i < alts.length; i++) {
          if (n.indexOf(alts[i]) !== -1) sc += 1;
        }
      });
      if (p.length > 280) sc -= 1;
      if (sc > bestSc) { bestSc = sc; best = p; }
    });
    return best;
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
    var qTerms = tokens(query);
    var top = hits[0].e;
    var lead = bestSentence(top, qTerms);
    if (intent === "define") {
      lead = top.t + " — " + bestSentence(top, qTerms);
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
      var bit = bestSentence(h.e, qTerms);
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
      var byUrl = {};
      var order = [];
      function absorb(e) {
        if (!e || !e.t) return;
        var key = e.u || e.t;
        if (!byUrl[key]) {
          byUrl[key] = e;
          order.push(key);
          return;
        }
        var prev = byUrl[key];
        var prevLen = (prev.x || prev.d || "").length;
        var nextLen = (e.x || e.d || "").length;
        if (nextLen > prevLen) byUrl[key] = e;
        if (e.g && byUrl[key] && !byUrl[key].g) byUrl[key].g = e.g;
      }
      rich.forEach(absorb);
      idx.forEach(absorb);
      corpus = order.map(function (k) { return byUrl[k]; });
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

  if (hasDom) {
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
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = {
      searchWith: function (docs, q, limit) {
        corpus = docs;
        return search(q, limit || 5);
      },
      tokens: function (q) { return tokens(q); },
    };
  }
})();
