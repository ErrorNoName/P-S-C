# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Pages de connexion et d'espace étudiant."""

import os

from shell import page_header, page_shell

BASE = os.path.dirname(os.path.abspath(__file__))


def _write(name, html):
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path


def render_compte():
    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Compte étudiant", None)],
        icon="👤", color="vert",
        title="Compte étudiant",
        subtitle="Suivre tes cours, tes notes et tes scores — e-mail et mot de passe, ou Google",
        chips=["E-mail / mot de passe", "Google", "Notes enregistrées", "Quiz notés"],
    )
    body = f"""{header}
<div class="section">
  <div class="compte-wrap">
    <div class="compte-card">
      <div class="compte-tabs" role="tablist">
        <button type="button" class="active" data-compte-tab="login">Connexion</button>
        <button type="button" data-compte-tab="register">Créer un compte</button>
      </div>
      <form id="compte-login" class="compte-form" autocomplete="on">
        <label>E-mail
          <input type="email" name="email" required maxlength="254" autocomplete="username">
        </label>
        <label>Mot de passe
          <input type="password" name="password" required minlength="8" autocomplete="current-password">
        </label>
        <button class="btn btn-primary" type="submit">Se connecter</button>
      </form>
      <form id="compte-register" class="compte-form" hidden autocomplete="on">
        <label>Nom affiché
          <input type="text" name="name" required maxlength="80" autocomplete="name">
        </label>
        <label>E-mail
          <input type="email" name="email" required maxlength="254" autocomplete="username">
        </label>
        <label>Mot de passe (8 caractères minimum)
          <input type="password" name="password" required minlength="8" autocomplete="new-password">
        </label>
        <button class="btn btn-primary" type="submit">Créer le compte</button>
      </form>
      <div class="compte-sep">ou</div>
      <div id="google-btn"></div>
      <p id="google-hint" class="compte-hint">La connexion Google s'affiche dès qu'un identifiant OAuth
      public est configuré sur le serveur (<code>PSYCLOPEDIA_GOOGLE_CLIENT_ID</code>).</p>
      <p id="compte-feedback" class="compte-msg" hidden></p>
      <p id="compte-mode" class="compte-mode"></p>
    </div>
    <div class="note-box" style="margin-top:1.4rem">
      <strong>Ce que le compte retient.</strong> Catégories lues, meilleurs scores de quiz (sur 20),
      présence aux cours de 50 minutes, et tes notes de séance. Rien n'est un dossier médical :
      c'est un carnet d'apprentissage. Sur GitHub Pages sans API, le carnet reste dans ce navigateur
      (IndexedDB). Avec le serveur SQLite, le même compte suit l'étudiant d'un appareil à l'autre.
    </div>
  </div>
</div>
"""
    _write("compte.html", page_shell(
        "Compte étudiant", body, depth=0,
        body_attrs='data-compte-page="login"',
        description="Créer un compte étudiant Psyclopédia : e-mail et mot de passe ou Google, notes de cours et scores enregistrés.",
    ))


def render_espace():
    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Compte", "compte.html"), ("Espace", None)],
        icon="🎒", color="or",
        title="Ton espace d'apprentissage",
        subtitle="Progression, notes de quiz et carnet de cours, enregistrés sur ton compte",
        chips=["Progression", "Notes /20", "Carnet de cours"],
    )
    body = f"""{header}
<div class="section">
  <div class="compte-wrap wide">
    <div class="compte-card espace-profile">
      <div class="espace-id">
        <div class="espace-avatar" aria-hidden="true">✓</div>
        <div>
          <h2 id="espace-name" style="margin:0;font-size:1.25rem">Étudiant</h2>
          <p id="espace-email" style="margin:0.2rem 0 0;color:var(--gris)"></p>
          <p id="espace-mode" class="compte-hint" style="margin:0.25rem 0 0"></p>
        </div>
      </div>
      <div class="cta-row" style="margin:0">
        <a class="btn btn-secondary" href="emploi-du-temps.html">Emploi du temps</a>
        <a class="btn btn-secondary" href="quiz/index.html">Quiz notés</a>
        <button class="btn btn-ghost" type="button" id="espace-logout">Se déconnecter</button>
      </div>
    </div>

    <div class="espace-grid">
      <div class="espace-stat"><div class="n" id="espace-visited">0</div><div class="l">catégories lues</div></div>
      <div class="espace-stat"><div class="n" id="espace-quizzes">0</div><div class="l">quiz enregistrés</div></div>
      <div class="espace-stat"><div class="n" id="espace-cours">0</div><div class="l">séances suivies</div></div>
      <div class="espace-stat"><div class="n" id="espace-moyenne">—</div><div class="l">moyenne des quiz</div></div>
    </div>

    <h2 class="section-title" style="font-size:1.25rem">Notes de quiz</h2>
    <p class="section-desc">Le meilleur score de chaque épreuve est conservé. Les quiz des cours de 50 minutes
    apparaissent aussi ici.</p>
    <div class="compte-card" style="padding:0.4rem 1rem 0.8rem;margin-bottom:1.6rem">
      <table class="notes-table">
        <thead><tr><th>Épreuve</th><th>Source</th><th>Score</th><th>Sur 20</th></tr></thead>
        <tbody id="espace-grades"></tbody>
      </table>
    </div>

    <h2 class="section-title" style="font-size:1.25rem">Carnet de notes</h2>
    <p class="section-desc">Une note par séance ou par thème, enregistrée avec le compte.</p>
    <form id="espace-note-form" class="compte-form compte-card" style="margin-bottom:1.2rem">
      <label>Identifiant de séance ou de thème
        <input type="text" name="courseId" maxlength="80" placeholder="ex. s01 ou 03-cognitive" required>
      </label>
      <label>Titre
        <input type="text" name="title" maxlength="120" placeholder="Titre facultatif">
      </label>
      <label>Texte
        <textarea name="body" required maxlength="50000" placeholder="Ce que tu retiens du cours…"></textarea>
      </label>
      <button class="btn btn-primary" type="submit">Enregistrer la note</button>
    </form>
    <div id="espace-notes"></div>
  </div>
</div>
"""
    _write("espace.html", page_shell(
        "Espace étudiant", body, depth=0,
        body_attrs='data-compte-page="espace"',
        description="Espace étudiant : progression, notes de quiz et carnet de cours enregistrés.",
    ))


def render_all():
    render_compte()
    render_espace()
    return 2


if __name__ == "__main__":
    print(render_all(), "pages compte")
