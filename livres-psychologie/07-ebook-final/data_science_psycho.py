# -*- coding: utf-8 -*-
"""Catégorie 27 — Science psychologique : tests sur le cerveau, techniques, caché, usages."""

IMG = "../../05-larousse-illustre-complet/illustrations/wikimedia"
PDF = "../../06-pdf-domaine-public"

CATEGORY_SCIENCE = {
    "id": "27-science-psychologique",
    "icon": "🔬", "color": "vert", "num": "27",
    "title": "Science psychologique",
    "subtitle": "Tests sur le cerveau, techniques, ce qui était caché, et ce qu'on peut réellement en faire",
    "read_time": "24 min",
    "objectives": [
        "Raconter les tests et lésions qui ont permis de cartographier le cerveau, sans les romancer",
        "Distinguer les techniques (EEG, IRMf, PET, TMS, lésion, cellule unique) et ce que chacune peut — et ne peut pas — montrer",
        "Reconnaître ce qui a été caché, exagéré ou simplement faux : phrénologie, 10 %, cerveau gauche/droit",
        "Relier ces faits aux fiches déjà présentes (neurosciences, expériences, cas, mythes) et savoir où regarder les images et les projets ouverts",
    ],
    "sections": [
        ("Une science du cerveau, pas une magie du crâne",
         "<p>La psychologie est devenue scientifique le jour où elle a accepté de <strong>mesurer</strong> "
         "et de <strong>mettre à l'épreuve</strong> ce que le cerveau fait — pas le jour où elle a dessiné "
         "des bosses sur un buste. Cette fiche rassemble les <em>tests</em> qui ont ouvert le crâne "
         "(au propre et au figuré), les <em>techniques</em> encore utilisées, ce que l'on a longtemps "
         "dissimulé ou mal raconté, et ce que l'on peut <em>faire</em> de ce savoir : apprendre, rééduquer, "
         "piloter une interface, ou simplement cesser de croire n'importe quoi.</p>"
         "<p>Elle ne remplace pas la fiche "
         "<a href=\"08-neurosciences.html\">Neurosciences</a> : elle la relie. Les protocoles complets "
         "sont dans les <a href=\"../references/experiences.html\">expériences</a> ; les patients "
         "singuliers dans les <a href=\"../references/cas.html\">cas</a> ; les neuromythes dans les "
         "<a href=\"../references/mythes.html\">idées reçues</a>. La "
         "<a href=\"../decouverte.html\">zone de découverte</a> rassemble les planches, les vraies "
         "images et les projets ouverts.</p>"
         "<p>Deux précautions. Première : <strong>aucun test décrit ici n'est un diagnostic</strong>, "
         "et rien de ce site ne remplace un soin. Seconde : un cerveau n'est pas une carte de "
         "territoires étanches. Les fonctions émergent de <em>réseaux</em>. Localiser n'est pas "
         "réduire une personne à une bosse, une aire ou un pourcentage.</p>"),
        ("Ce que les premiers tests ont réellement montré",
         "<p>Avant l'imagerie, on n'avait que trois portes : la <strong>lésion</strong> (un accident, "
         "une guerre, une opération), la <strong>stimulation</strong> (un courant sur le cortex exposé), "
         "et la <strong>mesure du temps</strong> (Donders, Helmholtz). Chacune a laissé une leçon encore vraie.</p>"
         "<ul>"
         "<li><strong>Broca, 1861</strong> — Le patient Leborgne, dit « Tan », ne peut plus articuler "
         "qu'une syllabe. L'autopsie montre une lésion frontale gauche. Première démonstration "
         "anatomique qu'une fonction mentale a une adresse. "
         "<a href=\"../references/experiences.html#broca-tan\">Fiche de l'expérience</a> · "
         "<a href=\"18-langage.html\">Psycholinguistique</a>.</li>"
         "<li><strong>Wernicke, 1874</strong> — L'aphasie opposée : le discours coule, le sens s'est "
         "vidé. Deux aires, un même réseau du langage. "
         "<a href=\"../references/experiences.html#wernicke-aphasie\">Protocole</a>.</li>"
         "<li><strong>Fritsch et Hitzig, 1870</strong> — Un faible courant sur le cortex d'un chien "
         "fait bouger la patte opposée. Le cortex moteur existe, il est organisé. "
         "<a href=\"../references/experiences.html#fritsch-hitzig\">Planche</a>.</li>"
         "<li><strong>Penfield, années 1930-1950</strong> — À Montréal, pendant des opérations "
         "d'épilepsie, le patient est éveillé. Stimuler le cortex dessine l'<em>homoncule</em> : "
         "mains et lèvres énormes, dos minuscule. La carte du corps n'est pas le corps. "
         "<a href=\"../references/experiences.html#penfield-homoncule\">Homoncule</a>.</li>"
         "<li><strong>Phineas Gage, 1848</strong> — Une barre à mine traverse le frontal. Il marche "
         "et parle ; la planification et le jugement social sont atteints. Premier grand argument "
         "clinique sur le cortex préfrontal — ensuite beaucoup trop romancé. "
         "<a href=\"../references/experiences.html#phineas-gage\">Le cas</a> · "
         "<a href=\"../references/cas.html\">Cas cliniques</a>.</li>"
         "<li><strong>H.M., 1953-2008</strong> — Ablation des hippocampes. Plus de souvenirs "
         "nouveaux conscients, mais l'apprentissage moteur continue. La mémoire n'est pas un tiroir. "
         "<a href=\"../references/experiences.html#patient-hm\">Patient H.M.</a>.</li>"
         "<li><strong>Cerveau divisé, Sperry et Gazzaniga</strong> — Section du corps calleux. "
         "Deux hémisphères, deux accès, un « interprète » qui invente des raisons. Prix Nobel 1981, "
         "et mythe populaire du cerveau gauche/droit. "
         "<a href=\"../references/experiences.html#split-brain\">Split-brain</a>.</li>"
         "</ul>"
         "<p>Ces tests ne « prouvent pas le destin ». Ils montrent des <em>dissociations</em> : "
         "quand A survit et B disparaît, A et B ne sont pas le même système. C'est la logique de "
         "toute la neuropsychologie.</p>"),
        ("Techniques : ce que chacune voit, et ce qu'elle invente",
         "<p>Une technique n'est pas une fenêtre transparente. Chacune a une résolution, un délai, "
         "un artefact. Confondre l'outil et l'objet est la première erreur de lecture d'une « étude cerveau ».</p>"
         "<ul>"
         "<li><strong>EEG</strong> (Berger, 1924-1929) — Électricité du scalp, milliseconde près, "
         "localisation floue. Idéal pour le sommeil, l'attention, les potentiels évoqués (P300, N400, "
         "MMN). <a href=\"../references/experiences.html#berger-eeg\">Berger</a> · "
         "<a href=\"../references/experiences.html#p300\">P300</a>.</li>"
         "<li><strong>MEG</strong> — Champs magnétiques, meilleure localisation que l'EEG, plus rare "
         "et plus coûteuse.</li>"
         "<li><strong>PET</strong> — Un traceur radioactif révèle métabolisme ou récepteurs. "
         "Historiquement fondateur, aujourd'hui surtout moléculaire (dopamine, amyloïde).</li>"
         "<li><strong>IRMf</strong> — Le signal BOLD suit l'oxygène du sang, avec 4 à 6 secondes de "
         "retard. On ne « voit pas la pensée » : on voit une corrélation hémodynamique. "
         "Voir aussi <a href=\"08-neurosciences.html\">signal BOLD</a>.</li>"
         "<li><strong>DTI / tractographie</strong> — Diffusion de l'eau le long de la myéline. "
         "Dessine des faisceaux, pas des intentions. Le "
         "<a href=\"https://www.humanconnectome.org\" target=\"_blank\" rel=\"noopener\">Human Connectome Project</a> "
         "en a fait une carte publique.</li>"
         "<li><strong>TMS / tDCS</strong> — Perturber ou faciliter une région depuis l'extérieur. "
         "Seule la TMS a une réelle valeur causale (et clinique, dans certaines dépressions). "
         "<a href=\"../references/experiences.html#tms-pascual\">TMS</a>.</li>"
         "<li><strong>Stimulation profonde (DBS)</strong> — Électrodes implantées, notamment dans "
         "la maladie de Parkinson (travaux d'Alim-Louis Benabid à Grenoble). "
         "<a href=\"../references/experiences.html#dbs-benabid\">DBS</a>.</li>"
         "<li><strong>Cellule unique</strong> — Hubel et Wiesel dans le cortex visuel du chat : "
         "une colonne, une orientation. "
         "<a href=\"../references/experiences.html#hubel-wiesel-colonnes\">Colonnes d'orientation</a>.</li>"
         "<li><strong>Optogénétique</strong> — Allumer ou éteindre une population de neurones avec "
         "la lumière (Deisseroth, Boyden). Révolution chez l'animal ; pas un traitement grand public. "
         "<a href=\"../references/experiences.html#optogenetique\">Optogénétique</a>.</li>"
         "<li><strong>Test de Wada</strong> — Anesthésier un hémisphère pour savoir où habite le "
         "langage avant une chirurgie. "
         "<a href=\"../references/experiences.html#wada-test\">Wada</a>.</li>"
         "</ul>"
         "<p>Règle de lecture : <strong>corrélation n'est pas causation</strong>, et une tache colorée "
         "sur une IRMf n'est pas une explication. La fiche "
         "<a href=\"01-fondamentaux.html\">Fondamentaux</a> et le cours de "
         "<a href=\"../methodes.html\">méthodes</a> servent précisément à ne pas se faire abuser.</p>"),
        ("Ce qui était caché, exagéré, ou simplement faux",
         "<p>La science du cerveau a aussi une cave. On y range les doctrines mortes, les techniques "
         "brutales, et les histoires trop belles pour être exactes.</p>"
         "<ul>"
         "<li><strong>La phrénologie</strong> (Gall, Spurzheim) — Lire le caractère dans les bosses "
         "du crâne. Entièrement fausse. Elle a pourtant laissé une idée juste : les fonctions ne sont "
         "pas répandues comme du beurre. L'erreur était la <em>méthode</em>, pas l'intuition de "
         "départ. Planche dans la <a href=\"../decouverte.html#cache\">zone cachée</a>.</li>"
         "<li><strong>« On n'utilise que 10 % du cerveau »</strong> — Faux. L'imagerie, le "
         "métabolisme et les lésions montrent le contraire. Une petite lésion suffit à tout faire "
         "basculer. <a href=\"../references/mythes.html\">Mythes</a>.</li>"
         "<li><strong>Cerveau gauche rationnel / cerveau droit créatif</strong> — Le split-brain a "
         "été mal traduit en magazine. Les deux hémisphères coopèrent en permanence. La "
         "spécialisation existe (langage plutôt à gauche chez la plupart) ; le cliché n'existe pas.</li>"
         "<li><strong>Styles d'apprentissage visuel / auditif</strong> — Croyance pédagogique "
         "robuste, effet scientifique quasi nul. Le "
         "<a href=\"../apprendre.html\">guide d'apprentissage</a> s'appuie sur le rappel actif, "
         "pas sur un « profil ».</li>"
         "<li><strong>Lashley et l'équiponentialité</strong> — Après avoir lésé le cortex de rats, "
         "Lashley conclut que la mémoire est partout. Il avait tort sur l'extrême, raison sur un "
         "point : une fonction complexe n'est pas un point unique. "
         "<a href=\"../references/experiences.html#lashley-masse\">Loi de masse</a>.</li>"
         "<li><strong>La lobotomie</strong> — Une technique réelle, massive au milieu du XXe siècle, "
         "présentée comme un progrès. Elle a détruit des vies. La cacher serait une autre violence : "
         "il faut la nommer comme avertissement éthique, pas comme modèle.</li>"
         "<li><strong>Les récits embellis</strong> — Gage « devenu un monstre », Kitty Genovese "
         "et « 38 témoins », Stanford comme preuve universelle. Les archives corrigent. Voir "
         "<a href=\"../references/experiences.html#prison-stanford\">Stanford</a> et "
         "<a href=\"../references/experiences.html#effet-temoin\">l'effet du témoin</a>.</li>"
         "</ul>"
         "<p>La zone de découverte a une section entière pour ces planches : ce que l'on montrait, "
         "ce que l'on taisait, et ce que les données disent maintenant.</p>"),
        ("Comment le cerveau fonctionne — le modèle actuel, en français clair",
         "<p>Le tableau contemporain, résumé sans jargon inutile :</p>"
         "<ol>"
         "<li><strong>Le cerveau prédit.</strong> Il ne développe pas une photo du monde : il "
         "anticipe, puis corrige l'erreur (traitement prédictif). D'où les illusions, le "
         "<a href=\"../references/experiences.html#mcgurk\">McGurk</a>, le "
         "<a href=\"../references/experiences.html#gorille-invisible\">gorille invisible</a>.</li>"
         "<li><strong>Il travaille en réseaux, pas en tiroirs.</strong> Le réseau du mode par "
         "défaut (Raichle) s'allume quand on n'a « rien à faire » : rumination, souvenir, projection. "
         "<a href=\"../references/experiences.html#raichle-reseau-defaut\">DMN</a>.</li>"
         "<li><strong>La mémoire est multiple.</strong> H.M. l'a prouvé : déclarative vs procédurale, "
         "hippocampe vs habitudes. Ebbinghaus avait déjà mesuré l'oubli. "
         "<a href=\"../references/experiences.html#ebbinghaus-oubli\">Courbe de l'oubli</a>.</li>"
         "<li><strong>L'émotion n'est pas l'ennemie de la raison.</strong> Le test de Iowa "
         "(Damasio, Bechara) : sans marqueurs somatiques, on décide plus mal, pas plus « logiquement ». "
         "<a href=\"../references/experiences.html#damasio-iowa-gambling\">Iowa gambling</a> · "
         "<a href=\"07-emotions.html\">Émotions</a>.</li>"
         "<li><strong>La plasticité est réelle et limitée.</strong> Merzenich, Ramachandran, "
         "la rééducation contrainte de Taub : le cortex se réorganise, surtout avec l'usage répété. "
         "On ne « reprogramme » pas un cerveau en un week-end. "
         "<a href=\"../references/experiences.html#merzenich-plasticite\">Plasticité</a>.</li>"
         "<li><strong>La conscience arrive en retard.</strong> Libet mesure un potentiel de "
         "préparation avant le moment où l'on croit décider. Cela ne clôt pas le débat du libre "
         "arbitre ; cela interdit le mythe d'un moi transparent. "
         "<a href=\"../references/experiences.html#libet-intention\">Libet</a> · "
         "<a href=\"../references/debats.html\">Débats</a>.</li>"
         "<li><strong>Voir n'est pas un canal unique.</strong> Deux voies visuelles (Goodale et "
         "Milner) : l'une dit « quoi », l'autre « comment ». Le blindsight (Weiskrantz) : on peut "
         "orienter la main vers un objet « non vu ». "
         "<a href=\"../references/experiences.html#two-streams-goodale\">Deux voies</a> · "
         "<a href=\"../references/experiences.html#blindsight\">Blindsight</a>.</li>"
         "</ol>"
         "<p>Pour le détail anatomique (lobes, synapses, neurotransmetteurs), rester sur "
         "<a href=\"08-neurosciences.html\">Neurosciences</a>. Pour les biais qui déforment "
         "l'interprétation, <a href=\"../references/biais.html\">biais</a>.</p>"),
        ("Ce qu'on peut en faire — usages réels, pas promesses",
         "<p>Le savoir sur le cerveau n'est utile que s'il change une pratique. Voici ce qui tient, "
         "côté quotidien et côté clinique, sans vendre de miracle.</p>"
         "<ul>"
         "<li><strong>Apprendre.</strong> Rappel actif, espacement, sommeil. Ce n'est pas une "
         "astuce YouTube : c'est la courbe d'Ebbinghaus plus un siècle de réplications. "
         "<a href=\"../apprendre.html\">Apprendre</a> · "
         "<a href=\"../revision.html\">Révision espacée</a> · "
         "<a href=\"13-education.html\">Éducation</a>.</li>"
         "<li><strong>Attention.</strong> Le gorille invisible et l'effet cocktail party disent "
         "la même chose : on rate ce qu'on n'a pas décidé de regarder. Conséquence concrète : "
         "une seule tâche critique à la fois (conduite, soin, examen). "
         "<a href=\"03-cognitive.html\">Cognitive</a> · "
         "<a href=\"../laboratoire.html\">Laboratoire</a>.</li>"
         "<li><strong>Rééducation.</strong> Après un AVC, l'usage forcé du membre atteint "
         "(thérapie contrainte) exploite la plasticité. Le miroir de Ramachandran soulage "
         "certains membres fantômes. "
         "<a href=\"../references/experiences.html#ramachandran-miroir\">Boîte à miroir</a>.</li>"
         "<li><strong>Interfaces cerveau-machine.</strong> Le P300, les implants moteurs, les "
         "exosquelettes expérimentaux : des personnes peuvent épeler ou bouger un curseur. "
         "Ce n'est pas encore un clavier pour tout le monde. "
         "<a href=\"../references/experiences.html#p300\">P300</a>.</li>"
         "<li><strong>Stimulation thérapeutique.</strong> DBS dans Parkinson (et quelques "
         "indications encadrées). TMS répétitive dans certaines dépressions résistantes. "
         "Pas un casque grand public « pour booster le QI ».</li>"
         "<li><strong>Sommeil.</strong> Le système glymphatique et la consolidation mnésique "
         "rendent la nuit plus rentable qu'une heure volée. "
         "<a href=\"14-sante.html\">Santé</a> · "
         "<a href=\"../pratique.html\">Fiches pratiques</a>.</li>"
         "<li><strong>Esprit critique.</strong> Savoir qu'une IRMf est un signal lent, qu'une "
         "lésion n'est pas une destinée, et qu'un mythe se vend mieux qu'une taille d'effet : "
         "c'est déjà une compétence civique. "
         "<a href=\"26-politique.html\">Politique et croyances</a>.</li>"
         "</ul>"
         "<p>Ce que l'on <em>ne</em> peut pas en faire : lire les pensées, détecter un menteur "
         "au tribunal par IRM, « débloquer » 90 % d'un cerveau, choisir l'école de son enfant "
         "selon un profil hémisphérique.</p>"),
        ("La zone de découverte : images, planches, projets ouverts",
         "<p>La <a href=\"../decouverte.html\">zone de découverte</a> est faite pour rester, "
         "pas pour survoler. On y trouve :</p>"
         "<ul>"
         "<li>des <strong>planches d'expériences</strong> — le protocole dessiné, le résultat, "
         "la source, le lien vers la fiche ;</li>"
         "<li>une <strong>galerie d'images réelles</strong> (Wikimedia Commons, domaine public "
         "ou licence libre) : Cajal, Golgi, Broca, Penfield, EEG, IRM, phrénologie ;</li>"
         "<li>les <strong>projets complets</strong> où l'on peut soi-même ouvrir des données : "
         "Human Connectome, OpenNeuro, Allen Brain Map, BigBrain / EBRAINS, NeuroVault, Neurosynth ;</li>"
         "<li>la cave : ce qui était caché, faux, ou présenté comme une évidence.</li>"
         "</ul>"
         "<p>Les crédits de chaque fichier sont sur la page "
         "<a href=\"../credits.html\">crédits</a>. Rien n'est inventé, rien n'est volé à un "
         "article payant : on cite, on lie, on montre ce qui est libre.</p>"),
        ("Fils tendus vers le reste du site",
         "<p>Cette catégorie n'est pas une île. Les lectures qui la rendent utile :</p>"
         "<ul>"
         "<li><a href=\"08-neurosciences.html\">Neurosciences</a> — anatomie, synapses, lobes, mythes biologiques.</li>"
         "<li><a href=\"03-cognitive.html\">Cognitive</a> — attention, mémoire, perception, Stroop, Miller.</li>"
         "<li><a href=\"18-langage.html\">Langage</a> — Broca, Wernicke, lecture, recyclage neuronal.</li>"
         "<li><a href=\"07-emotions.html\">Émotions</a> — Darwin, système limbique, décision.</li>"
         "<li><a href=\"19-psychometrie.html\">Psychométrie</a> — ce qu'un test mesure vraiment.</li>"
         "<li><a href=\"01-fondamentaux.html\">Méthode</a> — réplication, p-hacking, lire une étude.</li>"
         "<li><a href=\"../references/experiences.html\">Expériences</a> · "
         "<a href=\"../references/cas.html\">Cas</a> · "
         "<a href=\"../references/mythes.html\">Mythes</a> · "
         "<a href=\"../laboratoire.html\">Laboratoire jouable</a>.</li>"
         "<li><a href=\"../emploi-du-temps.html\">Cours de 50 minutes</a> — module Neurosciences.</li>"
         "<li><a href=\"../quiz/quiz.html?id=science-psychologique\">Quiz de cette fiche</a> · "
         "<a href=\"../quiz/quiz.html?id=neurosciences\">Quiz neurosciences</a>.</li>"
         "</ul>"),
    ],
    "figures": [
        "portrait-broca.jpg:Paul Broca",
        "portrait-wernicke.jpg:Carl Wernicke",
        "portrait-charcot.jpg:Jean-Martin Charcot",
        "portrait-fechner.jpg:Gustav Fechner",
        "portrait-helmholtz.jpg:Hermann von Helmholtz",
    ],
    "pdfs": [
        {"title": "Leçons sur les maladies du système nerveux", "author": "Jean-Martin Charcot (1884)",
         "path": f"{PDF}/psychopathologie/charcot-lecons-systeme-nerveux-1884.pdf",
         "desc": "La clinique de la Salpêtrière : observer, décrire, localiser — avant l'imagerie."},
        {"title": "Précis de psychologie", "author": "William James (1909)",
         "path": f"{PDF}/psychologie-generale/james-precis-de-psychologie-1909.pdf",
         "desc": "Cerveau, habitude, conscience : le fonctionnalisme qui refuse de séparer l'esprit du corps."},
    ],
    "fun_fact": "Cajal et Golgi ont partagé le Nobel 1906 en se détestant scientifiquement : Golgi voyait un réseau continu, Cajal des neurones séparés par des synapses. C'est Cajal qui avait raison — et ses dessins à l'encre restent parmi les plus belles planches jamais faites d'un cerveau.",
    "flashcards": [
        ("Que démontre le cas de Leborgne (« Tan ») ?",
         "Qu'une lésion frontale gauche peut détruire l'articulation du langage tout en laissant d'autres fonctions intactes — première localisation anatomique d'une fonction mentale."),
        ("Pourquoi l'IRMf ne « photographie » pas la pensée ?",
         "Elle mesure un signal BOLD (oxygène du sang) décalé de plusieurs secondes, corrélé à l'activité — pas les neurones eux-mêmes, et pas une cause à elle seule."),
        ("Quelle leçon tire-t-on du patient H.M. ?",
         "La mémoire n'est pas unique : sans hippocampe on perd les souvenirs déclaratifs nouveaux, pas l'apprentissage de gestes."),
        ("Qu'est-ce que l'homoncule de Penfield ?",
         "La carte corticale du corps, déformée selon la finesse sensorielle ou motrice : mains et lèvres énormes, dos minuscule."),
        ("Cite trois neuromythes encore vendus.",
         "On n'utilise que 10 % du cerveau ; cerveau gauche rationnel / droit créatif ; styles d'apprentissage visuel ou auditif comme loi pédagogique."),
        ("À quoi sert réellement un EEG ?",
         "À suivre l'activité électrique avec une excellente résolution temporelle : sommeil, attention, potentiels évoqués — pas à localiser précisément une pensée."),
        ("Que montre le test de Iowa ?",
         "Sans signaux corporels liés aux expériences passées, les décisions deviennent plus pauvres : l'émotion participe à la raison, elle ne s'y oppose pas."),
        ("Nomme trois projets ouverts pour voir de vrais cerveaux.",
         "Human Connectome Project, OpenNeuro, Allen Brain Map — plus BigBrain / EBRAINS, NeuroVault et Neurosynth."),
    ],
}
