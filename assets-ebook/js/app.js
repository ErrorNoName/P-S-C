/* ==========================================================================
   PSYCLOPÉDIA — Moteur JS (progression, flashcards, quiz, UI)
   ========================================================================== */

const STORAGE_KEY = "psyclopedia_progress_v1";
const TOTAL_CATEGORIES = 27;
const TOTAL_QUIZZES = 27;

function loadProgress() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return { visited: {}, quizBest: {} };
    return JSON.parse(raw);
  } catch (e) {
    return { visited: {}, quizBest: {} };
  }
}

function saveProgress(p) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(p));
}

function markVisited(categoryId) {
  const p = loadProgress();
  p.visited[categoryId] = true;
  saveProgress(p);
}

function recordQuizScore(quizId, score, total) {
  const p = loadProgress();
  const pct = Math.round((score / total) * 100);
  if (!p.quizBest[quizId] || p.quizBest[quizId].pct < pct) {
    p.quizBest[quizId] = { score, total, pct };
  }
  saveProgress(p);
}

function getMasteryPct() {
  const p = loadProgress();
  const visitedCount = Object.keys(p.visited).length;
  const quizIds = Object.keys(p.quizBest);
  const quizAvg = quizIds.length
    ? quizIds.reduce((s, k) => s + p.quizBest[k].pct, 0) / quizIds.length
    : 0;
  const readingScore = (visitedCount / TOTAL_CATEGORIES) * 60;
  const quizScore = (quizAvg / 100) * 40;
  return Math.round(readingScore + quizScore);
}

function toast(msg) {
  let stack = document.getElementById("toast-stack");
  if (!stack) {
    stack = document.createElement("div");
    stack.id = "toast-stack";
    stack.setAttribute("aria-live", "polite");
    document.body.appendChild(stack);
  }
  const el = document.createElement("div");
  el.className = "toast-item toast-plain";
  el.setAttribute("role", "status");
  el.innerHTML = '<div class="toast-t"></div>';
  el.querySelector(".toast-t").textContent = msg;
  while (stack.children.length >= 3) stack.removeChild(stack.firstChild);
  stack.appendChild(el);
  requestAnimationFrame(() => el.classList.add("show"));
  setTimeout(() => {
    el.classList.remove("show");
    setTimeout(() => { if (el.parentNode) el.parentNode.removeChild(el); }, 220);
  }, 2600);
}

/* ---------- Init on every page ---------- */
document.addEventListener("DOMContentLoaded", () => {
  // Highlight nav based on current page
  const path = window.location.pathname;
  document.querySelectorAll(".nav-links a").forEach((a) => {
    const href = a.getAttribute("href") || "";
    if (href !== "#" && path.endsWith(href.split("/").pop())) {
      a.classList.add("active");
    }
  });

  // Mark visited categories with badge on grid cards
  const progress = loadProgress();
  document.querySelectorAll("[data-cat-id]").forEach((card) => {
    const id = card.getAttribute("data-cat-id");
    if (progress.visited[id]) {
      card.classList.add("visited");
      const fill = card.querySelector(".cat-progress-fill");
      if (fill) fill.style.width = "100%";
    }
  });

  // Auto mark current category page as visited
  const autoId = document.body.getAttribute("data-mark-visited");
  if (autoId) {
    markVisited(autoId);
  }

  // Flashcards
  document.querySelectorAll(".flashcard").forEach((card) => {
    card.addEventListener("click", () => card.classList.toggle("flipped"));
  });

  // Mastery widgets (home page)
  document.querySelectorAll("[data-mastery-pct]").forEach((el) => {
    el.textContent = getMasteryPct() + "%";
  });
  document.querySelectorAll("[data-mastery-marker]").forEach((el) => {
    el.style.left = `calc(${getMasteryPct()}% - 2px)`;
  });
  document.querySelectorAll("[data-mastery-badge]").forEach((el) => {
    const pct = getMasteryPct();
    let label = "Débutant";
    if (pct >= 75) label = "Expert";
    else if (pct >= 50) label = "Avancé";
    else if (pct >= 25) label = "Intermédiaire";
    el.textContent = label;
  });
  document.querySelectorAll("[data-visited-count]").forEach((el) => {
    el.textContent = Object.keys(progress.visited).length;
  });
  document.querySelectorAll("[data-quiz-count]").forEach((el) => {
    el.textContent = Object.keys(progress.quizBest).length;
  });
  document.querySelectorAll("[data-best-quiz-pct]").forEach((el) => {
    const vals = Object.values(progress.quizBest).map((v) => v.pct);
    el.textContent = vals.length ? Math.max(...vals) + "%" : "—";
  });

  // Fill category mini-progress bars on home
  document.querySelectorAll(".cat-progress-fill[data-cat-key]").forEach((el) => {
    const key = el.getAttribute("data-cat-key");
    el.style.width = progress.visited[key] ? "100%" : "0%";
  });

  // Quiz best score badges (quiz hub)
  document.querySelectorAll("[data-quiz-id]").forEach((el) => {
    const id = el.getAttribute("data-quiz-id");
    const badge = el.querySelector(".quiz-best");
    if (badge && progress.quizBest[id]) {
      badge.textContent = "Meilleur : " + progress.quizBest[id].score + "/" + progress.quizBest[id].total;
      badge.style.display = "inline-block";
    } else if (badge) {
      badge.style.display = "none";
    }
  });

  document.querySelectorAll("[data-quiz-total]").forEach((el) => {
    el.textContent = TOTAL_QUIZZES;
  });
  document.querySelectorAll("[data-cat-total]").forEach((el) => {
    el.textContent = TOTAL_CATEGORIES;
  });

  // Cocher les étapes déjà consultées dans les parcours guidés
  document.querySelectorAll(".path-step[href]").forEach((step) => {
    const href = step.getAttribute("href") || "";
    const match = href.match(/categories\/([\w-]+)\.html/);
    const quizMatch = href.match(/quiz\.html\?id=([\w-]+)/);
    if (match && progress.visited[match[1]]) step.classList.add("done");
    else if (quizMatch && progress.quizBest[quizMatch[1]]) step.classList.add("done");
  });

  // Reader-card action buttons (random category / continue)
  const btnRandom = document.getElementById("btn-random-cat");
  if (btnRandom) {
    btnRandom.addEventListener("click", (e) => {
      e.preventDefault();
      const cats = btnRandom.getAttribute("data-cats").split(",");
      const pick = cats[Math.floor(Math.random() * cats.length)];
      window.location.href = "livres-psychologie/07-ebook-final/categories/" + pick + ".html";
    });
  }
});
