/* Cahier Psyclopédia — texte sur l'appareil, Drive facultatif, note orale WAV, dictée en direct. */
(function () {
  "use strict";

  var FMT = window.PsyCahierFormat;
  var DRIVE = "https://www.googleapis.com/drive/v3";
  var UPLOAD = "https://www.googleapis.com/upload/drive/v3";
  var SCOPE = "https://www.googleapis.com/auth/drive.file";
  var MAX_AUDIO = 3200000;
  var MAX_SEC = 60;
  var VOICE_RATE = 22050;

  var rootEl;
  var user;
  var docs = [];
  var active = null;
  var audios = {};
  var token = "";
  var tokenExp = 0;
  var tokenClient = null;
  var folderId = "";
  var saveTimer = 0;
  var savedRange = null;
  var recording = null;
  var listenOn = false;
  var dictateOn = false;
  var speechMode = "";
  var noteHold = false;
  var reelPhase = "idle";
  var reelMicCool = false;
  var reelMode = "vocal";
  var reel = null;
  var reelTranscript = "";
  var reelViewId = "";
  var listenRec = null;
  var speechState = null;
  var speechRunning = false;
  var speechStarting = false;
  var speechStartedAt = 0;
  var speechShort = 0;
  var speechTimer = null;
  var micStream = null;
  var lexicon = null;
  var shownAt = {};
  var player = null;
  var playingId = "";

  function $(id) { return document.getElementById(id); }
  function cfg() { return window.PSYCLOPEDIA_COMPTE || {}; }
  function rootPrefix() { return document.body.getAttribute("data-root") || "./"; }
  function toast(msg) { if (window.toast) window.toast(msg); }
  function hex(n) {
    var s = "";
    var bytes = new Uint8Array(n);
    crypto.getRandomValues(bytes);
    bytes.forEach(function (b) { s += b.toString(16).padStart(2, "0"); });
    return s;
  }
  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }
  function storageKey() { return "psyclopedia_cahier_v1:" + (user && user.id || "x"); }
  function isLocalTest() {
    var host = location.hostname;
    return (host === "127.0.0.1" || host === "localhost") && window.PSY_CAHIER_TEST && window.PSY_CAHIER_TEST.user;
  }

  function loadLocal() {
    try {
      var raw = JSON.parse(localStorage.getItem(storageKey()) || "null");
      docs = raw && raw.docs ? raw.docs : [];
    } catch (e) {
      docs = [];
    }
  }

  function slimDocs() {
    return docs.map(function (doc) {
      var aud = {};
      Object.keys(doc.audios || {}).forEach(function (id) {
        var meta = doc.audios[id] || {};
        var copy = {
          mime: meta.mime || "",
          duration: meta.duration || 0,
          transcript: meta.transcript || ""
        };
        if (meta.idb) copy.idb = 1;
        else if (meta.b64 && meta.b64.length < 400000) copy.b64 = meta.b64;
        aud[id] = copy;
      });
      return {
        id: doc.id,
        title: doc.title || "",
        html: doc.html || "",
        audios: aud,
        updatedAt: doc.updatedAt || "",
        driveId: doc.driveId || ""
      };
    });
  }

  function persistLocal() {
    try {
      localStorage.setItem(storageKey(), JSON.stringify({ docs: slimDocs() }));
    } catch (e) {
      setSave("Mémoire pleine — raccourcis les notes orales");
    }
  }

  function audioDb() {
    return new Promise(function (resolve, reject) {
      if (!window.indexedDB) { reject(new Error("idb")); return; }
      var req = indexedDB.open("psyclopedia-cahier-audio", 2);
      req.onupgradeneeded = function () {
        var db = req.result;
        if (!db.objectStoreNames.contains("clips")) db.createObjectStore("clips");
        if (!db.objectStoreNames.contains("seances")) db.createObjectStore("seances");
      };
      req.onsuccess = function () { resolve(req.result); };
      req.onerror = function () { reject(req.error || new Error("idb")); };
    });
  }

  function saveClip(id, meta) {
    if (!meta || !meta.b64) return Promise.resolve(false);
    return audioDb().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("clips", "readwrite");
        tx.objectStore("clips").put({
          mime: meta.mime,
          b64: meta.b64,
          duration: meta.duration,
          transcript: meta.transcript || ""
        }, id);
        tx.oncomplete = function () { resolve(true); };
        tx.onerror = function () { reject(tx.error || new Error("idb")); };
      });
    }).then(function () {
      meta.idb = 1;
      return true;
    }).catch(function () { return false; });
  }

  function loadClip(id) {
    return audioDb().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("clips", "readonly");
        var req = tx.objectStore("clips").get(id);
        req.onsuccess = function () { resolve(req.result || null); };
        req.onerror = function () { reject(req.error || new Error("idb")); };
      });
    }).catch(function () { return null; });
  }

  function hydrateClips() {
    var jobs = [];
    docs.forEach(function (doc) {
      Object.keys(doc.audios || {}).forEach(function (id) {
        var meta = doc.audios[id];
        if (!meta || meta.b64) return;
        jobs.push(loadClip(id).then(function (saved) {
          if (!saved || !saved.b64) return;
          doc.audios[id] = {
            mime: saved.mime || meta.mime,
            b64: saved.b64,
            duration: saved.duration || meta.duration,
            transcript: saved.transcript || meta.transcript || "",
            idb: 1
          };
        }));
      });
    });
    return Promise.all(jobs).then(function () {
      if (active) audios = active.audios || {};
    });
  }

  function publicDoc(doc) {
    return {
      format: "psyclopedia-cahier",
      version: 1,
      id: doc.id,
      title: doc.title || "",
      html: doc.html || "",
      audios: doc.audios || {},
      updatedAt: doc.updatedAt || ""
    };
  }

  function setSync(text) {
    var el = $("cahier-sync");
    var mob = $("cahier-sync-mobile");
    if (el) el.textContent = text;
    if (mob) mob.textContent = text;
  }

  function setSave(text) {
    var el = $("cahier-save");
    if (el) el.textContent = text;
  }

  function countWords() {
    var body = $("cahier-body");
    var clone = body.cloneNode(true);
    clone.querySelectorAll(".voix-bulle").forEach(function (n) { n.remove(); });
    var n = (clone.textContent || "").trim().split(/\s+/).filter(Boolean).length;
    $("cahier-words").textContent = n + (n > 1 ? " mots" : " mot");
  }

  function inlineHtml(el) {
    var html = "";
    Array.prototype.forEach.call(el.childNodes, function (node) {
      if (node.nodeType === 3) {
        html += escapeHtml(node.textContent);
        return;
      }
      if (node.nodeType !== 1) return;
      if (node.classList && node.classList.contains("voix-bulle")) {
        html += '<voix data-voix="' + escapeHtml(node.getAttribute("data-voix") || "") +
          '" data-sec="' + escapeHtml(node.getAttribute("data-sec") || "0") + '"></voix>';
        return;
      }
      var inner = inlineHtml(node);
      var tag = node.tagName;
      if (tag === "B" || tag === "STRONG") html += "<strong>" + inner + "</strong>";
      else if (tag === "I" || tag === "EM") html += "<em>" + inner + "</em>";
      else if (tag === "U") html += "<u>" + inner + "</u>";
      else if (tag === "S" || tag === "STRIKE" || tag === "DEL") html += "<s>" + inner + "</s>";
      else if (tag === "MARK") html += "<mark>" + inner + "</mark>";
      else if (tag === "FONT") html += '<font size="' + escapeHtml(node.getAttribute("size") || "3") + '">' + inner + "</font>";
      else if (tag === "BR") html += "<br>";
      else if (tag === "SPAN") {
        var piece = inner;
        var weight = node.style.fontWeight;
        if (weight === "bold" || Number(weight) >= 600) piece = "<strong>" + piece + "</strong>";
        if (node.style.fontStyle === "italic") piece = "<em>" + piece + "</em>";
        if (node.style.fontSize) piece = '<span style="font-size:' + node.style.fontSize + '">' + piece + "</span>";
        if (/background/i.test(node.getAttribute("style") || "")) piece = "<mark>" + piece + "</mark>";
        html += piece;
      } else html += inner;
    });
    return html;
  }

  function serializeBody() {
    var body = $("cahier-body");
    var blocks = [];
    Array.prototype.forEach.call(body.childNodes, function (node) {
      if (node.nodeType === 3) {
        if (node.textContent.trim()) blocks.push("<p>" + escapeHtml(node.textContent) + "</p>");
        return;
      }
      if (node.nodeType !== 1) return;
      if (node.classList && node.classList.contains("voix-bulle")) {
        blocks.push("<p>" + inlineHtml({ childNodes: [node] }) + "</p>");
        return;
      }
      if (node.tagName === "UL" || node.tagName === "OL") {
        Array.prototype.forEach.call(node.children, function (li) {
          blocks.push("<li>" + inlineHtml(li) + "</li>");
        });
        return;
      }
      var tag = node.tagName.toLowerCase();
      if (["h1", "h2", "h3", "blockquote", "li", "p"].indexOf(tag) < 0) tag = "p";
      var align = (node.style && node.style.textAlign) || node.getAttribute("align") || "";
      var style = "";
      if (align && align !== "start" && align !== "left") {
        var css = (align === "full" || align === "justify") ? "justify" : align;
        style = ' style="text-align:' + css + '"';
      }
      blocks.push("<" + tag + style + ">" + inlineHtml(node) + "</" + tag + ">");
    });
    return blocks.join("") || "<p><br></p>";
  }

  function renderList() {
    var ul = $("cahier-list");
    ul.textContent = "";
    docs.slice().sort(function (a, b) { return String(b.updatedAt).localeCompare(String(a.updatedAt)); })
      .forEach(function (doc) {
        var li = document.createElement("li");
        var btn = document.createElement("button");
        btn.type = "button";
        if (active && doc.id === active.id) btn.className = "is-on";
        var strong = document.createElement("strong");
        strong.textContent = doc.title || "Sans titre";
        var span = document.createElement("span");
        span.textContent = doc.driveId ? "Dans Drive" : "Sur cet appareil";
        btn.appendChild(strong);
        btn.appendChild(span);
        btn.addEventListener("click", function () { openDoc(doc.id); });
        li.appendChild(btn);
        ul.appendChild(li);
      });
  }

  function snapshot() {
    if (!active) return;
    active.title = $("cahier-title").value.trim();
    active.html = serializeBody();
    active.audios = audios;
    active.updatedAt = new Date().toISOString();
    var i;
    for (i = 0; i < docs.length; i++) if (docs[i].id === active.id) docs[i] = active;
    persistLocal();
    countWords();
    renderList();
  }

  function scheduleSave() {
    setSave("Enregistrement…");
    clearTimeout(saveTimer);
    saveTimer = setTimeout(function () {
      snapshot();
      pushDrive().then(function () {
        setSave(active && active.driveId ? "Enregistré dans Drive et sur cet appareil" : "Enregistré sur cet appareil");
      }).catch(function () {
        setSave("Enregistré sur cet appareil");
      });
    }, 700);
  }

  function sanitizeStored(html) {
    var raw = String(html || "")
      .replace(/<script[\s\S]*?<\/script>/gi, "")
      .replace(/\son\w+\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)/gi, "")
      .replace(/javascript:/gi, "");
    var wrap = document.createElement("div");
    wrap.innerHTML = raw;
    var allowed = {
      P: 1, H1: 1, H2: 1, H3: 1, BLOCKQUOTE: 1, UL: 1, OL: 1, LI: 1, BR: 1,
      STRONG: 1, B: 1, EM: 1, I: 1, U: 1, S: 1, STRIKE: 1, DEL: 1, MARK: 1,
      FONT: 1, SPAN: 1, VOIX: 1
    };
    function clean(node) {
      var child = node.firstChild;
      while (child) {
        var next = child.nextSibling;
        if (child.nodeType !== 1) { child = next; continue; }
        if (!allowed[child.tagName]) {
          while (child.firstChild) node.insertBefore(child.firstChild, child);
          node.removeChild(child);
          child = node.firstChild;
          continue;
        }
        Array.prototype.slice.call(child.attributes).forEach(function (attr) {
          var name = attr.name.toLowerCase();
          var keep = false;
          if (name === "style") {
            var align = (child.style.textAlign || "").toLowerCase();
            child.removeAttribute("style");
            if (align === "center" || align === "right" || align === "justify") child.style.textAlign = align;
            return;
          }
          if (name === "align" && /^(left|center|right|justify)$/i.test(attr.value)) keep = true;
          else if (name === "size" && child.tagName === "FONT" && /^[1-7]$/.test(attr.value)) keep = true;
          else if ((name === "data-voix" || name === "data-sec") && child.tagName === "VOIX" && /^[a-z0-9_-]{1,40}$/i.test(attr.value)) keep = true;
          if (!keep) child.removeAttribute(attr.name);
        });
        clean(child);
        child = next;
      }
    }
    clean(wrap);
    return wrap.innerHTML;
  }

  function hydrate(html) {
    var wrap = document.createElement("div");
    wrap.innerHTML = sanitizeStored(html) || "<p><br></p>";
    wrap.querySelectorAll("voix").forEach(function (node) {
      var span = document.createElement("span");
      span.className = "voix-bulle";
      span.contentEditable = "false";
      span.setAttribute("data-voix", node.getAttribute("data-voix") || "");
      var sec = node.getAttribute("data-sec") || "0";
      span.setAttribute("data-sec", sec);
      span.innerHTML = '<span class="voix-onde" aria-hidden="true"></span><span class="voix-temps">' +
        FMT.formatSec(sec) + "</span>";
      node.replaceWith(span);
    });
    return wrap.innerHTML || "<p><br></p>";
  }

  function fillEditor(doc) {
    active = doc;
    audios = doc.audios || {};
    $("cahier-title").value = doc.title || "";
    $("cahier-body").innerHTML = hydrate(doc.html);
    setTimeout(function () { decorateLinks($("cahier-body")); }, 300);
    countWords();
    renderList();
    setSave(doc.driveId ? "Dans Drive" : "Brouillon");
  }

  function openDoc(id) {
    var doc = null;
    docs.forEach(function (item) { if (item.id === id) doc = item; });
    if (!doc) return;
    if (doc.driveId && token) {
      driveFetch(DRIVE + "/files/" + encodeURIComponent(doc.driveId) + "?alt=media").then(function (res) {
        if (!res.ok) throw new Error("lecture");
        return res.json();
      }).then(function (data) {
        doc.html = data.html || doc.html;
        doc.audios = data.audios || doc.audios;
        doc.title = data.title || doc.title;
        fillEditor(doc);
        persistLocal();
      }).catch(function () { fillEditor(doc); });
      return;
    }
    fillEditor(doc);
  }

  function newDoc() {
    var doc = {
      id: hex(8),
      title: "",
      html: "<p><br></p>",
      audios: {},
      updatedAt: new Date().toISOString(),
      driveId: ""
    };
    docs.unshift(doc);
    fillEditor(doc);
    persistLocal();
    $("cahier-title").focus();
    scheduleSave();
  }

  function clientId() {
    return (cfg().googleClientId || "").trim();
  }

  function loadGsi() {
    return new Promise(function (resolve) {
      if (window.google && google.accounts) { resolve(); return; }
      var s = document.createElement("script");
      s.src = "https://accounts.google.com/gsi/client";
      s.async = true;
      s.onload = function () { resolve(); };
      s.onerror = function () { resolve(); };
      document.head.appendChild(s);
    });
  }

  function ensureToken(interactive) {
    if (isLocalTest()) return Promise.reject(new Error("essai"));
    if (token && tokenExp > Date.now() + 60000) return Promise.resolve(token);
    return loadGsi().then(function () {
      if (!window.google || !google.accounts || !google.accounts.oauth2) {
        throw new Error("Google est injoignable.");
      }
      if (!tokenClient) {
        tokenClient = google.accounts.oauth2.initTokenClient({
          client_id: clientId(),
          scope: SCOPE,
          callback: function () {}
        });
      }
      return new Promise(function (resolve, reject) {
        tokenClient.callback = function (resp) {
          if (!resp || resp.error) {
            reject(new Error(resp && resp.error || "Drive refusé"));
            return;
          }
          token = resp.access_token;
          tokenExp = Date.now() + (Number(resp.expires_in) || 3600) * 1000;
          resolve(token);
        };
        tokenClient.requestAccessToken({ prompt: interactive ? "consent" : "" });
      });
    });
  }

  function driveFetch(url, options) {
    options = options || {};
    var headers = options.headers || {};
    headers.Authorization = "Bearer " + token;
    options.headers = headers;
    return fetch(url, options);
  }

  function fileName(doc) {
    var title = (doc.title || "Sans titre").replace(/[\\/:*?"<>|]/g, " ").trim() || "Sans titre";
    return title.slice(0, 80) + ".psy.json";
  }

  function ensureFolder() {
    if (folderId) return Promise.resolve(folderId);
    var q = "mimeType='application/vnd.google-apps.folder' and trashed=false and appProperties has { key='psy' and value='cahiers' }";
    return driveFetch(DRIVE + "/files?spaces=drive&fields=files(id)&q=" + encodeURIComponent(q))
      .then(function (res) { return res.json(); })
      .then(function (data) {
        if (data.files && data.files[0]) {
          folderId = data.files[0].id;
          return folderId;
        }
        return driveFetch(DRIVE + "/files", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: "Psyclopédia — cahiers",
            mimeType: "application/vnd.google-apps.folder",
            appProperties: { psy: "cahiers" }
          })
        }).then(function (res) { return res.json(); }).then(function (created) {
          folderId = created.id;
          return folderId;
        });
      });
  }

  function pushDrive() {
    if (!active || isLocalTest() || !token) return Promise.resolve();
    return ensureToken(false).then(function () {
      return ensureFolder();
    }).then(function () {
      var boundary = "psy" + hex(6);
      var meta = {
        name: fileName(active),
        mimeType: "application/json",
        appProperties: { psy: "cahier", doc: active.id }
      };
      if (!active.driveId) meta.parents = [folderId];
      var payload = JSON.stringify(publicDoc(active));
      var body = "--" + boundary + "\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n" +
        JSON.stringify(meta) + "\r\n--" + boundary + "\r\nContent-Type: application/json\r\n\r\n" +
        payload + "\r\n--" + boundary + "--";
      var url = active.driveId
        ? UPLOAD + "/files/" + encodeURIComponent(active.driveId) + "?uploadType=multipart&fields=id"
        : UPLOAD + "/files?uploadType=multipart&fields=id";
      return driveFetch(url, {
        method: active.driveId ? "PATCH" : "POST",
        headers: { "Content-Type": "multipart/related; boundary=" + boundary },
        body: body
      }).then(function (res) {
        if (res.status === 401) { token = ""; throw new Error("session"); }
        if (!res.ok) throw new Error("drive");
        return res.json();
      }).then(function (data) {
        if (data.id) active.driveId = data.id;
        persistLocal();
        setSync("Relié à Google Drive");
        renderList();
      });
    }).catch(function (err) {
      if (!token) setSync("Enregistré sur cet appareil");
      throw err;
    });
  }

  function driveErrorText(err) {
    var code = String(err && (err.message || err.error) || err || "");
    if (code.indexOf("access_denied") !== -1 || code.indexOf("403") !== -1) {
      return "Google bloque le lien (erreur 403 : l'application est encore en test). " +
        "Le cahier reste sur cet appareil. Dans Google Cloud, écran de consentement OAuth : " +
        "ajoute ce Gmail comme utilisateur test, ou publie l'application. " +
        "Le site ne peut pas lever ce blocage tout seul.";
    }
    if (code.indexOf("popup") !== -1) return "Fenêtre Google fermée. Le cahier reste sur cet appareil.";
    return "Drive n'a pas autorisé le cahier. Le texte reste enregistré sur cet appareil.";
  }

  function showDriveMsg(text) {
    var el = $("cahier-drive-msg");
    if (!el) { setSync(text); return; }
    el.hidden = !text;
    el.textContent = text || "";
  }

  function pullDrive() {
    if (isLocalTest()) {
      setSync("Essai local, sans Drive");
      return Promise.resolve();
    }
    return ensureToken(false).then(function () {
      var q = "trashed=false and appProperties has { key='psy' and value='cahier' }";
      return driveFetch(DRIVE + "/files?spaces=drive&fields=files(id,name,appProperties,modifiedTime)&q=" + encodeURIComponent(q));
    }).then(function (res) {
      if (!res || !res.ok) throw new Error("liste");
      return res.json();
    }).then(function (data) {
      (data.files || []).forEach(function (file) {
        var id = file.appProperties && file.appProperties.doc;
        var known = null;
        docs.forEach(function (doc) { if (doc.driveId === file.id || (id && doc.id === id)) known = doc; });
        if (!known) {
          docs.push({
            id: id || hex(8),
            title: (file.name || "").replace(/\.psy\.json$/, ""),
            html: "<p><br></p>",
            audios: {},
            updatedAt: file.modifiedTime || "",
            driveId: file.id
          });
        } else if (!known.driveId) known.driveId = file.id;
      });
      persistLocal();
      renderList();
      setSync("Relié à Google Drive");
    }).catch(function () {
      setSync("Pas encore relié à Drive");
    });
  }

  function askDrive() {
    showDriveMsg("");
    ensureToken(true).then(pullDrive).then(function () {
      return pushDrive();
    }).then(function () {
      setSync("Enregistré sur cet appareil, et dans Google Drive");
      showDriveMsg("");
    }).catch(function (err) {
      token = "";
      setSync("Enregistré sur cet appareil");
      showDriveMsg(driveErrorText(err));
    });
  }

  function placeMic() {
    var mic = $("cahier-mic");
    var body = $("cahier-body");
    if (!mic || !body) return;
    if ($("cahier-work").hidden) { mic.hidden = true; return; }
    var sel = window.getSelection();
    var useSaved = (recording || speechMode) && savedRange && body.contains(savedRange.startContainer);
    if (!useSaved && (!sel || !sel.rangeCount || !body.contains(sel.anchorNode))) {
      mic.hidden = true;
      return;
    }
    var range = useSaved ? savedRange.cloneRange() : sel.getRangeAt(0).cloneRange();
    if (!recording) range.collapse(false);
    var rects = range.getClientRects();
    var rect = rects.length ? rects[rects.length - 1] : body.getBoundingClientRect();
    if (!rect || (!rect.width && !rect.height)) rect = body.getBoundingClientRect();
    var top = rect.bottom + 8;
    if (top > window.innerHeight - 56) top = Math.max(8, rect.top - 48);
    var left = Math.min(Math.max(8, rect.left), window.innerWidth - 140);
    mic.hidden = false;
    mic.style.top = top + "px";
    mic.style.left = left + "px";
  }

  function rememberRange() {
    var sel = window.getSelection();
    var body = $("cahier-body");
    if (!sel || !sel.rangeCount || !body.contains(sel.anchorNode)) return;
    savedRange = sel.getRangeAt(0).cloneRange();
  }

  function insertVoiceNote(opts) {
    opts = opts || {};
    var id = opts.id || hex(8);
    var sec = Math.max(1, Math.round(opts.duration || 1));
    audios[id] = {
      mime: opts.mime || "audio/webm",
      b64: opts.b64 || "",
      duration: sec,
      transcript: opts.transcript || ""
    };
    var span = document.createElement("span");
    span.className = "voix-bulle";
    span.contentEditable = "false";
    span.setAttribute("data-voix", id);
    span.setAttribute("data-sec", String(sec));
    span.innerHTML = '<span class="voix-onde" aria-hidden="true"></span><span class="voix-temps">' +
      FMT.formatSec(sec) + "</span>";
    var body = $("cahier-body");
    var range = savedRange;
    var live = window.getSelection();
    if ((!range || !body.contains(range.startContainer)) && live && live.rangeCount && body.contains(live.anchorNode)) {
      range = live.getRangeAt(0).cloneRange();
    }
    if (!range || !body.contains(range.startContainer)) {
      body.appendChild(document.createTextNode(" "));
      body.appendChild(span);
    } else {
      range.collapse(false);
      range.insertNode(span);
      var space = document.createTextNode(" ");
      span.after(space);
      range.setStartAfter(space);
      range.collapse(true);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    }
    scheduleSave();
    return id;
  }

  function bytesToB64(bytes) {
    var parts = [];
    var size = 0x8000;
    var i;
    for (i = 0; i < bytes.length; i += size) {
      parts.push(String.fromCharCode.apply(null, bytes.subarray(i, i + size)));
    }
    return btoa(parts.join(""));
  }

  function concatFloats(chunks) {
    var n = 0;
    var i;
    for (i = 0; i < chunks.length; i++) n += chunks[i].length;
    var out = new Float32Array(n);
    var offset = 0;
    for (i = 0; i < chunks.length; i++) {
      out.set(chunks[i], offset);
      offset += chunks[i].length;
    }
    return out;
  }

  function showLive(text) {
    var bar = $("cahier-live");
    var el = $("cahier-live-text");
    if (!bar || !el) return;
    var value = String(text || "").trim();
    bar.hidden = !value;
    el.textContent = value;
  }

  function writingBlock(body) {
    var el = body.lastElementChild;
    if (!el || !/^(P|DIV|H1|H2|H3|LI|BLOCKQUOTE)$/.test(el.tagName)) {
      el = document.createElement("p");
      body.appendChild(el);
    }
    var br = el.querySelector("br");
    if (br && (el.textContent || "").trim() === "") br.remove();
    return el;
  }

  function rememberInserted(node, offset) {
    var range = document.createRange();
    range.setStart(node, offset);
    range.collapse(true);
    savedRange = range;
  }

  function insertPlainText(text) {
    var value = String(text || "");
    if (!value) return;
    var body = $("cahier-body");
    if (!body) return;
    var range = savedRange;
    var node = null;
    var at = 0;
    if (range && range.startContainer.nodeType === 3 && body.contains(range.startContainer)) {
      node = range.startContainer;
      at = Math.min(range.startOffset, node.length);
      node.insertData(at, value);
      at += value.length;
    } else {
      var block = writingBlock(body);
      node = block.lastChild && block.lastChild.nodeType === 3 ? block.lastChild : null;
      if (!node) {
        node = document.createTextNode("");
        block.appendChild(node);
      }
      node.appendData(value);
      at = node.length;
    }
    rememberInserted(node, at);
    if (!speechMode) {
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(savedRange);
    }
    scheduleSave();
    placeMic();
  }

  function speechRecognizer() {
    var Ctor = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!Ctor) return null;
    var rec = new Ctor();
    rec.lang = "fr-FR";
    rec.interimResults = true;
    rec.continuous = true;
    rec.maxAlternatives = 1;
    return rec;
  }

  function clearSpeechTimer() {
    if (!speechTimer) return;
    clearTimeout(speechTimer);
    speechTimer = null;
  }

  function micLive() {
    return !!(micStream && micStream.getAudioTracks().some(function (track) {
      return track.readyState === "live";
    }));
  }

  function openMic() {
    if (micLive()) return Promise.resolve(micStream);
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      return Promise.reject(new Error("mic"));
    }
    return navigator.mediaDevices.getUserMedia({
      audio: {
        echoCancellation: true,
        noiseSuppression: false,
        autoGainControl: true
      }
    }).then(function (stream) {
      micStream = stream;
      return stream;
    });
  }

  function closeMic() {
    if (recording || desiredSpeech() || reelPhase === "run" || reelPhase === "pause") return;
    if (!micStream) return;
    try { micStream.getTracks().forEach(function (track) { track.stop(); }); } catch (e) { /* ignore */ }
    micStream = null;
  }

  function stopSpeech() {
    speechMode = "";
    speechRunning = false;
    speechStarting = false;
    clearSpeechTimer();
    if (listenRec) {
      var rec = listenRec;
      listenRec = null;
      try {
        rec.onstart = null;
        rec.onend = null;
        rec.onerror = null;
        rec.onresult = null;
        rec.stop();
      } catch (e) { /* ignore */ }
    }
    closeMic();
    if (!recording) restoreCaret();
  }

  function restoreCaret() {
    var body = $("cahier-body");
    if (!savedRange || !body || !body.contains(savedRange.startContainer)) return;
    try {
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(savedRange);
    } catch (e) { /* curseur déjà perdu */ }
  }

  function kickSpeech(rec, mode) {
    clearSpeechTimer();
    if (listenRec !== rec || speechMode !== mode || desiredSpeech() !== mode) return;
    if (speechRunning || speechStarting) return;
    speechStarting = true;
    try {
      rec.start();
    } catch (e) {
      speechStarting = false;
      speechTimer = setTimeout(function () { kickSpeech(rec, mode); }, 350);
    }
  }

  function desiredSpeech() {
    if (reelPhase === "run" || reelPhase === "arm") return "reel";
    if (recording || noteHold) return "note";
    if (dictateOn) return "dictate";
    if (listenOn) return "listen";
    return "";
  }

  function startSpeech(mode, keep) {
    var kept = keep && speechState ? speechState : null;
    stopSpeech();
    if (!mode) { showLive(""); return; }
    var rec = speechRecognizer();
    if (!rec) {
      if (mode === "reel") {
        toast("Le son est enregistré. La transcription demande Chrome, Edge ou Safari.");
        return;
      }
      if (mode !== "note") toast("La dictée fonctionne dans Chrome, Edge ou Safari.");
      if (mode === "dictate") {
        dictateOn = false;
        var dictateBtn = $("cahier-dictate");
        if (dictateBtn) dictateBtn.setAttribute("aria-pressed", "false");
      }
      if (mode === "listen") {
        listenOn = false;
        $("cahier-listen").setAttribute("aria-pressed", "false");
      }
      return;
    }
    speechMode = mode;
    speechState = kept || FMT.speechState();
    speechShort = 0;
    rec.onresult = function (ev) {
      if (speechMode !== mode || !speechState) return;
      var step = FMT.applySpeechEvent(speechState, ev, Date.now());
      if (mode === "reel") {
        var heard = speechState.log || "";
        if (step.live) heard = (heard + " " + step.live).trim();
        reelTranscript = heard.trim();
        paintReelLive();
        return;
      }
      if (step.added && mode === "dictate") insertPlainText(step.added + " ");
      if (mode === "note" && recording) {
        var noteHeard = speechState.log || "";
        if (step.live) noteHeard = (noteHeard + " " + step.live).trim();
        recording.said = noteHeard.trim();
      }
      if (step.added) considerUtterance(speechState.tail);
      else if (step.live && step.live.length > 10) considerUtterance(step.live);
      showLive(mode === "listen" ? step.preview : step.live);
    };
    var speechError = "";
    rec.onstart = function () {
      if (listenRec !== rec) return;
      speechStarting = false;
      speechRunning = true;
      speechStartedAt = Date.now();
      speechError = "";
      if (mode === "reel" && !reelMicCool) setTimeout(attachReelMic, 600);
    };
    rec.onerror = function (ev) {
      speechError = (ev && ev.error) || "";
      if (speechError === "not-allowed") toast("Micro refusé pour la dictée.");
    };
    rec.onend = function () {
      if (listenRec !== rec) return;
      var lasted = speechStartedAt ? Date.now() - speechStartedAt : 0;
      var failed = speechError;
      speechError = "";
      speechRunning = false;
      speechStarting = false;
      if (lasted > 0 && lasted < 400) speechShort += 1;
      else speechShort = 0;
      if (speechMode !== mode || desiredSpeech() !== mode) return;
      if (failed === "audio-capture" && mode === "reel") {
        reelMicCool = true;
        releaseReelMic();
        clearSpeechTimer();
        speechShort = 0;
        speechTimer = setTimeout(function () { kickSpeech(rec, mode); }, 200);
        return;
      }
      if (failed === "audio-capture" && mode === "note" && recording) {
        clearSpeechTimer();
        speechTimer = setTimeout(function () { kickSpeech(rec, mode); }, 700);
        return;
      }
      if (speechShort >= 8) return;
      clearSpeechTimer();
      var wait = speechShort >= 3 ? 800 : 80;
      speechTimer = setTimeout(function () { kickSpeech(rec, mode); }, wait);
    };
    listenRec = rec;
    kickSpeech(rec, mode);
  }

  function syncSpeech() {
    var mode = desiredSpeech();
    if (mode === speechMode && (mode === "" || listenRec)) return;
    startSpeech(mode);
  }

  function stopRecording() {
    if (!recording) return;
    noteHold = false;
    var rec = recording;
    recording = null;
    var rate = rec.sampleRate || VOICE_RATE;
    try { rec.processor.onaudioprocess = null; } catch (e0) { /* ignore */ }
    try { rec.processor.disconnect(); } catch (e1) { /* ignore */ }
    try { rec.source.disconnect(); } catch (e2) { /* ignore */ }
    try { rec.mute.disconnect(); } catch (e3) { /* ignore */ }
    try { rec.ctx.close(); } catch (e5) { /* ignore */ }
    clearInterval(rec.timer);
    $("cahier-mic").classList.remove("is-rec");
    $("cahier-mic-label").textContent = "Note orale";
    showLive("");
    if (speechState && speechState.log) rec.said = speechState.log;
    if (speechMode === "note") stopSpeech();
    else closeMic();
    var raw = concatFloats(rec.chunks);
    var prepared = FMT.prepareVoice(raw);
    var samples = FMT.resampleLinear(prepared, rate, VOICE_RATE);
    if (samples.length < VOICE_RATE / 5) {
      toast("Note trop courte.");
      syncSpeech();
      return;
    }
    var wav = FMT.encodeWav(samples, VOICE_RATE);
    if (wav.length > MAX_AUDIO) {
      toast("Note trop longue pour le cahier.");
      syncSpeech();
      return;
    }
    var said = (rec.said || "").trim();
    var id = insertVoiceNote({
      mime: "audio/wav",
      b64: bytesToB64(wav),
      duration: samples.length / VOICE_RATE,
      transcript: said
    });
    saveClip(id, audios[id]).then(function () { persistLocal(); });
    syncSpeech();
  }

  function startRecording() {
    if (reelBlocks()) return;
    if (recording) { stopRecording(); return; }
    if (noteHold) { noteHold = false; stopSpeech(); return; }
    rememberRange();
    var Ctx = window.AudioContext || window.webkitAudioContext;
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !Ctx) {
      toast("Ce navigateur ne peut pas enregistrer le micro.");
      return;
    }
    noteHold = true;
    startSpeech("note");
    openMic().then(function (stream) {
      var ctx = new Ctx();
      var ready = ctx.resume ? ctx.resume() : Promise.resolve();
      return ready.then(function () {
        var source = ctx.createMediaStreamSource(stream);
        var processor = ctx.createScriptProcessor(4096, 1, 1);
        var mute = ctx.createGain();
        mute.gain.value = 0;
        var chunks = [];
        var started = Date.now();
        processor.onaudioprocess = function (ev) {
          if (!recording) return;
          var buf = ev.inputBuffer;
          var frames = buf.length;
          var mixed = new Float32Array(frames);
          var channels = buf.numberOfChannels || 1;
          var ch, i;
          for (ch = 0; ch < channels; ch++) {
            var data = buf.getChannelData(ch);
            for (i = 0; i < frames; i++) mixed[i] += data[i];
          }
          if (channels > 1) {
            for (i = 0; i < frames; i++) mixed[i] /= channels;
          }
          chunks.push(mixed);
        };
        source.connect(processor);
        processor.connect(mute);
        mute.connect(ctx.destination);
        recording = {
          ctx: ctx,
          source: source,
          processor: processor,
          mute: mute,
          stream: stream,
          chunks: chunks,
          sampleRate: ctx.sampleRate || 48000,
          said: (speechState && speechState.log) || "",
          timer: setInterval(function () {
            var sec = Math.round((Date.now() - started) / 1000);
            $("cahier-mic-label").textContent = FMT.formatSec(sec);
            if (sec >= MAX_SEC) stopRecording();
          }, 250)
        };
        $("cahier-mic").classList.add("is-rec");
        placeMic();
        if (speechMode !== "note") startSpeech("note");
      });
    }).catch(function () {
      noteHold = false;
      stopSpeech();
      toast("Micro refusé. Autorise-le pour poser une note orale.");
      syncSpeech();
    });
  }

  function closePop() {
    var pop = $("cahier-pop");
    pop.hidden = true;
    pop.textContent = "";
  }

  function openFloat(id, title, node, opts) {
    var win = document.getElementById(id);
    if (!win) {
      win = document.createElement("section");
      win.id = id;
      win.className = "float-win";
      win.innerHTML = '<button type="button" class="float-grab" data-act="grab" aria-label="Déplacer"></button>'
        + '<div class="float-head"><strong></strong>'
        + '<button type="button" data-act="pin">Pin</button>'
        + '<button type="button" data-act="size">Réduire</button>'
        + '<button type="button" data-act="close">Fermer</button></div>'
        + '<div class="float-body"></div>';
      document.body.appendChild(win);
      var head = win.querySelector(".float-head");
      var grab = win.querySelector(".float-grab");
      var drag = null;
      function beginDrag(e) {
        if (win.classList.contains("is-pin") || (e.target.closest && e.target.closest("button:not(.float-grab)"))) return;
        var coarse = window.matchMedia && window.matchMedia("(pointer: coarse)").matches;
        if (coarse && e.currentTarget !== grab) return;
        var box = win.getBoundingClientRect();
        win.style.left = box.left + "px";
        win.style.top = box.top + "px";
        win.style.right = "auto";
        win.style.width = box.width + "px";
        drag = { x: e.clientX, y: e.clientY, l: box.left, t: box.top };
        if (e.currentTarget.setPointerCapture) e.currentTarget.setPointerCapture(e.pointerId);
      }
      head.addEventListener("pointerdown", beginDrag);
      grab.addEventListener("pointerdown", beginDrag);
      function moveDrag(e) {
        if (!drag || win.classList.contains("is-pin")) return;
        var maxL = Math.max(8, window.innerWidth - win.offsetWidth - 8);
        var maxT = Math.max(8, window.innerHeight - 48);
        win.style.left = Math.min(maxL, Math.max(8, drag.l + e.clientX - drag.x)) + "px";
        win.style.top = Math.min(maxT, Math.max(8, drag.t + e.clientY - drag.y)) + "px";
      }
      head.addEventListener("pointermove", moveDrag);
      grab.addEventListener("pointermove", moveDrag);
      head.addEventListener("pointerup", function () { drag = null; });
      grab.addEventListener("pointerup", function () { drag = null; });
      win.addEventListener("click", function (e) {
        var btn = e.target.closest && e.target.closest("[data-act]");
        if (!btn || !win.contains(btn)) return;
        var act = btn.getAttribute("data-act");
        if (act === "close") {
          if (win.classList.contains("is-pin")) {
            toast("Dépingle la fenêtre pour la fermer.");
            return;
          }
          win.hidden = true;
        }
        if (act === "pin") {
          var pinned = win.classList.toggle("is-pin");
          btn.textContent = pinned ? "Épinglé" : "Pin";
        }
        if (act === "size") win.classList.toggle("is-small");
      });
    }
    win.querySelector(".float-head strong").textContent = title;
    var body = win.querySelector(".float-body");
    if (node && node.parentNode !== body) {
      if (id !== "float-rec") body.textContent = "";
      body.appendChild(node);
    }
    win.hidden = false;
    win.classList.toggle("is-bare", !!(opts && opts.bare));
    win.style.zIndex = "360";
    return win;
  }

  function openFiche(title, desc, url) {
    var panel = document.createElement("article");
    panel.className = "fiche-card";
    var kicker = document.createElement("p");
    kicker.className = "fiche-kicker";
    kicker.textContent = "Psychopédia";
    var heading = document.createElement("h3");
    heading.textContent = title || "Fiche";
    var lead = document.createElement("p");
    lead.className = "fiche-desc";
    lead.textContent = desc || "";
    var more = document.createElement("div");
    more.className = "fiche-excerpt";
    more.textContent = "Chargement de la page…";
    panel.appendChild(kicker);
    panel.appendChild(heading);
    if (desc) panel.appendChild(lead);
    panel.appendChild(more);
    if (url) {
      var open = document.createElement("a");
      open.className = "fiche-open";
      open.href = rootPrefix() + url;
      open.target = "_blank";
      open.rel = "noopener";
      open.textContent = "Ouvrir la page";
      panel.appendChild(open);
    }
    var pop = document.getElementById("psy-pop");
    if (pop) pop.hidden = true;
    openFloat("float-fiche", title || "Fiche", panel, { bare: true });
    if (!url) { more.textContent = desc || ""; return; }
    fetch(rootPrefix() + url).then(function (res) { return res.text(); }).then(function (html) {
      var doc = new DOMParser().parseFromString(html, "text/html");
      var main = doc.querySelector(".content") || doc.querySelector("main") || doc.body;
      var bits = main.querySelectorAll("h2, h3, p, li");
      more.textContent = "";
      var count = 0;
      var i;
      for (i = 0; i < bits.length && count < 4; i++) {
        var line = (bits[i].innerText || "").replace(/\s+/g, " ").trim();
        if (line.length < 48) continue;
        var p = document.createElement("p");
        p.textContent = line.slice(0, 340);
        more.appendChild(p);
        count += 1;
      }
      if (!count) more.textContent = (main.innerText || "").replace(/\s+/g, " ").trim().slice(0, 700);
    }).catch(function () { more.textContent = "La page ne s'ouvre pas ici."; });
  }

  function openLinkPop(link) {
    var url = link.getAttribute("data-url") || "";
    var title = link.getAttribute("data-title") || "Fiche";
    var desc = link.getAttribute("data-desc") || "";
    var pop = document.getElementById("psy-pop");
    if (!pop) {
      pop = document.createElement("div");
      pop.id = "psy-pop";
      pop.className = "psy-pop";
      document.body.appendChild(pop);
    }
    pop.textContent = "";
    var label = document.createElement("p");
    label.className = "psy-pop-title";
    label.textContent = title;
    var row = document.createElement("div");
    row.className = "psy-pop-actions";
    var page = document.createElement("button");
    page.type = "button";
    page.className = "psy-act";
    page.textContent = "Ouvrir la page";
    page.addEventListener("click", function () {
      if (url) window.open(rootPrefix() + url, "_blank", "noopener");
      pop.hidden = true;
    });
    var here = document.createElement("button");
    here.type = "button";
    here.className = "psy-act psy-act-here";
    here.textContent = "Voir ici";
    here.addEventListener("click", function () { openFiche(title, desc, url); });
    row.appendChild(page);
    row.appendChild(here);
    pop.appendChild(label);
    pop.appendChild(row);
    pop.hidden = false;
    var rect = link.getBoundingClientRect();
    var width = Math.min(240, window.innerWidth - 16);
    var left = Math.max(8, Math.min(rect.left, window.innerWidth - width - 8));
    pop.style.width = width + "px";
    pop.style.left = left + "px";
    pop.style.top = (rect.bottom + 8) + "px";
    var height = pop.offsetHeight;
    if (rect.bottom + 8 + height > window.innerHeight - 8) {
      pop.style.top = Math.max(8, rect.top - height - 8) + "px";
    }
  }

  function textPos(root, node, offset) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    var count = 0;
    var current;
    while ((current = walker.nextNode())) {
      if (current.parentElement && current.parentElement.closest(".psy-star")) continue;
      if (current === node) return count + offset;
      count += current.nodeValue.length;
    }
    return count;
  }

  function placePos(root, pos) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    var current;
    var left = pos;
    while ((current = walker.nextNode())) {
      if (current.parentElement && current.parentElement.closest(".psy-star")) continue;
      if (left <= current.nodeValue.length) {
        var range = document.createRange();
        var sel = window.getSelection();
        range.setStart(current, Math.max(0, left));
        range.collapse(true);
        sel.removeAllRanges();
        sel.addRange(range);
        return;
      }
      left -= current.nodeValue.length;
    }
  }

  function foldSpan(raw) {
    var folded = "";
    var map = [];
    var i;
    var pendingSpace = false;
    for (i = 0; i < raw.length; i++) {
      var piece = FMT.fold(raw.charAt(i)).replace(/[^a-z0-9]+/g, "");
      if (!piece) { pendingSpace = folded.length > 0; continue; }
      if (pendingSpace) { folded += " "; map.push(i); pendingSpace = false; }
      var k;
      for (k = 0; k < piece.length; k++) { folded += piece.charAt(k); map.push(i); }
    }
    return { text: folded, map: map };
  }

  function unwrapMarks(root) {
    root.querySelectorAll(".psy-star").forEach(function (star) { star.remove(); });
    root.querySelectorAll(".psy-link").forEach(function (span) {
      span.replaceWith(document.createTextNode(span.textContent || ""));
    });
    root.normalize();
  }

  function decorateLinks(root) {
    if (!lexicon || !root || speechMode) return;
    var sel = window.getSelection();
    var mark = null;
    if (sel && sel.rangeCount && root.contains(sel.anchorNode)) {
      mark = textPos(root, sel.anchorNode, sel.anchorOffset);
    }
    unwrapMarks(root);
    var rows = lexicon.phrases || [];
    var words = lexicon.words || {};
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    var nodes = [];
    var guard = 0;
    while (walker.nextNode() && guard++ < 800) nodes.push(walker.currentNode);
    nodes.forEach(function (startNode) {
      var node = startNode;
      var spins = 0;
      while (node && node.nodeValue && spins++ < 24) {
        var parent = node.parentElement;
        if (!parent || parent.closest(".psy-link, .voix-bulle, .float-head, button")) break;
        var shaped = foldSpan(node.nodeValue);
        var found = null;
        var from = -1;
        var to = -1;
        var bestAt = 1e9;
        var i;
        for (i = 0; i < rows.length; i++) {
          var phrase = rows[i].phrase;
          if (!phrase || phrase.length < 4) continue;
          var at = (" " + shaped.text + " ").indexOf(" " + phrase + " ");
          if (at < 0 || at > bestAt) continue;
          if (at === bestAt && found && phrase.length <= found.phrase.length) continue;
          var start = shaped.map[at];
          var end = shaped.map[at + phrase.length - 1];
          if (start == null || end == null) continue;
          found = rows[i];
          from = start;
          to = end + 1;
          bestAt = at;
        }
        var parts = shaped.text.split(" ");
        var cursor = 0;
        for (i = 0; i < parts.length; i++) {
          var word = parts[i];
          var entry = word.length >= 5 ? words[word] : null;
          var wAt = entry ? shaped.text.indexOf(word, cursor) : -1;
          if (entry && wAt >= 0 && wAt < bestAt) {
            found = { phrase: word, entry: entry };
            from = shaped.map[wAt];
            to = shaped.map[wAt + word.length - 1] + 1;
            bestAt = wAt;
          }
          cursor += word.length + 1;
        }
        if (!found || from < 0) break;
        var span = document.createElement("span");
        span.className = "psy-link";
        span.contentEditable = "false";
        span.textContent = node.nodeValue.slice(from, to);
        span.setAttribute("data-url", found.entry.u || "");
        span.setAttribute("data-title", found.entry.t || "");
        span.setAttribute("data-desc", found.entry.d || "");
        var after = document.createTextNode(node.nodeValue.slice(to));
        node.nodeValue = node.nodeValue.slice(0, from);
        parent.insertBefore(span, node.nextSibling);
        parent.insertBefore(after, span.nextSibling);
        node = after;
      }
    });
    if (mark != null) placePos(root, mark);
  }

  function showNoteText(id, meta) {
    var panel = document.createElement("div");
    panel.className = "voix-transcript";
    var area = document.createElement("div");
    area.className = "note-read";
    area.textContent = "Transcription…";
    panel.appendChild(area);
    openFloat("float-note", "Note orale", panel, { bare: true });
    var publish = function (text, failed) {
      var clean = (text || "").trim();
      if (!clean) {
        area.textContent = failed
          ? "Incompréhensible : aucun mot n'a été reconnu."
          : "Aucun mot reconnu pendant l'enregistrement.";
        return;
      }
      area.textContent = clean;
      if (audios[id]) audios[id].transcript = clean;
      if (meta) meta.transcript = clean;
      decorateLinks(panel);
    };
    var known = ((audios[id] && audios[id].transcript) || (meta && meta.transcript) || "").trim();
    if (known) { publish(known, false); return; }
    var Ctor = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!Ctor || !meta || !meta.b64) { publish("", true); return; }
    ensureClip(id).then(function (full) {
      var source = full && full.b64 ? full : meta;
      if (!source || !source.b64) { publish("", true); return; }
      var mime = String(source.mime || "audio/wav").split(";")[0] || "audio/wav";
      var url = URL.createObjectURL(new Blob([bytesFromB64(source.b64)], { type: mime }));
      var audio = new Audio(url);
      var rec = new Ctor();
      rec.lang = "fr-FR";
      rec.continuous = true;
      rec.interimResults = true;
      var state = FMT.speechState();
      var heard = "";
      rec.onresult = function (ev) {
        var step = FMT.applySpeechEvent(state, ev, Date.now());
        heard = state.log || "";
        if (step.live) heard = (heard + " " + step.live).trim();
        if (heard) area.textContent = heard;
      };
      var done = false;
      var finish = function () {
        if (done) return;
        done = true;
        try { rec.stop(); } catch (e) { /* ignore */ }
        try { audio.pause(); } catch (e2) { /* ignore */ }
        URL.revokeObjectURL(url);
        publish(heard, !String(heard || "").trim());
      };
      rec.onerror = function () { finish(); };
      audio.onended = function () { setTimeout(finish, 600); };
      setTimeout(finish, Math.min(70000, ((source.duration || 10) + 3) * 1000));
      try { rec.start(); } catch (e3) { publish("", true); return; }
      audio.play().catch(function () { finish(); });
    });
  }

  function openPop(capsule) {
    var pop = $("cahier-pop");
    var id = capsule.getAttribute("data-voix");
    var meta = audios[id] || {};
    pop.textContent = "";
    var play = document.createElement("button");
    play.type = "button";
    play.textContent = playingId === id ? "Pause" : "Lire";
    var stt = document.createElement("button");
    stt.type = "button";
    stt.textContent = "Mettre en texte";
    play.addEventListener("click", function () { togglePlay(capsule, play); });
    stt.addEventListener("click", function () {
      ensureClip(id).then(function (full) { showNoteText(id, full || meta); });
    });
    pop.appendChild(play);
    pop.appendChild(stt);
    var rect = capsule.getBoundingClientRect();
    var top = rect.bottom + 8;
    if (top > window.innerHeight - 64) top = Math.max(8, rect.top - 56);
    pop.style.top = top + "px";
    pop.style.left = Math.min(Math.max(8, rect.left), window.innerWidth - 220) + "px";
    pop.hidden = false;
  }

  function bytesFromB64(b64) {
    var bin = atob(b64);
    var bytes = new Uint8Array(bin.length);
    var i;
    for (i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    return bytes;
  }

  function ensureClip(id) {
    var meta = audios[id] || {};
    if (meta.b64) return Promise.resolve(meta);
    return loadClip(id).then(function (saved) {
      if (!saved || !saved.b64) return meta;
      audios[id] = {
        mime: saved.mime || meta.mime || "audio/wav",
        b64: saved.b64,
        duration: saved.duration || meta.duration || 0,
        transcript: saved.transcript || meta.transcript || "",
        idb: 1
      };
      if (active && active.audios) active.audios[id] = audios[id];
      return audios[id];
    });
  }

  function togglePlay(capsule, button) {
    var id = capsule.getAttribute("data-voix");
    if (player && playingId === id) {
      player.pause();
      if (player._psyUrl) URL.revokeObjectURL(player._psyUrl);
      player = null;
      playingId = "";
      capsule.classList.remove("is-playing");
      button.textContent = "Lire";
      return;
    }
    ensureClip(id).then(function (meta) {
      if (!meta || !meta.b64) {
        toast("Le son de cette note n'est pas dans le cahier.");
        return;
      }
      if (player) {
        player.pause();
        if (player._psyUrl) URL.revokeObjectURL(player._psyUrl);
      }
      document.querySelectorAll(".voix-bulle.is-playing").forEach(function (n) { n.classList.remove("is-playing"); });
      var mime = String(meta.mime || "audio/wav").split(";")[0] || "audio/wav";
      var url = URL.createObjectURL(new Blob([bytesFromB64(meta.b64)], { type: mime }));
      player = new Audio(url);
      player._psyUrl = url;
      player.playbackRate = 1;
      playingId = id;
      capsule.classList.add("is-playing");
      button.textContent = "Pause";
      player.onended = function () {
        if (player && player._psyUrl) URL.revokeObjectURL(player._psyUrl);
        playingId = "";
        player = null;
        capsule.classList.remove("is-playing");
        button.textContent = "Lire";
      };
      player.play().catch(function () { toast("Lecture impossible."); });
    });
  }

  function kindLabel(kind) {
    var map = {
      categorie: "Catégorie", section: "Section", notion: "Notion", experience: "Expérience",
      auteur: "Auteur", theorie: "Théorie", courant: "Courant", mythe: "Idée reçue",
      trouble: "Trouble", biais: "Biais", test: "Test", metier: "Métier", livre: "Livre"
    };
    return map[kind] || "Fiche";
  }

  function showSuggest(entry) {
    var box = $("cahier-suggest");
    var key = entry.u || entry.t;
    var now = Date.now();
    if (shownAt[key] && now - shownAt[key] < 90000) return;
    shownAt[key] = now;
    box.textContent = "";
    var k = document.createElement("p");
    k.className = "k";
    k.textContent = "Dans Psyclopédia";
    var title = document.createElement("strong");
    title.textContent = entry.t || "Fiche";
    var desc = document.createElement("p");
    desc.textContent = kindLabel(entry.k) + (entry.d ? " — " + String(entry.d).slice(0, 110) : "");
    var row = document.createElement("div");
    row.className = "row";
    var link = document.createElement("a");
    link.href = rootPrefix() + entry.u;
    link.target = "_blank";
    link.rel = "noopener";
    link.textContent = "Lire";
    var later = document.createElement("button");
    later.type = "button";
    later.textContent = "Plus tard";
    later.addEventListener("click", function () { box.hidden = true; });
    row.appendChild(link);
    row.appendChild(later);
    box.appendChild(k);
    box.appendChild(title);
    box.appendChild(desc);
    box.appendChild(row);
    box.hidden = false;
  }

  function considerUtterance(text) {
    if (!lexicon || !text) return null;
    var hit = FMT.matchUtterance(lexicon, text);
    if (hit) showSuggest(hit);
    return hit;
  }

  function loadLexicon() {
    return fetch(rootPrefix() + "livres-psychologie/07-ebook-final/search-index.json")
      .then(function (res) { return res.json(); })
      .then(function (entries) { lexicon = FMT.buildLexicon(entries); })
      .catch(function () { lexicon = FMT.buildLexicon([]); })
      .then(function () { decorateLinks($("cahier-body")); });
  }

  function reelBlocks() {
    if (reelPhase !== "run" && reelPhase !== "pause") return false;
    toast("Enregistrement constant en cours. Note orale, dictée et écoute sont en pause.");
    return true;
  }

  function toggleListen() {
    if (reelBlocks()) return;
    listenOn = !listenOn;
    $("cahier-listen").setAttribute("aria-pressed", listenOn ? "true" : "false");
    if (!listenOn && speechMode === "listen") stopSpeech();
    syncSpeech();
  }

  function toggleDictate() {
    if (reelBlocks()) return;
    dictateOn = !dictateOn;
    var btn = $("cahier-dictate");
    if (btn) btn.setAttribute("aria-pressed", dictateOn ? "true" : "false");
    if (!dictateOn && speechMode === "dictate") {
      stopSpeech();
      showLive("");
    }
    if (dictateOn) rememberRange();
    syncSpeech();
  }

  function command(cmd) {
    $("cahier-body").focus();
    document.execCommand("styleWithCSS", false, false);
    if (cmd === "hiliteColor") document.execCommand("hiliteColor", false, "#fff3bf");
    else document.execCommand(cmd, false, null);
    scheduleSave();
  }

  function applySize(value) {
    $("cahier-body").focus();
    document.execCommand("styleWithCSS", false, false);
    document.execCommand("fontSize", false, value);
    scheduleSave();
  }

  function applyBlock(tag) {
    $("cahier-body").focus();
    document.execCommand("formatBlock", false, tag);
    scheduleSave();
  }

  function downloadDocx() {
    snapshot();
    var parts = FMT.docxParts(active.title, active.html, active.audios);
    function finish(bytes) {
      var blob = new Blob([bytes], { type: "application/vnd.openxmlformats-officedocument.wordprocessingml.document" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = fileName(active).replace(/\.psy\.json$/, "") + ".docx";
      a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 1500);
    }
    if (typeof CompressionStream === "undefined") {
      finish(FMT.zipStore(parts));
      return;
    }
    var chain = Promise.resolve();
    parts.forEach(function (part) {
      chain = chain.then(function () {
        var stream = new Blob([part.data]).stream().pipeThrough(new CompressionStream("deflate-raw"));
        return new Response(stream).arrayBuffer().then(function (buf) {
          part.stored = new Uint8Array(buf);
          part.method = 8;
        });
      });
    });
    chain.then(function () { finish(FMT.zipStore(parts)); });
  }

  function importDocx(file) {
    file.arrayBuffer().then(function (buf) {
      var bytes = new Uint8Array(buf);
      var inflate = function (slice) {
        if (typeof DecompressionStream === "undefined") return Promise.reject(new Error("inflate"));
        var stream = new Blob([slice]).stream().pipeThrough(new DecompressionStream("deflate-raw"));
        return new Response(stream).arrayBuffer().then(function (out) { return new Uint8Array(out); });
      };
      return FMT.docxToHtml(bytes, inflate);
    }).then(function (html) {
      var doc = {
        id: hex(8),
        title: file.name.replace(/\.docx$/i, ""),
        html: html || "<p><br></p>",
        audios: {},
        updatedAt: new Date().toISOString(),
        driveId: ""
      };
      docs.unshift(doc);
      fillEditor(doc);
      persistLocal();
      scheduleSave();
      toast("Document importé");
    }).catch(function () {
      toast("Ce .docx n'a pas pu être lu.");
    });
  }

  function removeDoc() {
    if (!active) return;
    if (!window.confirm("Supprimer ce cahier ?")) return;
    var gone = active;
    docs = docs.filter(function (doc) { return doc.id !== gone.id; });
    if (gone.driveId && token) {
      driveFetch(DRIVE + "/files/" + encodeURIComponent(gone.driveId), {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ trashed: true })
      }).catch(function () {});
    }
    persistLocal();
    if (!docs.length) newDoc();
    else fillEditor(docs[0]);
  }

  var REEL_AUDIO = {
    vocal: { echoCancellation: true, noiseSuppression: false, autoGainControl: true },
    normal: { echoCancellation: true, noiseSuppression: false, autoGainControl: true },
    room: { echoCancellation: false, noiseSuppression: false, autoGainControl: false }
  };
  var REEL_MAX = 7200;

  function reelClock() {
    if (!reel) return 0;
    var extra = reelPhase === "run" ? Date.now() - reel.tick : 0;
    return (reel.elapsed + extra) / 1000;
  }

  function paintReelTime() {
    var el = $("rec-time");
    if (!el) return;
    var total = Math.floor(reelClock());
    var h = String(Math.floor(total / 3600)).padStart(2, "0");
    var m = String(Math.floor(total / 60) % 60).padStart(2, "0");
    var s = String(total % 60).padStart(2, "0");
    el.textContent = h + ":" + m + ":" + s;
  }

  function paintReelLive() {
    var el = $("rec-live");
    if (!el) return;
    var text = (reelTranscript || "").trim();
    el.hidden = false;
    el.textContent = text ? text.slice(-320) : "La transcription s'écrit ici pendant la séance.";
  }

  function paintReelLock() {
    var on = reelPhase === "run" || reelPhase === "pause" || reelPhase === "arm";
    var app = $("cahier-app");
    if (app) app.classList.toggle("is-reel", on);
    ["cahier-dictate", "cahier-listen"].forEach(function (id) {
      var btn = $(id);
      if (btn) btn.disabled = on;
    });
    var opener = $("rec-open");
    if (opener) {
      opener.textContent = on ? "Enregistrement…" : "Enregistrer";
      opener.classList.toggle("is-on", on);
    }
    var go = $("rec-go");
    var pause = $("rec-pause");
    var stop = $("rec-stop");
    if (go) {
      go.setAttribute("aria-pressed", reelPhase === "run" ? "true" : "false");
      go.textContent = reelPhase === "pause" ? "Reprendre" : (reelPhase === "run" ? "En cours" : "Lancer");
    }
    if (pause) pause.disabled = reelPhase !== "run";
    if (stop) stop.disabled = reelPhase === "idle";
    document.querySelectorAll(".rec-modes button").forEach(function (btn) {
      btn.disabled = on;
      btn.setAttribute("aria-pressed", btn.getAttribute("data-reel") === reelMode ? "true" : "false");
    });
    var warn = $("rec-warn");
    if (warn) {
      warn.textContent = on
        ? "Séance en cours. La note orale, la dictée et l'écoute sont grisées jusqu'à l'arrêt."
        : "Pendant la séance, la note orale, la dictée et l'écoute sont indisponibles.";
    }
  }

  function seanceStore(mode) {
    return audioDb().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("seances", mode);
        var store = tx.objectStore("seances");
        resolve({ store: store, tx: tx });
      });
    });
  }

  function listSeances() {
    var box = $("rec-cache");
    if (!box) return;
    audioDb().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("seances", "readonly");
        var req = tx.objectStore("seances").getAll();
        req.onsuccess = function () { resolve(req.result || []); };
        req.onerror = function () { reject(req.error); };
      });
    }).then(function (rows) {
      rows.sort(function (a, b) { return (b.created || 0) - (a.created || 0); });
      box.textContent = "";
      if (!rows.length) {
        var empty = document.createElement("li");
        empty.className = "rec-empty";
        empty.textContent = "Aucune séance en cache.";
        box.appendChild(empty);
        return;
      }
      rows.forEach(function (row) {
        var li = document.createElement("li");
        var label = document.createElement("strong");
        var when = new Date(row.created || Date.now());
        label.textContent = when.toLocaleString("fr-FR", { day: "2-digit", month: "short", hour: "2-digit", minute: "2-digit" })
          + " · " + FMT.formatSec(row.duration || 0);
        li.appendChild(label);
        ["Écouter", "Transcription", "TXT", "MP3", "Supprimer"].forEach(function (name) {
          var btn = document.createElement("button");
          btn.type = "button";
          btn.textContent = name;
          btn.addEventListener("click", function () { onSeance(name, row.id); });
          li.appendChild(btn);
        });
        box.appendChild(li);
      });
    }).catch(function () {
      box.textContent = "";
    });
  }

  function loadSeance(id) {
    return audioDb().then(function (db) {
      return new Promise(function (resolve, reject) {
        var req = db.transaction("seances", "readonly").objectStore("seances").get(id);
        req.onsuccess = function () { resolve(req.result || null); };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function saveSeance(row) {
    return audioDb().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("seances", "readwrite");
        tx.objectStore("seances").put(row, row.id);
        tx.oncomplete = function () { resolve(row); };
        tx.onerror = function () { reject(tx.error); };
      });
    });
  }

  function downloadBytes(bytes, name, type) {
    var blob = new Blob([bytes], { type: type });
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = name;
    link.click();
    setTimeout(function () { URL.revokeObjectURL(link.href); }, 4000);
  }

  function samplesToMp3(samples, rate) {
    if (!window.lamejs || !lamejs.Mp3Encoder) throw new Error("mp3");
    var enc = new lamejs.Mp3Encoder(1, rate, 96);
    var pcm = new Int16Array(samples.length);
    var i;
    for (i = 0; i < samples.length; i++) {
      var s = samples[i];
      if (s > 1) s = 1;
      if (s < -1) s = -1;
      pcm[i] = s < 0 ? Math.round(s * 32768) : Math.round(s * 32767);
    }
    var parts = [];
    var block = 1152;
    for (i = 0; i < pcm.length; i += block) {
      var buf = enc.encodeBuffer(pcm.subarray(i, Math.min(i + block, pcm.length)));
      if (buf && buf.length) parts.push(buf);
    }
    var end = enc.flush();
    if (end && end.length) parts.push(end);
    return new Blob(parts, { type: "audio/mpeg" });
  }

  function openSeanceView(row) {
    reelViewId = row.id;
    var view = $("rec-view");
    $("rec-view-title").textContent = "Séance du " + new Date(row.created).toLocaleString("fr-FR");
    $("rec-script").textContent = (row.transcript || "").trim() || "Incompréhensible : aucun mot n'a été reconnu.";
    decorateLinks($("rec-script"));
    var view = $("rec-view");
    if (view) openFloat("float-text", "Transcription", view);
    var player = $("rec-player");
    if (player._url) URL.revokeObjectURL(player._url);
    var url = URL.createObjectURL(new Blob([row.wav], { type: "audio/wav" }));
    player._url = url;
    player.src = url;
    view.hidden = false;
  }

  function onSeance(action, id) {
    if (action === "Supprimer") {
      audioDb().then(function (db) {
        return new Promise(function (resolve) {
          var tx = db.transaction("seances", "readwrite");
          tx.objectStore("seances").delete(id);
          tx.oncomplete = function () { resolve(); };
        });
      }).then(listSeances);
      return;
    }
    loadSeance(id).then(function (row) {
      if (!row) return;
      var stamp = new Date(row.created || Date.now()).toISOString().slice(0, 16).replace(/[:T]/g, "-");
      if (action === "Écouter" || action === "Transcription") openSeanceView(row);
      if (action === "TXT") {
        downloadBytes(row.transcript || "", "psyclopedia-" + stamp + ".txt", "text/plain;charset=utf-8");
      }
      if (action === "MP3") {
        try {
          var pcm = FMT.wavPcm(row.wav);
          var blob = samplesToMp3(pcm.samples, pcm.rate || VOICE_RATE);
          var link = document.createElement("a");
          link.href = URL.createObjectURL(blob);
          link.download = "psyclopedia-" + stamp + ".mp3";
          link.click();
        } catch (e) {
          toast("MP3 indisponible, le WAV de la séance reste lisible.");
          downloadBytes(row.wav, "psyclopedia-" + stamp + ".wav", "audio/wav");
        }
      }
    });
  }

  function stopReelGraph() {
    if (!reel) return;
    try { reel.processor.onaudioprocess = null; } catch (e0) { /* ignore */ }
    try { reel.processor.disconnect(); } catch (e1) { /* ignore */ }
    try { reel.source.disconnect(); } catch (e2) { /* ignore */ }
    try { reel.mute.disconnect(); } catch (e3) { /* ignore */ }
    try { reel.stream.getTracks().forEach(function (track) { track.stop(); }); } catch (e4) { /* ignore */ }
    try { reel.ctx.close(); } catch (e5) { /* ignore */ }
    clearInterval(reel.timer);
  }

  function finishReel() {
    if (!reel) {
      reelPhase = "idle";
      stopSpeech();
      paintReelLock();
      return;
    }
    if (reelPhase === "run") reel.elapsed += Date.now() - reel.tick;
    var chunks = reel.chunks.slice();
    var said = (speechState && (speechState.log || speechState.tail)) || reelTranscript || "";
    stopReelGraph();
    reel = null;
    reelPhase = "idle";
    stopSpeech();
    paintReelLock();
    paintReelLive();
    var raw = concatFloats(chunks);
    var prepared = FMT.prepareVoice(raw);
    if (prepared.length < VOICE_RATE / 4 && !String(said || "").trim()) {
      toast("Séance trop courte pour être gardée.");
      return;
    }
    var wav = FMT.encodeWav(prepared, VOICE_RATE);
    var row = {
      id: hex(8),
      created: Date.now(),
      duration: prepared.length / VOICE_RATE,
      transcript: String(said || "").trim(),
      wav: wav
    };
    reelTranscript = "";
    paintReelLive();
    saveSeance(row).then(function () {
      toast("Séance gardée dans le cache.");
      listSeances();
      openSeanceView(row);
    }).catch(function () {
      toast("Le cache du navigateur a refusé la séance.");
    });
  }

  function pauseReel() {
    if (reelPhase !== "run" || !reel) return;
    reel.elapsed += Date.now() - reel.tick;
    reelPhase = "pause";
    if (speechState && speechState.log) reelTranscript = speechState.log;
    stopSpeech();
    paintReelLock();
    paintReelTime();
  }

  function resumeReel() {
    if (reelPhase !== "pause" || !reel) return;
    reel.tick = Date.now();
    reelPhase = "run";
    paintReelLock();
    startSpeech("reel", true);
  }

  function beginReel() {
    if (reelPhase === "pause") { resumeReel(); return; }
    if (reelPhase === "run" || reelPhase === "arm") return;
    reelTranscript = "";
    paintReelLive();
    if (recording) stopRecording();
    if (dictateOn) { dictateOn = false; var d = $("cahier-dictate"); if (d) d.setAttribute("aria-pressed", "false"); }
    if (listenOn) { listenOn = false; $("cahier-listen").setAttribute("aria-pressed", "false"); }
    reel = {
      chunks: [], elapsed: 0, tick: Date.now(), stream: null,
      timer: setInterval(function () {
        paintReelTime();
        if (reelClock() >= REEL_MAX) finishReel();
      }, 250)
    };
    reelPhase = "run";
    paintReelLock();
    startSpeech("reel");
  }

  function releaseReelMic() {
    if (!reel || !reel.stream) return;
    try { reel.processor.onaudioprocess = null; } catch (e0) { /* ignore */ }
    try { reel.processor.disconnect(); } catch (e1) { /* ignore */ }
    try { reel.source.disconnect(); } catch (e2) { /* ignore */ }
    try { reel.mute.disconnect(); } catch (e3) { /* ignore */ }
    try { reel.stream.getTracks().forEach(function (track) { track.stop(); }); } catch (e4) { /* ignore */ }
    try { if (reel.ctx) reel.ctx.close(); } catch (e5) { /* ignore */ }
    reel.stream = null;
    reel.ctx = null;
  }

  function attachReelMic() {
    if (!reel || reel.stream || (reelPhase !== "run" && reelPhase !== "arm")) return;
    if (!navigator.mediaDevices) return;
    var Ctx = window.AudioContext || window.webkitAudioContext;
    if (!Ctx) return;
    navigator.mediaDevices.getUserMedia({ audio: REEL_AUDIO[reelMode] || REEL_AUDIO.vocal }).then(function (stream) {
      if (!reel || reel.stream || (reelPhase !== "run" && reelPhase !== "arm")) {
        stream.getTracks().forEach(function (track) { track.stop(); });
        return;
      }
      var ctx = new Ctx();
      var ready = ctx.resume ? ctx.resume() : Promise.resolve();
      return ready.then(function () {
        var source = ctx.createMediaStreamSource(stream);
        var processor = ctx.createScriptProcessor(4096, 1, 1);
        var mute = ctx.createGain();
        mute.gain.value = 0;
        var chunks = reel.chunks;
        processor.onaudioprocess = function (ev) {
          if (reelPhase !== "run" || !reel) return;
          var buf = ev.inputBuffer;
          var frames = buf.length;
          var mixed = new Float32Array(frames);
          var channels = buf.numberOfChannels || 1;
          var ch, i, peak = 0;
          for (ch = 0; ch < channels; ch++) {
            var data = buf.getChannelData(ch);
            for (i = 0; i < frames; i++) mixed[i] += data[i];
          }
          if (channels > 1) {
            for (i = 0; i < frames; i++) mixed[i] /= channels;
          }
          for (i = 0; i < frames; i++) {
            var a = mixed[i] < 0 ? -mixed[i] : mixed[i];
            if (a > peak) peak = a;
          }
          var level = $("rec-level");
          if (level) level.style.height = Math.max(8, Math.min(88, Math.round(peak * 180))) + "px";
          chunks.push(FMT.resampleLinear(mixed, ctx.sampleRate || 48000, VOICE_RATE));
        };
        source.connect(processor);
        processor.connect(mute);
        mute.connect(ctx.destination);
        reel.ctx = ctx;
        reel.source = source;
        reel.processor = processor;
        reel.mute = mute;
        reel.stream = stream;
        paintReelLock();
        paintReelTime();
      });
    }).catch(function () {
      toast("Le fichier son attend : la transcription garde le micro, comme la dictée.");
    });
  }

  function bindEditor() {
    var body = $("cahier-body");
    document.execCommand("defaultParagraphSeparator", false, "p");
    $("cahier-title").addEventListener("input", scheduleSave);
    body.addEventListener("input", function () {
      scheduleSave();
      placeMic();
      clearTimeout(body._markTimer);
      body._markTimer = setTimeout(function () {
        if (!speechMode) decorateLinks(body);
      }, 400);
    });
    document.addEventListener("pointerdown", function (e) {
      var pop = document.getElementById("psy-pop");
      var inLink = e.target.closest && e.target.closest(".psy-link");
      if (pop && !pop.hidden && !pop.contains(e.target) && !inLink) pop.hidden = true;
      document.querySelectorAll(".float-win.is-bare").forEach(function (w) {
        if (w.hidden || w.contains(e.target) || inLink) return;
        if (e.target.closest && e.target.closest("#psy-pop")) return;
        w.hidden = true;
      });
    });
    document.addEventListener("click", function (e) {
      var link = e.target.closest && e.target.closest(".psy-link");
      if (!link) return;
      e.preventDefault();
      e.stopPropagation();
      openLinkPop(link);
    });
    body.addEventListener("keyup", function () { rememberRange(); placeMic(); });
    body.addEventListener("mouseup", function () { rememberRange(); placeMic(); });
    body.addEventListener("focus", placeMic);
    body.addEventListener("blur", function () {
      setTimeout(function () {
        if (!recording && document.activeElement !== $("cahier-mic")) $("cahier-mic").hidden = true;
      }, 180);
    });
    body.addEventListener("paste", function (e) {
      e.preventDefault();
      var text = (e.clipboardData || window.clipboardData).getData("text/plain");
      document.execCommand("insertText", false, text);
    });
    body.addEventListener("click", function (e) {
      var cap = e.target.closest(".voix-bulle");
      if (!cap) { closePop(); return; }
      e.preventDefault();
      openPop(cap);
    });
    document.addEventListener("selectionchange", function () {
      if (speechMode) return;
      if (document.activeElement === body || body.contains(document.activeElement)) {
        rememberRange();
        placeMic();
      }
    });
    window.addEventListener("scroll", placeMic, true);
    window.addEventListener("resize", placeMic);
    document.addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "s") {
        e.preventDefault();
        snapshot();
        pushDrive().catch(function () {});
        setSave("Enregistré");
      }
    });
    $("cahier-mic").addEventListener("mousedown", function (e) { e.preventDefault(); rememberRange(); });
    $("cahier-mic").addEventListener("click", startRecording);
    document.querySelectorAll(".cahier-toolbar [data-cmd]").forEach(function (btn) {
      btn.addEventListener("mousedown", function (e) { e.preventDefault(); });
      btn.addEventListener("click", function () { command(btn.getAttribute("data-cmd")); });
    });
    document.querySelectorAll(".cahier-toolbar [data-block]").forEach(function (btn) {
      btn.addEventListener("mousedown", function (e) { e.preventDefault(); });
      btn.addEventListener("click", function () { applyBlock(btn.getAttribute("data-block")); });
    });
    $("cahier-size").addEventListener("change", function () { applySize($("cahier-size").value); });
    $("cahier-export").addEventListener("click", downloadDocx);
    $("rec-open").addEventListener("click", function () {
      var card = document.querySelector("#rec-const .rec-card");
      if (!card) return;
      openFloat("float-rec", "Enregistreur", card);
    });
    $("rec-dismiss").addEventListener("click", function () {
      var win = document.getElementById("float-rec");
      if (win && win.classList.contains("is-pin")) {
        toast("Dépingle la fenêtre pour la fermer.");
        return;
      }
      if (win) win.hidden = true;
    });
    $("rec-go").addEventListener("click", beginReel);
    $("rec-pause").addEventListener("click", pauseReel);
    $("rec-stop").addEventListener("click", finishReel);
    $("rec-close").addEventListener("click", function () { $("rec-view").hidden = true; });
    $("rec-txt").addEventListener("click", function () { if (reelViewId) onSeance("TXT", reelViewId); });
    $("rec-mp3").addEventListener("click", function () { if (reelViewId) onSeance("MP3", reelViewId); });
    document.querySelectorAll(".rec-modes button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (reelPhase !== "idle") return;
        reelMode = btn.getAttribute("data-reel") || "vocal";
        paintReelLock();
      });
    });
    listSeances();
    $("cahier-listen").addEventListener("click", toggleListen);
    var dictateBtn = $("cahier-dictate");
    if (dictateBtn) dictateBtn.addEventListener("click", toggleDictate);
    var driveBtn = $("cahier-drive");
    if (driveBtn) driveBtn.addEventListener("click", askDrive);
    $("cahier-delete").addEventListener("click", removeDoc);
    $("cahier-new").addEventListener("click", function () { newDoc(); $("cahier-side").classList.remove("is-open"); });
    $("cahier-import").addEventListener("click", function () { $("cahier-file").click(); });
    $("cahier-file").addEventListener("change", function () {
      var file = $("cahier-file").files && $("cahier-file").files[0];
      $("cahier-file").value = "";
      if (file) importDocx(file);
    });
    $("cahier-side-open").addEventListener("click", function () { $("cahier-side").classList.add("is-open"); });
    $("cahier-side-close").addEventListener("click", function () { $("cahier-side").classList.remove("is-open"); });
    var sync = $("cahier-sync");
    sync.style.cursor = "pointer";
    sync.addEventListener("click", askDrive);
  }

  function owner() {
    var current = window.PsycCompte && PsycCompte.currentUser();
    if (current && current.id) return current;
    var id = "";
    try { id = localStorage.getItem("psyclopedia_cahier_owner") || ""; } catch (e) { id = ""; }
    if (!id) {
      id = hex(8);
      try { localStorage.setItem("psyclopedia_cahier_owner", id); } catch (e2) { /* ignore */ }
    }
    return { id: id, google: false };
  }

  function showApp(person) {
    user = person;
    var gate = $("cahier-gate");
    if (gate) gate.hidden = true;
    $("cahier-work").hidden = false;
    loadLocal();
    if (!docs.length) newDoc();
    else fillEditor(docs[0]);
    if (!rootEl.getAttribute("data-bound")) {
      rootEl.setAttribute("data-bound", "1");
      bindEditor();
    }
    setSync("Enregistré sur cet appareil. Google Drive est facultatif.");
    loadLexicon();
    hydrateClips();
    listSeances();
  }

  function boot() {
    rootEl = $("cahier-app");
    if (!rootEl || !FMT) return;
    if (isLocalTest()) {
      showApp(window.PSY_CAHIER_TEST.user);
      window.PsyCahier = {
        insertVoiceNote: insertVoiceNote,
        serialize: serializeBody,
        command: command,
        applySize: applySize,
        applyBlock: applyBlock,
        consider: considerUtterance,
        audios: function () { return audios; },
        body: function () { return $("cahier-body"); }
      };
      if (window.PSY_CAHIER_TEST.run) window.PSY_CAHIER_TEST.run();
      return;
    }
    showApp(owner());
    document.addEventListener("psyc-compte-ready", function () {
      var current = window.PsycCompte && PsycCompte.currentUser();
      if (current && current.id && user && current.id !== user.id) showApp(current);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
