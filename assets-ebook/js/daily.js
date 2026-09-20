/* ==========================================================================
   PSYCLOPÉDIA — Rappels de cours, pensées du jour, planches
   ========================================================================== */

(function () {
  "use strict";

  var ROOT = document.body.getAttribute("data-root") || "./";
  var STORE = "psyclopedia_notif_v1";
  var DATA_URL = ROOT + "livres-psychologie/07-ebook-final/pensees.json";
  var PROG_URL = ROOT + "livres-psychologie/07-ebook-final/cours/programme.json";
  var TZ = "Europe/Paris";

  var data = null;
  var programme = null;
  var timer = null;

  function loadStore() {
    try {
      var raw = localStorage.getItem(STORE);
      if (!raw) return defaultStore();
      return Object.assign(defaultStore(), JSON.parse(raw));
    } catch (e) {
      return defaultStore();
    }
  }

  function defaultStore() {
    return {
      thoughts: true,
      cours: true,
      browser: false,
      quietStart: "22:00",
      quietEnd: "08:00",
      shown: {},
      unread: 0,
    };
  }

  function saveStore(s) {
    localStorage.setItem(STORE, JSON.stringify(s));
  }

  function todayKey(d) {
    return parisYmd(d || new Date());
  }

  function parisYmd(d) {
    return new Intl.DateTimeFormat("en-CA", {
      timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit",
    }).format(d);
  }

  function parisParts(d) {
    var fmt = new Intl.DateTimeFormat("fr-FR", {
      timeZone: TZ, hour: "2-digit", minute: "2-digit", hourCycle: "h23",
    });
    var parts = fmt.formatToParts(d);
    var h = "00";
    var m = "00";
    parts.forEach(function (p) {
      if (p.type === "hour") h = p.value;
      if (p.type === "minute") m = p.value;
    });
    return { h: parseInt(h, 10), m: parseInt(m, 10), hm: h + ":" + m };
  }

  function hashDay(str) {
    var n = 0;
    for (var i = 0; i < str.length; i++) n = (n * 33 + str.charCodeAt(i)) >>> 0;
    return n;
  }

  function pickPensee(slotId, day) {
    if (!data) return null;
    var pool = data.pensees.filter(function (p) { return p.slot === slotId; });
    if (!pool.length) pool = data.pensees;
    return pool[hashDay(day + "|" + slotId) % pool.length];
  }

  function plateById(id) {
    if (!data || !id) return data && data.plates[0];
    return data.plates.find(function (p) { return p.id === id; }) || data.plates[0];
  }

  function plateForCat(cat) {
    if (!data) return null;
    return data.plates.find(function (p) { return p.id === "cat-" + cat; })
      || data.plates.find(function (p) { return (p.cats || []).indexOf(cat) !== -1; })
      || data.plates[0];
  }

  function plateSrc(plate) {
    return ROOT + plate.file;
  }

  function displayPlate(plate) {
    if (!data || !plate) return plate;
    if (plate.origin && plate.origin !== "svg") return plate;
    var cats = plate.cats || [];
    return data.plates.find(function (p) {
      return p.origin && p.origin !== "svg" && (p.cats || []).some(function (c) {
        return cats.indexOf(c) !== -1;
      });
    }) || plate;
  }

  function hrefOf(pensee) {
    if (!pensee || !pensee.href) return ROOT + "livres-psychologie/07-ebook-final/rappels.html";
    if (/^https?:\/\//i.test(pensee.href)) return pensee.href;
    return ROOT + "livres-psychologie/07-ebook-final/" + pensee.href;
  }

  function inQuiet(now, store) {
    var hm = parisParts(now).hm;
    var a = store.quietStart || "22:00";
    var b = store.quietEnd || "08:00";
    if (a === b) return false;
    if (a < b) return hm >= a && hm < b;
    return hm >= a || hm < b;
  }

  function hmToMin(hm) {
    var p = (hm || "00:00").split(":");
    return parseInt(p[0], 10) * 60 + parseInt(p[1], 10);
  }

  function minutesSinceSlot(slot, now) {
    var nowM = hmToMin(parisParts(now).hm);
    var slotM = hmToMin(slot.time);
    var delta = nowM - slotM;
    if (delta < 0) delta += 24 * 60;
    return delta;
  }

  function slotReached(slot, now) {
    return parisParts(now).hm >= slot.time;
  }

  function slotJustReached(slot, now) {
    return slotReached(slot, now) && minutesSinceSlot(slot, now) <= 45;
  }

  function shownKey(kind, id, day) {
    return kind + ":" + day + ":" + id;
  }

  function markShown(store, key) {
    store.shown[key] = Date.now();
    store.unread = (store.unread || 0) + 1;
    saveStore(store);
    updateBadge(store);
  }

  function updateBadge(store) {
    var el = document.querySelector(".nav-notify-badge");
    if (!el) return;
    var n = store.unread || 0;
    el.hidden = n < 1;
    el.textContent = n > 9 ? "9+" : String(n);
  }

  function toastPlate(title, text, plate, href) {
    var el = document.getElementById("toast");
    if (!el) {
      el = document.createElement("div");
      el.id = "toast";
      document.body.appendChild(el);
    }
    el.className = "toast-plate show";
    el.innerHTML =
      (plate ? '<img src="' + plateSrc(plate) + '" alt="">' : "") +
      '<div class="toast-body"><div class="toast-k">' + esc(title) + "</div>" +
      '<div class="toast-t">' + esc(text) + "</div></div>";
    el.onclick = function () {
      if (href) window.location.href = href;
    };
    clearTimeout(window.__toastTimer);
    window.__toastTimer = setTimeout(function () {
      el.classList.remove("show");
    }, 6400);
  }

  function maybeBrowserNotify(title, body, href) {
    var store = loadStore();
    if (!store.browser || typeof Notification === "undefined") return;
    if (Notification.permission !== "granted") return;
    try {
      var n = new Notification(title, { body: body, silent: false });
      n.onclick = function () {
        window.focus();
        if (href) window.location.href = href;
        n.close();
      };
    } catch (e) {}
  }

  function tick() {
    if (!data) return;
    var store = loadStore();
    var now = new Date();
    var day = todayKey(now);
    if (inQuiet(now, store)) return;

    if (store.thoughts) {
      data.slots.forEach(function (slot) {
        if (!slotJustReached(slot, now)) return;
        var item = pickPensee(slot.id, day);
        if (!item) return;
        var key = shownKey("pensee", slot.id, day);
        if (store.shown[key]) return;
        var plate = plateById(item.plate);
        markShown(store, key);
        toastPlate(slot.label, item.text, plate, hrefOf(item));
        maybeBrowserNotify(slot.label, item.text, hrefOf(item));
      });
    }

    if (store.cours && programme) {
      var next = nextCourse(programme.cours, now);
      if (next) {
        var start = new Date(next.start);
        var mins = Math.round((start - now) / 60000);
        (data.coursOffsets || []).forEach(function (off) {
          if (mins > off.minutes || mins < off.minutes - 2) return;
          var key = shownKey("cours", off.minutes + "-" + next.id, day);
          if (store.shown[key]) return;
          var plate = plateForCat(next.cat);
          var title = off.label + " · " + next.kind;
          var body = next.title;
          var href = ROOT + "livres-psychologie/07-ebook-final/cours/lecteur.html?id=" + encodeURIComponent(next.id);
          markShown(store, key);
          toastPlate(title, body, plate, href);
          maybeBrowserNotify(title, body, href);
        });
      }
    }
  }

  function nextCourse(list, now) {
    var best = null;
    list.forEach(function (c) {
      var end = new Date(c.start).getTime() + (c.duration || 50) * 60000;
      if (end < now.getTime()) return;
      if (!best || new Date(c.start) < new Date(best.start)) best = c;
    });
    return best;
  }

  function esc(s) {
    return String(s || "").replace(/[&<>"']/g, function (ch) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch];
    });
  }

  function figureHtml(plate, extraClass) {
    if (!plate) return "";
    return '<figure class="geo-plate ' + (plate.paper || "cream") + (extraClass ? " " + extraClass : "") + '">' +
      '<img src="' + plateSrc(plate) + '" alt="' + esc(plate.title) + '">' +
      '<figcaption><span class="geo-fig">Fig. ' + esc(plate.fig) + ".</span>" +
      "<strong>" + esc(plate.title) + "</strong>" +
      "<em>" + esc(plate.meaning) + "</em></figcaption></figure>";
  }

  function fillHome() {
    var host = document.querySelector("[data-pensee-home]");
    if (!host || !data) return;
    var day = todayKey();
    var item = pickPensee("matin", day);
    var plate = displayPlate(plateById(item.plate));
    host.innerHTML =
      figureHtml(plate) +
      '<div class="pensee-copy">' +
        '<p class="section-eyebrow">Planche du jour</p>' +
        "<blockquote>« " + esc(item.text) + " »</blockquote>" +
        "<cite>" + esc(item.by) + "</cite>" +
        '<div class="cta-row">' +
          '<a class="btn btn-secondary" href="' + hrefOf(item) + '">Lire autour</a>' +
          '<a class="btn btn-secondary" href="' + ROOT + 'livres-psychologie/07-ebook-final/rappels.html">Rappels &amp; cabinet</a>' +
        "</div>" +
      "</div>";
  }

  function fillRappels() {
    var page = document.querySelector("[data-rappels-page]");
    if (!page || !data) return;
    var day = todayKey();
    data.slots.forEach(function (slot) {
      var box = page.querySelector('[data-slot-body="' + slot.id + '"]');
      if (!box) return;
      var item = pickPensee(slot.id, day);
      var plate = plateById(item.plate);
      box.innerHTML =
        "<blockquote>« " + esc(item.text) + " »</blockquote>" +
        "<cite>" + esc(item.by) + "</cite>" +
        '<p><a class="pill-link" href="' + hrefOf(item) + '">Ouvrir</a></p>' +
        '<img src="' + plateSrc(plate) + '" alt="" style="width:100%;border-radius:6px;margin-top:0.6rem">';
    });
    bindSettings(page);
    fillNextCourse(page);
  }

  function fillNextCourse(page) {
    if (!programme) return;
    var next = nextCourse(programme.cours, new Date());
    var title = page.querySelector("[data-cours-next-title]");
    var meta = page.querySelector("[data-cours-next-meta]");
    var actions = page.querySelector("[data-cours-next-actions]");
    if (!title) return;
    if (!next) {
      title.textContent = "Aucun cours à venir dans le calendrier chargé.";
      return;
    }
    var when = new Date(next.start);
    title.textContent = next.kind + " · " + next.title;
    meta.textContent = when.toLocaleString("fr-FR", { timeZone: TZ }) +
      " · " + (next.module || "") + " · 50 min";
    actions.innerHTML =
      '<a class="btn btn-primary" href="' + ROOT +
      "livres-psychologie/07-ebook-final/cours/lecteur.html?id=" +
      encodeURIComponent(next.id) + '">Ouvrir le lecteur</a>';
  }

  function fillLecteurPlate() {
    var host = document.querySelector("[data-cours-plate]");
    if (!host || !data) return;
    var params = new URLSearchParams(window.location.search);
    var id = params.get("id");
    var cat = host.getAttribute("data-cat") || "";
    if (programme && id) {
      var course = programme.cours.find(function (c) { return c.id === id; });
      if (course) cat = course.cat;
    }
    var plate = plateForCat(cat);
    host.innerHTML = figureHtml(plate, "cours-plate");
  }

  function fillEmploiPlate() {
    var host = document.querySelector("[data-emploi-plate]");
    if (!host || !data || !programme) return;
    var next = nextCourse(programme.cours, new Date());
    var plate = next ? plateForCat(next.cat) : plateById("hero-frontispice");
    host.innerHTML = figureHtml(plate);
  }

  function bindSettings(page) {
    var store = loadStore();
    page.querySelectorAll("[data-opt]").forEach(function (el) {
      var key = el.getAttribute("data-opt");
      if (el.type === "checkbox") el.checked = !!store[key];
      else if (store[key]) el.value = store[key];
    });
    var save = page.querySelector("[data-opt-save]");
    var test = page.querySelector("[data-opt-test]");
    var status = page.querySelector("[data-opt-status]");
    if (save) {
      save.addEventListener("click", function () {
        var next = loadStore();
        page.querySelectorAll("[data-opt]").forEach(function (el) {
          var key = el.getAttribute("data-opt");
          next[key] = el.type === "checkbox" ? el.checked : el.value;
        });
        var enable = next.browser;
        saveStore(next);
        if (enable) requestBrowser(status);
        else if (status) status.textContent = "Réglages enregistrés.";
      });
    }
    if (test) {
      test.addEventListener("click", function () {
        var item = pickPensee("matin", todayKey());
        toastPlate("Exemple de rappel", item.text, plateById(item.plate), hrefOf(item));
        maybeBrowserNotify("Exemple de rappel", item.text, hrefOf(item));
      });
    }
  }

  function requestBrowser(status) {
    if (typeof Notification === "undefined") {
      if (status) status.textContent = "Ce navigateur ne propose pas les notifications.";
      return;
    }
    Notification.requestPermission().then(function (perm) {
      var store = loadStore();
      store.browser = perm === "granted";
      saveStore(store);
      if (status) {
        status.textContent = perm === "granted"
          ? "Notifications du navigateur activées. Gardez un onglet du site ouvert."
          : "Permission refusée — les rappels restent dans la page.";
      }
    });
  }

  function buildChrome() {
    if (document.querySelector(".notify-panel")) return;
    var overlay = document.createElement("div");
    overlay.className = "notify-overlay";
    overlay.setAttribute("data-notify-close", "");
    var panel = document.createElement("aside");
    panel.className = "notify-panel";
    panel.setAttribute("aria-label", "Rappels");
    panel.innerHTML =
      '<div class="notify-panel-head"><h2>Rappels du jour</h2>' +
      '<button type="button" class="pill-link" data-notify-close>Fermer</button></div>' +
      '<div class="notify-feed" data-notify-feed></div>' +
      '<div style="padding:0.8rem 1.1rem 1.2rem">' +
        '<a class="btn btn-secondary" href="' + ROOT +
        'livres-psychologie/07-ebook-final/rappels.html">Ouvrir le cabinet</a>' +
      "</div>";
    document.body.appendChild(overlay);
    document.body.appendChild(panel);
    document.addEventListener("click", function (e) {
      if (e.target.closest("[data-notify-open]")) {
        e.preventDefault();
        openPanel();
      }
      if (e.target.closest("[data-notify-close]")) closePanel();
    });
  }

  function feedItems() {
    if (!data) return [];
    var day = todayKey();
    return data.slots.map(function (slot) {
      var item = pickPensee(slot.id, day);
      return { slot: slot, item: item, plate: plateById(item.plate) };
    });
  }

  function renderFeed() {
    var box = document.querySelector("[data-notify-feed]");
    if (!box || !data) return;
    var items = feedItems();
    box.innerHTML = items.map(function (row) {
      return '<a class="notify-item" href="' + hrefOf(row.item) + '">' +
        '<img src="' + plateSrc(row.plate) + '" alt="">' +
        "<div><span class=\"when\">" + esc(row.slot.label) + "</span>" +
        "<strong>" + esc(row.item.by) + "</strong>" +
        "<p>" + esc(row.item.text) + "</p></div></a>";
    }).join("");
  }

  function openPanel() {
    renderFeed();
    document.querySelector(".notify-overlay").classList.add("open");
    document.querySelector(".notify-panel").classList.add("open");
    var store = loadStore();
    store.unread = 0;
    saveStore(store);
    updateBadge(store);
  }

  function closePanel() {
    var o = document.querySelector(".notify-overlay");
    var p = document.querySelector(".notify-panel");
    if (o) o.classList.remove("open");
    if (p) p.classList.remove("open");
  }

  function boot() {
    buildChrome();
    updateBadge(loadStore());
    fetch(DATA_URL).then(function (r) { return r.json(); }).then(function (json) {
      data = json;
      fillHome();
      fillRappels();
      fillLecteurPlate();
      renderFeed();
      return fetch(PROG_URL).then(function (r) { return r.ok ? r.json() : null; });
    }).then(function (prog) {
      programme = prog;
      fillNextCourse(document);
      fillLecteurPlate();
      fillEmploiPlate();
      tick();
      timer = setInterval(tick, 30000);
    }).catch(function () {});
  }

  document.addEventListener("DOMContentLoaded", boot);
})();
