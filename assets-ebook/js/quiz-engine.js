/* ==========================================================================
   PSYCLOPÉDIA — Moteur de quiz (notation /20, corrigé complet, explications)
   Nécessite QUIZ_ID, QUIZ_TITLE, QUIZ_QUESTIONS définis avant ce script.
   ========================================================================== */

(function () {
  let current = 0;
  let score = 0;
  const answers = [];

  function renderQuestion() {
    const q = QUIZ_QUESTIONS[current];
    const container = document.getElementById("quiz-container");
    const pct = Math.round((current / QUIZ_QUESTIONS.length) * 100);

    container.innerHTML = `
      <div class="quiz-progress-bar"><div class="quiz-progress-fill" style="width:${pct}%"></div></div>
      <p style="font-size:0.8rem;color:var(--gris);margin-bottom:0.5rem">Question ${current + 1} / ${QUIZ_QUESTIONS.length}</p>
      <p class="quiz-q-text">${q.q}</p>
      <div class="quiz-answers">
        ${q.a.map((ans, i) => `<button class="quiz-answer-btn" data-i="${i}">${ans}</button>`).join("")}
      </div>
      <div class="quiz-explain" id="quiz-explain"></div>
      <div style="text-align:right">
        <button class="btn btn-primary quiz-next-btn" id="quiz-next" style="display:none">Question suivante →</button>
      </div>
    `;

    container.querySelectorAll(".quiz-answer-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const i = +btn.dataset.i;
        const correct = q.correct;
        container.querySelectorAll(".quiz-answer-btn").forEach((b) => (b.disabled = true));
        if (i === correct) {
          btn.classList.add("correct");
          score++;
          answers.push({ q: q.q, chosen: q.a[i], correct: q.a[correct], ok: true, explain: q.explain });
        } else {
          btn.classList.add("wrong");
          container.querySelector(`[data-i="${correct}"]`).classList.add("correct");
          answers.push({ q: q.q, chosen: q.a[i], correct: q.a[correct], ok: false, explain: q.explain });
        }
        const explainBox = document.getElementById("quiz-explain");
        explainBox.innerHTML = `💡 <strong>Explication :</strong> ${q.explain}`;
        explainBox.classList.add("show");
        document.getElementById("quiz-next").style.display = "inline-flex";
      });
    });

    const nextBtn = document.getElementById("quiz-next");
    nextBtn.onclick = () => {
      current++;
      if (current < QUIZ_QUESTIONS.length) {
        renderQuestion();
      } else {
        renderResult();
      }
    };
  }

  function gradeOn20() {
    return Math.round((score / QUIZ_QUESTIONS.length) * 20 * 10) / 10;
  }

  function renderResult() {
    const container = document.getElementById("quiz-container");
    const grade = gradeOn20();
    const pct = Math.round((score / QUIZ_QUESTIONS.length) * 100);
    let msg = "Continue à explorer les fiches pour progresser !";
    let emoji = "📚";
    if (pct >= 90) { msg = "Excellent ! Tu maîtrises parfaitement ce thème."; emoji = "🏆"; }
    else if (pct >= 70) { msg = "Très bon niveau, encore quelques notions à consolider."; emoji = "🎯"; }
    else if (pct >= 50) { msg = "Bonne base ! Relis les fiches pour aller plus loin."; emoji = "🌱"; }

    if (typeof recordQuizScore === "function") {
      recordQuizScore(QUIZ_ID, score, QUIZ_QUESTIONS.length);
    }

    container.innerHTML = `
      <div class="quiz-result">
        <div style="font-size:2.5rem">${emoji}</div>
        <div class="quiz-result-grade">${grade}<span style="font-size:1.2rem;color:var(--gris)">/20</span></div>
        <p class="quiz-result-msg">${score}/${QUIZ_QUESTIONS.length} bonnes réponses — ${msg}</p>
        <div class="cta-row" style="justify-content:center">
          <button class="btn btn-primary" id="quiz-restart">🔄 Recommencer</button>
          <a class="btn btn-secondary" href="index.html">← Tous les quiz</a>
        </div>
        <h3 style="font-family:var(--serif);margin-top:2.5rem;margin-bottom:0.5rem">📋 Corrigé complet</h3>
        <div class="quiz-recap">
          ${answers
            .map(
              (a, i) => `<div class="quiz-recap-item ${a.ok ? "ok" : "ko"}">
              <div class="q">${i + 1}. ${a.q}</div>
              <div class="a">${a.ok ? "✅" : "❌"} Ta réponse : <strong>${a.chosen}</strong>${a.ok ? "" : ` — Bonne réponse : <strong>${a.correct}</strong>`}</div>
              <div class="a" style="margin-top:0.35rem">💡 ${a.explain}</div>
            </div>`
            )
            .join("")}
        </div>
      </div>
    `;

    document.getElementById("quiz-restart").onclick = () => {
      current = 0;
      score = 0;
      answers.length = 0;
      renderQuestion();
    };
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("quiz-title").textContent = QUIZ_TITLE;
    renderQuestion();
  });
})();
