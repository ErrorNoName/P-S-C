/* ==========================================================================
   PSYCLOPÉDIA — Compte étudiant (API distante : notes, scores, photo)
   ========================================================================== */

(function () {
  "use strict";

  var SESSION_KEY = "psyclopedia_session_v1";
  var ANON_KEY = "psyclopedia_anon_backup_v1";
  var PROGRESS_KEY = "psyclopedia_progress_v1";
  var COURS_KEY = "psyclopedia_cours_v1";
  var IDB_NAME = "psyclopedia-compte";
  var IDB_VER = 1;
  var PBKDF2_ITERS = 210000;

  var state = {
    mode: "local",
    apiUrl: "",
    googleClientId: "",
    user: null,
    token: "",
    ready: null,
    syncTimer: null,
  };

  function cfg() {
    return window.PSYCLOPEDIA_COMPTE || {};
  }

  function toast(msg) {
    if (typeof window.toast === "function") window.toast(msg);
  }

  function loadSession() {
    try {
      return JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
    } catch (e) {
      return null;
    }
  }

  function saveSession() {
    if (!state.user || !state.token) {
      localStorage.removeItem(SESSION_KEY);
      return;
    }
    localStorage.setItem(SESSION_KEY, JSON.stringify({
      token: state.token,
      user: state.user,
      mode: state.mode,
    }));
  }

  function emptyProgress() {
    return { visited: {}, quizBest: {} };
  }

  function emptyCours() {
    return { watched: {}, attendance: {}, quizzes: {}, notes: {} };
  }

  function readProgress() {
    try {
      return JSON.parse(localStorage.getItem(PROGRESS_KEY) || "null") || emptyProgress();
    } catch (e) {
      return emptyProgress();
    }
  }

  function readCours() {
    try {
      var data = JSON.parse(localStorage.getItem(COURS_KEY) || "null") || emptyCours();
      data.watched = data.watched || {};
      data.attendance = data.attendance || {};
      data.quizzes = data.quizzes || {};
      data.notes = data.notes || {};
      return data;
    } catch (e) {
      return emptyCours();
    }
  }

  function writeLocal(progress, cours) {
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress || emptyProgress()));
    localStorage.setItem(COURS_KEY, JSON.stringify(cours || emptyCours()));
  }

  function mergeProgress(a, b) {
    a = a || emptyProgress();
    b = b || emptyProgress();
    var visited = Object.assign({}, a.visited || {}, b.visited || {});
    var quizBest = Object.assign({}, a.quizBest || {});
    Object.keys(b.quizBest || {}).forEach(function (k) {
      var cur = quizBest[k];
      var inc = b.quizBest[k];
      if (!cur || (inc && (inc.pct || 0) > (cur.pct || 0))) quizBest[k] = inc;
    });
    return { visited: visited, quizBest: quizBest };
  }

  function mergeMaps(a, b, pick) {
    var out = Object.assign({}, a || {});
    Object.keys(b || {}).forEach(function (k) {
      out[k] = out[k] ? pick(out[k], b[k]) : b[k];
    });
    return out;
  }

  function mergeCours(a, b) {
    a = a || emptyCours();
    b = b || emptyCours();
    return {
      watched: mergeMaps(a.watched, b.watched, function (x, y) {
        return {
          seconds: Math.max(x.seconds || 0, y.seconds || 0),
          completed: !!(x.completed || y.completed),
          at: (y.at || x.at || ""),
        };
      }),
      attendance: Object.assign({}, a.attendance || {}, b.attendance || {}),
      quizzes: mergeMaps(a.quizzes, b.quizzes, function (x, y) {
        return (y.score || 0) >= (x.score || 0) ? y : x;
      }),
      notes: mergeMaps(a.notes, b.notes, function (x, y) {
        var xs = typeof x === "string" ? x : "";
        var ys = typeof y === "string" ? y : "";
        return ys.length >= xs.length ? ys : xs;
      }),
    };
  }

  /* ------------------------------ IndexedDB ------------------------------ */

  function idbOpen() {
    return new Promise(function (resolve, reject) {
      if (!window.indexedDB) {
        reject(new Error("IndexedDB indisponible"));
        return;
      }
      var req = indexedDB.open(IDB_NAME, IDB_VER);
      req.onupgradeneeded = function () {
        var db = req.result;
        if (!db.objectStoreNames.contains("users")) {
          var users = db.createObjectStore("users", { keyPath: "id" });
          users.createIndex("email", "email", { unique: true });
          users.createIndex("googleSub", "googleSub", { unique: false });
        }
        if (!db.objectStoreNames.contains("sessions")) {
          db.createObjectStore("sessions", { keyPath: "token" });
        }
        if (!db.objectStoreNames.contains("notes")) {
          var notes = db.createObjectStore("notes", { keyPath: "id" });
          notes.createIndex("userId", "userId", { unique: false });
        }
        if (!db.objectStoreNames.contains("grades")) {
          var grades = db.createObjectStore("grades", { keyPath: "id" });
          grades.createIndex("userId", "userId", { unique: false });
        }
        if (!db.objectStoreNames.contains("snapshots")) {
          db.createObjectStore("snapshots", { keyPath: "userId" });
        }
      };
      req.onsuccess = function () { resolve(req.result); };
      req.onerror = function () { reject(req.error); };
    });
  }

  function idbOp(store, mode, fn) {
    return idbOpen().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction(store, mode);
        var os = tx.objectStore(store);
        var result;
        try {
          result = fn(os);
        } catch (e) {
          reject(e);
          return;
        }
        tx.oncomplete = function () { resolve(result); };
        tx.onerror = function () { reject(tx.error); };
        if (result && typeof result.onsuccess !== "undefined") {
          result.onsuccess = function () { result = result.result; };
          result.onerror = function () { reject(result.error); };
        }
      });
    });
  }

  function bufToHex(buf) {
    return Array.from(new Uint8Array(buf)).map(function (b) {
      return b.toString(16).padStart(2, "0");
    }).join("");
  }

  function hexToBuf(hex) {
    var arr = new Uint8Array(hex.length / 2);
    for (var i = 0; i < arr.length; i++) arr[i] = parseInt(hex.substr(i * 2, 2), 16);
    return arr;
  }

  function randomHex(n) {
    var arr = new Uint8Array(n);
    crypto.getRandomValues(arr);
    return bufToHex(arr);
  }

  function hashPassword(password, saltHex) {
    var enc = new TextEncoder();
    var salt = saltHex ? hexToBuf(saltHex) : crypto.getRandomValues(new Uint8Array(16));
    return crypto.subtle.importKey("raw", enc.encode(password), "PBKDF2", false, ["deriveBits"])
      .then(function (key) {
        return crypto.subtle.deriveBits(
          { name: "PBKDF2", salt: salt, iterations: PBKDF2_ITERS, hash: "SHA-256" },
          key,
          256
        );
      })
      .then(function (bits) {
        var saltOut = saltHex || bufToHex(salt);
        return "pbkdf2$sha256$" + PBKDF2_ITERS + "$" + saltOut + "$" + bufToHex(bits);
      });
  }

  function verifyPassword(password, stored) {
    var parts = (stored || "").split("$");
    if (parts.length !== 5) return Promise.resolve(false);
    return hashPassword(password, parts[3]).then(function (got) {
      return got === stored;
    });
  }

  function localGetUserByEmail(email) {
    return idbOpen().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("users", "readonly");
        var idx = tx.objectStore("users").index("email");
        var req = idx.get(email);
        req.onsuccess = function () { resolve(req.result || null); };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function localGetUserByGoogle(sub) {
    return idbOpen().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("users", "readonly");
        var idx = tx.objectStore("users").index("googleSub");
        var req = idx.get(sub);
        req.onsuccess = function () { resolve(req.result || null); };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function localPutUser(user) {
    return idbOp("users", "readwrite", function (os) { return os.put(user); }).then(function () { return user; });
  }

  function publicUser(user) {
    return {
      id: user.id,
      email: user.email,
      name: user.name,
      hasPassword: !!user.passwordHash,
      google: !!user.googleSub,
      createdAt: user.createdAt,
      avatarUrl: user.avatarUrl || user.picture || "",
      avatarCustom: !!user.avatarCustom,
    };
  }

  function localCreateSession(user) {
    var token = randomHex(32);
    var expiresAt = new Date(Date.now() + 30 * 24 * 3600 * 1000).toISOString();
    return idbOp("sessions", "readwrite", function (os) {
      return os.put({ token: token, userId: user.id, expiresAt: expiresAt });
    }).then(function () {
      return { token: token, expiresAt: expiresAt, user: publicUser(user) };
    });
  }

  function api(method, path, body) {
    var headers = { "Content-Type": "application/json" };
    if (state.token) headers.Authorization = "Bearer " + state.token;
    var url = state.apiUrl + path;
    return fetch(url, {
      method: method,
      headers: headers,
      body: body ? JSON.stringify(body) : undefined,
    }).then(function (resp) {
      return resp.json().catch(function () { return {}; }).then(function (data) {
        if (!resp.ok) {
          var err = new Error((data && data.error) || "Erreur réseau");
          err.status = resp.status;
          throw err;
        }
        return data;
      });
    });
  }

  function pingHealth(base, timeoutMs) {
    var ctrl = typeof AbortController !== "undefined" ? new AbortController() : null;
    var timer = ctrl ? setTimeout(function () { ctrl.abort(); }, timeoutMs || 20000) : null;
    return fetch(base + "/api/health", { method: "GET", signal: ctrl ? ctrl.signal : undefined })
      .then(function (resp) { return resp.ok; })
      .catch(function () { return false; })
      .then(function (ok) {
        if (timer) clearTimeout(timer);
        return ok;
      });
  }

  function wakeApi(base) {
    function attempt(n) {
      return pingHealth(base, n === 0 ? 25000 : 80000).then(function (ok) {
        if (ok) return true;
        if (n >= 4) return false;
        return attempt(n + 1);
      });
    }
    return attempt(0);
  }

  function detectApi() {
    var configured = (cfg().apiUrl || "").replace(/\/$/, "");
    if (configured) {
      return wakeApi(configured).then(function () { return configured; });
    }
    var candidates = [""];
    if (location.port === "8000") candidates.push(location.protocol + "//" + location.hostname + ":8787");
    var i = 0;
    function next() {
      if (i >= candidates.length) return Promise.resolve(configured || "");
      var base = candidates[i++];
      return pingHealth(base, 4000).then(function (ok) {
        if (ok) return base;
        return next();
      });
    }
    return next();
  }

  function applyAuth(payload, mode) {
    state.mode = mode;
    state.token = payload.token;
    state.user = payload.user;
    saveSession();
    return afterLogin();
  }

  function afterLogin() {
    var anon = { progress: readProgress(), cours: readCours() };
    sessionStorage.setItem(ANON_KEY, JSON.stringify(anon));
    return loadRemoteData().then(function (remote) {
      var mergedP = mergeProgress(anon.progress, remote.progress);
      var mergedC = mergeCours(anon.cours, remote.cours);
      writeLocal(mergedP, mergedC);
      return persistData(mergedP, mergedC);
    }).then(function () {
      paintNav();
      paintPages();
      notifyCompte();
      return state.user;
    });
  }

  function notifyCompte() {
    try {
      document.dispatchEvent(new CustomEvent("psyc-compte-ready"));
    } catch (e) { /* document absent */ }
  }

  function nextAfterLogin() {
    var back = "";
    try { back = sessionStorage.getItem("psyc_retour") || ""; } catch (e) { /* ignore */ }
    try { sessionStorage.removeItem("psyc_retour"); } catch (e2) { /* ignore */ }
    if (back === "cahier") return compteHref("cahier.html");
    return compteHref("espace.html");
  }

  function loadRemoteData() {
    if (state.mode === "remote") {
      return api("GET", "/api/data");
    }
    return idbOpen().then(function (db) {
      return new Promise(function (resolve) {
        var tx = db.transaction("snapshots", "readonly");
        var req = tx.objectStore("snapshots").get(state.user.id);
        req.onsuccess = function () {
          var row = req.result;
          resolve(row ? { progress: row.progress, cours: row.cours } : { progress: emptyProgress(), cours: emptyCours() });
        };
        req.onerror = function () {
          resolve({ progress: emptyProgress(), cours: emptyCours() });
        };
      });
    }).catch(function () {
      return { progress: emptyProgress(), cours: emptyCours() };
    });
  }

  function persistData(progress, cours) {
    progress = progress || readProgress();
    cours = cours || readCours();
    if (!state.user) return Promise.resolve();
    if (state.mode === "remote") {
      return api("PUT", "/api/data", { progress: progress, cours: cours });
    }
    return idbOp("snapshots", "readwrite", function (os) {
      return os.put({
        userId: state.user.id,
        progress: progress,
        cours: cours,
        updatedAt: new Date().toISOString(),
      });
    }).then(function () {
      return ingestLocal(progress, cours);
    });
  }

  function ingestLocal(progress, cours) {
    var jobs = [];
    Object.keys((progress.quizBest) || {}).forEach(function (id) {
      var rec = progress.quizBest[id];
      jobs.push(recordGradeLocal(id, rec.score, rec.total, rec.pct, "quiz"));
    });
    Object.keys((cours.quizzes) || {}).forEach(function (id) {
      var rec = cours.quizzes[id];
      jobs.push(recordGradeLocal(id, rec.score, rec.total, null, "cours"));
    });
    Object.keys((cours.notes) || {}).forEach(function (id) {
      jobs.push(upsertNoteLocal(id, cours.notes[id], ""));
    });
    return Promise.all(jobs);
  }

  function recordGradeLocal(quizId, score, total, pct, source) {
    if (!state.user) return Promise.resolve();
    pct = pct == null ? Math.round(100 * score / (total || 1)) : pct;
    return idbOpen().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("grades", "readwrite");
        var os = tx.objectStore("grades");
        var idx = os.index("userId");
        var req = idx.getAll(state.user.id);
        req.onsuccess = function () {
          var found = (req.result || []).find(function (g) {
            return g.quizId === quizId && g.source === source;
          });
          if (found && found.pct > pct) {
            resolve(found);
            return;
          }
          var row = found || {
            id: randomHex(16),
            userId: state.user.id,
            quizId: quizId,
            source: source,
          };
          row.score = score;
          row.total = total;
          row.pct = pct;
          row.at = new Date().toISOString();
          os.put(row);
          resolve(row);
        };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function upsertNoteLocal(courseId, body, title) {
    if (!state.user) return Promise.resolve();
    return idbOpen().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("notes", "readwrite");
        var os = tx.objectStore("notes");
        var idx = os.index("userId");
        var req = idx.getAll(state.user.id);
        req.onsuccess = function () {
          var found = (req.result || []).find(function (n) { return n.courseId === courseId; });
          var row = found || {
            id: randomHex(16),
            userId: state.user.id,
            courseId: courseId,
          };
          row.title = title || row.title || "";
          row.body = body || "";
          row.updatedAt = new Date().toISOString();
          os.put(row);
          resolve(row);
        };
        req.onerror = function () { reject(req.error); };
      });
    });
  }

  function listNotes() {
    if (!state.user) return Promise.resolve([]);
    if (state.mode === "remote") {
      return api("GET", "/api/notes").then(function (d) { return d.notes || []; });
    }
    return idbOpen().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("notes", "readonly");
        var req = tx.objectStore("notes").index("userId").getAll(state.user.id);
        req.onsuccess = function () { resolve(req.result || []); };
        req.onerror = function () { reject(req.error); };
      });
    }).catch(function () { return []; });
  }

  function listGrades() {
    if (!state.user) return Promise.resolve([]);
    if (state.mode === "remote") {
      return api("GET", "/api/grades").then(function (d) { return d.grades || []; });
    }
    return idbOpen().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction("grades", "readonly");
        var req = tx.objectStore("grades").index("userId").getAll(state.user.id);
        req.onsuccess = function () { resolve(req.result || []); };
        req.onerror = function () { reject(req.error); };
      });
    }).catch(function () { return []; });
  }

  function saveNote(courseId, body, title, noteId) {
    if (!state.user) return Promise.reject(new Error("Connexion requise"));
    var cours = readCours();
    cours.notes[courseId] = body;
    localStorage.setItem(COURS_KEY, JSON.stringify(cours));
    if (state.mode === "remote") {
      var payload = { courseId: courseId, body: body, title: title || "" };
      var method = noteId ? "PUT" : "POST";
      var path = noteId ? "/api/notes/" + noteId : "/api/notes";
      return api(method, path, payload).then(function (d) {
        return persistData();
      });
    }
    return upsertNoteLocal(courseId, body, title).then(function () { return persistData(); });
  }

  function deleteNote(noteId, courseId) {
    if (!state.user) return Promise.reject(new Error("Connexion requise"));
    if (courseId) {
      var cours = readCours();
      delete cours.notes[courseId];
      localStorage.setItem(COURS_KEY, JSON.stringify(cours));
    }
    if (state.mode === "remote") {
      return api("DELETE", "/api/notes/" + noteId).then(function () { return persistData(); });
    }
    return idbOp("notes", "readwrite", function (os) { return os.delete(noteId); })
      .then(function () { return persistData(); });
  }

  function recordGrade(quizId, score, total, source) {
    if (!state.user) return;
    var pct = Math.round(100 * score / (total || 1));
    if (state.mode === "remote") {
      api("POST", "/api/grades", {
        quizId: quizId, score: score, total: total, pct: pct, source: source || "quiz",
      }).catch(function () {});
    } else {
      recordGradeLocal(quizId, score, total, pct, source || "quiz").catch(function () {});
    }
    queueSync();
  }

  function queueSync() {
    if (!state.user) return;
    clearTimeout(state.syncTimer);
    state.syncTimer = setTimeout(function () {
      persistData().catch(function () {});
    }, 800);
  }

  function validEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email || "");
  }

  function register(email, password, name) {
    email = (email || "").trim().toLowerCase();
    name = (name || "").trim() || email.split("@")[0];
    if (!validEmail(email)) return Promise.reject(new Error("Adresse e-mail invalide."));
    if (!password || password.length < 8) return Promise.reject(new Error("Le mot de passe doit contenir au moins 8 caractères."));
    if (state.mode === "remote") {
      return api("POST", "/api/auth/register", { email: email, password: password, name: name })
        .then(function (d) { return applyAuth(d, "remote"); });
    }
    return localGetUserByEmail(email).then(function (existing) {
      if (existing) throw new Error("Cette adresse est déjà utilisée.");
      return hashPassword(password).then(function (hash) {
        var user = {
          id: randomHex(16),
          email: email,
          name: name,
          passwordHash: hash,
          googleSub: "",
          createdAt: new Date().toISOString(),
        };
        return localPutUser(user).then(function () { return localCreateSession(user); });
      });
    }).then(function (d) { return applyAuth(d, "local"); });
  }

  function login(email, password) {
    email = (email || "").trim().toLowerCase();
    if (state.mode === "remote") {
      return api("POST", "/api/auth/login", { email: email, password: password })
        .then(function (d) { return applyAuth(d, "remote"); });
    }
    return localGetUserByEmail(email).then(function (user) {
      if (!user || !user.passwordHash) throw new Error("E-mail ou mot de passe incorrect.");
      return verifyPassword(password, user.passwordHash).then(function (ok) {
        if (!ok) throw new Error("E-mail ou mot de passe incorrect.");
        return localCreateSession(user);
      });
    }).then(function (d) { return applyAuth(d, "local"); });
  }

  function decodeJwtPayload(token) {
    try {
      var part = token.split(".")[1].replace(/-/g, "+").replace(/_/g, "/");
      while (part.length % 4) part += "=";
      return JSON.parse(atob(part));
    } catch (e) {
      return null;
    }
  }

  function loginGoogle(credential) {
    if (state.mode === "remote") {
      return api("POST", "/api/auth/google", { credential: credential })
        .then(function (d) { return applyAuth(d, "remote"); });
    }
    var payload = decodeJwtPayload(credential);
    if (!payload || !payload.email || !payload.sub) {
      return Promise.reject(new Error("Jeton Google invalide."));
    }
    var email = String(payload.email).toLowerCase();
    var sub = String(payload.sub);
    var name = payload.name || email.split("@")[0];
    var picture = payload.picture || "";
    return localGetUserByGoogle(sub).then(function (user) {
      if (user) {
        if (picture && !user.avatarCustom) user.avatarUrl = picture;
        return localPutUser(user);
      }
      return localGetUserByEmail(email).then(function (existing) {
        if (existing) {
          existing.googleSub = sub;
          existing.name = existing.name || name;
          if (picture && !existing.avatarCustom) existing.avatarUrl = picture;
          return localPutUser(existing);
        }
        return localPutUser({
          id: randomHex(16),
          email: email,
          name: name,
          passwordHash: "",
          googleSub: sub,
          avatarUrl: picture,
          createdAt: new Date().toISOString(),
        });
      });
    }).then(function (user) {
      return localCreateSession(user);
    }).then(function (d) { return applyAuth(d, "local"); });
  }

  function logout() {
    var token = state.token;
    var finish = function () {
      state.user = null;
      state.token = "";
      saveSession();
      try {
        var backup = JSON.parse(sessionStorage.getItem(ANON_KEY) || "null");
        if (backup) writeLocal(backup.progress, backup.cours);
      } catch (e) { /* ignore */ }
      sessionStorage.removeItem(ANON_KEY);
      paintNav();
      var page = document.body.getAttribute("data-compte-page");
      if (page === "espace") {
        location.href = compteHref("compte.html");
      } else {
        paintPages();
        notifyCompte();
      }
    };
    if (state.mode === "remote" && token) {
      return api("POST", "/api/auth/logout").catch(function () {}).then(finish);
    }
    if (token) {
      return idbOp("sessions", "readwrite", function (os) { return os.delete(token); })
        .catch(function () {}).then(finish);
    }
    return Promise.resolve(finish());
  }

  function restoreSession() {
    var saved = loadSession();
    if (!saved || !saved.token || !saved.user) return Promise.resolve();
    if (saved.mode === "local") {
      state.user = null;
      state.token = "";
      saveSession();
      return Promise.resolve();
    }
    state.token = saved.token;
    state.user = saved.user;
    state.mode = "remote";
    return api("GET", "/api/me").then(function (d) {
      state.user = d.user;
      saveSession();
      return loadRemoteData().then(function (remote) {
        var mergedP = mergeProgress(readProgress(), remote.progress);
        var mergedC = mergeCours(readCours(), remote.cours);
        writeLocal(mergedP, mergedC);
        return persistData(mergedP, mergedC);
      });
    }).catch(function () {
      state.user = null;
      state.token = "";
      saveSession();
    });
  }

  function compteHref(file) {
    var root = document.body.getAttribute("data-root") || "./";
    return root + "livres-psychologie/07-ebook-final/" + file;
  }

  function initials(name) {
    var parts = String(name || "?").trim().split(/\s+/);
    var a = (parts[0] || "?").charAt(0);
    var b = parts.length > 1 ? parts[1].charAt(0) : "";
    return (a + b).toUpperCase();
  }

  function paintMark(el, user) {
    if (!el) return;
    el.textContent = "";
    if (user && user.avatarUrl) {
      var img = document.createElement("img");
      img.src = user.avatarUrl;
      img.alt = "";
      img.referrerPolicy = "no-referrer";
      img.decoding = "async";
      el.appendChild(img);
      return;
    }
    el.textContent = user ? initials(user.name) : "👤";
  }

  function paintNav() {
    var btn = document.getElementById("nav-compte");
    if (!btn) return;
    var label = btn.querySelector(".nav-compte-label");
    var mark = btn.querySelector(".nav-compte-mark");
    if (state.user) {
      btn.href = compteHref("espace.html");
      btn.setAttribute("aria-label", "Espace de " + state.user.name);
      btn.classList.add("is-on");
      if (label) label.textContent = state.user.name.split(" ")[0];
      paintMark(mark, state.user);
    } else {
      btn.href = compteHref("compte.html");
      btn.setAttribute("aria-label", "Compte étudiant");
      btn.classList.remove("is-on");
      if (label) label.textContent = "Compte";
      paintMark(mark, null);
    }
  }

  function setMsg(el, text, kind) {
    if (!el) return;
    el.hidden = !text;
    el.textContent = text || "";
    el.className = "compte-msg" + (kind ? " " + kind : "");
  }

  function setModeHint(el) {
    if (!el) return;
    el.textContent = "Compte enregistré sur le serveur — notes, scores et photo te suivent.";
  }

  function bindLoginPage() {
    if (document.body.getAttribute("data-compte-page") !== "login") return;
    if (state.user) {
      location.replace(nextAfterLogin());
      return;
    }
    var formIn = document.getElementById("compte-login");
    var formUp = document.getElementById("compte-register");
    var msg = document.getElementById("compte-feedback");
    var tabs = document.querySelectorAll("[data-compte-tab]");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var which = tab.getAttribute("data-compte-tab");
        tabs.forEach(function (t) { t.classList.toggle("active", t === tab); });
        if (formIn) formIn.hidden = which !== "login";
        if (formUp) formUp.hidden = which !== "register";
        setMsg(msg, "", "");
      });
    });
    if (formIn) {
      formIn.addEventListener("submit", function (e) {
        e.preventDefault();
        var email = formIn.querySelector('[name="email"]').value;
        var password = formIn.querySelector('[name="password"]').value;
        login(email, password).then(function () {
          toast("Connexion réussie");
          location.href = nextAfterLogin();
        }).catch(function (err) {
          setMsg(msg, err.message || "Connexion impossible", "err");
        });
      });
    }
    if (formUp) {
      formUp.addEventListener("submit", function (e) {
        e.preventDefault();
        var name = formUp.querySelector('[name="name"]').value;
        var email = formUp.querySelector('[name="email"]').value;
        var password = formUp.querySelector('[name="password"]').value;
        register(email, password, name).then(function () {
          toast("Compte créé");
          location.href = nextAfterLogin();
        }).catch(function (err) {
          setMsg(msg, err.message || "Inscription impossible", "err");
        });
      });
    }
    var googleMount = document.getElementById("google-btn");
    var googleHint = document.getElementById("google-hint");
    if (state.googleClientId && googleMount) {
      loadGoogle(googleMount);
      if (googleHint) googleHint.hidden = true;
    } else if (googleHint) {
      googleHint.hidden = false;
    }
    var modeEl = document.getElementById("compte-mode");
    setModeHint(modeEl);
  }

  function loadGoogle(mount) {
    function render() {
      if (!window.google || !google.accounts || !google.accounts.id) return;
      google.accounts.id.initialize({
        client_id: state.googleClientId,
        ux_mode: "popup",
        auto_select: false,
        cancel_on_tap_outside: true,
        callback: function (resp) {
          loginGoogle(resp.credential).then(function () {
            toast("Connexion Google réussie");
            location.href = nextAfterLogin();
          }).catch(function (err) {
            setMsg(document.getElementById("compte-feedback"), err.message, "err");
          });
        },
      });
      google.accounts.id.renderButton(mount, {
        theme: "outline",
        size: "large",
        locale: "fr",
        text: "continue_with",
        shape: "pill",
        width: 320,
      });
    }
    if (window.google && google.accounts) {
      render();
      return;
    }
    var s = document.createElement("script");
    s.src = "https://accounts.google.com/gsi/client";
    s.async = true;
    s.defer = true;
    s.onload = render;
    document.head.appendChild(s);
  }

  function pctOn20(score, total) {
    if (!total) return "—";
    return Math.round((score / total) * 20 * 10) / 10 + " / 20";
  }

  function paintEspace() {
    if (document.body.getAttribute("data-compte-page") !== "espace") return;
    if (!state.user) {
      location.replace(compteHref("compte.html"));
      return;
    }
    var nameEl = document.getElementById("espace-name");
    var mailEl = document.getElementById("espace-email");
    var modeEl = document.getElementById("espace-mode");
    if (nameEl) nameEl.textContent = state.user.name;
    if (mailEl) mailEl.textContent = state.user.email;
    setModeHint(modeEl);
    paintMark(document.getElementById("espace-avatar"), state.user);
    var file = document.getElementById("espace-avatar-file");
    if (file && !file.getAttribute("data-bound")) {
      file.setAttribute("data-bound", "1");
      file.addEventListener("change", function () {
        var chosen = file.files && file.files[0];
        file.value = "";
        if (!chosen) return;
        resizeAvatar(chosen).then(function (dataUrl) {
          return api("PUT", "/api/me/avatar", { image: dataUrl });
        }).then(function (d) {
          state.user = d.user;
          saveSession();
          paintNav();
          paintMark(document.getElementById("espace-avatar"), state.user);
          toast("Photo enregistrée sur le serveur");
        }).catch(function (err) {
          toast(err.message || "Photo impossible à enregistrer");
        });
      });
    }
    var progress = readProgress();
    var cours = readCours();
    var visited = Object.keys(progress.visited || {}).length;
    var quizzes = Object.keys(progress.quizBest || {});
    var quizN = quizzes.length;
    var attendance = Object.keys(cours.attendance || {}).length;
    var setText = function (id, val) {
      var el = document.getElementById(id);
      if (el) el.textContent = val;
    };
    setText("espace-visited", visited);
    setText("espace-quizzes", quizN);
    setText("espace-cours", attendance);
    var avg = 0;
    if (quizN) {
      avg = Math.round(quizzes.reduce(function (s, k) { return s + (progress.quizBest[k].pct || 0); }, 0) / quizN);
    }
    setText("espace-moyenne", quizN ? avg + " %" : "—");
    var tbody = document.getElementById("espace-grades");
    if (tbody) {
      tbody.textContent = "";
      listGrades().then(function (grades) {
        if (!grades.length) {
          Object.keys(progress.quizBest || {}).forEach(function (id) {
            grades.push({
              quizId: id,
              score: progress.quizBest[id].score,
              total: progress.quizBest[id].total,
              pct: progress.quizBest[id].pct,
              source: "quiz",
              at: "",
            });
          });
        }
        if (!grades.length) {
          var tr = document.createElement("tr");
          var td = document.createElement("td");
          td.colSpan = 4;
          td.textContent = "Aucune note enregistrée pour l'instant. Passe un quiz : le meilleur score est gardé.";
          tr.appendChild(td);
          tbody.appendChild(tr);
          return;
        }
        grades.sort(function (a, b) { return (b.pct || 0) - (a.pct || 0); });
        grades.forEach(function (g) {
          var tr = document.createElement("tr");
          var cells = [
            g.quizId,
            g.source === "cours" ? "Cours" : "Quiz",
            (g.score || 0) + " / " + (g.total || 0) + " (" + (g.pct || 0) + " %)",
            pctOn20(g.score, g.total),
          ];
          cells.forEach(function (txt) {
            var td = document.createElement("td");
            td.textContent = txt;
            tr.appendChild(td);
          });
          tbody.appendChild(tr);
        });
      });
    }
    var notesEl = document.getElementById("espace-notes");
    if (notesEl) {
      listNotes().then(function (notes) {
        notesEl.textContent = "";
        if (!notes.length) {
          var p = document.createElement("p");
          p.className = "compte-empty";
          p.textContent = "Pas encore de notes. Elles s'enregistrent aussi depuis le lecteur de cours.";
          notesEl.appendChild(p);
          return;
        }
        notes.forEach(function (n) {
          var card = document.createElement("article");
          card.className = "note-card";
          var h = document.createElement("h3");
          h.textContent = n.title || n.courseId;
          var meta = document.createElement("p");
          meta.className = "note-meta";
          meta.textContent = (n.courseId || "") + (n.updatedAt ? " · " + n.updatedAt.replace("T", " ").slice(0, 16) : "");
          var pre = document.createElement("pre");
          pre.textContent = n.body || "";
          var del = document.createElement("button");
          del.type = "button";
          del.className = "btn btn-ghost";
          del.textContent = "Supprimer";
          del.addEventListener("click", function () {
            deleteNote(n.id, n.courseId).then(function () { paintEspace(); });
          });
          card.appendChild(h);
          card.appendChild(meta);
          card.appendChild(pre);
          card.appendChild(del);
          notesEl.appendChild(card);
        });
      });
    }
    var form = document.getElementById("espace-note-form");
    if (form && !form.getAttribute("data-bound")) {
      form.setAttribute("data-bound", "1");
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var courseId = form.querySelector('[name="courseId"]').value.trim() || "general";
        var title = form.querySelector('[name="title"]').value.trim();
        var body = form.querySelector('[name="body"]').value;
        saveNote(courseId, body, title).then(function () {
          form.reset();
          toast("Note enregistrée");
          paintEspace();
        }).catch(function (err) {
          toast(err.message || "Enregistrement impossible");
        });
      });
    }
    var out = document.getElementById("espace-logout");
    if (out && !out.getAttribute("data-bound")) {
      out.setAttribute("data-bound", "1");
      out.addEventListener("click", function () { logout(); });
    }
  }

  function paintPages() {
    bindLoginPage();
    paintEspace();
  }

  function resizeAvatar(file) {
    return new Promise(function (resolve, reject) {
      if (!file || !file.type || file.type.indexOf("image/") !== 0) {
        reject(new Error("Choisis une image JPEG, PNG ou WebP."));
        return;
      }
      if (file.size > 8 * 1024 * 1024) {
        reject(new Error("Image trop lourde."));
        return;
      }
      var url = URL.createObjectURL(file);
      var img = new Image();
      img.onload = function () {
        URL.revokeObjectURL(url);
        var size = 256;
        var canvas = document.createElement("canvas");
        canvas.width = size;
        canvas.height = size;
        var ctx = canvas.getContext("2d");
        var w = img.naturalWidth || img.width;
        var h = img.naturalHeight || img.height;
        if (!w || !h) {
          reject(new Error("Image illisible."));
          return;
        }
        var scale = Math.max(size / w, size / h);
        var dw = w * scale;
        var dh = h * scale;
        ctx.drawImage(img, (size - dw) / 2, (size - dh) / 2, dw, dh);
        resolve(canvas.toDataURL("image/jpeg", 0.85));
      };
      img.onerror = function () {
        URL.revokeObjectURL(url);
        reject(new Error("Image illisible."));
      };
      img.src = url;
    });
  }

  function boot() {
    state.googleClientId = (cfg().googleClientId || "").trim();
    return detectApi().then(function (base) {
      state.apiUrl = base || (cfg().apiUrl || "").replace(/\/$/, "");
      state.mode = "remote";
      if (!state.apiUrl) {
        throw new Error("API indisponible");
      }
    }).then(function () {
      return fetch(state.apiUrl + "/api/config").then(function (r) { return r.json(); })
        .then(function (d) {
          if (d.googleClientId) state.googleClientId = d.googleClientId;
        }).catch(function () {});
    }).then(restoreSession).then(function () {
      paintNav();
      paintPages();
      notifyCompte();
      setInterval(function () {
        pingHealth(state.apiUrl, 15000);
      }, 4 * 60 * 1000);
    }).catch(function () {
      state.mode = "remote";
      paintNav();
      paintPages();
      notifyCompte();
    });
  }

  window.PsycCompte = {
    queueSync: queueSync,
    recordGrade: recordGrade,
    currentUser: function () { return state.user; },
    isLoggedIn: function () { return !!state.user; },
    register: register,
    login: login,
    loginGoogle: loginGoogle,
    logout: logout,
    listNotes: listNotes,
    listGrades: listGrades,
    saveNote: saveNote,
    syncNow: function () { return persistData(); },
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
