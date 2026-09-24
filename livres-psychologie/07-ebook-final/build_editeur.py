# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Cahier : éditeur local, Drive facultatif, dictée et notes orales."""

import os

from shell import asset, page_shell

BASE = os.path.dirname(os.path.abspath(__file__))


def render():
    body = """
<div class="cahier" id="cahier-app">
  <section class="cahier-home" id="cahier-home">
    <header class="cahier-home-head">
      <div>
        <p class="cahier-kicker">Cahiers</p>
        <h1>Toutes les notes</h1>
        <p class="cahier-lead">Choisis une note, ou importe un document. Rien ne s'ouvre tout seul.</p>
      </div>
      <div class="cahier-home-actions">
        <button type="button" class="btn btn-primary" id="cahier-new">Nouvelle note</button>
        <button type="button" class="btn btn-secondary" id="cahier-import">Importer .docx</button>
        <button type="button" class="btn btn-secondary" id="cahier-gdoc">Google Doc</button>
        <button type="button" class="btn btn-secondary" id="cahier-drive">Relier Drive</button>
        <input type="file" id="cahier-file" accept=".docx,application/vnd.openxmlformats-officedocument.wordprocessingml.document" hidden>
      </div>
    </header>
    <form class="gdoc-box" id="gdoc-box" hidden>
      <label>Lien du Google Doc
        <input id="gdoc-url" type="url" placeholder="https://docs.google.com/document/d/…" autocomplete="off">
      </label>
      <button type="submit" class="btn btn-primary" id="gdoc-go">Afficher dans le cahier</button>
      <p class="cahier-lead">Le document est lu puis affiché ici. S'il refuse, dans Google Docs : Fichier, Télécharger, Microsoft Word, puis Importer .docx.</p>
    </form>
    <p id="cahier-drive-msg" class="cahier-msg" hidden></p>
    <p class="cahier-sync" id="cahier-sync">Enregistré sur cet appareil. Google Drive est facultatif.</p>
    <div class="cahier-grid" id="cahier-grid"></div>
  </section>
  <div class="cahier-work" id="cahier-work" hidden>
    <aside class="cahier-side" id="cahier-side">
      <div class="cahier-side-head">
        <strong>Tes cahiers</strong>
        <button type="button" class="cahier-textbtn" id="cahier-side-close">Fermer</button>
      </div>
      <div class="cahier-side-actions">
        <button type="button" class="btn btn-secondary" id="cahier-all">Toutes les notes</button>
      </div>
      <ul class="cahier-list" id="cahier-list"></ul>
    </aside>
    <div class="cahier-editor">
      <div class="cahier-mobilebar">
        <button type="button" class="btn btn-secondary" id="cahier-side-open">Toutes les notes</button>
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
        <button type="button" id="rec-open" title="Ouvrir l'enregistrement constant">Enregistrer</button>
        <button type="button" id="cahier-dictate" aria-pressed="false" title="Écrit dans le cahier, en direct, ce qui est dit">Dicter</button>
        <button type="button" id="cahier-listen" aria-pressed="false" title="Écoute continue : propose une fiche Psyclopédia quand un terme est reconnu">Écoute</button>
        <button type="button" class="cahier-danger" id="cahier-delete" title="Mettre ce cahier à la corbeille">Supprimer</button>
      </div>
      <div id="cahier-live" class="cahier-live" hidden>
        <span class="cahier-live-k">En direct</span>
        <span id="cahier-live-text"></span>
      </div>
      <div class="cahier-sheet">
        <label class="cahier-title-label">Titre
          <input id="cahier-title" maxlength="140" placeholder="Titre du cahier" autocomplete="off">
        </label>
        <div id="cahier-body" class="cahier-body" contenteditable="true" role="textbox" aria-multiline="true" spellcheck="true" data-placeholder="Écris ici, ou dicte. Le micro sous le curseur pose une note orale."></div>
      </div>
      <div class="cahier-status">
        <span id="cahier-words">0 mot</span>
        <span id="cahier-save">Brouillon</span>
      </div>
      <div class="rec-layer" id="rec-const" hidden>
        <div class="rec-card" role="dialog" aria-label="Enregistrement constant">
          <div class="rec-head">
            <p class="rec-kicker">Enregistreur</p>
            <button type="button" id="rec-dismiss" aria-label="Fermer">Fermer</button>
          </div>
          <p class="rec-warn" id="rec-warn">Pendant la séance, la note orale, la dictée et l'écoute restent grisées.</p>
          <p class="rec-time" id="rec-time">00:00:00</p>
          <div class="rec-meter" aria-hidden="true"><i id="rec-level"></i></div>
          <div class="rec-actions">
            <button type="button" class="rec-go" id="rec-go" aria-pressed="false">Lancer</button>
            <button type="button" id="rec-pause" disabled>Pause</button>
            <button type="button" id="rec-stop" disabled>Stop</button>
          </div>
          <div class="rec-modes" role="radiogroup" aria-label="Clarté du micro">
            <button type="button" data-reel="vocal" aria-pressed="true">Point vocal</button>
            <button type="button" data-reel="normal" aria-pressed="false">Normal</button>
            <button type="button" data-reel="room" aria-pressed="false">Environnement</button>
          </div>
          <p class="rec-live" id="rec-live">La transcription s'écrit ici pendant la séance.</p>
          <ul class="rec-cache" id="rec-cache"></ul>
        </div>
        <div class="rec-view" id="rec-view" hidden>
          <div class="rec-view-card">
            <p class="rec-kicker" id="rec-view-title">Transcription</p>
            <audio id="rec-player" controls preload="none"></audio>
            <pre id="rec-script"></pre>
            <div class="rec-actions">
              <button type="button" id="rec-txt">TXT</button>
              <button type="button" id="rec-mp3">MP3</button>
              <button type="button" id="rec-close">Fermer</button>
            </div>
          </div>
        </div>
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
    css = asset(0, "css/editeur.css") + "?v=float7"
    scripts = (
        f'<script src="{asset(0, "js/lame.min.js")}?v=float7"></script>\n'
        f'<script src="{asset(0, "js/editeur-format.js")}?v=float7"></script>\n'
        f'<script src="{asset(0, "js/editeur.js")}?v=float7"></script>'
    )
    html = page_shell(
        "Cahier",
        body,
        depth=0,
        active="Cahier",
        description="Cahier Psyclopédia : éditeur sur cet appareil, dictée en direct, notes orales et, si tu le veux, copie dans Google Drive.",
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
