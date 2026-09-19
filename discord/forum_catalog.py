# -*- coding: utf-8 -*-
"""Catalogue des fils de forum : données Psyclopédia + ressources ouvertes.

Chaque entrée : forum, titre (≤ 100), tags (noms), embeds, éventuellement épinglé.
Aucun secret ici. Les textes viennent des modules du site.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

from blueprint import APP, COLOR_GRIS, COLOR_OR, COLOR_ROSE, COLOR_VERT, LINKS, SITE
from embeds import FOOTER

EBOOK = Path(__file__).resolve().parents[1] / "livres-psychologie" / "07-ebook-final"
if str(EBOOK) not in sys.path:
    sys.path.insert(0, str(EBOOK))

from content import BOOKS  # noqa: E402
from data_auteurs import AUTEURS  # noqa: E402
from data_cas import CAS  # noqa: E402
from data_categories import CATEGORIES  # noqa: E402
from data_categories_plus import CATEGORIES_PLUS  # noqa: E402
from data_cours import ANNEE, get_cours, get_modules  # noqa: E402
from data_experiences import EXPERIENCES  # noqa: E402
from data_glossaire import GLOSSAIRE_PLUS  # noqa: E402
from data_mythes import MYTHES  # noqa: E402
from data_theories import THEORIES  # noqa: E402

SEP = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"


def _strip(text, limit=900):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[: limit - 1].rsplit(" ", 1)[0] + "…"
    return text


def _embed(title, description, color=COLOR_VERT, fields=None, url=None):
    payload = {
        "title": title[:256],
        "description": description[:4096],
        "color": color,
        "footer": {"text": FOOTER},
    }
    if url:
        payload["url"] = url
    if fields:
        payload["fields"] = [
            {"name": n[:256], "value": v[:1024], "inline": inline}
            for n, v, inline in fields
        ]
    return payload


def _thread(forum, title, tags, embeds, pin=False):
    return {
        "forum": forum,
        "title": title[:100],
        "tags": tags,
        "embeds": embeds,
        "pin": pin,
    }


def _cat_tag(cat_id):
    mapping = {
        "01": "Méthodes",
        "02": "Histoire",
        "03": "Cognitive",
        "04": "Sociale",
        "05": "Sociale",
        "06": "Méthodes",
        "07": "Cognitive",
        "08": "Neurosciences",
        "09": "Psychopatho",
        "10": "Psychopatho",
        "11": "Santé",
        "12": "Appliquée",
        "13": "Appliquée",
        "14": "Santé",
        "15": "Appliquée",
        "16": "Neurosciences",
        "17": "Sociale",
        "18": "Cognitive",
        "19": "Méthodes",
        "20": "Appliquée",
        "21": "Appliquée",
        "22": "Appliquée",
        "23": "Neurosciences",
        "24": "Santé",
        "25": "Appliquée",
        "26": "Sociale",
    }
    return mapping.get(cat_id[:2], "Méthodes")


def _page(path):
    return f"{APP}/{path}"


def _fiches():
    rows = []
    for cat in list(CATEGORIES) + list(CATEGORIES_PLUS):
        objectives = cat.get("objectives") or []
        fact = _strip(cat.get("fun_fact") or cat.get("subtitle") or "", 280)
        rows.append(_thread(
            "fiches_synthese",
            f"{cat['icon']} {cat['title']}",
            [_cat_tag(cat["id"])],
            [_embed(
                f"{cat['icon']} {cat['title']}",
                "\n".join([
                    f"{SEP}",
                    f"**{cat['subtitle']}**",
                    "",
                    fact,
                    f"{SEP}",
                    "Objectifs de la fiche :",
                    *[f"• {o}" for o in objectives[:4]],
                    "",
                    f"Lire : {_page('fiches/' + cat['id'] + '.html')}",
                    f"Catégorie : {_page('categories/' + cat['id'] + '.html')}",
                ]),
                COLOR_VERT,
                url=_page(f"fiches/{cat['id']}.html"),
            )],
        ))
    return rows


def _livres():
    rows = []
    author_tag = {
        "William James": "James",
        "Pierre Janet": "Janet",
        "Théodule Ribot": "Ribot",
    }
    for book in BOOKS:
        tags = ["Domaine public", "À lire"]
        if book["author"] in author_tag:
            tags.append(author_tag[book["author"]])
        href = f"{APP}/lecteur.html"
        rows.append(_thread(
            "livres_dp",
            f"{book['icon']} {book['title']} — {book['author']}",
            tags,
            [_embed(
                book["title"],
                "\n".join([
                    f"**{book['author']} · {book['year']}** — {book['pages']}",
                    f"Champ : {book['cat']}",
                    "",
                    book["desc"],
                    "",
                    "Ouvrage du **domaine public**, lisible dans le lecteur du site "
                    "(modernisation du français, OCR si besoin).",
                    f"Bibliothèque : {LINKS['bibliotheque']}",
                ]),
                COLOR_OR,
                url=href,
                fields=[("Fichier", book["path"], False)],
            )],
        ))
    return rows


def _cliniques():
    rows = []
    for cid, nom, periode, domaine, resume, histoire, apport, aujourdhui in CAS:
        rows.append(_thread(
            "fiches_cliniques",
            f"{nom} ({periode})",
            ["Cas historique", "Pédagogique", "Pas un diagnostic"],
            [_embed(
                nom,
                "\n".join([
                    f"**{periode} · {domaine}**",
                    "",
                    f"*{resume}*",
                    "",
                    "**Ce que le cas a fait comprendre**",
                    _strip(apport, 500),
                    "",
                    "Cadre pédagogique uniquement — pas un diagnostic, pas un soin.",
                ]),
                COLOR_ROSE,
                url=_page(f"references/cas.html#{cid}"),
                fields=[
                    ("Récit", _strip(histoire, 900), False),
                    ("Aujourd'hui", _strip(aujourdhui, 700), False),
                ],
            )],
        ))
    return rows


def _citations():
    rows = []
    for auteur in AUTEURS[:24]:
        aid, nom, dates, pays, courant, apport, _bio, citation, oeuvres = auteur
        rows.append(_thread(
            "citations",
            f"« {citation[:70]}… »" if len(citation) > 72 else f"« {citation} »",
            ["Classique", "Source"],
            [_embed(
                nom,
                "\n".join([
                    f"**« {citation} »**",
                    "",
                    f"{nom} ({dates}, {pays}) — *{courant}*",
                    "",
                    _strip(apport, 400),
                    "",
                    f"Œuvres : {oeuvres}",
                ]),
                COLOR_GRIS,
                url=_page(f"references/auteurs.html#{aid}"),
            )],
        ))
    return rows


GLOSSAIRE_CLE = {
    "Mémoire de travail", "Mémoire épisodique", "Mémoire procédurale",
    "Chunking", "Consolidation", "Aléatorisation", "Double aveugle",
    "Taille d'effet", "Méta-analyse", "P-hacking", "Falsifiabilité",
    "Consentement éclairé", "Validité écologique", "Désirabilité sociale",
    "Préenregistrement", "Réplication directe", "Variable confondue",
    "Puissance statistique", "Opérationnalisation", "HARKing",
    "Biais de publication", "Étude longitudinale", "Reconsolidation",
    "Mémoire sémantique",
}


def _glossaire():
    rows = []
    for terme, definition, cat in GLOSSAIRE_PLUS:
        if terme not in GLOSSAIRE_CLE:
            continue
        rows.append(_thread(
            "glossaire",
            terme,
            ["Définition", "À retenir"],
            [_embed(
                terme,
                f"{definition}\n\nCatégorie liée : `{cat}`\nDictionnaire : {LINKS['dictionnaire']}",
                COLOR_VERT,
                url=LINKS["dictionnaire"],
            )],
        ))
    return rows


def _revision():
    rows = []
    cours = get_cours()
    by_mod = {}
    for item in cours:
        by_mod.setdefault(item["module"], []).append(item)
    for module in get_modules(cours):
        items = by_mod[module]
        lines = [
            f"**Module · {module}** — {len(items)} séance(s) de {ANNEE['duration_min']} min",
            f"Année {ANNEE['id']} · CM {ANNEE['cm_time']} · TD {ANNEE['td_time']} · {ANNEE['tz']}",
            "",
        ]
        for item in items[:8]:
            lines.append(f"• **{item['kind']} S{item['week']:02d}** — {item['title']}")
        lines += [
            "",
            f"Emploi du temps : {LINKS['cours']}",
            f"Archives : {LINKS['archives']}",
            f"Révision SM-2 : {LINKS['revision']}",
        ]
        rows.append(_thread(
            "forum_revision",
            f"Module — {module}",
            ["Licence", "Synthèse"],
            [_embed(f"Révision · {module}", "\n".join(lines), COLOR_OR, url=LINKS["cours"])],
        ))
    return rows


def _niveaux():
    starters = [
        ("L1", "1️⃣", "Licence 1 : se repérer dans les fondamentaux, l'histoire et les méthodes."),
        ("L2", "2️⃣", "Licence 2 : cognitive, sociale, développement — relier cours et fiches."),
        ("L3", "3️⃣", "Licence 3 : clinique pédagogique, stats, préparation des oraux."),
        ("M1", "4️⃣", "Master 1 : lecture d'articles, mémoire, méthodologie avancée."),
        ("M2", "5️⃣", "Master 2 : spécialisation, stages, écriture scientifique."),
        ("Autodidacte", "🌱", "Hors cursus universitaire : parcours guidés et emploi du temps libre."),
    ]
    rows = []
    for name, _emoji, blurb in starters:
        rows.append(_thread(
            "entraide_niveaux",
            f"Point d'entrée {name}",
            [name, "Posé"],
            [_embed(
                f"Entraide {name}",
                "\n".join([
                    blurb,
                    "",
                    "Ouvrez **votre** fil pour une question précise : ce que vous avez lu, où vous bloquez.",
                    "On n'écrit pas les copies. On aide à structurer.",
                    "",
                    f"{LINKS['apprendre']} · {LINKS['methodes']} · {LINKS['parcours']}",
                ]),
                COLOR_OR,
            )],
        ))
    return rows


def _socle():
    rows = []
    for auteur in AUTEURS[:12]:
        aid, nom, dates, pays, courant, apport, bio, _cit, oeuvres = auteur
        rows.append(_thread(
            "socle",
            f"{nom} — {courant}",
            ["Auteur", "Histoire"],
            [_embed(
                nom,
                "\n".join([
                    f"**{dates} · {pays}**",
                    f"*{courant}*",
                    "",
                    _strip(apport, 350),
                    "",
                    _strip(bio, 600),
                    "",
                    f"Œuvres : {oeuvres}",
                ]),
                COLOR_GRIS,
                url=_page(f"references/auteurs.html#{aid}"),
            )],
        ))
    rows.append(_thread(
        "socle",
        "1879 — Leipzig et la naissance du laboratoire",
        ["Histoire", "Courant"],
        [_embed(
            "Le laboratoire de Wundt",
            "En 1879, Wilhelm Wundt ouvre à Leipzig le premier laboratoire dédié à "
            "la psychologie expérimentale. La discipline se sépare de la philosophie : "
            "temps de réaction, sensation, introspection contrôlée.\n\n"
            f"Fiche histoire : {_page('categories/02-histoire.html')}\n"
            f"Chronologie : {_page('references/chronologie.html')}",
            COLOR_GRIS,
            url=_page("categories/02-histoire.html"),
        )],
    ))
    rows.append(_thread(
        "socle",
        "La tradition française : Ribot, Binet, Janet",
        ["Histoire", "Courant"],
        [_embed(
            "Une psychologie française",
            "Ribot (maladies de la mémoire et de la volonté), Binet (mesure de "
            "l'intelligence, suggestibilité), Janet (automatisme, dissociation). "
            "Trois portes d'entrée, trois livres du domaine public dans la bibliothèque.\n\n"
            f"{LINKS['bibliotheque']}",
            COLOR_GRIS,
            url=LINKS["bibliotheque"],
        )],
    ))
    return rows


def _esprit():
    rows = []
    wanted_th = {
        "conditionnement-classique", "conditionnement-operant", "memoire-atkinson",
        "stades-piaget", "apprentissage-social",
    }
    for th in THEORIES:
        if th[0] in wanted_th:
            tid, nom, auteur, annee, domaine, idee, mecanisme, application, limite = th
            rows.append(_thread(
                "esprit",
                f"{nom} ({annee})",
                ["Cognitive", "Expérience"] if "conditionnement" in tid else ["Cognitive"],
                [_embed(
                    nom,
                    f"**{auteur}, {annee} · {domaine}**\n\n{idee}\n\n"
                    f"**Mécanisme.** {_strip(mecanisme, 450)}\n\n"
                    f"**Limite.** {_strip(limite, 280)}",
                    COLOR_VERT,
                    url=_page(f"references/theories.html#{tid}"),
                    fields=[("Application", _strip(application, 400), False)],
                )],
            ))
    for exp in EXPERIENCES[:8]:
        eid, titre, chercheur, annee, _cat, resume, protocole, resultat, portee, critique = exp
        rows.append(_thread(
            "esprit",
            f"{titre} — {chercheur}",
            ["Expérience", "Cognitive"],
            [_embed(
                titre,
                f"**{chercheur}, {annee}**\n\n{resume}\n\n"
                f"**Protocole.** {_strip(protocole, 380)}\n"
                f"**Résultat.** {_strip(resultat, 320)}",
                COLOR_VERT,
                url=_page(f"references/experiences.html#{eid}"),
                fields=[
                    ("Portée", _strip(portee, 400), False),
                    ("Critique", _strip(critique, 400), False),
                ],
            )],
        ))
    for mythe in MYTHES[:6]:
        mid, affirmation, famille, verdict, sait, origine, nuance = mythe
        rows.append(_thread(
            "esprit",
            f"Mythe : {affirmation.strip('«» ' )[:70]}",
            ["Neurosciences"],
            [_embed(
                affirmation,
                f"**Verdict : {verdict}** · {famille}\n\n{_strip(sait, 700)}\n\n"
                f"*Nuance.* {_strip(nuance, 280)}",
                COLOR_OR,
                url=_page(f"references/mythes.html#{mid}"),
            )],
        ))
    return rows


def _societe():
    rows = []
    wanted_exp = {
        "conformite-asch", "obeissance-milgram", "prison-stanford",
        "effet-temoin", "robbers-cave", "kitty-dissonance",
    }
    picked = []
    for exp in EXPERIENCES:
        if exp[0] in wanted_exp or (exp[4] == "04-sociale" and len(picked) < 8):
            if exp[0] in {p[0] for p in picked}:
                continue
            picked.append(exp)
        if len(picked) >= 10:
            break
    for exp in picked:
        eid, titre, chercheur, annee, _cat, resume, protocole, resultat, portee, critique = exp
        rows.append(_thread(
            "societe",
            f"{titre} — {annee}",
            ["Sociale", "Expérience"],
            [_embed(
                titre,
                f"**{chercheur}, {annee}**\n\n{resume}\n\n"
                f"{_strip(protocole, 360)}\n\n**Résultat.** {_strip(resultat, 300)}",
                COLOR_OR,
                url=_page(f"references/experiences.html#{eid}"),
                fields=[("Critique", _strip(critique, 500), False)],
            )],
        ))
    for tid in ("attachement", "zone-proximale", "stades-piaget"):
        th = next(t for t in THEORIES if t[0] == tid)
        _id, nom, auteur, annee, domaine, idee, mecanisme, application, limite = th
        rows.append(_thread(
            "societe",
            f"{nom} — {auteur}",
            ["Développement"],
            [_embed(
                nom,
                f"**{auteur}, {annee} · {domaine}**\n\n{idee}\n\n{_strip(mecanisme, 450)}\n\n"
                f"**Limite.** {_strip(limite, 260)}",
                COLOR_OR,
                url=_page(f"references/theories.html#{_id}"),
            )],
        ))
    return rows


def _clinique_forum():
    rows = [
        _thread(
            "clinique",
            "Cadre : ici on n'est pas un cabinet",
            ["Éthique", "Pédagogique"],
            [_embed(
                "Clinique pédagogique",
                "On discute des **concepts**, des **cas historiques publiés** et de l'éthique.\n"
                "On ne diagnostique personne, on ne prescrit rien.\n\n"
                f"Urgence : 15 / 112 · Suicide : 3114 · {LINKS['aide']}",
                COLOR_ROSE,
                url=LINKS["aide"],
            )],
            pin=False,
        ),
        _thread(
            "clinique",
            "Rosenhan 1973 — et ce qu'on en sait aujourd'hui",
            ["Éthique", "Cas historique"],
            [_embed(
                "On Being Sane in Insane Places",
                "L'article de Rosenhan a ébranlé la confiance dans le diagnostic psychiatrique. "
                "Une enquête de 2019 a ensuite mis en doute une partie des données. "
                "Le problème qu'il pointait (étiquetage, asiles) reste un objet d'histoire et d'éthique, "
                "pas une recette pour « tester » un service de soin.\n\n"
                f"{_page('references/cas.html#rosenhan')}",
                COLOR_ROSE,
                url=_page("references/cas.html#rosenhan"),
            )],
        ),
        _thread(
            "clinique",
            "Facteurs communs des psychothérapies",
            ["Pédagogique"],
            [_embed(
                "Ce qui se retrouve d'une approche à l'autre",
                "Alliance, attente, rituel, techniques spécifiques : la recherche sur "
                "l'efficacité des thérapies distingue ce qui est commun et ce qui est propre "
                "à un modèle. Page thérapies du site, sans prescription.\n\n"
                f"{_page('categories/10-therapies.html')}",
                COLOR_ROSE,
                url=_page("categories/10-therapies.html"),
            )],
        ),
        _thread(
            "clinique",
            "Modèle biopsychosocial",
            ["Pédagogique"],
            [_embed(
                "Corps, psychisme, milieu",
                "Engel (1977) propose de ne plus réduire la maladie à une lésion. "
                "Utile comme **grille de lecture**, pas comme diagnostic.\n\n"
                f"{_page('categories/14-sante.html')}",
                COLOR_ROSE,
                url=_page("categories/14-sante.html"),
            )],
        ),
    ]
    return rows


def _applique():
    specs = [
        ("Karasek et la demande-contrôle", "Travail", "12-travail",
         "Le stress au travail selon l'équilibre entre exigences et latitude décisionnelle."),
        ("Charge cognitive", "Éducation", "13-education",
         "Ce que la mémoire de travail peut absorber — et ce qu'un cours ne devrait pas lui demander."),
        ("Faux souvenirs et témoignage", "Légale", "15-legale",
         "Elizabeth Loftus : la mémoire du témoin n'est pas un enregistrement."),
        ("Psychologie du sport", "Sport", "20-sport",
         "Motivation, anxiété de compétition, routines — fiche site."),
        ("Attention et écrans", "Numérique", "22-numerique",
         "Notifications, défilement, renforcement à ratio variable."),
        ("WEIRD et interculturel", "Éducation", "17-interculturelle",
         "Une grande part de la psychologie a été faite sur des étudiants occidentaux."),
    ]
    rows = []
    for title, tag, slug, blurb in specs:
        rows.append(_thread(
            "applique",
            title,
            [tag],
            [_embed(
                title,
                f"{blurb}\n\n{_page('categories/' + slug + '.html')}\nMétiers : {LINKS['metiers']}",
                COLOR_VERT,
                url=_page(f"categories/{slug}.html"),
            )],
        ))
    return rows


def _articles():
    extras = [
        ("Le site Psyclopédia — carte", "Francophone",
         f"Portail, 26 catégories, fiches, références, laboratoire, quiz.\n{SITE}", SITE),
        ("Emploi du temps 2026-2027", "Francophone",
         f"60 séances × 50 min, CM lundi 10:00, TD jeudi 14:00.\n{LINKS['cours']}", LINKS["cours"]),
        ("Laboratoire interactif", "Vulgarisation",
         f"Stroop, empan, Flanker, ancrage… expériences pédagogiques en JS.\n{LINKS['labo']}", LINKS["labo"]),
        ("Idées reçues et neuromythes", "Lecture critique",
         f"10 %, cerveau gauche/droit, styles d'apprentissage…\n{_page('references/mythes.html')}",
         _page("references/mythes.html")),
        ("Grands débats", "Lecture critique",
         f"Dossiers argumentés : inné/acquis, réplication, WEIRD…\n{_page('references/debats.html')}",
         _page("references/debats.html")),
        ("Méthodes et statistiques", "Article",
         f"Causalité, taille d'effet, préenregistrement.\n{LINKS['methodes']}", LINKS["methodes"]),
        ("Page Aide et numéros", "Francophone",
         f"3114, 15, 112, 3919, 119, SOS Amitié…\n{LINKS['aide']}", LINKS["aide"]),
        ("Collège de France — sciences cognitives", "Francophone",
         "Cours ouverts de Stanislas Dehaene et d'autres chaires, en français, utilisés dans le lecteur.",
         "https://www.college-de-france.fr/fr"),
        ("Canal-U — universités francophones", "Francophone",
         "Vidéos de cours universitaires en français (psychologie, neurosciences, éducation).",
         "https://www.canal-u.tv/"),
        ("HAL — archives ouvertes", "Article",
         "Prépublications et articles francophones en accès ouvert. Toujours lire méthodes et limites.",
         "https://hal.science/"),
        ("OpenEdition — revues SHS", "Article",
         "Revues de sciences humaines et sociales en français, souvent en libre accès.",
         "https://www.openedition.org/"),
        ("Gallica — textes du domaine public", "Francophone",
         "James, Ribot, Janet, Taine, Le Bon : éditions originales numérisées par la BnF.",
         "https://gallica.bnf.fr/"),
        ("INA — archives parlées", "Vulgarisation",
         "Entretiens historiques (Piaget et d'autres) cités dans le cursus.",
         "https://www.ina.fr/"),
        ("PubMed Central", "Article",
         "Textes biomédicaux et psychologiques en accès ouvert. Anglais dominant ; vérifier l'échantillon.",
         "https://www.ncbi.nlm.nih.gov/pmc/"),
    ]
    rows = []
    for title, tag, body, url in extras:
        rows.append(_thread(
            "articles",
            title,
            [tag],
            [_embed(title, body, COLOR_OR, url=url)],
        ))
    return rows


def build_catalog():
    catalog = []
    for block in (
        _fiches, _livres, _cliniques, _citations, _glossaire,
        _revision, _niveaux, _socle, _esprit, _societe,
        _clinique_forum, _applique, _articles,
    ):
        catalog.extend(block())
    return catalog


def validate_catalog(catalog=None):
    catalog = catalog or build_catalog()
    errors = []
    for item in catalog:
        if len(item["title"]) > 100:
            errors.append(f"title {item['title'][:40]!r}")
        for embed in item["embeds"]:
            if len(embed.get("description") or "") > 4096:
                errors.append(f"desc {item['title']!r}")
            for field in embed.get("fields") or []:
                if len(field["value"]) > 1024:
                    errors.append(f"field {item['title']!r} {field['name']}")
    return errors
