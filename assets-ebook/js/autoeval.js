/* ==========================================================================
   PSYCLOPÉDIA — Auto-évaluations pédagogiques
   Passation item par item, score par dimension, restitution en barres.
   Aucune donnée n'est envoyée : tout reste dans la page.
   ========================================================================== */

(function () {
  "use strict";

  var shell = document.getElementById("eval-shell");
  if (!shell) return;

  var data;
  try {
    data = JSON.parse(document.getElementById("eval-data").textContent);
  } catch (err) {
    shell.innerHTML = "<p>Ce questionnaire n'a pas pu être chargé.</p>";
    return;
  }

  var items = data.items;
  var echelle = data.echelle;
  var reponses = new Array(items.length).fill(null);
  var index = 0;

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html !== undefined) n.innerHTML = html;
    return n;
  }

  function render() {
    shell.innerHTML = "";

    var progress = el("div", "eval-progress",
      "Affirmation " + (index + 1) + " sur " + items.length);
    shell.appendChild(progress);

    var track = el("div", "eval-bar-track");
    var fill = el("div", "eval-bar-fill");
    fill.style.width = ((index / items.length) * 100) + "%";
    track.appendChild(fill);
    track.style.marginBottom = "1.4rem";
    shell.appendChild(track);

    shell.appendChild(el("p", "eval-question", items[index][0]));

    var choix = el("div", "eval-echelle");
    echelle.forEach(function (label, i) {
      var btn = el("button", "eval-choix");
      btn.type = "button";
      btn.innerHTML = '<span class="eval-n">' + (i + 1) + "</span><span>" + label + "</span>";
      btn.addEventListener("click", function () { answer(i); });
      choix.appendChild(btn);
    });
    shell.appendChild(choix);

    var nav = el("div", "cta-row");
    nav.style.marginTop = "1.2rem";
    if (index > 0) {
      var back = el("button", "btn btn-secondary", "← Revenir");
      back.type = "button";
      back.addEventListener("click", function () { index--; render(); });
      nav.appendChild(back);
    }
    shell.appendChild(nav);

    shell.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function answer(value) {
    reponses[index] = value;
    if (index < items.length - 1) {
      index++;
      render();
    } else {
      showResults();
    }
  }

  function scores() {
    var somme = {}, total = {};
    data.dimensions.forEach(function (d) { somme[d.cle] = 0; total[d.cle] = 0; });

    items.forEach(function (item, i) {
      var dim = item[1];
      var inverse = item[2];
      var brut = reponses[i];
      if (brut === null || !(dim in somme)) return;
      var note = inverse ? (echelle.length - 1 - brut) : brut;
      somme[dim] += note;
      total[dim] += echelle.length - 1;
    });

    return data.dimensions.map(function (d) {
      var pct = total[d.cle] > 0 ? Math.round((somme[d.cle] / total[d.cle]) * 100) : 0;
      return { dim: d, pct: pct };
    });
  }

  function showResults() {
    var results = scores();

    shell.innerHTML = "";
    shell.appendChild(el("p", "eval-progress", "Vos résultats · " + items.length + " affirmations"));

    var box = el("div", "eval-resultat");
    results.forEach(function (r) {
      var row = el("div", "eval-bar-row");

      var head = el("div", "eval-bar-head");
      head.innerHTML = "<b>" + r.dim.nom + "</b><span>" + r.pct + " / 100</span>";
      row.appendChild(head);

      var track = el("div", "eval-bar-track");
      var fill = el("div", "eval-bar-fill " + r.dim.couleur);
      track.appendChild(fill);
      row.appendChild(track);

      row.appendChild(el("p", "eval-bar-desc", r.dim.description));
      row.appendChild(el("p", "eval-bar-desc",
        "<b>Votre position :</b> " + (r.pct >= 50 ? r.dim.haut : r.dim.bas)));

      box.appendChild(row);
      // L'animation ne démarre qu'une fois la barre insérée dans le document.
      setTimeout(function () { fill.style.width = r.pct + "%"; }, 60);
    });
    shell.appendChild(box);

    if (data.note) {
      var note = el("div", "note-box", "<strong>Pour lire ces résultats.</strong> " + data.note);
      note.style.marginTop = "1.5rem";
      shell.appendChild(note);
    }

    var actions = el("div", "cta-row");
    actions.style.marginTop = "1.4rem";

    var again = el("button", "btn btn-secondary", "↻ Refaire le questionnaire");
    again.type = "button";
    again.addEventListener("click", function () {
      reponses = new Array(items.length).fill(null);
      index = 0;
      render();
    });
    actions.appendChild(again);

    var back = el("a", "btn btn-secondary", "← Toutes les auto-évaluations");
    back.href = "auto-evaluations.html";
    actions.appendChild(back);

    shell.appendChild(actions);
    shell.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  render();
})();
