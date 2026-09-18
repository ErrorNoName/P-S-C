/* =============================================================================
   PSYCLOPÉDIA — Laboratoire
   Sept mini-expériences jouables dans le navigateur. Chaque expérience expose
   une fonction init(stage, onDone) où `stage` est le conteneur et `onDone`
   reçoit le tableau de lignes de résultat à afficher.

   Avertissement assumé : un navigateur n'est pas un chronomètre de laboratoire.
   Les temps mesurés incluent la latence de l'écran, de la souris et du moteur
   de rendu. Les ordres de grandeur restent parlants, les valeurs absolues non.
   ============================================================================= */

(function () {
  "use strict";

  var stage = document.querySelector("[data-lab]");
  if (!stage) return;
  var labId = stage.getAttribute("data-lab");
  var resultBox = document.getElementById("lab-result");

  // ---------------------------------------------------------------- utilitaires

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html !== undefined) n.innerHTML = html;
    return n;
  }

  function clear() {
    stage.innerHTML = "";
  }

  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function mean(arr) {
    if (!arr.length) return 0;
    return arr.reduce(function (s, v) { return s + v; }, 0) / arr.length;
  }

  function sd(arr) {
    if (arr.length < 2) return 0;
    var m = mean(arr);
    return Math.sqrt(arr.reduce(function (s, v) { return s + (v - m) * (v - m); }, 0) / (arr.length - 1));
  }

  function showResults(lines, comment) {
    if (!resultBox) return;
    var rows = lines.map(function (l) {
      return "<tr><td>" + l[0] + "</td><td>" + l[1] + "</td></tr>";
    }).join("");
    resultBox.innerHTML =
      '<h3 style="font-family:var(--serif);font-size:1.15rem;margin-bottom:0.9rem">📊 Vos résultats</h3>' +
      '<table class="lab-result-table">' + rows + "</table>" +
      (comment ? '<p style="margin-top:1rem;font-size:0.88rem;line-height:1.7;color:var(--gris)">' + comment + "</p>" : "") +
      '<div class="cta-row" style="margin-top:1.2rem">' +
      '<button class="btn btn-secondary" onclick="window.location.reload()">↻ Recommencer</button>' +
      "</div>";
    resultBox.style.display = "block";
    resultBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function startButton(label, fn) {
    clear();
    var b = el("button", "btn btn-primary", label);
    b.addEventListener("click", fn);
    stage.appendChild(b);
  }

  // ------------------------------------------------------------------- Stroop

  var STROOP_COULEURS = [
    { nom: "ROUGE", hex: "#C7395D" },
    { nom: "VERT", hex: "#50A67E" },
    { nom: "BLEU", hex: "#3A6EA5" },
    { nom: "ORANGE", hex: "#E3AE33" }
  ];

  function runStroop() {
    var essais = [];
    var i;
    for (i = 0; i < 10; i++) essais.push({ congruent: true });
    for (i = 0; i < 10; i++) essais.push({ congruent: false });
    essais = shuffle(essais).map(function (e) {
      var mot = STROOP_COULEURS[Math.floor(Math.random() * 4)];
      var encre = mot;
      if (!e.congruent) {
        var autres = STROOP_COULEURS.filter(function (c) { return c.nom !== mot.nom; });
        encre = autres[Math.floor(Math.random() * autres.length)];
      }
      return { mot: mot.nom, encre: encre, congruent: e.congruent };
    });

    var idx = 0, t0 = 0;
    var data = { cong: [], incong: [], erreurs: 0 };

    function afficher() {
      if (idx >= essais.length) return fin();
      clear();
      var e = essais[idx];
      var progress = el("p", "rev-tag", "Essai " + (idx + 1) + " / " + essais.length);
      var mot = el("div", "lab-word", e.mot);
      mot.style.color = e.encre.hex;
      var consigne = el("p", "lab-prompt", "Cliquez sur la <strong>couleur de l'encre</strong>.");
      var choices = el("div", "lab-choices");
      STROOP_COULEURS.forEach(function (c) {
        var b = el("button", "lab-choice", c.nom.charAt(0) + c.nom.slice(1).toLowerCase());
        b.style.borderColor = c.hex;
        b.addEventListener("click", function () { repondre(c.nom); });
        choices.appendChild(b);
      });
      stage.appendChild(progress);
      stage.appendChild(mot);
      stage.appendChild(consigne);
      stage.appendChild(choices);
      t0 = performance.now();
    }

    function repondre(nom) {
      var rt = performance.now() - t0;
      var e = essais[idx];
      if (nom !== e.encre.nom) data.erreurs++;
      else (e.congruent ? data.cong : data.incong).push(rt);
      idx++;
      afficher();
    }

    function fin() {
      clear();
      stage.appendChild(el("p", "lab-prompt", "✅ Terminé. Regardez la différence entre les deux conditions."));
      var mc = Math.round(mean(data.cong));
      var mi = Math.round(mean(data.incong));
      var diff = mi - mc;
      showResults([
        ["Temps moyen — mot et encre identiques", mc + " ms"],
        ["Temps moyen — mot et encre différents", mi + " ms"],
        ["Interférence Stroop", (diff > 0 ? "+" : "") + diff + " ms"],
        ["Erreurs", data.erreurs + " / " + essais.length]
      ], diff > 0
        ? "Vous avez été plus lent quand le mot contredisait l'encre : c'est l'interférence attendue. Ce coût correspond au travail d'inhibition de la lecture automatique."
        : "Vous n'avez pas montré d'interférence sur cet essai. Cela arrive : avec seulement dix essais par condition, le bruit de mesure dépasse facilement l'effet. C'est précisément pourquoi une vraie expérience en utilise des centaines, sur des dizaines de participants.");
    }

    startButton("▶ Commencer les 20 essais", afficher);
  }

  // -------------------------------------------------------------------- Empan

  function runEmpan() {
    var longueur = 3, echecs = 0, meilleur = 0, historique = [];

    function nouvelleSuite() {
      var s = "";
      for (var i = 0; i < longueur; i++) s += Math.floor(Math.random() * 10);
      return s;
    }

    function manche() {
      clear();
      var suite = nouvelleSuite();
      stage.appendChild(el("p", "rev-tag", "Longueur " + longueur + " chiffres"));
      var aff = el("div", "lab-big", suite);
      stage.appendChild(aff);
      stage.appendChild(el("p", "lab-prompt", "Mémorisez, sans noter."));
      var duree = 900 + longueur * 350;
      setTimeout(function () { demander(suite); }, duree);
    }

    function demander(suite) {
      clear();
      stage.appendChild(el("p", "rev-tag", "Saisissez la suite dans l'ordre"));
      var input = el("input");
      input.type = "text";
      input.inputMode = "numeric";
      input.autocomplete = "off";
      input.className = "lab-slider";
      input.style.cssText = "font-family:var(--serif);font-size:1.8rem;text-align:center;letter-spacing:0.25em;" +
        "padding:0.6rem;border:1px solid var(--border);border-radius:10px;width:100%;max-width:340px";
      var b = el("button", "btn btn-primary", "Valider");
      function valider() {
        var ok = input.value.replace(/\D/g, "") === suite;
        historique.push({ n: longueur, ok: ok });
        if (ok) {
          meilleur = Math.max(meilleur, longueur);
          echecs = 0;
          longueur++;
          if (longueur > 14) return fin();
          manche();
        } else {
          echecs++;
          if (echecs >= 2) return fin();
          manche();
        }
      }
      b.addEventListener("click", valider);
      input.addEventListener("keydown", function (e) { if (e.key === "Enter") valider(); });
      stage.appendChild(input);
      stage.appendChild(b);
      input.focus();
    }

    function fin() {
      clear();
      stage.appendChild(el("p", "lab-prompt", "✅ Terminé."));
      var reussies = historique.filter(function (h) { return h.ok; }).length;
      showResults([
        ["Votre empan (plus longue suite réussie)", meilleur + " chiffres"],
        ["Suites réussies", reussies + " / " + historique.length],
        ["Repère : moyenne adulte en empan de chiffres", "6 à 7"],
        ["Repère : capacité sans regroupement", "≈ 4 unités"]
      ], meilleur >= 7
        ? "Au-dessus de la moyenne. Il y a de fortes chances que vous ayez regroupé les chiffres en unités plus grandes — dates, numéros connus, rythmes. C'est exactement la stratégie qui fait la différence."
        : "Un résultat dans les normes. Essayez une seconde fois en regroupant volontairement les chiffres deux par deux ou en cherchant des dates : l'empan apparent augmente souvent de deux à trois chiffres.");
    }

    startButton("▶ Commencer", manche);
  }

  // ------------------------------------------------------------ Temps de réaction

  function runReaction() {
    var temps = [], essai = 0, total = 5, t0 = 0, timer = null, pret = false;

    function manche() {
      clear();
      stage.appendChild(el("p", "rev-tag", "Essai " + (essai + 1) + " / " + total));
      var zone = el("div", "lab-target wait", "Attendez le vert…");
      stage.appendChild(zone);
      stage.appendChild(el("p", "lab-prompt", "Cliquez dès que la zone devient verte."));
      pret = false;
      var delai = 1200 + Math.random() * 2800;
      timer = setTimeout(function () {
        pret = true;
        zone.className = "lab-target go";
        zone.textContent = "MAINTENANT !";
        t0 = performance.now();
      }, delai);
      zone.addEventListener("click", function () {
        if (!pret) {
          clearTimeout(timer);
          zone.className = "lab-target wait";
          zone.textContent = "Trop tôt — essai annulé";
          setTimeout(manche, 1100);
          return;
        }
        temps.push(performance.now() - t0);
        essai++;
        if (essai >= total) return fin();
        setTimeout(manche, 600);
      });
    }

    function fin() {
      clear();
      stage.appendChild(el("p", "lab-prompt", "✅ Terminé."));
      var m = Math.round(mean(temps));
      var e = Math.round(sd(temps));
      var best = Math.round(Math.min.apply(null, temps));
      showResults([
        ["Temps moyen", m + " ms"],
        ["Meilleur essai", best + " ms"],
        ["Variabilité (écart-type)", e + " ms"],
        ["Repère adulte reposé (visuel)", "200 à 280 ms"]
      ], e > 60
        ? "Votre variabilité est élevée : d'un essai à l'autre, votre attention n'était pas au même niveau. C'est normal sur cinq essais, et c'est aussi le marqueur que les chercheurs surveillent pour détecter la fatigue et les relâchements attentionnels."
        : "Vos essais sont réguliers, signe d'une attention stable pendant la tâche. Notez que votre écran et votre souris ajoutent leur propre latence : la valeur absolue compte moins que la comparaison de vos propres essais entre eux.");
    }

    startButton("▶ Commencer", manche);
  }

  // -------------------------------------------------------------- Müller-Lyer

  function runMullerLyer() {
    clear();
    var cible = 260;
    var reglage = 150 + Math.floor(Math.random() * 90);

    var wrap = el("div");
    wrap.style.cssText = "width:100%;display:flex;flex-direction:column;align-items:center;gap:1rem";
    var svgNS = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("viewBox", "0 0 460 190");
    svg.setAttribute("class", "lab-svg");
    svg.style.width = "100%";
    svg.style.maxWidth = "460px";

    function fleche(y, longueur, sortante) {
      var g = document.createElementNS(svgNS, "g");
      var x0 = 230 - longueur / 2, x1 = 230 + longueur / 2;
      var ligne = document.createElementNS(svgNS, "line");
      ligne.setAttribute("x1", x0); ligne.setAttribute("y1", y);
      ligne.setAttribute("x2", x1); ligne.setAttribute("y2", y);
      ligne.setAttribute("stroke", "#1C1E1D"); ligne.setAttribute("stroke-width", "3");
      g.appendChild(ligne);
      var d = sortante ? -1 : 1;
      [[x0, 1], [x1, -1]].forEach(function (p) {
        [-1, 1].forEach(function (sens) {
          var l = document.createElementNS(svgNS, "line");
          l.setAttribute("x1", p[0]); l.setAttribute("y1", y);
          l.setAttribute("x2", p[0] + p[1] * d * 22); l.setAttribute("y2", y + sens * 22);
          l.setAttribute("stroke", "#1C1E1D"); l.setAttribute("stroke-width", "3");
          g.appendChild(l);
        });
      });
      return g;
    }

    function dessiner() {
      svg.innerHTML = "";
      svg.appendChild(fleche(55, cible, true));
      svg.appendChild(fleche(135, reglage, false));
    }
    dessiner();

    var slider = el("input");
    slider.type = "range";
    slider.min = "80"; slider.max = "420"; slider.value = String(reglage);
    slider.className = "lab-slider";
    slider.addEventListener("input", function () {
      reglage = parseInt(slider.value, 10);
      dessiner();
    });

    var b = el("button", "btn btn-primary", "C'est bon, les deux sont égaux");
    b.addEventListener("click", function () {
      var erreur = reglage - cible;
      var pct = Math.round((erreur / cible) * 1000) / 10;
      showResults([
        ["Longueur du trait de référence", cible + " px"],
        ["Longueur que vous avez réglée", reglage + " px"],
        ["Écart", (erreur > 0 ? "+" : "") + erreur + " px"],
        ["Erreur relative", (pct > 0 ? "+" : "") + pct + " %"],
        ["Repère typique", "15 à 25 %"]
      ], Math.abs(pct) > 8
        ? "Vous avez été trompé dans le sens attendu par l'illusion : le segment aux pointes rentrantes paraît plus long, vous avez donc mal réglé l'autre. Regardez à nouveau les deux traits en connaissant la réponse — ils continuent de paraître différents."
        : "Vous êtes resté proche de l'égalité réelle. Certaines personnes y parviennent en se concentrant sur les extrémités et en ignorant les pointes, ou en comparant les traits en les regardant de biais. L'illusion s'affaiblit aussi quand les pointes sont petites.");
      slider.disabled = true;
      b.disabled = true;
    });

    wrap.appendChild(el("p", "lab-prompt", "Réglez le <strong>trait du bas</strong> pour qu'il vous paraisse de la même longueur que celui du haut."));
    wrap.appendChild(svg);
    wrap.appendChild(slider);
    wrap.appendChild(b);
    stage.appendChild(wrap);
  }

  // --------------------------------------------------------- Position sérielle

  var MOTS_SERIE = [
    "bougie", "rivière", "tambour", "fenêtre", "orage", "cerise", "montagne", "violon",
    "clavier", "brouillard", "sandale", "carotte", "lanterne", "falaise", "trompette",
    "coussin", "prairie", "escalier", "citron", "coquille", "tonnerre", "pinceau"
  ];

  function runSerie() {
    var liste = shuffle(MOTS_SERIE).slice(0, 15);
    var idx = 0;

    function afficher() {
      clear();
      if (idx >= liste.length) return rappel();
      stage.appendChild(el("p", "rev-tag", (idx + 1) + " / " + liste.length));
      stage.appendChild(el("div", "lab-word", liste[idx]));
      idx++;
      setTimeout(afficher, 1000);
    }

    function rappel() {
      clear();
      stage.appendChild(el("p", "lab-prompt", "Écrivez tous les mots dont vous vous souvenez, un par ligne, dans l'ordre que vous voulez."));
      var ta = document.createElement("textarea");
      ta.rows = 8;
      ta.style.cssText = "width:100%;max-width:420px;padding:0.8rem;border:1px solid var(--border);" +
        "border-radius:10px;font-family:var(--sans);font-size:0.95rem;line-height:1.7";
      var b = el("button", "btn btn-primary", "Corriger");
      b.addEventListener("click", function () {
        var donnes = ta.value.toLowerCase().split(/[\n,;]+/).map(function (s) {
          return s.trim().replace(/[^a-zàâäéèêëîïôöùûüç]/g, "");
        }).filter(Boolean);
        corriger(donnes);
      });
      stage.appendChild(ta);
      stage.appendChild(b);
      ta.focus();
    }

    function norm(s) {
      return s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    }

    function corriger(donnes) {
      var setDonnes = donnes.map(norm);
      var trouves = liste.map(function (m) { return setDonnes.indexOf(norm(m)) !== -1; });
      var debut = trouves.slice(0, 5).filter(Boolean).length;
      var milieu = trouves.slice(5, 10).filter(Boolean).length;
      var fin = trouves.slice(10, 15).filter(Boolean).length;

      clear();
      stage.appendChild(el("p", "lab-prompt", "Voici la liste d'origine — les mots retrouvés sont en vert."));
      var grid = el("div");
      grid.style.cssText = "display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:0.4rem;width:100%;max-width:520px";
      liste.forEach(function (m, i) {
        var c = el("span", null, (i + 1) + ". " + m);
        c.style.cssText = "font-size:0.84rem;padding:0.3rem 0.5rem;border-radius:8px;" +
          (trouves[i] ? "background:var(--vert-light);color:var(--vert);font-weight:600"
                      : "background:var(--gris-light);color:var(--gris)");
        grid.appendChild(c);
      });
      stage.appendChild(grid);

      var total = debut + milieu + fin;
      showResults([
        ["Mots rappelés", total + " / 15"],
        ["Début de liste (positions 1-5)", debut + " / 5"],
        ["Milieu de liste (positions 6-10)", milieu + " / 5"],
        ["Fin de liste (positions 11-15)", fin + " / 5"]
      ], (debut + fin) > milieu * 2
        ? "La courbe attendue apparaît nettement : le début et la fin l'emportent largement sur le milieu. Vous venez de reproduire chez vous les effets de primauté et de récence."
        : "Votre profil est plus plat que la courbe classique. Cela arrive quand on utilise une stratégie délibérée — récit, images mentales, moyen mnémotechnique — qui protège justement le milieu de liste. Si c'est votre cas, vous avez découvert par vous-même pourquoi les stratégies d'encodage sont si efficaces.");
    }

    startButton("▶ Afficher les 15 mots", afficher);
  }

  // ------------------------------------------------------------------- Flanker

  function runFlanker() {
    var essais = [];
    var i;
    for (i = 0; i < 12; i++) essais.push(true);
    for (i = 0; i < 12; i++) essais.push(false);
    essais = shuffle(essais).map(function (congruent) {
      var cible = Math.random() < 0.5 ? "◀" : "▶";
      var flanc = congruent ? cible : (cible === "◀" ? "▶" : "◀");
      return { congruent: congruent, cible: cible, flanc: flanc };
    });

    var idx = 0, t0 = 0, actif = false;
    var data = { cong: [], incong: [], erreurs: 0 };

    function afficher() {
      if (idx >= essais.length) return fin();
      clear();
      var e = essais[idx];
      stage.appendChild(el("p", "rev-tag", "Essai " + (idx + 1) + " / " + essais.length));
      var suite = e.flanc + e.flanc + e.cible + e.flanc + e.flanc;
      var d = el("div", "lab-big", suite);
      d.style.letterSpacing = "0.2em";
      stage.appendChild(d);
      stage.appendChild(el("p", "lab-prompt", "Direction de la flèche <strong>du milieu</strong> ?"));
      var choices = el("div", "lab-choices");
      [["◀ Gauche", "◀"], ["Droite ▶", "▶"]].forEach(function (c) {
        var b = el("button", "lab-choice", c[0]);
        b.addEventListener("click", function () { repondre(c[1]); });
        choices.appendChild(b);
      });
      stage.appendChild(choices);
      actif = true;
      t0 = performance.now();
    }

    function repondre(dir) {
      if (!actif) return;
      actif = false;
      var rt = performance.now() - t0;
      var e = essais[idx];
      if (dir !== e.cible) data.erreurs++;
      else (e.congruent ? data.cong : data.incong).push(rt);
      idx++;
      afficher();
    }

    document.addEventListener("keydown", function (ev) {
      if (ev.key === "ArrowLeft") { ev.preventDefault(); repondre("◀"); }
      if (ev.key === "ArrowRight") { ev.preventDefault(); repondre("▶"); }
    });

    function fin() {
      clear();
      stage.appendChild(el("p", "lab-prompt", "✅ Terminé."));
      var mc = Math.round(mean(data.cong));
      var mi = Math.round(mean(data.incong));
      var diff = mi - mc;
      showResults([
        ["Temps moyen — flèches cohérentes", mc + " ms"],
        ["Temps moyen — flèches contradictoires", mi + " ms"],
        ["Effet flanker", (diff > 0 ? "+" : "") + diff + " ms"],
        ["Erreurs", data.erreurs + " / " + essais.length],
        ["Repère habituel", "30 à 80 ms"]
      ], diff > 0
        ? "L'effet apparaît : les distracteurs ont été traités malgré votre intention de les ignorer, et il a fallu inhiber la réponse qu'ils activaient. L'attention sélective n'est pas un projecteur étanche."
        : "Pas d'effet mesurable sur cette série. Avec douze essais par condition et une réponse à la souris, le bruit est considérable. Réessayez au clavier avec les touches fléchées : la mesure est nettement plus propre.");
    }

    startButton("▶ Commencer les 24 essais", afficher);
  }

  // ------------------------------------------------------------------- Ancrage

  function runAncrage() {
    var ancreHaute = Math.random() < 0.5;
    var ancre = ancreHaute ? 84 : 12;

    clear();
    stage.appendChild(el("p", "rev-tag", "Étape 1 sur 2"));
    stage.appendChild(el("p", "lab-prompt", "Voici un nombre tiré au hasard. Regardez-le simplement."));
    stage.appendChild(el("div", "lab-big", String(ancre)));
    var b1 = el("button", "btn btn-primary", "J'ai vu ce nombre, continuer");
    b1.addEventListener("click", question);
    stage.appendChild(b1);

    function question() {
      clear();
      stage.appendChild(el("p", "rev-tag", "Étape 2 sur 2"));
      stage.appendChild(el("p", "lab-prompt",
        "Selon vous, quel <strong>pourcentage des adultes français</strong> déclare avoir déjà consulté " +
        "un psychologue au moins une fois dans sa vie ? Répondez spontanément."));
      var input = el("input");
      input.type = "number";
      input.min = "0"; input.max = "100";
      input.style.cssText = "font-family:var(--serif);font-size:1.8rem;text-align:center;padding:0.6rem;" +
        "border:1px solid var(--border);border-radius:10px;width:160px";
      var b = el("button", "btn btn-primary", "Valider ma réponse");
      function valider() {
        var v = parseInt(input.value, 10);
        if (isNaN(v)) return;
        showResults([
          ["Le nombre que vous avez vu", String(ancre)],
          ["Votre groupe", ancreHaute ? "Ancre haute (84)" : "Ancre basse (12)"],
          ["Votre estimation", v + " %"],
          ["Tendance habituelle — groupe ancre basse", "estimations plus faibles"],
          ["Tendance habituelle — groupe ancre haute", "estimations plus élevées"]
        ], "Vous avez été affecté au hasard à l'un des deux groupes. Dans les études d'ancrage, le groupe " +
           "exposé au grand nombre produit des estimations nettement supérieures, alors même que le nombre est " +
           "manifestement sans rapport avec la question — et que les participants savent qu'il est aléatoire. " +
           "Avec un seul participant (vous), impossible de conclure quoi que ce soit : l'effet ne se voit qu'en " +
           "comparant des groupes. C'est exactement pourquoi la psychologie a besoin de répartition aléatoire et " +
           "de grands échantillons. Faites l'essai avec plusieurs personnes autour de vous : le tirage change à " +
           "chaque chargement de la page.");
        input.disabled = true;
        b.disabled = true;
      }
      b.addEventListener("click", valider);
      input.addEventListener("keydown", function (e) { if (e.key === "Enter") valider(); });
      stage.appendChild(input);
      stage.appendChild(b);
      input.focus();
    }
  }

  // ------------------------------------------------------------------ routeur

  var LABS = {
    "stroop": runStroop,
    "empan": runEmpan,
    "reaction": runReaction,
    "muller-lyer": runMullerLyer,
    "serie": runSerie,
    "flanker": runFlanker,
    "ancrage": runAncrage
  };

  var run = LABS[labId];
  if (run) {
    run();
  } else {
    stage.innerHTML = '<p class="lab-prompt">Expérience introuvable.</p>';
  }
})();
