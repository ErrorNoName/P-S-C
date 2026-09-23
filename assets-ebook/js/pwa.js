/* Psyclopédia — installation en application et alertes de cours. */
(function () {
  "use strict";

  var ROOT = (document.body && document.body.getAttribute("data-root")) || "./";
  var DISMISS_KEY = "psyclopedia_pwa_prompt_v1";
  var NOTIF_KEY = "psyclopedia_notif_v1";
  var DISMISS_MS = 14 * 24 * 60 * 60 * 1000;
  var deferredInstall = null;

  function abs(url) {
    try { return new URL(url, location.href).href; } catch (e) { return url; }
  }

  function injectHead() {
    if (!document.querySelector('link[rel="manifest"]')) {
      var link = document.createElement("link");
      link.rel = "manifest";
      link.href = abs(ROOT + "manifest.webmanifest");
      document.head.appendChild(link);
    }
    var metas = [
      ["theme-color", "#50A67E"],
      ["mobile-web-app-capable", "yes"],
      ["apple-mobile-web-app-capable", "yes"],
      ["apple-mobile-web-app-title", "Psyclopédia"],
    ];
    metas.forEach(function (pair) {
      if (document.querySelector('meta[name="' + pair[0] + '"]')) return;
      var meta = document.createElement("meta");
      meta.name = pair[0];
      meta.content = pair[1];
      document.head.appendChild(meta);
    });
    if (!document.querySelector('link[rel="apple-touch-icon"]')) {
      var icon = document.createElement("link");
      icon.rel = "apple-touch-icon";
      icon.href = abs(ROOT + "assets-ebook/icons/icon-192.png");
      document.head.appendChild(icon);
    }
  }

  function registerWorker() {
    if (!("serviceWorker" in navigator)) return;
    var script = abs(ROOT + "sw.js");
    navigator.serviceWorker.register(script).catch(function () {});
  }

  function standalone() {
    return window.matchMedia("(display-mode: standalone)").matches || window.navigator.standalone === true;
  }

  function ios() {
    return /iphone|ipad|ipod/i.test(navigator.userAgent) && !window.MSStream;
  }

  function loadDismiss() {
    try { return JSON.parse(localStorage.getItem(DISMISS_KEY) || "{}"); }
    catch (e) { return {}; }
  }

  function saveDismiss(patch) {
    var cur = loadDismiss();
    Object.keys(patch).forEach(function (k) { cur[k] = patch[k]; });
    localStorage.setItem(DISMISS_KEY, JSON.stringify(cur));
  }

  function fresh(ts) {
    return ts && (Date.now() - ts) < DISMISS_MS;
  }

  function notifState() {
    if (typeof Notification === "undefined") return "unsupported";
    return Notification.permission;
  }

  function enableCourseAlerts() {
    if (typeof Notification === "undefined") return Promise.resolve("unsupported");
    return Notification.requestPermission().then(function (perm) {
      var store = {};
      try { store = JSON.parse(localStorage.getItem(NOTIF_KEY) || "{}"); } catch (e) {}
      store.thoughts = store.thoughts !== false;
      store.cours = true;
      store.browser = perm === "granted";
      store.quietStart = store.quietStart || "22:00";
      store.quietEnd = store.quietEnd || "08:00";
      store.shown = store.shown || {};
      store.unread = store.unread || 0;
      localStorage.setItem(NOTIF_KEY, JSON.stringify(store));
      return perm;
    });
  }

  function hideBanner() {
    var el = document.querySelector(".pwa-banner");
    if (el && el.parentNode) el.parentNode.removeChild(el);
  }

  function showBanner() {
    if (document.querySelector(".pwa-banner")) return;
    var dismissed = loadDismiss();
    var needInstall = !standalone() && !fresh(dismissed.install);
    var needNotif = notifState() === "default" && !fresh(dismissed.notif);
    if (!needInstall && !needNotif) return;

    var el = document.createElement("aside");
    el.className = "pwa-banner";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-label", "Installer Psyclopédia");
    var installBtn = needInstall
      ? '<button type="button" class="btn btn-primary" data-pwa-install>Installer l\'application</button>'
      : "";
    var notifBtn = needNotif
      ? '<button type="button" class="btn btn-secondary" data-pwa-notif>Alertes de cours</button>'
      : "";
    var hint = "";
    if (needInstall && ios()) {
      hint = "<p class=\"pwa-hint\">Sur iPhone : Partager, puis « Sur l'écran d'accueil ».</p>";
    } else if (needInstall && !deferredInstall) {
      hint = "<p class=\"pwa-hint\">Tu peux aussi l'installer depuis le menu du navigateur.</p>";
    }
    el.innerHTML =
      "<strong>Garder Psyclopédia sous la main</strong>" +
      "<p>Installe le site comme une application, et demande à être prévenu quand un cours va commencer.</p>" +
      hint +
      '<div class="pwa-actions">' + installBtn + notifBtn +
      '<button type="button" class="pwa-later" data-pwa-later>Plus tard</button></div>';
    document.body.appendChild(el);
  }

  window.addEventListener("beforeinstallprompt", function (event) {
    event.preventDefault();
    deferredInstall = event;
    var hint = document.querySelector(".pwa-hint");
    if (hint) hint.textContent = "L'installation s'ouvre dans le navigateur.";
  });

  document.addEventListener("click", function (event) {
    var install = event.target.closest("[data-pwa-install]");
    var notif = event.target.closest("[data-pwa-notif], [data-cours-alerts]");
    var later = event.target.closest("[data-pwa-later]");
    if (install) {
      event.preventDefault();
      if (deferredInstall) {
        deferredInstall.prompt();
        deferredInstall.userChoice.then(function () {
          deferredInstall = null;
          saveDismiss({ install: Date.now() });
          hideBanner();
        });
      } else if (ios()) {
        saveDismiss({ install: Date.now() });
      } else {
        saveDismiss({ install: Date.now() });
        hideBanner();
      }
    }
    if (notif) {
      event.preventDefault();
      enableCourseAlerts().then(function () {
        saveDismiss({ notif: Date.now() });
        hideBanner();
      });
    }
    if (later) {
      saveDismiss({ install: Date.now(), notif: Date.now() });
      hideBanner();
    }
  });

  injectHead();
  registerWorker();
  window.PsyPwa = { enableCourseAlerts: enableCourseAlerts, abs: abs };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(showBanner, 900);
    });
  } else {
    setTimeout(showBanner, 900);
  }
})();
