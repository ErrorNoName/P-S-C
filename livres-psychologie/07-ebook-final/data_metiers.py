# -*- coding: utf-8 -*-
"""Métiers, études et cadre professionnel de la psychologie dans l'espace francophone.

Les informations sur les diplômes et les titres décrivent le cadre général ; les
règles évoluent et varient d'un pays à l'autre. Vérifiez toujours auprès des
sources officielles avant une décision d'orientation.
"""

# (id, nom, famille, mission, formation, quotidien, ou_exercer, a_savoir)
METIERS = [
    ("psychologue-clinicien", "Psychologue clinicien", "Soin",
     "Évaluer, comprendre et accompagner la souffrance psychique d'enfants, d'adolescents ou d'adultes, en s'appuyant sur des entretiens, des tests et une approche thérapeutique.",
     "Licence de psychologie puis master de psychologie clinique et psychopathologie (bac+5), incluant un stage professionnel long. Le titre de psychologue est protégé par la loi en France.",
     "Entretiens cliniques, passation et interprétation de bilans, psychothérapies, réunions d'équipe pluriprofessionnelle, rédaction de comptes rendus, travail avec les familles et les partenaires.",
     "Hôpital, centre médico-psychologique, protection de l'enfance, établissement médico-social, cabinet libéral, associations.",
     "L'inscription au répertoire ADELI (ou son successeur) est obligatoire pour exercer. En libéral, une part des séances peut être prise en charge via les dispositifs publics selon les conditions en vigueur."),

    ("psychiatre", "Psychiatre", "Soin",
     "Diagnostiquer et traiter les troubles psychiatriques, avec la possibilité de prescrire des médicaments et d'hospitaliser lorsque c'est nécessaire.",
     "Études de médecine puis internat de psychiatrie : environ onze ans après le baccalauréat en France.",
     "Consultations, prescriptions et suivi des traitements, coordination des soins, urgences psychiatriques, expertises, parfois psychothérapie selon la formation complémentaire.",
     "Hôpital, clinique, centre médico-psychologique, cabinet libéral, urgences, unités spécialisées.",
     "Différence essentielle avec le psychologue : le psychiatre est médecin, donc il prescrit et les consultations sont remboursées par l'Assurance maladie."),

    ("neuropsychologue", "Neuropsychologue", "Soin / Évaluation",
     "Évaluer les fonctions cognitives (mémoire, attention, langage, fonctions exécutives) après une lésion cérébrale, une maladie neurodégénérative ou dans un trouble du neurodéveloppement, et proposer une remédiation.",
     "Licence de psychologie puis master de neuropsychologie (bac+5). C'est une spécialité du titre de psychologue, pas une profession distincte.",
     "Bilans neuropsychologiques standardisés, rédaction de comptes rendus détaillés, remédiation cognitive, guidance des proches, travail avec neurologues et orthophonistes.",
     "Services de neurologie et de gériatrie, consultations mémoire, centres de rééducation, unités de neurodéveloppement, libéral.",
     "Spécialité en forte demande, notamment avec le vieillissement de la population et le développement des consultations mémoire."),

    ("psychologue-travail", "Psychologue du travail", "Organisations",
     "Améliorer la santé, la sécurité et l'efficacité au travail : recrutement, prévention des risques psychosociaux, accompagnement des transitions professionnelles, ergonomie cognitive.",
     "Master de psychologie du travail et des organisations (bac+5), parfois complété par une formation en ergonomie ou en prévention.",
     "Entretiens et évaluations, diagnostics organisationnels, animation de groupes de travail, conception de dispositifs de prévention, accompagnement individuel.",
     "Entreprises, cabinets de conseil, services de santé au travail, France Travail, organismes de formation, fonction publique.",
     "Attention à ne pas confondre avec les consultants en ressources humaines : seul le titre de psychologue garantit la formation et le cadre déontologique."),

    ("psychologue-education", "Psychologue de l'Éducation nationale", "Éducation",
     "Accompagner la réussite et le bien-être des élèves : repérage des difficultés, appui aux équipes, orientation, prévention du décrochage.",
     "Master de psychologie puis concours de psychologue de l'Éducation nationale, avec deux spécialités : éducation-développement-apprentissages (premier degré) ou éducation-développement-conseil en orientation (second degré).",
     "Entretiens avec élèves et familles, bilans psychologiques, participation aux équipes éducatives, travail sur les projets d'orientation, prévention et gestion de situations de crise.",
     "Écoles, collèges, lycées, centres d'information et d'orientation.",
     "Métier de la fonction publique, accessible par concours : les places sont limitées et la préparation demande une anticipation dès le master."),

    ("psychomotricien", "Psychomotricien", "Soin (paramédical)",
     "Travailler le lien entre le corps, le mouvement et la vie psychique : tonus, coordination, schéma corporel, régulation émotionnelle, du bébé à la personne âgée.",
     "Diplôme d'État de psychomotricien en trois ans après le baccalauréat, dans un institut de formation agréé.",
     "Bilans psychomoteurs, séances individuelles ou en groupe, médiation corporelle, relaxation, travail avec les familles et les équipes.",
     "Hôpital, crèche, institut médico-éducatif, EHPAD, centre d'action médico-sociale précoce, libéral.",
     "Profession paramédicale distincte de la psychologie, avec un diplôme d'État spécifique et une approche centrée sur le corps en mouvement."),

    ("orthophoniste", "Orthophoniste / Logopède", "Soin (paramédical)",
     "Évaluer et traiter les troubles de la communication, du langage oral et écrit, de la voix, de la parole et de la déglutition.",
     "Certificat de capacité d'orthophoniste en cinq ans après le baccalauréat en France, sur concours ou dossier selon les universités. Le titre de logopède est utilisé en Belgique et en Suisse.",
     "Bilans de langage, rééducation individuelle, travail avec les familles et les enseignants, accompagnement après accident vasculaire cérébral ou dans les maladies neurodégénératives.",
     "Cabinet libéral (majoritaire), hôpital, centres de rééducation, établissements médico-sociaux.",
     "Formation très sélective à l'entrée et débouchés nombreux ; forte proximité avec la psycholinguistique et la neuropsychologie."),

    ("psychotherapeute", "Psychothérapeute", "Soin",
     "Conduire des psychothérapies structurées pour traiter des troubles psychiques.",
     "En France, le titre est réglementé depuis 2010 : il exige une formation en psychopathologie clinique et un stage, accessible essentiellement aux médecins, psychologues et, sous conditions, psychanalystes justifiant d'un parcours reconnu.",
     "Séances de psychothérapie selon l'approche pratiquée (TCC, thérapies systémiques, psychodynamiques, humanistes, EMDR, ACT…), supervision régulière, formation continue.",
     "Cabinet libéral, structures de soin, centres spécialisés.",
     "Ne pas confondre avec « psychanalyste », « praticien en développement personnel » ou « coach » : ces appellations ne sont protégées par aucune loi et n'offrent aucune garantie de formation."),

    ("chercheur", "Enseignant-chercheur en psychologie", "Recherche",
     "Produire des connaissances nouvelles par la recherche expérimentale ou clinique, et former les futurs professionnels.",
     "Master recherche puis doctorat (bac+8), suivi généralement d'un ou plusieurs contrats postdoctoraux avant une éventuelle titularisation.",
     "Conception et réalisation d'études, analyses statistiques, rédaction d'articles, recherche de financements, encadrement d'étudiants, enseignement, évaluation par les pairs.",
     "Universités, CNRS, Inserm, laboratoires hospitaliers, instituts de recherche publics et privés.",
     "Voie passionnante mais très sélective : le nombre de doctorats délivrés dépasse largement le nombre de postes permanents ouverts chaque année."),

    ("psychologue-sport", "Psychologue du sport", "Performance",
     "Accompagner sportifs, entraîneurs et équipes sur la préparation mentale, la gestion du stress de compétition, la cohésion, la blessure et la reconversion.",
     "Master de psychologie complété par une formation spécialisée en psychologie du sport ; le titre de psychologue reste la base indispensable.",
     "Entretiens individuels, travail d'équipe, préparation à la compétition, accompagnement du retour de blessure, soutien lors des fins de carrière.",
     "Clubs professionnels, fédérations, centres de formation, pôles espoirs, libéral.",
     "Distinguer le psychologue du sport du « préparateur mental », dont le titre n'est pas protégé et dont les formations sont très inégales."),

    ("psychologue-legal", "Psychologue en milieu judiciaire", "Justice",
     "Évaluer, accompagner ou expertiser dans le cadre pénal et civil : victimes, auteurs, mineurs, décisions de placement.",
     "Master de psychologie, souvent complété par une formation en psychologie légale ou en criminologie. L'expertise judiciaire suppose une inscription sur une liste de cour d'appel.",
     "Entretiens d'évaluation, rédaction de rapports destinés aux magistrats, suivi de personnes placées sous main de justice, accompagnement des victimes, témoignage à l'audience.",
     "Services pénitentiaires d'insertion et de probation, protection judiciaire de la jeunesse, associations d'aide aux victimes, expertise indépendante.",
     "Le rapport écrit engage fortement : ces fonctions demandent une grande rigueur méthodologique et une claire conscience des limites de l'évaluation psychologique."),

    ("psychologue-sante", "Psychologue de la santé", "Santé",
     "Accompagner les personnes atteintes de maladies somatiques : annonce diagnostique, observance, douleur, qualité de vie, fin de vie.",
     "Master de psychologie de la santé ou de psychologie clinique avec spécialisation ; formations complémentaires en soins palliatifs, oncologie ou éducation thérapeutique.",
     "Entretiens au lit du patient, soutien aux proches, participation aux staffs médicaux, groupes d'éducation thérapeutique, soutien aux équipes soignantes.",
     "Services d'oncologie, de dialyse, de transplantation, unités de soins palliatifs, réseaux de santé, maisons de santé.",
     "Domaine en croissance avec l'augmentation des maladies chroniques et le développement de l'éducation thérapeutique du patient."),

    ("psychologue-gerontologie", "Psychologue en gérontologie", "Vieillissement",
     "Accompagner les personnes âgées et leurs proches : troubles cognitifs, dépression, entrée en institution, fin de vie, soutien aux aidants.",
     "Master de psychologie, souvent avec une composante neuropsychologique ou clinique du vieillissement.",
     "Évaluations cognitives et thymiques, entretiens individuels, ateliers de stimulation, soutien des familles, accompagnement et formation des équipes soignantes.",
     "EHPAD, services de gériatrie, consultations mémoire, accueils de jour, services à domicile.",
     "Besoins en forte croissance démographique, mais postes souvent à temps partiel et répartis sur plusieurs établissements."),

    ("ergonome", "Ergonome", "Organisations",
     "Adapter le travail à l'humain : postes, outils, interfaces, organisation, en s'appuyant sur l'analyse de l'activité réelle.",
     "Master d'ergonomie, accessible depuis la psychologie, la physiologie ou l'ingénierie.",
     "Observation du travail réel, entretiens, analyse de l'activité, propositions de transformation, conception participative, suivi des projets.",
     "Entreprises industrielles et de services, cabinets de conseil, services de santé au travail, éditeurs de logiciels, secteur public.",
     "L'ergonomie de conception logicielle (souvent appelée UX) constitue un débouché important pour les profils issus de la psychologie cognitive."),

    ("ux-researcher", "Chercheur en expérience utilisateur", "Numérique",
     "Comprendre les usages, les besoins et les difficultés des utilisateurs pour orienter la conception de produits numériques.",
     "Master de psychologie cognitive, d'ergonomie ou de sciences cognitives ; la maîtrise des méthodes qualitatives et quantitatives est déterminante.",
     "Entretiens utilisateurs, tests d'utilisabilité, analyse comportementale, tests A/B, synthèse et restitution aux équipes de conception.",
     "Entreprises technologiques, agences, startups, grands groupes, secteur public numérique.",
     "La formation en psychologie y est un atout distinctif : méthodologie d'étude, connaissance des biais, rigueur dans l'interprétation des données."),

    ("conseiller-orientation", "Conseiller en évolution professionnelle", "Orientation",
     "Accompagner les personnes dans leurs choix de formation, de métier ou de reconversion.",
     "Master de psychologie du travail ou de l'orientation, ou formations spécialisées selon les structures. Les bilans de compétences réalisés par un psychologue offrent un cadre déontologique renforcé.",
     "Entretiens d'accompagnement, passation et restitution de questionnaires d'intérêts et de valeurs, exploration des métiers, construction de projets, suivi.",
     "France Travail, APEC, missions locales, cabinets de bilan de compétences, organismes de formation, centres d'information et d'orientation.",
     "Attention à la qualité très variable des tests d'orientation commercialisés : beaucoup n'ont aucune validité psychométrique établie."),

    ("psychologue-interculturel", "Psychologue en contexte interculturel", "Interculturel",
     "Accompagner des personnes migrantes, exilées ou en situation de minorité, en tenant compte de la langue, de la culture et du parcours d'exil.",
     "Master de psychologie clinique avec spécialisation en psychologie interculturelle ou en psychotraumatologie ; la formation au travail avec interprète est essentielle.",
     "Entretiens avec interprète, évaluation et soin du psychotraumatisme, rédaction de certificats pour les demandes d'asile, médiation avec les institutions.",
     "Associations d'accueil et d'accompagnement, centres de soins spécialisés en psychotraumatisme, permanences d'accès aux soins de santé, protection de l'enfance.",
     "Exige une vigilance particulière : les instruments d'évaluation standardisés sont rarement validés hors de leur culture d'origine."),

    ("psychologue-crise", "Psychologue en cellule d'urgence", "Urgence",
     "Intervenir immédiatement après un événement traumatique collectif : attentat, catastrophe, accident grave, décès en milieu scolaire ou professionnel.",
     "Master de psychologie clinique avec formation spécifique au psychotraumatisme et aux protocoles d'intervention d'urgence.",
     "Interventions sur site, soutien immédiat et post-immédiat, orientation vers un suivi, appui aux institutions, formation des équipes.",
     "Cellules d'urgence médico-psychologique, SAMU, associations agréées, services de santé au travail.",
     "Le débriefing psychologique collectif systématique n'est plus recommandé : certaines études suggèrent qu'il peut aggraver le devenir de certaines personnes. Les protocoles actuels privilégient les premiers secours psychologiques et le repérage."),

    ("psychologue-institution", "Psychologue en établissement médico-social", "Médico-social",
     "Accompagner des personnes en situation de handicap, leurs familles et les équipes éducatives, tout au long du parcours de vie.",
     "Master de psychologie clinique, du développement ou de neuropsychologie selon les publics accueillis.",
     "Évaluations, projets personnalisés, soutien aux familles, analyse de pratiques avec les équipes, articulation avec les partenaires de soin et scolaires.",
     "Instituts médico-éducatifs, services d'éducation spéciale et de soins à domicile, foyers d'accueil médicalisés, établissements de service d'aide par le travail.",
     "Poste souvent isolé : la supervision et l'analyse de pratiques y sont d'autant plus nécessaires."),

    ("data-comportement", "Analyste comportemental / sciences comportementales", "Numérique",
     "Appliquer les sciences du comportement aux politiques publiques ou aux organisations : mieux concevoir formulaires, campagnes, parcours et incitations.",
     "Master de psychologie cognitive, sociale ou d'économie comportementale ; solide maîtrise des statistiques et de l'expérimentation.",
     "Conception et analyse d'expérimentations de terrain, tests A/B, revue de littérature, restitution aux décideurs, évaluation d'impact.",
     "Unités « nudge » publiques, ministères, collectivités, cabinets de conseil, entreprises, organisations internationales.",
     "Champ où la rigueur méthodologique est décisive : plusieurs effets popularisés se sont révélés non réplicables, et l'éthique des incitations reste un débat ouvert."),
]

# (id, titre, contenu_html)
PARCOURS_ETUDES = [
    ("licence", "La licence de psychologie", """
<p>La licence dure trois ans et couvre l'ensemble des grands domaines : psychologie cognitive, sociale, du
développement, clinique, différentielle, neurosciences, mais aussi <strong>statistiques et méthodologie</strong>,
qui occupent une place bien plus importante que ne l'imaginent la plupart des nouveaux étudiants.</p>

<p>C'est le principal motif d'abandon en première année : beaucoup arrivent en s'attendant à parler
d'accompagnement et découvrent des tests statistiques, des protocoles expérimentaux et de la physiologie.
Pourtant, c'est exactement cette formation qui distingue un psychologue d'un praticien autoproclamé.</p>

<p>La licence seule ne permet pas d'exercer ni de porter le titre de psychologue. Elle ouvre en revanche vers
d'autres masters (ressources humaines, sciences de l'éducation, santé publique, sciences cognitives) et vers
des concours de la fonction publique.</p>
"""),

    ("master", "Le master : le passage décisif", """
<p>Le master, en deux ans, est le moment de la spécialisation et le véritable goulot d'étranglement du
parcours : la sélection à l'entrée est forte, et tous les titulaires de licence n'y accèdent pas.</p>

<p>C'est le master professionnel, avec ses stages, qui donne accès au <strong>titre de psychologue</strong>. Le
choix de la spécialité (clinique, neuropsychologie, travail, développement, santé, cognitive) oriente
largement la suite, même si des réorientations restent possibles par la formation continue.</p>

<p>Conseil pratique valable dès la première année : multipliez les expériences de terrain — bénévolat
associatif, animation, aide aux devoirs, service civique, emploi en établissement de soin. Les dossiers de
master valorisent fortement cette confrontation au réel, et elle vous dira surtout si ce métier vous
correspond vraiment.</p>
"""),

    ("titre", "Le titre de psychologue et la déontologie", """
<p>En France, le titre de psychologue est protégé par la loi de 1985 : l'usurper est un délit. Il suppose un
cursus complet de cinq ans incluant un mémoire de recherche et un stage professionnel, puis une inscription
au répertoire national des professionnels de santé.</p>

<p>Le <strong>Code de déontologie des psychologues</strong> encadre l'exercice : respect de la personne et de
son consentement, secret professionnel, compétence limitée à son champ de formation, indépendance
professionnelle, responsabilité des instruments utilisés et des écrits produits. Il n'a pas force de loi en
lui-même, mais il est régulièrement invoqué par les juridictions.</p>

<p>Dans l'espace francophone, les cadres diffèrent : en Belgique, la Commission des psychologues gère
l'inscription obligatoire ; en Suisse, la loi fédérale sur les professions de la psychologie encadre les
titres postgrades ; au Québec, l'Ordre des psychologues délivre le permis d'exercice et impose une formation
continue obligatoire.</p>
"""),

    ("autres-voies", "Travailler avec la psychologie sans être psychologue", """
<p>Beaucoup de métiers s'appuient sur des connaissances en psychologie sans relever du titre : éducateur
spécialisé, assistant de service social, conseiller en insertion, formateur, chargé de prévention, médiateur
familial, animateur en gérontologie, chargé d'études en sciences comportementales, concepteur pédagogique,
chercheur en sciences cognitives.</p>

<p>Ces voies passent par des diplômes d'État, des BUT, des licences professionnelles ou des masters non
psychologiques. Elles offrent souvent des débouchés plus nombreux et un accès plus rapide à l'emploi.</p>

<div class="warn-box"><strong>Vigilance sur les formations privées.</strong> De nombreux organismes proposent
des certifications en « psychopraticien », « thérapeute holistique », « coach en développement personnel » ou
« analyste comportemental », parfois très coûteuses. Aucune ne confère le titre de psychologue ni celui de
psychothérapeute. Avant de vous engager, vérifiez : le diplôme est-il reconnu par l'État ? Quel titre
légal permet-il d'exercer ? Que dit précisément le contrat sur les débouchés promis ?</div>
"""),
]
