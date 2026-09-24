# -*- coding: utf-8 -*-
"""Essai visuel : menu et deux index. Ne remplace pas le site."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EB = "../livres-psychologie/07-ebook-final/"

GROUPS = [
    ("Lire", [
        ("index.html", "oeil-bleu.png", "Accueil", "home"),
        ("categories.html", "cerveau-petit.png", "Catégories", "cats"),
        (EB + "decouverte.html", "iris.png", "Découverte", ""),
        (EB + "references/index.html", "livres.png", "Références", ""),
        (EB + "bibliotheque.html", "livre.png", "Bibliothèque", ""),
    ]),
    ("Étudier", [
        (EB + "emploi-du-temps.html", "horloge.png", "Cours", ""),
        (EB + "apprendre.html", "stylo.png", "Apprendre", ""),
        (EB + "cahier.html", "machine.png", "Cahier", ""),
        (EB + "quiz/index.html", "trophee.png", "Quiz", ""),
        (EB + "methodes.html", "loupe.png", "Méthodes", ""),
    ]),
    ("Autour", [
        (EB + "pratique.html", "mains.png", "Pratique", ""),
        (EB + "aide.html", "coeur.png", "Aide", ""),
        (EB + "compte.html", "tete.png", "Compte", ""),
        ("https://discord.gg/sX3TAqH4pD", "voix.png", "Discord", "ext"),
        (EB + "rappels.html", "soleil.png", "Rappels", ""),
    ]),
]

CATS = [
    ("Socles de la discipline", "loupe.png", "Méthode, histoire, pensée, groupe.", [
        ("01-fondamentaux", "loupe.png", "Fondamentaux et méthodes", "Qu'est-ce que la psychologie, et comment on l'étudie."),
        ("02-histoire", "time.png", "Histoire et grands courants", "De la philosophie antique à la science de l'esprit."),
        ("03-cognitive", "memoire.png", "Psychologie cognitive", "Percevoir, mémoriser, raisonner."),
        ("04-sociale", "lien.png", "Psychologie sociale", "Ce que le groupe fait à la pensée et à l'action."),
    ]),
    ("La personne", "cerveau.png", "Développement, personnalité, émotions, cerveau.", [
        ("05-developpement", "croissance.png", "Développement", "De la petite enfance au grand âge."),
        ("06-personnalite", "tete.png", "Personnalité", "Traits, intelligence, volonté."),
        ("07-emotions", "coeur.png", "Émotions et motivation", "Ressentir, désirer, agir."),
        ("08-neurosciences", "cerveau-petit.png", "Neurosciences", "Le cerveau au service de l'esprit."),
    ]),
    ("Souffrance et soin", "pince.png", "Comprendre sans stigmatiser.", [
        ("09-psychopathologie", "pince.png", "Psychopathologie", "La souffrance psychique, sans étiquette facile."),
        ("10-therapies", "mains.png", "Thérapies", "Les grandes façons de soigner l'esprit."),
    ]),
    ("La vie quotidienne", "soleil.png", "Bien-être, travail, école, santé, justice, animal.", [
        ("11-positive", "soleil.png", "Psychologie positive", "La science du bien vivre."),
        ("12-travail", "ordi.png", "Travail et organisations", "Motivation et vie au travail."),
        ("13-education", "stylo.png", "Éducation", "Comment on apprend vraiment."),
        ("14-sante", "coeur-rouge.png", "Santé", "Corps, stress et maladie."),
        ("15-legale", "globe.png", "Psychologie légale", "Témoignage, crime, expertise."),
        ("16-comparee", "colibri.png", "Psychologie comparée", "Ce que les animaux montrent de l'esprit."),
    ]),
    ("Frontières", "papillon.png", "Culture, langage, mesure, écrans, âge, politique.", [
        ("17-interculturelle", "globe.png", "Interculturel", "Universel et culturel."),
        ("18-langage", "parole.png", "Langage", "Parler, comprendre, apprendre une langue."),
        ("19-psychometrie", "loupe.png", "Psychométrie", "Mesurer l'invisible."),
        ("20-sport", "trophee.png", "Sport", "Préparation mentale et pression."),
        ("21-consommation", "livre.png", "Consommation", "Décider, acheter, être influencé."),
        ("22-numerique", "ecran.png", "Numérique", "Écrans, attention, réseaux."),
        ("23-evolutionniste", "papillon.png", "Évolution", "Pourquoi l'esprit a cette forme."),
        ("24-vieillissement", "lune.png", "Vieillissement", "Ce qui tient, ce qui change."),
        ("25-environnementale", "colibri.png", "Environnement", "Lieux, nature, éco-anxiété."),
        ("26-politique", "voix.png", "Politique et croyances", "Idées, polarisation, esprit critique."),
        ("27-science-psychologique", "oeil.png", "Science psychologique", "Ce que les tests du cerveau permettent vraiment."),
    ]),
]


def icon(name):
    return '<img src="stickers/%s" alt="">' % name


def nav(active):
    groups = []
    for title, links in GROUPS:
        bits = []
        for href, img, label, flag in links:
            extra = ""
            if flag == "ext":
                extra = ' target="_blank" rel="noopener"'
            cls = ' class="is-on"' if flag == active else ""
            bits.append('<a href="%s"%s%s>%s%s</a>' % (href, cls, extra, icon(img), label))
        groups.append('<div class="nav-group"><p>%s</p>%s</div>' % (title, "".join(bits)))
    return """<div class="banner">Essai de mise en page. Le site actuel reste en place. <a href="../index.html">Revenir à l'accueil publié</a></div>
<header class="desk">
  <div class="desk-bar">
    <a class="mark" href="index.html">%s<span>Psyclopédia</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="sheet">Menu</button>
    <div class="desk-tools">
      <button class="tool" type="button" data-search-open="">%s<span class="long">Rechercher</span></button>
      <a class="tool" href="%scompte.html">%s<span class="long">Compte</span></a>
    </div>
  </div>
  <nav class="sheet" id="sheet">%s</nav>
</header>""" % (icon("oeil-bleu.png"), icon("loupe.png"), EB, icon("tete.png"), "".join(groups))


def page(name, title, active, body):
    html = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — essai Psyclopédia</title>
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,620&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="collage.css">
</head>
<body data-root="../">
%s
<main class="wrap">
%s
</main>
<p class="foot">Essai visuel à valider avant de l'étendre au reste de Psyclopédia. Les textes restent ceux du site. Les images sont des découpes du pack de collages. <a href="../index.html">Site actuel</a></p>
<script>
document.querySelector(".menu-btn").addEventListener("click", function (e) {
  var sheet = document.getElementById("sheet");
  var open = sheet.classList.toggle("is-open");
  e.currentTarget.setAttribute("aria-expanded", open ? "true" : "false");
});
</script>
<script src="../assets-ebook/js/search.js"></script>
</body>
</html>
""" % (title, nav(active), body)
    path = os.path.join(HERE, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)


def home():
    doors = [
        (EB + "parcours.html", "livre.png", "Parcours", "Un itinéraire, pas toute la bibliothèque d'un coup."),
        ("categories.html", "cerveau-petit.png", "Catégories", "Les 27 domaines, rangés par questions."),
        (EB + "emploi-du-temps.html", "horloge.png", "Cours", "Le calendrier et les séances."),
        (EB + "cahier.html", "machine.png", "Cahier", "Écrire, dicter, garder une note."),
    ]
    door_html = "".join(
        '<a class="door" href="%s">%s<strong>%s</strong><span>%s</span></a>' % (h, icon(i), t, d)
        for h, i, t, d in doors
    )
    tools = [
        (EB + "references/courants.html", "time.png", "Courants", "Chaque école naît d'une objection."),
        (EB + "references/mythes.html", "oeil.png", "Idées reçues", "Ce que les données disent vraiment."),
        (EB + "faq.html", "parole.png", "Questions", "Des réponses qui disent aussi l'inconnu."),
        (EB + "laboratoire.html", "camera.png", "Laboratoire", "Expériences à faire dans le navigateur."),
        (EB + "bibliotheque.html", "livres.png", "Bibliothèque", "Livres du domaine public."),
        (EB + "aide.html", "mains.png", "Aide", "Où s'adresser, sans se substituer à un soin."),
    ]
    tool_html = "".join(
        '<a href="%s">%s<div><strong>%s</strong><br><small>%s</small></div></a>' % (h, icon(i), t, d)
        for h, i, t, d in tools
    )
    shorts = [
        ("03-cognitive", "memoire.png", "Cognitive"),
        ("04-sociale", "lien.png", "Sociale"),
        ("08-neurosciences", "cerveau-petit.png", "Neurosciences"),
        ("09-psychopathologie", "pince.png", "Clinique"),
        ("07-emotions", "coeur.png", "Émotions"),
        ("27-science-psychologique", "oeil.png", "Science"),
    ]
    short_html = "".join(
        '<a class="cat" href="%scategories/%s.html">%s<div><strong>%s</strong></div></a>' % (EB, slug, icon(img), label)
        for slug, img, label in shorts
    )
    body = """
<section class="hero">
  <div>
    <p class="kicker">Encyclopédie de psychologie</p>
    <h1>Lire l'esprit sans se perdre dans les tiroirs.</h1>
    <p class="lede">Vingt-sept domaines, les cours, le cahier et les livres. Le collage montre le sujet. Le texte reste au premier plan.</p>
    <div class="actions">
      <a class="btn btn-main" href="categories.html">%sVoir les catégories</a>
      <a class="btn btn-ghost" href="%sparcours.html">%sCommencer un parcours</a>
      <a class="btn btn-ghost" href="%scahier.html">%sOuvrir le cahier</a>
    </div>
  </div>
  <div class="stage" aria-hidden="true">
    <img class="s-eye" src="stickers/oeil.png" alt="">
    <img class="s-heart" src="stickers/coeur.png" alt="">
    <img class="s-brain" src="stickers/cerveau.png" alt="">
    <img class="s-sun" src="stickers/soleil.png" alt="">
    <img class="s-moon" src="stickers/lune.png" alt="">
  </div>
</section>
<div class="doors">%s</div>
<div class="block">%s<div><h2>Domaines proches</h2><p>Six portes, pas vingt-sept d'un coup.</p></div></div>
<div class="cats">%s</div>
<div class="block">%s<div><h2>Le cabinet</h2><p>Autour des chapitres : histoire, doutes, expériences, livres.</p></div></div>
<div class="cabinet">%s</div>
""" % (
        icon("cerveau-petit.png"), EB, icon("livre.png"), EB, icon("machine.png"),
        door_html, icon("lien.png"), short_html, icon("livres.png"), tool_html,
    )
    page("index.html", "Accueil", "home", body)


def categories():
    chunks = []
    for title, img, desc, items in CATS:
        cards = []
        for slug, cimg, label, text in items:
            cards.append(
                '<a class="cat" href="%scategories/%s.html">%s<div><strong>%s</strong><span>%s</span></div></a>'
                % (EB, slug, icon(cimg), label, text)
            )
        chunks.append(
            '<div class="block">%s<div><h2>%s</h2><p>%s</p></div></div><div class="cats">%s</div>'
            % (icon(img), title, desc, "".join(cards))
        )
    body = """
<p class="kicker">Index</p>
<h1>Les catégories, par questions.</h1>
<p class="lede">Le même sommaire que le site, sans pastilles ni symboles. Chaque image indique le sujet du domaine.</p>
""" + "".join(chunks)
    page("categories.html", "Catégories", "cats", body)


if __name__ == "__main__":
    home()
    categories()
    print("apercu ok")
