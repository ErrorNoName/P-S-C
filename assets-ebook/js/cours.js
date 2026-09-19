/* ==========================================================================
   PSYCLOPÉDIA — Cursus : calendrier, lecteur YouTube, sync, notes, quiz
   ========================================================================== */

(function () {
  "use strict";

  var ROOT = document.body.getAttribute("data-root") || "./";
  var PROG_URL = ROOT + "livres-psychologie/07-ebook-final/cours/programme.json";
  var STORE = "psyclopedia_cours_v1";
  var LECTEUR = "livres-psychologie/07-ebook-final/cours/lecteur.html";
  var DUREE = 50 * 60;
  var JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"];
  var JOURS_COURT = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"];

  var KIND_FR = {
    auteur: "Auteur", theorie: "Théorie", cas: "Cas", experience: "Expérience",
    courant: "Courant", trouble: "Trouble", biais: "Biais", mythe: "Idée reçue",
    debat: "Débat", pratique: "Pratique", test: "Test", glossaire: "Glossaire",
  };

  var programme = null;
  var page = "";
  var view = "semaine";
  var cursor = new Date();
  var session = { id: "", t: 0, running: false, timer: null, player: null, course: null };
  var captionCues = [];

  /* ------------------------------ Stockage ------------------------------ */

  function loadStore() {
    try {
      var raw = localStorage.getItem(STORE);
      if (!raw) return { watched: {}, attendance: {}, quizzes: {}, notes: {} };
      var data = JSON.parse(raw);
      data.watched = data.watched || {};
      data.attendance = data.attendance || {};
      data.quizzes = data.quizzes || {};
      data.notes = data.notes || {};
      return data;
    } catch (e) {
      return { watched: {}, attendance: {}, quizzes: {}, notes: {} };
    }
  }

  function saveStore(data) {
    localStorage.setItem(STORE, JSON.stringify(data));
  }

  function markAttendance(id, seconds, completed) {
    var s = loadStore();
    s.attendance[id] = true;
    var prev = s.watched[id] || { seconds: 0, completed: false };
    s.watched[id] = {
      seconds: Math.max(prev.seconds || 0, seconds || 0),
      completed: !!(prev.completed || completed),
      at: new Date().toISOString(),
    };
    saveStore(s);
  }

  /* ------------------------------ Dates ------------------------------ */

  function parseStart(iso) {
    var parts = iso.split("T");
    var d = parts[0].split("-");
    var t = (parts[1] || "10:00:00").split(":");
    return new Date(+d[0], +d[1] - 1, +d[2], +t[0], +t[1], +(t[2] || 0));
  }

  function mondayOf(d) {
    var x = new Date(d.getFullYear(), d.getMonth(), d.getDate());
    var day = x.getDay();
    var diff = day === 0 ? -6 : 1 - day;
    x.setDate(x.getDate() + diff);
    x.setHours(0, 0, 0, 0);
    return x;
  }

  function sameDay(a, b) {
    return a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
  }

  function fmtDate(d) {
    return d.toLocaleDateString("fr-FR", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
  }

  function fmtHM(d) {
    return d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
  }

  function pad(n) {
    return n < 10 ? "0" + n : String(n);
  }

  function fmtClock(sec) {
    sec = Math.max(0, Math.floor(sec));
    return pad(Math.floor(sec / 60)) + ":" + pad(sec % 60);
  }

  function statusOf(course, now) {
    var start = parseStart(course.start);
    var end = new Date(start.getTime() + course.duration * 60000);
    if (now >= start && now <= end) return "live";
    if (now > end) return "replay";
    return "soon";
  }

  function nextCourse(list, now) {
    var upcoming = list.filter(function (c) { return parseStart(c.start) > now; })
      .sort(function (a, b) { return parseStart(a.start) - parseStart(b.start); });
    if (upcoming.length) return upcoming[0];
    var live = list.filter(function (c) { return statusOf(c, now) === "live"; });
    return live[0] || null;
  }

  function lecteurHref(id) {
    return ROOT + LECTEUR + "?id=" + encodeURIComponent(id);
  }

  /* ------------------------------ Chargement ------------------------------ */

  function boot() {
    var root = document.querySelector("[data-cours-page]");
    if (!root) return;
    page = root.getAttribute("data-cours-page");
    fetch(PROG_URL).then(function (r) {
      if (!r.ok) throw new Error("programme");
      return r.json();
    }).then(function (data) {
      programme = data;
      if (page === "emploi") renderEmploi();
      else if (page === "archives") renderArchives();
      else if (page === "lecteur") renderLecteur();
    }).catch(function () {
      var title = document.getElementById("countdown-title") || document.getElementById("lec-title");
      if (title) title.textContent = "Impossible de charger le programme des cours.";
    });
  }

  /* ------------------------------ Progression ------------------------------ */

  function fillProgress() {
    if (!programme) return;
    var s = loadStore();
    var total = programme.cours.length;
    var followed = Object.keys(s.attendance).length;
    var quizIds = Object.keys(s.quizzes);
    var avg = "—";
    if (quizIds.length) {
      var sum = quizIds.reduce(function (acc, id) {
        var q = s.quizzes[id];
        return acc + (q.total ? (q.score / q.total) * 20 : 0);
      }, 0);
      avg = (sum / quizIds.length).toFixed(1) + " / 20";
    }
    var elF = document.querySelector("[data-cours-followed]");
    var elA = document.querySelector("[data-cours-attendance]");
    var elQ = document.querySelector("[data-cours-quizavg]");
    if (elF) elF.textContent = followed + " / " + total;
    if (elA) elA.textContent = Math.round((followed / total) * 100) + " %";
    if (elQ) elQ.textContent = avg;
  }

  /* ------------------------------ Emploi du temps ------------------------------ */

  function renderCountdown() {
    var now = new Date();
    var next = nextCourse(programme.cours, now);
    var live = programme.cours.filter(function (c) { return statusOf(c, now) === "live"; })[0];
    var box = document.getElementById("cours-countdown");
    var title = document.getElementById("countdown-title");
    var meta = document.getElementById("countdown-meta");
    var actions = document.getElementById("countdown-actions");
    if (!title) return;

    var target = live || next;
    if (!target) {
      title.textContent = "Année écoulée — tous les replays sont ouverts";
      meta.textContent = "Rouvre n'importe quelle séance depuis les archives, avec le même lecteur synchronisé.";
      actions.innerHTML = '<a class="btn btn-primary" href="cours/index.html">Ouvrir les archives</a>';
      ["cd-j", "cd-h", "cd-m", "cd-s"].forEach(function (id) {
        var n = document.getElementById(id);
        if (n) n.textContent = "0";
      });
      return;
    }

    var start = parseStart(target.start);
    var end = new Date(start.getTime() + target.duration * 60000);
    if (live) {
      box.classList.add("live");
      title.textContent = "En direct · " + target.title;
      meta.textContent = target.kind + " · " + target.guest + " · fin à " + fmtHM(end);
      actions.innerHTML = '<a class="btn btn-primary" href="' + lecteurHref(target.id) + '">Entrer dans le cours</a>';
    } else {
      box.classList.remove("live");
      title.textContent = target.title;
      meta.textContent = target.kind + " · " + fmtDate(start) + " à " + fmtHM(start) + " · " + target.guest;
      actions.innerHTML = '<a class="btn btn-primary" href="' + lecteurHref(target.id) + '">Préparer / replay anticipé</a>';
    }

    var diff = Math.max(0, (live ? end : start) - now);
    var j = Math.floor(diff / 86400000);
    var h = Math.floor((diff % 86400000) / 3600000);
    var m = Math.floor((diff % 3600000) / 60000);
    var s = Math.floor((diff % 60000) / 1000);
    var map = { "cd-j": j, "cd-h": h, "cd-m": m, "cd-s": s };
    Object.keys(map).forEach(function (id) {
      var n = document.getElementById(id);
      if (n) n.textContent = map[id];
    });
  }

  function chipHtml(course, now) {
    var st = statusOf(course, now);
    var store = loadStore();
    var cls = "cours-chip" + (course.kind === "TD" ? " td" : "") + (st === "live" ? " live" : "") + (store.attendance[course.id] ? " done" : "");
    var label = st === "live" ? "En direct" : (st === "replay" ? "Replay" : "Planifié");
    return '<a class="' + cls + '" href="' + lecteurHref(course.id) + '"><strong>' +
      course.kind + " · " + fmtHM(parseStart(course.start)) + "</strong> " +
      course.title + "<small>" + label + " · " + course.guest + "</small></a>";
  }

  function renderWeek() {
    var now = new Date();
    var mon = mondayOf(cursor);
    var label = document.getElementById("cours-view-label");
    var sun = new Date(mon);
    sun.setDate(mon.getDate() + 6);
    if (label) {
      label.textContent = "Semaine du " + mon.toLocaleDateString("fr-FR", { day: "numeric", month: "long" }) +
        " au " + sun.toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric" });
    }
    var html = '<div class="week-grid">';
    for (var i = 0; i < 7; i++) {
      var day = new Date(mon);
      day.setDate(mon.getDate() + i);
      var items = programme.cours.filter(function (c) { return sameDay(parseStart(c.start), day); });
      html += '<div class="week-day' + (sameDay(day, now) ? " today" : "") + '">';
      html += '<div class="wd-name">' + JOURS[i] + "</div>";
      html += '<div class="wd-num">' + day.getDate() + "</div>";
      html += items.map(function (c) { return chipHtml(c, now); }).join("") ||
        '<span class="tiny-note">Pas de séance</span>';
      html += "</div>";
    }
    html += "</div>";
    document.getElementById("cours-calendar").innerHTML = html;
  }

  function renderMonth() {
    var now = new Date();
    var y = cursor.getFullYear();
    var m = cursor.getMonth();
    var label = document.getElementById("cours-view-label");
    if (label) {
      label.textContent = cursor.toLocaleDateString("fr-FR", { month: "long", year: "numeric" });
    }
    var first = new Date(y, m, 1);
    var startPad = (first.getDay() + 6) % 7;
    var daysIn = new Date(y, m + 1, 0).getDate();
    var html = '<div class="month-grid">';
    JOURS_COURT.forEach(function (j) { html += '<div class="month-head">' + j + "</div>"; });
    for (var p = 0; p < startPad; p++) html += '<div class="month-cell empty"></div>';
    for (var d = 1; d <= daysIn; d++) {
      var day = new Date(y, m, d);
      var items = programme.cours.filter(function (c) { return sameDay(parseStart(c.start), day); });
      html += '<div class="month-cell' + (sameDay(day, now) ? " today" : "") + '">';
      html += '<span class="dn">' + d + "</span>";
      html += items.map(function (c) { return chipHtml(c, now); }).join("");
      html += "</div>";
    }
    html += "</div>";
    document.getElementById("cours-calendar").innerHTML = html;
  }

  function renderCalendar() {
    if (view === "mois") renderMonth();
    else renderWeek();
  }

  function renderEmploi() {
    fillProgress();
    renderCountdown();
    renderCalendar();
    setInterval(function () {
      renderCountdown();
      fillProgress();
    }, 1000);
    document.querySelectorAll("[data-cours-view]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        view = btn.getAttribute("data-cours-view");
        document.querySelectorAll("[data-cours-view]").forEach(function (b) {
          b.classList.toggle("active", b === btn);
        });
        renderCalendar();
      });
    });
    document.querySelectorAll("[data-cours-jump]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var j = btn.getAttribute("data-cours-jump");
        if (j === "0") cursor = new Date();
        else if (view === "mois") cursor.setMonth(cursor.getMonth() + (+j));
        else cursor.setDate(cursor.getDate() + (7 * +j));
        renderCalendar();
      });
    });
  }

  /* ------------------------------ Archives ------------------------------ */

  function renderArchives() {
    var cat = document.getElementById("arch-cat");
    var mod = document.getElementById("arch-mod");
    var guest = document.getElementById("arch-guest");
    var q = document.getElementById("arch-q");
    function paint() {
      var store = loadStore();
      var query = (q.value || "").toLowerCase();
      var list = programme.cours.filter(function (c) {
        if (cat.value && c.cat !== cat.value) return false;
        if (mod.value && c.module !== mod.value) return false;
        if (guest.value && c.guest !== guest.value) return false;
        if (query) {
          var blob = (c.title + " " + c.theme + " " + c.guest + " " + c.module).toLowerCase();
          if (blob.indexOf(query) === -1) return false;
        }
        return true;
      });
      document.getElementById("arch-count").textContent = list.length + " séance(s)";
      document.getElementById("arch-grid").innerHTML = list.map(function (c) {
        var start = parseStart(c.start);
        var done = store.attendance[c.id] ? " done" : "";
        var note = store.quizzes[c.id] ? " · quiz " + store.quizzes[c.id].score + "/" + store.quizzes[c.id].total : "";
        return '<a class="arch-card' + done + '" href="lecteur.html?id=' + encodeURIComponent(c.id) + '">' +
          '<div class="kind' + (c.kind === "TD" ? " td" : "") + '">' + c.kind + " · S" + c.semester + " · sem. " + c.week + "</div>" +
          "<h3>" + c.title + "</h3>" +
          "<p>" + c.module + " · " + c.theme + "<br>" + c.guest + " — " + c.video.source + "</p>" +
          '<div class="meta">' + fmtDate(start) + " · " + fmtHM(start) + " · 50 min" + note + "</div></a>";
      }).join("");
    }
    [cat, mod, guest, q].forEach(function (el) { el.addEventListener("input", paint); });
    paint();
  }

  /* ------------------------------ Lecteur ------------------------------ */

  function courseById(id) {
    for (var i = 0; i < programme.cours.length; i++) {
      if (programme.cours[i].id === id) return programme.cours[i];
    }
    return programme.cours[0];
  }

  function queryId() {
    var p = new URLSearchParams(location.search);
    return p.get("id") || "";
  }

  function markerAt(course, t) {
    var current = course.timeline[0];
    for (var i = 0; i < course.timeline.length; i++) {
      if (course.timeline[i].t <= t) current = course.timeline[i];
    }
    return current;
  }

  function phaseAt(course, t) {
    var phases = course.phases || [];
    for (var i = 0; i < phases.length; i++) {
      if (t >= phases[i].start && t < phases[i].end) return phases[i];
    }
    return phases[phases.length - 1];
  }

  function highlightText(text, keywords) {
    if (!text) return "";
    var out = text;
    (keywords || []).slice().sort(function (a, b) { return b.length - a.length; }).forEach(function (kw) {
      if (!kw) return;
      var re = new RegExp("(" + kw.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
      out = out.replace(re, "<mark>$1</mark>");
    });
    return out;
  }

  function updateSync(course, t) {
    var mark = markerAt(course, t);
    var phase = phaseAt(course, t);
    var needle = document.getElementById("phase-needle");
    if (needle) needle.style.left = Math.min(100, (t / DUREE) * 100) + "%";
    var nowEl = document.getElementById("phase-now");
    if (nowEl) nowEl.textContent = phase.label + " · " + fmtClock(t) + " / 50:00";

    document.getElementById("sync-title").textContent = mark.title;
    document.getElementById("sync-body").innerHTML = highlightText(mark.body, mark.keywords);

    var karaoke = document.getElementById("sync-karaoke");
    var cue = captionAt(t, mark);
    if (cue) karaoke.innerHTML = highlightText(cue, mark.keywords);
    else karaoke.innerHTML = highlightText((mark.keywords || []).join(" · "), mark.keywords);

    var active = {};
    (mark.resources || []).forEach(function (k) { active[k] = true; });
    document.querySelectorAll(".res-card").forEach(function (card) {
      var key = card.getAttribute("data-key");
      var kws = (card.getAttribute("data-kw") || "").split("|");
      var hit = !!active[key];
      if (!hit && mark.keywords) {
        hit = mark.keywords.some(function (k) {
          return kws.some(function (w) { return w && w.indexOf(k.toLowerCase()) !== -1; });
        });
      }
      card.classList.toggle("active", hit);
    });
  }

  function captionAt(sessionT, mark) {
    if (!captionCues.length) return "";
    var vt = mark.videoT || sessionT;
    if (session.player && session.player.getCurrentTime) {
      try { vt = session.player.getCurrentTime(); } catch (e) {}
    }
    var line = "";
    for (var i = 0; i < captionCues.length; i++) {
      if (captionCues[i].start <= vt && vt <= captionCues[i].end) line = captionCues[i].text;
    }
    return line;
  }

  function renderResources(course) {
    var box = document.getElementById("res-list");
    var depthPrefix = "../";
    box.innerHTML = course.resources.map(function (r) {
      return '<a class="res-card" data-key="' + r.key + '" data-kw="' +
        (r.keywords || []).join("|").toLowerCase() + '" href="' + depthPrefix + r.href + '">' +
        '<div class="rk">' + (KIND_FR[r.kind] || r.kind) + "</div>" +
        "<h4>" + r.title + "</h4>" +
        "<p>Ouvrir la fiche Psyclopédia correspondante</p></a>";
    }).join("");
  }

  function renderQuiz(course) {
    var mount = document.getElementById("quiz-mount");
    var store = loadStore();
    var html = "";
    course.quiz.forEach(function (q, i) {
      html += '<div class="q-item" data-qi="' + i + '"><p>' + (i + 1) + ". " + q.q + "</p>";
      q.a.forEach(function (ans, j) {
        html += '<button type="button" data-a="' + j + '">' + ans + "</button>";
      });
      html += '<div class="explain" hidden></div></div>';
    });
    html += '<div class="quiz-score" id="quiz-score"></div>';
    mount.innerHTML = html;
    if (store.quizzes[course.id]) {
      showQuizResult(course, store.quizzes[course.id].score);
    }
    mount.querySelectorAll(".q-item").forEach(function (item) {
      item.querySelectorAll("button").forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (item.getAttribute("data-locked")) return;
          var qi = +item.getAttribute("data-qi");
          var choice = +btn.getAttribute("data-a");
          var q = course.quiz[qi];
          item.setAttribute("data-locked", "1");
          item.setAttribute("data-ok", choice === q.correct ? "1" : "0");
          item.querySelectorAll("button").forEach(function (b) {
            var idx = +b.getAttribute("data-a");
            if (idx === q.correct) b.classList.add("ok");
            else if (idx === choice) b.classList.add("ko");
          });
          var ex = item.querySelector(".explain");
          ex.hidden = false;
          ex.textContent = q.explain;
          maybeFinishQuiz(course);
        });
      });
    });
  }

  function maybeFinishQuiz(course) {
    var items = document.querySelectorAll("#quiz-mount .q-item");
    if (!items.length) return;
    var locked = 0;
    var ok = 0;
    items.forEach(function (it) {
      if (it.getAttribute("data-locked")) locked += 1;
      if (it.getAttribute("data-ok") === "1") ok += 1;
    });
    if (locked < items.length) return;
    var s = loadStore();
    s.quizzes[course.id] = { score: ok, total: items.length, at: new Date().toISOString() };
    saveStore(s);
    showQuizResult(course, ok);
    markAttendance(course.id, session.t, true);
  }

  function showQuizResult(course, score) {
    var el = document.getElementById("quiz-score");
    if (!el) return;
    var note = Math.round((score / course.quiz.length) * 20);
    el.textContent = "Score : " + score + " / " + course.quiz.length + " · " + note + " / 20";
  }

  function renderNotes(course) {
    var ta = document.getElementById("cours-notes");
    var store = loadStore();
    ta.value = store.notes[course.id] || "";
    var save = function () {
      var s = loadStore();
      s.notes[course.id] = ta.value;
      saveStore(s);
    };
    ta.addEventListener("input", save);
    document.getElementById("btn-md").addEventListener("click", function () {
      var md = "# " + course.title + "\n\n" +
        "_ " + course.kind + " · " + course.guest + " · " + course.start + " _\n\n" +
        ta.value + "\n";
      var blob = new Blob([md], { type: "text/markdown;charset=utf-8" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = course.id + "-notes.md";
      a.click();
    });
    document.getElementById("btn-pdf").addEventListener("click", function () {
      var w = window.open("", "_blank");
      w.document.write("<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><title>" +
        course.title + "</title><style>body{font-family:Georgia,serif;padding:2rem;max-width:720px;margin:auto}h1{font-size:1.4rem}</style></head><body><h1>" +
        course.title + "</h1><p>" + course.guest + " · " + course.start + "</p><pre style='white-space:pre-wrap;font:inherit'>" +
        ta.value.replace(/</g, "&lt;") + "</pre></body></html>");
      w.document.close();
      w.focus();
      w.print();
    });
  }

  function startSession(course) {
    if (session.running) return;
    session.running = true;
    session.id = course.id;
    markAttendance(course.id, session.t, false);
    if (session.player && session.player.playVideo) {
      try { session.player.playVideo(); } catch (e) {}
    }
    session.timer = setInterval(function () { tick(course); }, 400);
    document.getElementById("btn-start").textContent = "Séance en cours";
  }

  function tick(course) {
    session.t = Math.min(DUREE, session.t + 0.4);
    if (session.player && session.player.getCurrentTime) {
      try {
        var vt = session.player.getCurrentTime();
        var mapped = mapVideoToSession(course, vt);
        if (mapped >= 0) session.t = Math.min(DUREE, mapped);
      } catch (e) {}
    }
    updateSync(course, session.t);
    if (session.t >= DUREE) {
      markAttendance(course.id, DUREE, true);
      clearInterval(session.timer);
      session.running = false;
    } else {
      markAttendance(course.id, session.t, session.t > DUREE * 0.85);
    }
  }

  function mapVideoToSession(course, vt) {
    var tl = course.timeline;
    if (!tl.length) return vt;
    var prev = tl[0];
    for (var i = 0; i < tl.length; i++) {
      if (tl[i].videoT <= vt) prev = tl[i];
    }
    var next = null;
    for (var j = 0; j < tl.length; j++) {
      if (tl[j].videoT > prev.videoT) { next = tl[j]; break; }
    }
    if (!next) return prev.t + Math.max(0, vt - prev.videoT);
    var spanV = Math.max(1, next.videoT - prev.videoT);
    var spanS = next.t - prev.t;
    var r = (vt - prev.videoT) / spanV;
    return prev.t + r * spanS;
  }

  function setupPlayer(course) {
    var fallback = document.getElementById("yt-fallback");
    function onReady(e) {
      try { e.target.playVideo(); } catch (err) {}
      setTimeout(function () {
        var st = -2;
        try { st = e.target.getPlayerState(); } catch (err2) {}
        if (st !== 1) {
          fallback.hidden = false;
        }
      }, 900);
    }
    function onState(e) {
      if (e.data === 1) {
        fallback.hidden = true;
        startSession(course);
      }
    }
    function build() {
      if (!window.YT || !window.YT.Player) return false;
      session.player = new window.YT.Player("yt-player", {
        videoId: course.video.youtube,
        playerVars: {
          rel: 0,
          modestbranding: 1,
          hl: "fr",
          cc_lang_pref: "fr",
          cc_load_policy: 1,
          autoplay: 1,
          playsinline: 1,
        },
        events: { onReady: onReady, onStateChange: onState },
      });
      return true;
    }
    if (!build()) {
      window.onYouTubeIframeAPIReady = function () { build(); };
    }
    fallback.addEventListener("click", function () {
      if (session.player && session.player.playVideo) session.player.playVideo();
      fallback.hidden = true;
      startSession(course);
    });
    tryCaptions(course.video.youtube);
  }

  function tryCaptions(videoId) {
    var urls = [
      "https://video.google.com/timedtext?v=" + videoId + "&lang=fr&fmt=vtt",
      "https://www.youtube.com/api/timedtext?v=" + videoId + "&lang=fr&fmt=vtt",
    ];
    (function next(i) {
      if (i >= urls.length) return;
      fetch(urls[i]).then(function (r) {
        if (!r.ok) throw new Error("no captions");
        return r.text();
      }).then(function (text) {
        captionCues = parseVtt(text);
      }).catch(function () { next(i + 1); });
    })(0);
  }

  function parseVtt(text) {
    var cues = [];
    var blocks = text.replace(/\r/g, "").split("\n\n");
    blocks.forEach(function (block) {
      var lines = block.split("\n").filter(Boolean);
      var time = "";
      var body = [];
      lines.forEach(function (ln) {
        if (ln.indexOf("-->") !== -1) time = ln;
        else if (!/^\d+$/.test(ln) && ln.indexOf("WEBVTT") !== 0) body.push(ln);
      });
      if (!time) return;
      var bits = time.split("-->");
      cues.push({
        start: vttSec(bits[0]),
        end: vttSec(bits[1]),
        text: body.join(" ").replace(/<[^>]+>/g, ""),
      });
    });
    return cues;
  }

  function vttSec(stamp) {
    var clean = stamp.trim().split(" ")[0];
    var parts = clean.split(":");
    var s = parts.pop() || "0";
    var m = +(parts.pop() || 0);
    var h = +(parts.pop() || 0);
    return h * 3600 + m * 60 + parseFloat(s.replace(",", "."));
  }

  function renderLecteur() {
    var course = courseById(queryId());
    session.course = course;
    var store = loadStore();
    if (store.watched[course.id]) session.t = Math.min(DUREE - 1, store.watched[course.id].seconds || 0);

    document.getElementById("lec-kicker").textContent =
      course.kind + " · Semaine " + course.week + " · Semestre " + course.semester + " · " + course.module;
    document.getElementById("lec-title").textContent = course.title;
    document.getElementById("lec-meta").textContent =
      fmtDate(parseStart(course.start)) + " à " + fmtHM(parseStart(course.start)) +
      " · " + course.guest + " (" + course.video.source + ")";
    document.getElementById("yt-credit").textContent =
      "Vidéo : « " + course.video.title + " » — " + course.video.speaker + " · " + course.video.source +
      " · sous-titres YouTube si disponibles, sinon timeline JSON.";

    var links = document.getElementById("lec-links");
    links.innerHTML = (course.pages || []).map(function (p) {
      return '<a class="pill-link" href="../' + p + '">' + p + "</a>";
    }).join("");

    renderResources(course);
    renderQuiz(course);
    renderNotes(course);
    updateSync(course, session.t);
    setupPlayer(course);

    document.getElementById("btn-start").addEventListener("click", function () {
      startSession(course);
    });
    document.getElementById("btn-cinema").addEventListener("click", function () {
      document.body.classList.toggle("cinema");
      this.textContent = document.body.classList.contains("cinema") ? "⤢ Quitter le cinéma" : "🎬 Mode cinéma";
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        document.body.classList.remove("cinema");
        document.getElementById("btn-cinema").textContent = "🎬 Mode cinéma";
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
