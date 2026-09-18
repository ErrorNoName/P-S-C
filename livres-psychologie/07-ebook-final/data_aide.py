# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Aide, orientation et ressources.

Un site qui décrit des troubles psychiques a le devoir d'indiquer où trouver de
l'aide. Les numéros rassemblés ici sont des dispositifs publics ou associatifs
nationaux, gratuits sauf mention contraire. Ils peuvent évoluer : la page invite
explicitement à vérifier auprès de la source officielle.
"""

# (zone, nom, numero, horaires, description)
URGENCES = [
    ("France", "Urgences médicales (SAMU)", "15",
     "24 h/24, 7 j/7",
     "À composer devant une urgence vitale : tentative de suicide en cours, intoxication, "
     "état de conscience altéré. Depuis un mobile ou à l'étranger, le 112 aboutit au même service."),
    ("France", "Numéro national de prévention du suicide", "3114",
     "24 h/24, 7 j/7 — gratuit",
     "Une ligne dédiée, tenue par des professionnels de santé formés à la crise suicidaire. "
     "Elle s'adresse aussi bien aux personnes en souffrance qu'à leurs proches et aux professionnels "
     "qui s'inquiètent pour quelqu'un."),
    ("France", "Enfance en danger", "119",
     "24 h/24, 7 j/7 — gratuit",
     "Pour signaler ou demander conseil face à une situation d'enfant en danger ou en risque de l'être. "
     "L'appel n'apparaît pas sur les factures téléphoniques."),
    ("France", "Violences Femmes Info", "3919",
     "24 h/24, 7 j/7 — gratuit et anonyme",
     "Écoute, information et orientation pour les femmes victimes de violences, ainsi que pour leur "
     "entourage. Ce n'est pas un numéro d'urgence : en cas de danger immédiat, composer le 17 ou le 112."),
    ("France", "Aide aux victimes", "116 006",
     "7 j/7 — gratuit",
     "Soutien psychologique et information sur les droits après toute forme d'infraction : agression, "
     "vol, accident, harcèlement."),
    ("Belgique", "Centre de prévention du suicide", "0800 32 123",
     "24 h/24, 7 j/7 — gratuit",
     "Ligne d'écoute pour les personnes en crise suicidaire et leur entourage."),
    ("Belgique", "Télé-Accueil", "107",
     "24 h/24, 7 j/7",
     "Écoute anonyme pour toute forme de détresse psychologique."),
    ("Suisse", "La Main Tendue", "143",
     "24 h/24, 7 j/7",
     "Écoute confidentielle pour toute difficulté psychologique ou existentielle."),
    ("Suisse", "Pro Juventute — conseils aux jeunes", "147",
     "24 h/24, 7 j/7",
     "Ligne destinée aux enfants et aux adolescents, par téléphone, message ou tchat."),
    ("Canada", "Ligne d'aide en cas de crise de suicide", "988",
     "24 h/24, 7 j/7 — appel ou texto",
     "Service national bilingue, accessible partout au Canada."),
    ("Québec", "Ligne québécoise de prévention du suicide", "1 866 277-3553",
     "24 h/24, 7 j/7",
     "Intervention de crise et orientation vers les ressources locales."),
]

# (nom, numero, description)
ECOUTE = [
    ("SOS Amitié", "09 72 39 40 50",
     "Écoute anonyme et sans jugement, 24 h/24, pour la solitude, l'angoisse ou le simple besoin de "
     "parler à quelqu'un. Également par tchat et par messagerie sur leur site."),
    ("Suicide Écoute", "01 45 39 40 00",
     "Ligne associative spécialisée, 24 h/24, tenue par des bénévoles formés à l'écoute de la "
     "souffrance suicidaire."),
    ("Fil Santé Jeunes", "0 800 235 236",
     "Pour les 12-25 ans, tous les jours : santé, sexualité, mal-être, relations, addictions. "
     "Anonyme et gratuit depuis un poste fixe."),
    ("Nightline", "—",
     "Service d'écoute nocturne par et pour les étudiants, présent dans plusieurs villes "
     "universitaires françaises, par téléphone et par tchat."),
    ("Alcool Info Service", "0 980 980 930",
     "Information, évaluation de sa consommation et orientation, sans jugement, pour soi ou pour un "
     "proche."),
    ("Drogues Info Service", "0 800 23 13 13",
     "Écoute et orientation sur les consommations de substances, y compris pour l'entourage."),
    ("Tabac Info Service", "39 89",
     "Accompagnement à l'arrêt du tabac, avec possibilité d'un suivi par un tabacologue."),
    ("Joueurs Info Service", "09 74 75 13 13",
     "Pour les difficultés liées aux jeux d'argent et de hasard, et pour les proches concernés."),
    ("Net Écoute / 3018", "3018",
     "Harcèlement en ligne, diffusion d'images sans consentement, piratage de comptes : accompagnement "
     "et procédure de signalement accélérée auprès des plateformes."),
]

# (id, titre, contenu_html)
PARCOURS_SOIN = [
    (
        "par-ou-commencer",
        "Par où commencer quand on ne va pas bien",
        "<p>Le médecin généraliste est la porte d'entrée la plus simple et la plus rapide. Il évalue la "
        "situation, écarte les causes médicales qui imitent un trouble psychique — thyroïde, carences, "
        "effets de traitements, troubles du sommeil — et oriente vers le bon interlocuteur. Il peut aussi "
        "prescrire un arrêt de travail et un traitement si c'est indiqué.</p>"
        "<p>Si vous êtes étudiant, le service de santé universitaire propose des consultations "
        "psychologiques gratuites, et les bureaux d'aide psychologique universitaire offrent un suivi "
        "sans avance de frais dans plusieurs villes.</p>"
        "<p>Si vous travaillez, la médecine du travail est tenue au secret médical vis-à-vis de "
        "l'employeur et peut être consultée à votre seule demande.</p>",
    ),
    (
        "cmp",
        "Les centres médico-psychologiques",
        "<p>Les CMP sont des structures publiques de secteur qui assurent consultations, suivis et soins "
        "psychiatriques et psychologiques. La prise en charge y est gratuite, sans avance de frais, et "
        "l'équipe associe psychiatres, psychologues, infirmiers et travailleurs sociaux.</p>"
        "<p>Il existe des CMP pour adultes et des CMP pour enfants et adolescents, rattachés à un secteur "
        "géographique : on s'adresse à celui dont dépend son domicile. Le principal obstacle est le délai "
        "d'attente, souvent long pour un premier rendez-vous non urgent — raison de plus pour s'inscrire "
        "tôt, quitte à consulter ailleurs en attendant.</p>",
    ),
    (
        "remboursement",
        "Ce qui est remboursé, et comment",
        "<p>Les consultations de psychiatre sont remboursées comme celles de tout médecin. Les "
        "consultations de psychologue en cabinet libéral ne le sont pas au titre du droit commun, sauf "
        "dispositifs particuliers.</p>"
        "<p>Un dispositif public permet de bénéficier de séances chez un psychologue partenaire prises en "
        "charge par l'Assurance maladie, dans la limite d'un nombre de séances par an. Les modalités — "
        "nécessité ou non d'un adressage médical, nombre de séances, tarif — ont évolué plusieurs fois : "
        "vérifiez les conditions en vigueur sur le site de l'Assurance maladie.</p>"
        "<p>Par ailleurs, les soins en CMP, en hôpital de jour et en établissement public sont pris en "
        "charge, et de nombreuses mutuelles remboursent un forfait annuel de séances chez un psychologue.</p>",
    ),
    (
        "premiere-seance",
        "À quoi ressemble une première séance",
        "<p>Elle sert autant à vous qu'au professionnel. On vous demandera ce qui vous amène, depuis "
        "quand, ce que cela change dans votre quotidien, vos antécédents, votre sommeil, votre "
        "consommation éventuelle d'alcool ou de substances, et votre entourage. Vous n'êtes pas obligé de "
        "tout dire d'emblée.</p>"
        "<p>Vous pouvez poser vos propres questions : quelle approche est utilisée, quelle durée est "
        "envisagée, à quelle fréquence, quel tarif, comment on saura que cela fonctionne. Un "
        "professionnel sérieux répond volontiers à ces questions.</p>"
        "<p>Il est normal de se sentir vidé ou remué après une première séance. Il est normal aussi de ne "
        "pas « accrocher » : la qualité de la relation est le meilleur prédicteur du résultat, et changer "
        "d'interlocuteur n'est pas un échec.</p>",
    ),
    (
        "urgence-psychiatrique",
        "Quand il s'agit d'une urgence",
        "<p>Appelez immédiatement le 15 ou le 112, ou rendez-vous aux urgences, dans ces situations : "
        "idées suicidaires avec un plan ou des moyens à disposition, tentative en cours, état de "
        "confusion ou de délire aigu, mise en danger immédiate de soi ou d'autrui, arrêt brutal d'un "
        "traitement avec symptômes sévères.</p>"
        "<p>Le 3114 peut être appelé en amont, y compris par un proche inquiet, et travaille en lien avec "
        "les services d'urgence lorsque c'est nécessaire.</p>"
        "<p>Si vous accompagnez quelqu'un, restez avec la personne, éloignez les moyens dangereux "
        "accessibles, et ne la laissez pas seule en attendant les secours.</p>",
    ),
    (
        "aider-proche",
        "Aider un proche sans s'épuiser",
        "<p>Trois principes tiennent la route. Décrivez ce que vous observez plutôt que de poser un "
        "diagnostic. Posez la question du suicide directement si vous y pensez : cela n'induit pas "
        "l'idée, et cela permet d'en parler. Proposez une aide concrète — chercher un numéro ensemble, "
        "prendre le rendez-vous, accompagner — plutôt qu'un encouragement général.</p>"
        "<p>Ce qui n'aide pas : minimiser, comparer avec pire, exiger des explications, ou promettre un "
        "secret absolu quand il y a un risque vital.</p>"
        "<p>Protégez-vous enfin. Accompagner durablement quelqu'un qui va mal use réellement, et il "
        "existe des dispositifs de soutien aux aidants. Vous avez le droit de dire ce que vous ne pouvez "
        "pas porter.</p>",
    ),
]

# (nom, url, description) — ressources francophones en accès libre
RESSOURCES_LIBRES = [
    ("Psychomédia et sites de vulgarisation scientifique", None,
     "Utiles pour suivre l'actualité, à condition de remonter systématiquement à l'étude citée : "
     "le titre d'un article de presse surestime presque toujours la portée d'un résultat."),
    ("Wikipédia en français et en anglais", "https://fr.wikipedia.org/wiki/Psychologie",
     "Point de départ honnête pour une première définition. La version anglaise des articles de "
     "psychologie est souvent plus complète et mieux sourcée : les références en bas de page valent "
     "davantage que le texte lui-même."),
    ("Wikisource et Gallica", "https://gallica.bnf.fr",
     "Bibliothèques numériques donnant accès aux textes fondateurs en français, libres de droits. "
     "C'est là que se trouvent les ouvrages proposés dans la bibliothèque de ce site."),
    ("Internet Archive", "https://archive.org",
     "Fonds considérable d'ouvrages anciens numérisés, dont la quasi-totalité de la psychologie "
     "francophone d'avant 1930."),
    ("PubMed", "https://pubmed.ncbi.nlm.nih.gov",
     "Base de référence pour la recherche biomédicale et psychologique. Les résumés sont libres ; "
     "chercher le titre suivi de la mention d'un dépôt ouvert permet souvent de trouver le texte "
     "intégral légalement déposé par les auteurs."),
    ("Cairn", "https://www.cairn.info",
     "Portail francophone de revues en sciences humaines, avec une part importante d'articles en accès "
     "libre, notamment après une période d'embargo."),
    ("HAL — archives ouvertes", "https://hal.science",
     "Dépôt public français où les chercheurs déposent légalement leurs articles. Excellente porte "
     "d'entrée pour lire de la recherche francophone récente sans abonnement."),
    ("Cochrane — revues systématiques", "https://www.cochrane.org/fr",
     "Synthèses méthodiques sur l'efficacité des interventions, y compris psychothérapeutiques. "
     "Les résumés en langage simplifié sont rédigés pour le grand public."),
]
