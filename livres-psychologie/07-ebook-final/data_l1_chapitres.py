# -*- coding: utf-8 -*-
"""Chapitres de licence intégrés aux fiches de catégorie.

Synthèse originale pour Psyclopédia. Les plans de cours et les articles
servent de fil ; ils ne sont pas recopiés. Aucun diagnostic, aucun conseil
de soin. Le titre de psychologue reste un diplôme, pas une page web.
"""


def _table(headers, rows):
    head = "".join(
        f"<th style='padding:0.5rem;text-align:left'>{cell}</th>" for cell in headers
    )
    body = ""
    for row in rows:
        cells = "".join(
            "<td style='padding:0.5rem;border-bottom:1px solid var(--border)'>"
            f"{cell}</td>"
            for cell in row
        )
        body += f"<tr>{cells}</tr>"
    return (
        "<table style='width:100%;border-collapse:collapse;margin:1rem 0;font-size:0.9rem'>"
        f"<tr style='background:var(--gris-light)'>{head}</tr>{body}</table>"
    )


L1_EXTRA = {
    "01-fondamentaux": {
        "objectives": [
            "Dire ce qui rend une démarche systématique, précise et communicable",
            "Distinguer variable indépendante, variable dépendante et standardisation",
            "Suivre le cycle d'une étude, de l'observation à la discussion",
            "Situer le modèle biopsychosocial et les limites du laboratoire",
        ],
        "sections": [
            ("Trois critères d'une psychologie scientifique",
             "<p>La psychologie étudie la conduite et la vie mentale : ce qui est conscient, ce qui ne l'est pas, "
             "et la façon dont une personne le ressent. Le sens commun cherche aussi des causes. La philosophie "
             "aussi. Une science s'en distingue par la façon dont elle accepte d'être contredite.</p>"
             "<p>Trois critères tiennent ensemble. La démarche est <strong>systématique</strong> : on ne retient "
             "pas seulement l'anecdote qui arrange. Elle est <strong>précise</strong> : une autre équipe peut "
             "refaire le protocole, parce que les gestes sont décrits. Elle est <strong>communicable</strong> : "
             "les résultats se présentent, se discutent, se publient. S'il en manque un, on a quitté la science, "
             "même si le texte est plein de mots savants.</p>"
             "<p>Le <strong>modèle biopsychosocial</strong> (Engel, 1977, <em>Science</em>) rappelle qu'une "
             "expérience humaine se tient au croisement du corps, de l'histoire personnelle et du milieu. Engel "
             "l'oppose à un modèle biomédical qui ne verrait que l'écart à une norme biologique. Les courants "
             "de la psychologie ne sont pas des camps qui auraient « raison » une fois pour toutes : chacun "
             "choisit quoi expliquer, quelles données compter, et quel type de cause privilégier. La question "
             "utile est : que voit cette approche, et que laisse-t-elle dans l'ombre si on l'utilise seule ?</p>"
             "<p>On range aussi les questions selon d'autres axes. Le temps présent, la trajectoire d'une vie, "
             "ou l'histoire de l'espèce. Le fonctionnement ordinaire, la vulnérabilité, ou le soin. Deux équipes "
             "peuvent décrire la même scène sans se contredire, parce qu'elles ne cherchent pas la même cause.</p>"
             "<div class='learn-tip-box'><span class='emoji'>🔎</span><p><strong>Réflexe de lecture.</strong> "
             "Devant une affirmation, demande : comment pourrait-on la mettre en échec ? Si aucune observation "
             "ne pourrait la gêner, ce n'est pas encore une hypothèse.</p></div>"),
            ("Le cycle d'une recherche",
             "<p>Une étude n'est pas une intuition habillée après coup. Elle enchaîne des temps que l'on peut "
             "nommer, même si, dans la pratique, on revient en arrière.</p>"
             "<ol>"
             "<li><strong>Observer</strong> assez longtemps pour que le phénomène ne soit pas une coïncidence.</li>"
             "<li><strong>Formuler des hypothèses</strong> à trois étages : une idée théorique, une version "
             "opérationnelle (ce que l'on mesurera concrètement), une version statistique (ce que l'on comparera).</li>"
             "<li><strong>Vérifier</strong> : protocole, participants, matériel. La variable indépendante est "
             "manipulée. La variable dépendante est mesurée.</li>"
             "<li><strong>Traiter</strong> les données et les confronter aux hypothèses. Un chiffre ne parle "
             "pas tout seul : il répond à la comparaison que l'on avait annoncée.</li>"
             "<li><strong>Discuter</strong> ce qui tient, ce qui ne tient pas, et ce que l'on ne peut pas "
             "généraliser. La limite fait partie du résultat.</li>"
             "</ol>"
             "<p>La recherche est aussi une pratique sociale. La personne qui observe a une histoire, une "
             "langue, des attentes. La démarche dite <em>processuelle</em> insiste là-dessus : une étude est "
             "un processus, pas une photographie. La question se précise en chemin. Prétendre que le chercheur "
             "serait hors de la situation qu'il décrit est une fiction commode, pas une description honnête.</p>"),
            ("Variables, standardisation et comparaison",
             "<p>La <strong>variable indépendante</strong> est le paramètre que l'on fait varier. Ses modalités "
             "doivent rester sur la même dimension psychologique, sinon on ne sait plus ce que l'on compare. "
             "Changer à la fois le bruit, l'heure et la consigne, ce n'est pas « une » variable. La "
             "<strong>variable dépendante</strong> est la mesure qui sert à voir l'effet : un temps, un taux "
             "de rappel, un regard, une réponse.</p>"
             + _table(
                 ["Pièce", "Rôle", "Exemple"],
                 [
                     ["Variable indépendante", "Cause présumée, manipulée", "Liste à apprendre avec ou sans image"],
                     ["Variable dépendante", "Effet observé, mesuré", "Nombre de mots rappelés"],
                     ["Variable contrôlée", "Tenue constante", "Même durée, même salle, mêmes consignes"],
                     ["Variable parasite", "Confond le résultat", "L'heure du test, l'entraînement caché"],
                 ],
             )
             + "<p>La <strong>standardisation</strong> impose la même situation à tous : consignes, matériel, "
             "durée, environnement. Elle rend les données comparables et la réplication possible. Elle ne rend "
             "pas la situation « naturelle ». Un laboratoire achète de la comparaison en perdant une part du "
             "monde ordinaire. Le dire n'invalide pas l'expérience. Cela borne ce qu'elle autorise à conclure.</p>"
             "<p>Établir une causalité demande plus qu'une corrélation. Deux mesures qui varient ensemble "
             "peuvent partager une troisième cause. Seule une manipulation, avec le reste tenu aussi égal "
             "que possible, autorise à parler d'effet. Et encore : un effet dans cet échantillon n'est pas "
             "une loi pour toute l'humanité. Les échantillons d'étudiants des pays riches ne représentent "
             "pas l'espèce. C'est le biais souvent nommé WEIRD.</p>"),
            ("Chiffres, paroles et démarche processuelle",
             "<p>Quantitatif et qualitatif ne sont pas une hiérarchie de sérieux. Ils répondent à des questions "
             "différentes. Compter des rappels, des temps de regard ou des scores compare des groupes et estime "
             "une taille d'effet. Recueillir des entretiens, décrire une situation, suivre un cas éclaire "
             "le sens qu'une personne donne à ce qu'elle vit, et fait apparaître des catégories que le "
             "questionnaire n'avait pas prévues.</p>"
             "<p>Une même recherche peut mêler les deux : des chiffres pour la régularité, des paroles pour "
             "comprendre ce que le chiffre agrège. L'erreur est de croire que le tableau suffit, ou que le "
             "récit suffit. Le tableau sans question est muet. Le récit sans trace vérifiable reste une opinion.</p>"
             "<p>La crise de la réplication, déjà traitée plus haut dans cette fiche, concerne surtout les "
             "études quantitatives publiées trop vite. Elle ne dispense pas les démarches qualitatives de "
             "précision : qui a été rencontré, comment les propos ont été choisis, ce qui contredirait "
             "l'interprétation. Dans les deux cas, la communicabilité est le critère. Un résultat que personne "
             "ne peut examiner n'est pas encore un savoir.</p>"),
            ("Ce que la méthode ne promet pas",
             "<p>Le cadre expérimental a des limites que la discipline a apprises à ses dépens.</p>"
             "<ul>"
             "<li><strong>Éthique.</strong> On ne refait pas Milgram « pour voir ». Le consentement, le droit "
             "de retrait, la confidentialité et le débriefing ne sont pas un décor. Un comité les examine "
             "avant le premier participant.</li>"
             "<li><strong>Artificialité.</strong> Plus on contrôle, plus on s'éloigne de la rue, de la classe, "
             "du service de soin. La validité interne (c'est bien cette variable) et la validité externe "
             "(cela se retrouve ailleurs) tirent souvent en sens inverse.</li>"
             "<li><strong>Généralisation.</strong> Un effet chez trente volontaires d'une ville n'est pas "
             "une loi humaine. Il faut d'autres âges, d'autres langues, d'autres laboratoires.</li>"
             "<li><strong>Causes multiples.</strong> Une conduite a rarement une seule raison. Le modèle "
             "biopsychosocial sert ici de garde-fou contre l'explication unique.</li>"
             "</ul>"
             "<p>Ces limites ne renvoient pas au café du commerce. Elles disent où s'arrête une conclusion. "
             "Une psychologie de comptoir donne une cause à tout, sans dire comment on pourrait la contredire. "
             "Une psychologie scientifique publie aussi ses échecs.</p>"),
        ],
        "mythes": [
            ("Une étude est scientifique dès qu'elle contient des pourcentages.",
             "Le chiffre ne remplace pas la question, le protocole comparable et la discussion. Une recherche qualitative précise peut être scientifique. Une série de pourcentages mal construite peut ne pas l'être."),
            ("Si le laboratoire contrôle tout, le résultat vaut pour la vie réelle.",
             "La standardisation rend les participants comparables. Elle ne rend pas la situation naturelle. Généraliser est un argument à construire, pas un automatisme."),
            ("Une bonne théorie n'a pas à pouvoir être contredite.",
             "Sans observation capable de la gêner, une idée n'est pas encore une hypothèse. La communicabilité inclut la critique."),
        ],
        "chiffres": [
            ("3", "Critères ensemble : systématique, précise, communicable"),
            ("1977", "Engel, le modèle biopsychosocial dans Science"),
            ("VI / VD", "On manipule l'une, on mesure l'autre"),
            ("5 temps", "Observer, hypothèses, vérifier, traiter, discuter"),
        ],
        "flashcards": [
            ("Quels sont les trois critères d'une méthode scientifique ?",
             "Systématique, précise (une autre équipe peut refaire), communicable et donc discutable."),
            ("Quelle est la différence entre VI et VD ?",
             "La variable indépendante est manipulée. La variable dépendante est la mesure de l'effet."),
            ("À quoi sert la standardisation ?",
             "À rendre la situation identique d'un participant à l'autre, pour comparer et répliquer."),
            ("Que demande le modèle biopsychosocial ?",
             "De ne pas expliquer une expérience par le seul corps, la seule histoire ou le seul milieu (Engel, 1977)."),
            ("Pourquoi une corrélation ne suffit-elle pas à dire « cause » ?",
             "Deux phénomènes peuvent varier ensemble à cause d'un troisième facteur. La manipulation isole mieux l'effet."),
        ],
    },
    "03-cognitive": {
        "objectives": [
            "Relier l'écoute dichotique, la courbe de position sérielle et l'amorçage à des systèmes distincts",
            "Expliquer en quoi l'oubli dirigé et la mémoire dépendante de l'état sont des fonctions, pas seulement des pannes",
            "Dire ce que le raccourci de Tolman change au behaviorisme des réponses",
        ],
        "sections": [
            ("Suivre une voix et perdre l'autre",
             "<p>Colin Cherry (1953) fait répéter à voix haute un message arrivé à une oreille — c'est l'ombre, "
             "ou <em>shadowing</em> — pendant qu'un autre message arrive à l'autre oreille. Les auditeurs suivent "
             "la voix qu'on leur a désignée. Du message ignoré, il reste peu : parfois que c'était une voix, "
             "presque jamais le sens, ni même un changement de langue. Un changement brutal de timbre, lui, "
             "peut percer.</p>"
             "<p>C'est le laboratoire de l'effet cocktail : dans une salle bruyante, on tient une conversation "
             "et le reste devient un fond. L'attention n'éclaire pas toute la scène. Elle sélectionne. Les "
             "modèles de filtre (Broadbent, puis Treisman) discuteront ensuite <em>où</em> se fait le tri, "
             "tôt sur les traits physiques ou plus tard sur le sens. L'expérience de Cherry ne tranche pas "
             "toute la théorie. Elle montre le fait : on peut être présent et ne pas traiter un message clair.</p>"
             "<p>Le gorille invisible, déjà dans cette fiche, est le cousin visuel du même principe. L'oreille "
             "et l'œil ont ceci de commun qu'une tâche occupée ferme la porte à l'inattendu.</p>"),
            ("Le début et la fin d'une liste",
             "<p>Bennet Murdock (1962) fait apprendre des listes de mots, puis demande un rappel dans n'importe "
             "quel ordre. La courbe a la forme d'un U. Les premiers mots reviennent mieux : c'est l'<strong>effet "
             "de primauté</strong>. Les derniers aussi : c'est l'<strong>effet de récence</strong>. Le milieu "
             "s'effondre. L'article paraît dans le <em>Journal of Experimental Psychology</em> (volume 64, "
             "p. 482-488). La courbe s'allonge avec la liste, mais les deux bosses restent.</p>"
             "<p>Murray Glanzer et Anita Cunitz (1966) dissocient les deux bosses. Un court délai occupé — "
             "compter à rebours — abaisse surtout la récence, comme si les derniers mots n'avaient pas eu le "
             "temps de s'installer au-delà d'un registre temporaire. La primauté, elle, résiste mieux : les "
             "premiers mots ont été répétés. Deux portions de la même courbe ne racontent donc pas la même "
             "mémoire. C'est un argument classique pour distinguer un stockage bref et un stockage plus durable, "
             "sans prétendre que le cerveau serait deux boîtes étanches.</p>"
             + _table(
                 ["Portion de la courbe", "Ce qui la fait bouger", "Lecture utile"],
                 [
                     ["Primauté (début)", "Rythme plus lent, répétition", "Les premiers items sont travaillés"],
                     ["Milieu", "Liste plus longue", "Moins de répétition, plus d'interférence"],
                     ["Récence (fin)", "Délai occupé avant le rappel", "Encore disponibles, pas encore consolidés"],
                 ],
             )
             + "<p>D'où un conseil d'étude qui n'est pas une morale : le début et la fin d'une séance marquent "
             "davantage. Couper une leçon en plusieurs bouts multiplie les débuts. Ce n'est pas de la magie, "
             "c'est la courbe.</p>"),
            ("Oublier pour mieux retenir",
             "<p>Robert Bjork et ses collègues (1968) montrent que l'oubli n'est pas seulement une défaillance. "
             "On présente un premier matériel verbal, puis la consigne de l'oublier ou de le retenir, puis un "
             "second matériel à rappeler. La consigne d'oublier réduit l'interférence du premier sur le second. "
             "Ce qu'il fallait laisser tomber gêne moins.</p>"
             "<p>Oublier, ici, est une mise à jour. Réviser un cours, changer de tâche, cesser de ruminer une "
             "liste devenue inutile : la mémoire de travail ne peut pas tout garder actif. La consigne n'efface "
             "pas toujours la trace. Une reconnaissance ultérieure peut encore la retrouver. « Oublier sur "
             "commande » n'est pas une gomme. C'est un relâchement de ce qui n'est plus la cible.</p>"
             "<p>La courbe d'Ebbinghaus, plus haut dans les planches, décrit une perte avec le temps. L'oubli "
             "dirigé décrit une perte utile, décidée par la tâche. Les deux se complètent : sans oubli, chaque "
             "nouvelle liste serait noyée sous les précédentes.</p>"),
            ("Le contexte interne comme indice",
             "<p>Donald Goodwin et ses collègues (1969) font apprendre des volontaires sous alcool ou sobres, "
             "puis les testent dans le même état ou dans l'état inverse. Le rappel est meilleur quand l'état "
             "d'apprentissage et l'état de test coïncident. Le contexte n'est pas seulement la pièce ou l'odeur. "
             "Il est aussi interne : ce que le corps et l'humeur fournissent comme indices au moment de retrouver.</p>"
             "<p>C'est une mémoire dépendante de l'état. Elle rejoint un principe plus large : on récupère "
             "mieux un souvenir quand les indices du test ressemblent à ceux de l'encodage. Réviser dans des "
             "conditions proches de l'examen aide un peu pour cette raison. L'alcool, lui, n'est pas une méthode. "
             "Il détériore d'abord l'encodage. L'effet de congruence est réel et modeste. Le raconter comme "
             "une permission de boire pour « se souvenir pareil » est un contresens.</p>"),
            ("Une trace qui survit au souvenir",
             "<p>Endel Tulving, Daniel Schacter et Heather Stark (1982) font voir une liste de 96 mots. Une heure "
             "plus tard, puis sept jours plus tard, les mêmes personnes passent deux épreuves. Reconnaître les "
             "mots vus. Compléter des fragments graphiques, du type A _ _ A _ _ I N, dont certains correspondent "
             "à ces mots. L'article, dans le <em>Journal of Experimental Psychology: Learning, Memory, and "
             "Cognition</em>, s'intitule : les effets d'amorçage en complètement de fragments sont indépendants "
             "de la mémoire de reconnaissance.</p>"
             "<p>La reconnaissance chute nettement sur la semaine. La facilitation du fragment, elle, reste. "
             "Elle est aussi forte pour des mots que la personne juge « nouveaux ». Avoir lu le mot laisse une "
             "trace qui agit sans le souvenir de l'épisode « je l'ai vu ». Deux mesures que le sens commun "
             "appellerait « mémoire » ne se confondent donc pas.</p>"
             "<p>Ce n'est pas toute la mémoire implicite. Un fragment visuel n'est pas un amorçage de sens, "
             "ni une procédure motrice. L'étude sépare au moins l'épisode racontable et une facilitation qui "
             "s'en passe. Elle prépare la distinction, chez Tulving, entre mémoire épisodique et d'autres "
             "systèmes qui n'exigent pas de se rappeler l'occasion.</p>"),
            ("Une carte des lieux, pas une chaîne de virages",
             "<p>Edward Tolman, Ritchie et Kalish (1946) entraînent des rats à trouver la nourriture toujours "
             "au même endroit d'un labyrinthe. Puis on les fait partir d'un bras nouveau. Beaucoup prennent "
             "le chemin le plus direct vers le but, un raccourci qu'ils n'ont pas pratiqué comme une réponse "
             "musculaire. Si l'apprentissage n'était qu'une chaîne « stimulus, virage, récompense », le "
             "raccourci ne devrait pas être choisi.</p>"
             "<p>Tolman parle d'attente et de <strong>carte cognitive</strong> : une disposition des lieux, "
             "pas une liste de muscles. L'expérience est un argument contre un behaviorisme qui refuserait "
             "toute représentation. Elle ne filme pas le cerveau du rat, et d'autres lectures discuteront "
             "plus tard ce qui est vraiment encodé. Elle suffit à interdire la formule « l'animal ne fait "
             "qu'associer ». La psychologie cognitive reprendra cette autorisation : on peut étudier des "
             "états internes, à condition de les attacher à un comportement que l'on peut mesurer.</p>"
             "<p>Les autres lectures du corpus — mémoire partagée, caches du geai, outils gardés pour plus "
             "tard, intelligence culturelle, effet des moteurs de recherche — sont développées dans les fiches "
             "où elles ont leur place : sociale, comparée, numérique, développement. Les protocoles sont dans "
             "les <a href=\"../references/experiences.html\">expériences</a>.</p>"),
        ],
        "mythes": [
            ("Oublier, c'est toujours une panne.",
             "Une consigne d'oubli peut réduire l'interférence et protéger ce qu'il faut retenir (Bjork, 1968). L'oubli a aussi une fonction de mise à jour."),
            ("Si l'on ne reconnaît plus un mot, il n'en reste aucune trace.",
             "Tulving, Schacter et Stark (1982) : compléter un fragment reste facilité une semaine plus tard, alors que la reconnaissance a chuté."),
            ("On traite tout ce qui arrive aux oreilles, quitte à l'oublier ensuite.",
             "Dans l'écoute dichotique de Cherry (1953), le message non suivi est presque entièrement perdu. L'attention sélectionne avant le souvenir."),
        ],
        "chiffres": [
            ("96 mots", "Liste de Tulving, Schacter et Stark (1982)"),
            ("7 jours", "Délai où l'amorçage tient et où la reconnaissance chute"),
            ("U", "Forme de la courbe de position sérielle en rappel libre"),
            ("1962", "Murdock, Journal of Experimental Psychology, 64, 482-488"),
        ],
        "flashcards": [
            ("Que reste-t-il du message ignoré dans l'expérience de Cherry ?",
             "Très peu de sens. On suit une voix, et l'autre oreille ne livre presque pas le contenu."),
            ("Que montre la courbe en U de Murdock ?",
             "En rappel libre, le début (primauté) et la fin (récence) d'une liste sont mieux rappelés que le milieu."),
            ("Que fait un délai occupé selon Glanzer et Cunitz ?",
             "Il abaisse surtout l'effet de récence, pas la primauté."),
            ("Que survit quand la reconnaissance a chuté, chez Tulving (1982) ?",
             "L'amorçage : on complète mieux un fragment de mot déjà vu, sans le reconnaître."),
            ("Que montre le raccourci de Tolman ?",
             "Un apprentissage spatial de type carte, pas seulement une chaîne de virages."),
        ],
    },
    "04-sociale": {
        "objectives": [
            "Définir la mémoire transactive comme un savoir réparti, pas comme une fusion des esprits",
        ],
        "sections": [
            ("La mémoire que l'on partage",
             "<p>Daniel Wegner, Toni Giuliano et Paula Hertel (1985) décrivent l'<strong>interdépendance "
             "cognitive</strong> des relations proches. Dans un couple qui se connaît bien, chacun ne retient "
             "pas tout. Les savoirs se spécialisent : l'un garde les dates, l'autre les démarches, et les deux "
             "savent à qui demander le reste. Des duos de circonstance se recouvrent davantage et se complètent "
             "moins. Le groupe soudé peut ainsi savoir plus que la somme de ses membres isolés.</p>"
             "<p>C'est la <strong>mémoire transactive</strong>. Elle n'est pas une télépathie. C'est une "
             "répartition, plus un répertoire de « qui sait quoi ». Une séparation, un départ, un conflit "
             "désorganisent parfois des souvenirs très pratiques : non parce que la trace a fondu dans la tête, "
             "mais parce que l'adresse a disparu. Le laboratoire ne capture pas une vie de couple. La "
             "spécialisation peut aussi créer une dépendance, quand une seule personne détient un pan entier "
             "du quotidien.</p>"
             "<p>Le même principe éclaire les équipes de travail et, plus tard, les machines. Savoir où "
             "chercher est déjà une forme de mémoire. L'effet des moteurs de recherche, dans la fiche numérique, "
             "en est le prolongement : l'externe n'est plus seulement un proche, c'est un index.</p>"
             "<p>À l'échelle du groupe, cela nuance l'image de la foule qui abolirait toute pensée. Ici le "
             "collectif n'efface pas l'individu. Il organise le savoir. La conformité d'Asch et l'obéissance "
             "de Milgram montrent l'influence qui déforme. La mémoire transactive montre l'influence qui "
             "répartit. Les deux sont sociales. Elles ne produisent pas le même effet.</p>"),
        ],
        "mythes": [
            ("Pour qu'un groupe soit compétent, chacun doit tout retenir seul.",
             "Dans une relation proche, le savoir se répartit : on retient une partie, et l'on sait à qui demander le reste (Wegner, Giuliano et Hertel, 1985)."),
        ],
        "chiffres": [
            ("1985", "Wegner : la mémoire transactive des relations proches"),
            ("Qui sait quoi", "Le répertoire compte autant que le contenu"),
        ],
        "flashcards": [
            ("Qu'est-ce que la mémoire transactive ?",
             "Une répartition du savoir dans un groupe : chacun garde une partie, et sait à qui demander le reste."),
            ("En quoi un couple stable diffère-t-il d'un duo de circonstance, selon Wegner ?",
             "Les proches se spécialisent et se recouvrent moins. Ils savent qui détient quelle information."),
        ],
    },
    "05-developpement": {
        "objectives": [
            "Distinguer phylogenèse, ontogenèse et microgenèse",
            "Nommer les quatre paradigmes qui permettent d'étudier un nourrisson",
            "Relier hospitalisme, attachement et pédagogie naturelle sans réduire l'enfant à un stade",
        ],
        "sections": [
            ("Changement et continuité, tout au long de la vie",
             "<p>La psychologie du développement répond à une question : <strong>comment devient-on qui l'on est</strong>, "
             "et qu'est-ce qui demeure pendant que tout change. La perspective « tout au long de la vie », "
             "formulée notamment par Baltes et Goulet (1970), porte sur les changements du fonctionnement "
             "psychologique <em>et</em> sur les continuités. Ce n'est pas une échelle qui monterait jusqu'à "
             "l'âge adulte pour redescendre ensuite. Chaque période a ses adaptations, ses gains et ses pertes.</p>"
             "<p>L'enfant n'est donc pas un adulte incomplet, et le grand âge n'est pas seulement une ruine "
             "de l'adulte. Les stades de Piaget, les crises d'Erikson et le vieillissement cognitif, déjà "
             "dans cette fiche, sont des découpes de cette longue durée. Ils ne l'épuisent pas.</p>"
             "<p>Trois horloges s'emboîtent. La <strong>phylogenèse</strong> est celle de l'espèce, sur des "
             "temps très longs : ce que l'évolution a rendu possible. L'<strong>ontogenèse</strong> est une "
             "vie, de la conception à la mort. La <strong>microgenèse</strong> est l'apprentissage d'une "
             "compétence précise — un mot, la marche, une stratégie de mémoire — sur des jours ou des mois. "
             "Le cours ordinaire porte sur l'ontogenèse. Les deux autres l'éclairent : une compétence peut "
             "être préparée par l'espèce et pourtant s'acquérir, chez cet enfant, en quelques semaines.</p>"),
            ("D'où viennent les théories du développement",
             "<p>Les modèles ne sortent pas du laboratoire seuls. Ils héritent de disputes sur l'enfance.</p>"
             + _table(
                 ["Courant", "Idée directrice", "Angle mort"],
                 [
                     ["Locke", "L'enfant arrive comme une page à écrire", "Sous-estime ce que le nouveau-né apporte déjà"],
                     ["Rousseau", "Un développement à protéger plus qu'à remplir", "Idéalise une nature peu observée"],
                     ["Darwin", "L'enfant comme document de l'espèce", "Le carnet d'un père n'est pas un échantillon"],
                     ["Haeckel", "L'individu récapitulerait l'espèce", "Cette « loi » est abandonnée"],
                     ["Gesell", "Un calendrier de maturation", "Le milieu n'est pas un décor"],
                     ["Behaviorisme", "L'apprentissage construit la conduite", "Le bébé n'est pas une cire passive"],
                     ["Piaget", "L'enfant construit en agissant sur les objets", "Il a sous-estimé le tout-petit et le social"],
                     ["Wallon, Vygotski", "Le psychisme se construit avec autrui", "Le stade individuel ne disparaît pas pour autant"],
                     ["Bronfenbrenner", "Des milieux emboîtés, de la famille à la société", "Le schéma ne mesure pas tout seul"],
                 ],
             )
             + "<p>La psychanalyse de l'enfant ajoute une autre question : la vie affective et les liens, "
             "pas seulement la logique. Aucun de ces courants ne couvre le développement à lui seul. Les "
             "épreuves de conservation, la zone proximale et l'attachement sont déjà des chapitres de cette "
             "fiche. Ils deviennent plus clairs quand on voit de quelle dispute ils sortent.</p>"
             "<p>Le développement <strong>typique</strong> est un repère statistique, pas une morale. Le "
             "développement <strong>atypique</strong> n'est pas un échec de volonté. Cette page ne nomme "
             "pas le développement d'une personne réelle.</p>"),
            ("Le lien n'est pas un supplément de ration",
             "<p>Le récit de l'enfant sauvage — Victor de l'Aveyron, dont Itard a tenu le journal — a fait "
             "croire qu'un humain pourrait se construire hors de toute relation, comme une expérience naturelle. "
             "Le cas est tragique et mal documenté comme preuve. Il a surtout montré l'inverse de ce que le "
             "mythe promet : privé de langue et de liens au moment où ils se construisent, l'enfant ne "
             "« rattrape » pas comme si de rien n'était.</p>"
             "<p>René Spitz décrit l'<strong>hospitalisme</strong> chez des nourrissons séparés d'une figure "
             "stable : ils sont nourris, parfois propres, et pourtant le développement se grippe, le regard "
             "se retire, le corps ralentit. Le soin n'est pas une ration. Harry Harlow le retrouve chez le "
             "singe rhésus : le petit s'attache au substitut doux qui ne nourrit pas, plus qu'au fil de fer "
             "qui donne le lait. Le contact est un besoin, pas une récompense ajoutée. Konrad Lorenz, sur un "
             "autre registre, décrit l'<strong>empreinte</strong> : une fenêtre précoce où un oisillon se lie "
             "à la première figure mobile. La fenêtre n'est pas la même chez l'humain. Le principe demeure : "
             "le lien a un temps, et ce temps n'est pas interchangeable avec de la nourriture.</p>"
             "<p>De là viennent Bowlby et la situation étrange d'Ainsworth, déjà détaillés plus haut. "
             "L'hospitalisme n'est pas un « style d'attachement » à coller sur un enfant d'aujourd'hui. "
             "C'est un tableau historique qui a forcé la psychologie à compter la relation parmi les "
             "conditions du développement.</p>"),
            ("Comment interroger un nourrisson",
             "<p>On ne fait pas passer un questionnaire à un bébé. On lit son regard, sa succion, son "
             "orientation, parfois son rythme cardiaque. Quatre paradigmes reviennent dans presque tous "
             "les cours de développement.</p>"
             + _table(
                 ["Paradigme", "Ce que l'on fait", "Ce que l'on peut conclure"],
                 [
                     ["Préférence visuelle", "Deux images. On mesure où le regard reste (Fantz, dès 1961).", "Il distingue, et il préfère l'une."],
                     ["Habituation", "On répète jusqu'à ce que le regard baisse, puis on change.", "La reprise du regard = discrimination."],
                     ["Transgression des attentes", "Un événement possible, un événement impossible.", "Un regard plus long suggère une attente."],
                     ["Conditionnement", "Une succion ou un tour de tête est renforcé.", "Le bébé peut répondre oui ou non par un geste."],
                 ],
             )
             + "<p>Fantz montre que le nouveau-né regarde plus longtemps un motif qu'une surface unie, et "
             "qu'un visage schématique l'attire. Le système visuel n'attend pas la parole pour être sélectif. "
             "L'habituation est le complément : l'intérêt tombe quand la scène est devenue familière, et "
             "repart si elle change. La transgression des attentes va un cran plus loin. Si le bébé regarde "
             "plus longtemps une boîte qui semble traverser un mur, on infère qu'il avait une attente sur "
             "les objets solides. Le conditionnement transforme un réflexe en réponse utilisable.</p>"
             "<p>Ces mesures disent une discrimination ou une attente. Elles ne traduisent pas le bébé en "
             "phrases d'adulte. « Il a le concept de gravité » est une formulation trop forte pour un temps "
             "de regard. « Il est surpris par cet événement » est déjà une interprétation. La formulation "
             "juste reste proche du geste : il a regardé plus longtemps.</p>"),
            ("Visages, enseignement et métamémoire",
             "<p>Mark Johnson et John Morton (1991) proposent deux temps pour les visages. <strong>CONSPEC</strong> "
             "est un biais précoce vers une configuration de type visage : de quoi orienter le nouveau-né "
             "vers les visages plutôt que vers n'importe quelle tache. <strong>CONLERN</strong> est "
             "l'apprentissage des visages réellement rencontrés, qui prend le relais et se spécialise. "
             "L'un prépare la rencontre. L'autre la précise. Ce n'est pas « l'instinct contre la culture ». "
             "C'est un biais qui rend l'apprentissage possible.</p>"
             "<p>Gergely Csibra et György Gergely (2009) appellent <strong>pédagogie naturelle</strong> "
             "une autre préparation. Les signaux ostensifs — contact visuel, voix adressée, pointage — "
             "indiquent au nourrisson que l'information vaut pour le genre d'objet, pas seulement pour "
             "cet exemplaire. Montrer et nommer n'est pas la même chose que laisser explorer. Après un "
             "enseignement ostensif, les bébés généralisent davantage. C'est un cadre, pas une expérience "
             "unique. Tous les savoirs culturels ne passent pas par ce canal.</p>"
             "<p>Plus tard, l'enfant apprend à se regarder apprendre. John Flavell décrit la "
             "<strong>métacognition</strong> : savoir ce que l'on sait, choisir une stratégie, surveiller "
             "une mémorisation. En 1970, avec Friedrichs et Hoyt, il montre que les jeunes enfants "
             "surestiment leur rappel et étudient peu. L'estimation s'ajuste avec l'âge. En 1979, il "
             "nomme le contrôle que l'on exerce pendant la tâche, pas seulement le savoir sur la mémoire.</p>"
             "<p>Kathrin Lockl et Wolfgang Schneider (2007) relient ce contrôle au social. Dans un suivi, "
             "la théorie de l'esprit précoce — comprendre qu'autrui peut avoir une croyance fausse, comme "
             "dans Sally et Anne — prédit une partie de la métamémoire ultérieure, au-delà du seul niveau "
             "de langage. Comprendre que les autres ont un esprit aide, plus tard, à comprendre le sien. "
             "Prédiction n'est pas destin. L'école et les stratégies enseignées pèsent aussi.</p>"),
        ],
        "mythes": [
            ("Le développement s'arrête à l'enfance, puis il ne fait que décliner.",
             "La perspective vie entière décrit des changements et des continuités à chaque âge. Certaines fonctions ralentissent, d'autres — vocabulaire, régulation — peuvent encore progresser."),
            ("Un bébé qui ne parle pas ne peut pas être étudié.",
             "Le regard, la succion et l'orientation servent de réponses : préférence visuelle, habituation, transgression des attentes, conditionnement."),
            ("L'enfant se construirait très bien sans relation stable, pourvu qu'il soit nourri.",
             "L'hospitalisme décrit par Spitz et les singes de Harlow montrent que le contact et le lien ne sont pas un supplément de ration."),
        ],
        "chiffres": [
            ("3", "Horloges : phylogenèse, ontogenèse, microgenèse"),
            ("1961", "Fantz et la préférence visuelle du nourrisson"),
            ("4", "Paradigmes sans parole : préférence, habituation, attente, conditionnement"),
            ("2009", "Csibra et Gergely, la pédagogie naturelle"),
        ],
        "flashcards": [
            ("Quelle est la différence entre ontogenèse et microgenèse ?",
             "L'ontogenèse est le temps d'une vie. La microgenèse est le temps d'un apprentissage précis."),
            ("À quoi sert l'habituation chez le nourrisson ?",
             "À montrer qu'il distingue un stimulus nouveau d'un stimulus devenu familier, via la reprise du regard."),
            ("Que proposent CONSPEC et CONLERN ?",
             "Un biais précoce vers une configuration de visage, puis l'apprentissage des visages rencontrés (Johnson et Morton, 1991)."),
            ("Que change un signal ostensif, selon Csibra et Gergely ?",
             "Le nourrisson prend l'information comme valable pour le genre d'objet, pas seulement pour cet exemplaire."),
            ("Que prédit la théorie de l'esprit précoce dans l'étude de Lockl et Schneider ?",
             "Une partie de la métamémoire plus tardive : mieux juger ce que l'on va retenir."),
        ],
    },
    "09-psychopathologie": {
        "objectives": [
            "Distinguer l'objet de la psychologie clinique et un diagnostic posé hors cadre",
            "Comparer clinique à mains nues et clinique armée",
            "Situer le titre protégé de psychologue et le vocabulaire métapsychologique comme un référentiel parmi d'autres",
        ],
        "sections": [
            ("La clinique regarde une personne",
             "<p>Là où l'expérience isole une variable, la psychologie clinique s'intéresse à une "
             "<strong>personne singulière</strong> : sa subjectivité, ses liens, son histoire infantile "
             "et familiale, sa vie affective. L'objet va du fonctionnement ordinaire jusqu'à la souffrance. "
             "« Du normal au pathologique » désigne ici un continuum à comprendre, pas une case à cocher "
             "depuis un article ou un quiz.</p>"
             "<p>La <strong>méthode clinique</strong> cherche d'abord à saisir cette singularité. Elle "
             "ne commence pas par l'étiquette. Observer, écouter, restituer une histoire, formuler une "
             "hypothèse et la tenir ouverte : voilà le geste. Classer peut venir ensuite, dans un cadre "
             "de soin, avec des outils et une responsabilité. Ce site ne fait pas ce geste. Décrire des "
             "familles de troubles, plus haut dans la fiche, sert à s'orienter dans un vocabulaire. "
             "Cela ne dit rien d'une personne que vous connaissez.</p>"
             "<p>Le modèle biopsychosocial, déjà rencontré en méthodes, est ici une règle de lecture. "
             "Une souffrance ne se réduit ni à un neuromédiateur, ni à une enfance, ni à un contexte "
             "social. Les trois s'entrecroisent. En rester à un seul est déjà une erreur de méthode, "
             "avant d'être une erreur de soin.</p>"),
            ("Mains nues et clinique armée",
             "<p>Juliette Favez-Boutonnier a nommé <strong>clinique à mains nues</strong> le travail qui "
             "s'appuie sur l'observation et l'entretien, sans test entre les deux personnes. Daniel Lagache "
             "parle de <strong>clinique armée</strong> quand s'y ajoutent des épreuves, des échelles, des "
             "médiations. L'opposition est pédagogique. Dans la pratique, les deux s'articulent.</p>"
             + _table(
                 ["", "À mains nues", "Armée"],
                 [
                     ["Repère", "Favez-Boutonnier", "Lagache"],
                     ["Outils", "Observation, entretien souvent semi-directif", "Tests, échelles, supports"],
                     ["Ce que cela voit", "Le récit, la relation, le singulier", "Une comparaison à des normes"],
                     ["Risque", "Rester dans l'impression", "Prendre le score pour la personne"],
                 ],
             )
             + "<p>L'entretien semi-directif tient un fil — des thèmes prévus — sans fermer la parole. "
             "Ce n'est ni un interrogatoire, ni une conversation ordinaire. L'observation note ce qui se "
             "passe, pas ce que l'on espérait voir. Un test, de son côté, n'est utile que si l'on sait "
             "ce qu'il mesure, sur quelle population il a été étalonné, et ce qu'il ne dit pas. La fiche "
             "des tests du site rappelle cette prudence. Aucun des deux outils ne se bricole.</p>"),
            ("Titre, diplôme et déontologie",
             "<p>En France, l'usage professionnel du titre de psychologue est protégé par l'article 44 "
             "de la loi n° 85-772 du 25 juillet 1985, complété ensuite par l'obligation de faire enregistrer "
             "le diplôme. Cette inscription, longtemps portée sur les listes ADELI, est aujourd'hui versée "
             "au répertoire partagé des professionnels de santé (RPPS). Le titre suppose un diplôme "
             "universitaire de psychologie prévu par la loi — dans le cursus actuel, un master. Il ne "
             "s'improvise pas par la lecture, ni par un stage, ni par ce site.</p>"
             "<p>Le code de déontologie des psychologues s'applique au titre, y compris en recherche et "
             "en enseignement. Compétence, respect de la personne, responsabilité, secret : le cadre "
             "protège le public. Le psychologue n'est pas le psychiatre. Le psychiatre est un médecin. "
             "Les deux métiers se croisent dans le soin. Ils ne se remplacent pas.</p>"
             "<p>Les terrains sont nombreux, et tous exigent le cadre : soin, psychiatrie, justice, "
             "éducation spécialisée, petite enfance, prévention, gérontologie, travail social. Une page "
             "qui décrit ces lieux ne vous y autorise pas. Si une souffrance vous concerne, les numéros "
             "de la page d'aide du site sont le bon relais, pas un chapitre de cours.</p>"),
            ("Un vocabulaire métapsychologique, parmi d'autres",
             "<p>En licence francophone, un référentiel fréquent est celui de la métapsychologie. C'est "
             "une langue théorique, héritée de Freud et retravaillée après lui. Ce n'est pas le seul "
             "modèle clinique. Les thérapies cognitives et comportementales, l'approche humaniste, les "
             "modèles systémiques décrivent autrement. En garder un seul, c'est accepter son angle mort.</p>"
             "<p>Dans cette langue, le psychisme est d'abord un <strong>appareil</strong>. La première "
             "topique distingue conscient, préconscient et inconscient. La seconde distingue ça, moi et "
             "surmoi. Aucune de ces instances n'est une zone du cerveau. Ce sont des fonctions dans un "
             "modèle : ce qui pousse, ce qui négocie, ce qui interdit.</p>"
             "<p>Le psychisme y est aussi un lieu de <strong>conflit</strong> et de <strong>défenses</strong>. "
             "Le refoulement écarte une représentation de la conscience. La projection l'attribue à autrui. "
             "La formation réactionnelle la remplace par son contraire. La rationalisation lui trouve une "
             "raison présentable. Le déplacement déplace l'affect. La sublimation en fait une activité "
             "valorisée. Savoir nommer ces opérations permet de lire un texte. Cela ne permet pas de "
             "les diagnostiquer chez quelqu'un.</p>"
             "<p>Une <strong>pulsion</strong>, dans le même vocabulaire, n'est pas un instinct mesuré "
             "en laboratoire. On lui décrit quatre caractères : une source corporelle, une poussée, un "
             "but, un objet. Des principes règlent le modèle : plaisir, réalité, et, dans les présentations "
             "de licence, constance et répétition. Des dualismes organisent le conflit (pulsions de vie "
             "et de mort, ou pulsions sexuelles et d'autoconservation, selon les textes). Les phases "
             "orale, anale, phallique, latence, génitale sont une chronologie théorique de l'investissement, "
             "pas un calendrier à appliquer à un enfant. L'objet et l'entourage comptent : un psychisme, "
             "dans ce cadre, ne se fabrique pas seul.</p>"
             "<p>Tout ce paragraphe est un lexique. Il aide à ne pas être perdu dans un cours. Il ne dit "
             "pas ce que vous êtes, ni ce qu'il faudrait entreprendre. D'autres fiches du site présentent "
             "d'autres langues, avec d'autres preuves. Les comparer est déjà le travail de la licence.</p>"),
        ],
        "mythes": [
            ("Psychologue et psychiatre font le même métier.",
             "Le titre de psychologue est protégé par la loi du 25 juillet 1985 et suppose un diplôme universitaire de psychologie. Le psychiatre est un médecin. Les deux ne se remplacent pas, et une page de cours ne remplace ni l'un ni l'autre."),
            ("Faire de la clinique, c'est d'abord poser une étiquette.",
             "La méthode clinique cherche à comprendre une personne singulière. Classer peut venir dans un cadre de soin. Ce site ne le fait pas."),
            ("Le vocabulaire freudien décrit des pièces du cerveau.",
             "Ça, moi, surmoi, ou conscient et inconscient, sont des fonctions dans un modèle. Ce ne sont pas des aires que l'on verrait sur une IRM."),
        ],
        "chiffres": [
            ("1985", "Loi du 25 juillet : le titre de psychologue est protégé"),
            ("2", "Cliniques pédagogiques : à mains nues, et armée"),
            ("4", "Caractères d'une pulsion dans ce vocabulaire : source, poussée, but, objet"),
            ("RPPS", "Registre actuel d'inscription du diplôme"),
        ],
        "flashcards": [
            ("Que désigne la clinique à mains nues ?",
             "L'observation et l'entretien, sans test, selon la formule de Juliette Favez-Boutonnier."),
            ("Que ajoute la clinique armée, selon Lagache ?",
             "Des tests, des échelles ou des médiations. La relation reste le cadre."),
            ("Quel texte protège le titre de psychologue en France ?",
             "L'article 44 de la loi n° 85-772 du 25 juillet 1985."),
            ("Quels sont les quatre caractères d'une pulsion dans le vocabulaire métapsychologique ?",
             "Source, poussée, but et objet. C'est un modèle, pas une mesure de laboratoire."),
            ("Pourquoi cette fiche ne sert-elle pas à qualifier une personne ?",
             "Décrire un vocabulaire ou une famille de troubles n'est pas un diagnostic. Le diagnostic exige un cadre, un diplôme et une rencontre."),
        ],
    },
    "16-comparee": {
        "objectives": [
            "Distinguer une mémoire de type épisodique, chez le geai, d'un récit humain",
            "Dire ce que l'hypothèse de l'intelligence culturelle compare chez l'enfant et les grands singes",
        ],
        "sections": [
            ("Quoi, où, quand : le geai et les outils",
             "<p>Nicola Clayton et Anthony Dickinson (1998) travaillent avec des geais buissonniers, des "
             "oiseaux qui cachent leur nourriture. Les oiseaux dissimulent des vers, qui se gâtent, et des "
             "cacahuètes, qui durent, dans des sites distincts. Après un délai court, ils cherchent les vers. "
             "Après un délai long, quand les vers seraient avariés, ils vont aux cacahuètes — à condition "
             "d'avoir pu apprendre que les vers se dégradent. Le comportement tient ensemble le quoi, le où "
             "et le quand.</p>"
             "<p>On parle de mémoire <strong>de type épisodique</strong>. Le mot « type » est indispensable. "
             "L'oiseau ne se raconte pas l'épisode comme un humain. Le critère est comportemental : il agit "
             "en fonction d'un épisode passé précis. C'est assez pour refuser l'idée que seul l'humain "
             "aurait une mémoire située dans le temps. Ce n'est pas assez pour lui prêter une autobiographie.</p>"
             "<p>Nicholas Mulcahy et Josep Call (2006) regardent un autre futur. Un bonobo ou un orang-outan "
             "choisit un outil, attend, puis doit l'utiliser dans une autre pièce. Plusieurs sujets "
             "sélectionnent et conservent l'outil utile, au-delà de l'attrait du moment. Cela suggère une "
             "planification. Les effectifs sont petits. Planifier n'est pas encore le voyage mental dans le "
             "temps que Tulving décrit chez l'humain. Rapprocher le geai et le grand singe sert à ça : "
             "montrer des continuités, et garder les critères.</p>"),
            ("L'hypothèse de l'intelligence culturelle",
             "<p>Esther Herrmann et ses collègues (2007) comparent de jeunes enfants, des chimpanzés et des "
             "orangs-outans. La batterie couvre l'espace, les quantités, la causalité, puis la communication, "
             "la théorie de l'esprit et l'apprentissage social. Sur les problèmes physiques, les performances "
             "sont proches. Sur les problèmes sociaux, les enfants distancent les singes.</p>"
             "<p>L'<strong>hypothèse de l'intelligence culturelle</strong> en tire une proposition : la "
             "cognition humaine serait spécialisée pour apprendre des autres, pas seulement pour raisonner "
             "sur les objets. Cela rejoint la pédagogie naturelle, dans la fiche développement, et la mémoire "
             "transactive, dans la fiche sociale. Nous serions des animaux dont le savoir est fait pour "
             "circuler.</p>"
             "<p>Une batterie ne résume pas une espèce. Les enfants et les singes de sanctuaire n'ont pas "
             "le même élevage. Réussir une épreuve de communication humaine avantage l'humain par construction. "
             "L'hypothèse est un cadre de recherche, pas un palmarès. Elle interdit toutefois la formule "
             "paresseuse selon laquelle l'humain serait « simplement plus intelligent » sur tous les tableaux. "
             "La différence mesurée ici est sociale.</p>"),
        ],
        "mythes": [
            ("Seuls les humains situent un souvenir dans le temps.",
             "Des geais retrouvent une cache selon ce qui a été caché, où, et depuis combien de temps (Clayton et Dickinson, 1998). « De type épisodique » décrit le comportement, pas un récit intérieur."),
            ("L'humain surpasse le singe dans toutes les épreuves cognitives.",
             "Herrmann et al. (2007) : sur l'espace, les quantités et la causalité, les performances sont proches. L'écart se creuse sur le social."),
        ],
        "chiffres": [
            ("1998", "Clayton et Dickinson : quoi, où, quand chez le geai"),
            ("2006", "Mulcahy et Call : des grands singes gardent un outil"),
            ("2007", "Herrmann : l'écart humain se voit surtout sur le social"),
        ],
        "flashcards": [
            ("Que retient le geai de Clayton et Dickinson ?",
             "Quoi a été caché, où, et depuis assez longtemps pour que les vers soient gâtés."),
            ("Pourquoi dit-on « de type épisodique » et non « épisodique » ?",
             "Le critère est le comportement. On ne prête pas à l'oiseau un récit autobiographique humain."),
            ("Que compare l'hypothèse de l'intelligence culturelle ?",
             "Enfants et grands singes : proches sur le physique, enfants en avance sur le social."),
        ],
    },
    "22-numerique": {
        "objectives": [
            "Décrire l'effet Google comme un déplacement de l'encodage, pas comme une destruction de la mémoire",
        ],
        "sections": [
            ("Quatre études sur l'effet Google",
             "<p>Betsy Sparrow, Jenny Liu et Daniel Wegner publient en 2011, dans <em>Science</em>, "
             "« Google Effects on Memory ». Quatre études montrent que l'accès en ligne est devenu une "
             "mémoire transactive : on ne stocke pas seulement des faits, on stocke le chemin pour les "
             "retrouver. Le paragraphe plus haut de cette fiche en donnait l'idée. Voici le dispositif.</p>"
             "<ul>"
             "<li>Quand une question difficile se pose, les participants pensent ensuite davantage aux "
             "mots liés aux moteurs de recherche. Le besoin d'information amorce l'outil, comme un proche "
             "amorcerait le nom de la personne qui sait.</li>"
             "<li>On retient moins bien des énoncés que l'on croit pouvoir retrouver plus tard, et mieux "
             "ceux que l'on croit effacés. L'attente d'un accès futur change l'encodage.</li>"
             "<li>Le fait d'avoir sauvegardé ou non module encore ce qui reste. Ce n'est pas le sujet "
             "de la phrase qui décide seul. C'est la croyance sur sa disponibilité.</li>"
             "<li>On se souvient mieux de l'endroit où l'information a été rangée — quel dossier — que "
             "de l'information elle-même.</li>"
             "</ul>"
             "<p>L'effet ne dit pas qu'Internet « détruit la mémoire ». Il dit que la mémoire s'organise "
             "autrement quand un index externe est fiable. Platon, dans le <em>Phèdre</em>, craignait déjà "
             "que l'écriture ne dispense de se souvenir. L'écriture n'a pas aboli la mémoire. Elle en a "
             "déplacé une partie. Les moteurs font un déplacement du même genre, plus rapide, et sans "
             "le contexte qu'un proche ajouterait au fait.</p>"
             "<p>Les interfaces de 2011 ne sont pas les nôtres. L'effet décrit une stratégie d'encodage, "
             "pas une lésion. S'en servir pour étudier consiste à décider ce qui mérite d'être su sans "
             "fichier, et ce qui mérite seulement d'être retrouvable. Les deux ne se valent pas le jour "
             "de l'examen, ni dans une conversation où le téléphone reste dans la poche.</p>"),
        ],
        "mythes": [
            ("Chercher en ligne détruit la mémoire.",
             "Sparrow, Liu et Wegner (2011) montrent un déplacement : on encode davantage l'endroit où retrouver l'information que le fait lui-même, quand on s'attend à pouvoir le rechercher."),
        ],
        "chiffres": [
            ("2011", "Science : quatre études sur l'effet Google"),
            ("4", "Études : amorçage, effacement, sauvegarde, lieu de stockage"),
            ("Où", "Mieux retenu que le fait, quand le fait reste accessible"),
        ],
        "flashcards": [
            ("Que retient-on mieux, selon Sparrow, Liu et Wegner, quand l'information reste en ligne ?",
             "L'endroit où la retrouver, davantage que le contenu lui-même."),
            ("Pourquoi parle-t-on de mémoire transactive à propos d'un moteur de recherche ?",
             "Comme avec un proche, on délègue une partie du savoir et l'on garde le chemin d'accès."),
        ],
    },
}
