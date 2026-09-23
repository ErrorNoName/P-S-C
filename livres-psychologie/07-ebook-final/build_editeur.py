# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Cahier : éditeur relié au Drive Google."""

import os

from shell import asset, page_shell

BASE = os.path.dirname(os.path.abspath(__file__))


def render():
    body = """
<div class="cahier" id="cahier-app">
  <div class="cahier-gate" id="cahier-gate">
    <div class="cahier-gate-card">
      <p class="cahier-kicker">Cahier</p>
      <h1>Écrire avec ton compte Google</h1>
      <p id="cahier-gate-text">Le cahier enregistre tes textes dans Google Drive. Il faut un compte Google connecté à Psyclopédia.</p>
      <div id="cahier-google"></div>
      <p id="cahier-gate-msg" class="cahier-msg" hidden></p>
    </div>
  </div>
  <div class="cahier-work" id="cahier-work" hidden>
    <aside class="cahier-side" id="cahier-side">
      <div class="cahier-side-head">
        <strong>Tes cahiers</strong>
        <button type="button" class="cahier-textbtn" id="cahier-side-close">Fermer</button>
      </div>
      <div class="cahier-side-actions">
        <button type="button" class="btn btn-primary" id="cahier-new">Nouveau</button>
        <button type="button" class="btn btn-secondary" id="cahier-import">Importer .docx</button>
        <input type="file" id="cahier-file" accept=".docx,application/vnd.openxmlformats-officedocument.wordprocessingml.document" hidden>
      </div>
      <ul class="cahier-list" id="cahier-list"></ul>
      <p class="cahier-sync" id="cahier-sync">Connexion à Drive…</p>
    </aside>
    <div class="cahier-editor">
      <div class="cahier-mobilebar">
        <button type="button" class="btn btn-secondary" id="cahier-side-open">Cahiers</button>
        <span id="cahier-sync-mobile"></span>
      </div>
      <div class="cahier-toolbar" role="toolbar" aria-label="Mise en forme">
        <button type="button" data-cmd="bold" title="Gras"><b>G</b></button>
        <button type="button" data-cmd="italic" title="Italique"><i>I</i></button>
        <button type="button" data-cmd="underline" title="Souligné"><u>S</u></button>
        <button type="button" data-cmd="strikeThrough" title="Barré"><s>B</s></button>
        <label class="cahier-size">Taille
          <select id="cahier-size" aria-label="Taille du texte">
            <option value="2">Petit</option>
            <option value="3" selected>Normal</option>
            <option value="4">Grand</option>
            <option value="5">Titre</option>
            <option value="6">Très grand</option>
          </select>
        </label>
        <button type="button" data-cmd="justifyLeft" title="Aligner à gauche">Gauche</button>
        <button type="button" data-cmd="justifyCenter" title="Centrer">Centre</button>
        <button type="button" data-cmd="justifyRight" title="Aligner à droite">Droite</button>
        <button type="button" data-cmd="justifyFull" title="Justifier">Justifier</button>
        <button type="button" data-cmd="insertUnorderedList" title="Liste">Liste</button>
        <button type="button" data-cmd="insertOrderedList" title="Liste numérotée">1.</button>
        <button type="button" data-cmd="hiliteColor" title="Surligner">Surligner</button>
        <button type="button" data-block="h2" title="Intertitre">Intertitre</button>
        <button type="button" data-block="blockquote" title="Citation">Citation</button>
        <button type="button" data-cmd="undo" title="Annuler">Annuler</button>
        <button type="button" data-cmd="redo" title="Rétablir">Rétablir</button>
        <button type="button" id="cahier-export" title="Télécharger un .docx">.docx</button>
        <button type="button" id="cahier-listen" aria-pressed="false" title="Écoute continue : propose une fiche Psyclopédia quand un terme est reconnu">Écoute</button>
        <button type="button" class="cahier-danger" id="cahier-delete" title="Mettre ce cahier à la corbeille">Supprimer</button>
      </div>
      <div class="cahier-sheet">
        <label class="cahier-title-label">Titre
          <input id="cahier-title" maxlength="140" placeholder="Titre du cahier" autocomplete="off">
        </label>
        <div id="cahier-body" class="cahier-body" contenteditable="true" role="textbox" aria-multiline="true" spellcheck="true" data-placeholder="Écris ici. Le micro sous le curseur pose une note orale."></div>
      </div>
      <div class="cahier-status">
        <span id="cahier-words">0 mot</span>
        <span id="cahier-save">Brouillon</span>
      </div>
    </div>
  </div>
  <button type="button" id="cahier-mic" class="cahier-mic" hidden aria-label="Enregistrer une note orale sous le curseur">
    <span class="cahier-mic-dot" aria-hidden="true"></span>
    <span id="cahier-mic-label">Note orale</span>
  </button>
  <div id="cahier-pop" class="voix-menu" hidden role="dialog" aria-label="Note orale"></div>
  <aside id="cahier-suggest" class="cahier-suggest" hidden></aside>
</div>
"""
    css = asset(0, "css/editeur.css")
    scripts = (
        f'<script src="{asset(0, "js/editeur-format.js")}"></script>\n'
        f'<script src="{asset(0, "js/editeur.js")}"></script>'
    )
    html = page_shell(
        "Cahier",
        body,
        depth=0,
        active="Cahier",
        description="Cahier Psyclopédia : éditeur de texte relié à Google Drive, notes orales au curseur et suggestions de fiches.",
        extra_head=f'<link rel="stylesheet" href="{css}">',
        extra_scripts=scripts,
        body_attrs='data-compte-page="cahier"',
    )
    path = os.path.join(BASE, "cahier.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path


if __name__ == "__main__":
    print(render())
