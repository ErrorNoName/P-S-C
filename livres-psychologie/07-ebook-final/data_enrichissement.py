# -*- coding: utf-8 -*-
"""Enrichissement des 16 catégories fondatrices : sections d'approfondissement,
idées reçues, chiffres clés et flashcards supplémentaires."""

# EXTRA[cat_id] = {
#   "sections": [(titre, html), ...],
#   "mythes": [(idée reçue, réalité), ...],
#   "chiffres": [(valeur, libellé), ...],
#   "flashcards": [(q, r), ...],
# }

EXTRA = {
    "01-fondamentaux": {
        "sections": [
            ("La crise de la réplication et la réforme de la discipline",
             "<p>En 2015, le <em>Reproducibility Project</em> a tenté de reproduire 100 études publiées dans les meilleures revues "
             "de psychologie. Seules <strong>36 %</strong> ont donné un résultat significatif, et les tailles d'effet étaient en "
             "moyenne divisées par deux. Ce constat a provoqué la plus grande remise en question méthodologique de l'histoire de la discipline.</p>"
             "<p>Les causes sont aujourd'hui bien identifiées :</p>"
             "<ul>"
             "<li><strong>Le p-hacking</strong> : tester de multiples analyses jusqu'à obtenir p &lt; 0,05, sans le déclarer.</li>"
             "<li><strong>HARKing</strong> (<em>Hypothesizing After the Results are Known</em>) : présenter une hypothèse "
             "formulée après coup comme si elle avait été posée au départ.</li>"
             "<li><strong>Le biais de publication</strong> : les résultats négatifs ne sont pas publiés, ce qui gonfle "
             "artificiellement l'apparente solidité des effets (le « tiroir à résultats »).</li>"
             "<li><strong>La faible puissance statistique</strong> : des échantillons trop petits produisent des effets surestimés.</li>"
             "</ul>"
             "<p>Les réponses apportées sont considérables : <strong>préenregistrement</strong> des hypothèses et des analyses avant "
             "recueil des données, <strong>rapports enregistrés</strong> (la revue accepte l'article sur la base du protocole, avant "
             "de connaître les résultats), partage systématique des données et du code, réplications à grande échelle multi-laboratoires, "
             "et exigence de tailles d'échantillon justifiées. La psychologie est devenue, paradoxalement, l'une des sciences les plus "
             "rigoureuses sur ces questions : elle a regardé son problème en face.</p>"),
            ("Lire une étude sans se faire abuser",
             "<p>Six réflexes permettent d'évaluer rapidement la solidité d'un résultat rapporté dans les médias :</p>"
             "<ol>"
             "<li><strong>Quel est le type d'étude ?</strong> Un essai randomisé contrôlé &gt; une étude longitudinale &gt; une étude "
             "transversale &gt; une étude de cas. Une méta-analyse de bonne qualité les surplombe toutes.</li>"
             "<li><strong>Combien de participants ?</strong> 30 participants dans un design complexe ne permettent aucune conclusion générale.</li>"
             "<li><strong>Qui a été étudié ?</strong> Des étudiants en psychologie de 20 ans ne représentent pas l'humanité (biais WEIRD).</li>"
             "<li><strong>Corrélation ou causalité ?</strong> Seule la randomisation autorise une conclusion causale.</li>"
             "<li><strong>Quelle taille d'effet ?</strong> « Significatif » ne veut pas dire « important ». Un effet de d = 0,1 "
             "statistiquement significatif sur 50 000 personnes est négligeable en pratique.</li>"
             "<li><strong>A-t-elle été répliquée ?</strong> Un résultat unique et spectaculaire mérite prudence par défaut.</li>"
             "</ol>"),
            ("Les grandes revues et sources fiables",
             "<p>Pour aller aux sources sans se perdre :</p>"
             "<ul>"
             "<li><strong>Bases de données</strong> : PubMed (biomédical et santé mentale), PsycINFO (référence en psychologie), "
             "Google Scholar (large mais peu filtré), Cairn et Persée pour la production francophone.</li>"
             "<li><strong>Revues systématiques</strong> : Cochrane pour les interventions en santé, Campbell Collaboration pour "
             "les interventions sociales et éducatives.</li>"
             "<li><strong>Recommandations officielles</strong> : Haute Autorité de Santé (France), NICE (Royaume-Uni), APA (États-Unis).</li>"
             "<li><strong>Prépublications</strong> : PsyArXiv donne accès aux travaux avant relecture — rapides mais non validés.</li>"
             "</ul>"
             "<p>Signal de qualité méthodologique : la présence d'un préenregistrement (badge OSF), d'un accès aux données brutes, "
             "et d'une déclaration de conflits d'intérêts.</p>"),
        ],
        "mythes": [
            ("Nous n'utilisons que 10 % de notre cerveau.",
             "Faux. L'imagerie montre une activité dans l'ensemble du cerveau au cours d'une journée. Aucune région n'est inutile : une lésion, même minime, entraîne des conséquences mesurables."),
            ("La psychologie, c'est du bon sens habillé de jargon.",
             "Le bon sens produit des affirmations contradictoires (« qui se ressemble s'assemble » et « les opposés s'attirent »). La psychologie tranche par l'expérimentation, et ses résultats sont souvent contre-intuitifs."),
            ("Un psychologue peut lire dans les pensées.",
             "Aucune technique ne le permet. Un psychologue observe, interroge, mesure et formule des hypothèses qu'il vérifie — comme tout scientifique ou clinicien."),
        ],
        "chiffres": [
            ("1879", "Naissance officielle de la psychologie scientifique"),
            ("36 %", "Taux de réplication du Reproducibility Project (2015)"),
            ("12 %", "Part de l'humanité représentée par les échantillons WEIRD"),
            ("p < 0,05", "Seuil conventionnel — et très critiqué — de significativité"),
        ],
        "flashcards": [
            ("Qu'est-ce que le p-hacking ?", "Tester de multiples analyses jusqu'à obtenir un résultat significatif, sans le déclarer."),
            ("Quel design permet seul de conclure à une causalité ?", "L'essai randomisé contrôlé, car la randomisation neutralise les variables confondues."),
            ("Qu'apporte le préenregistrement ?", "Il fige hypothèses et analyses avant le recueil des données, ce qui empêche le HARKing et le p-hacking."),
        ],
    },
    "02-histoire": {
        "sections": [
            ("Les précurseurs oubliés et la psychologie non occidentale",
             "<p>L'histoire officielle commence souvent à Leipzig en 1879. C'est commode, mais incomplet.</p>"
             "<ul>"
             "<li><strong>Avicenne</strong> (980-1037) décrit des troubles mentaux, le rôle du sommeil et propose des interventions "
             "psychologiques documentées, dont un diagnostic de mélancolie amoureuse établi par la variation du pouls.</li>"
             "<li><strong>Al-Balkhi</strong> (IXe siècle) distingue déjà les troubles du corps et de l'âme et décrit des formes "
             "d'anxiété, d'obsession et de dépression avec des propositions thérapeutiques.</li>"
             "<li><strong>Le bouddhisme</strong> a développé pendant 2 500 ans une psychologie de l'attention et de la souffrance "
             "dont l'Occident a extrait, tardivement, les protocoles de pleine conscience.</li>"
             "<li><strong>La médecine chinoise classique</strong> et l'<strong>Ayurveda</strong> proposaient des typologies "
             "tempéramentales bien avant les modèles européens.</li>"
             "</ul>"
             "<p>Ignorer ces traditions n'est pas neutre : cela renforce l'illusion que la psychologie est une invention purement "
             "occidentale, ce qui alimente ensuite le biais WEIRD dans le choix des objets d'étude.</p>"),
            ("Les femmes effacées de l'histoire de la discipline",
             "<p>Elles ont été nombreuses, et systématiquement minorées :</p>"
             "<ul>"
             "<li><strong>Mary Whiton Calkins</strong> a réalisé l'intégralité d'un doctorat à Harvard ; l'université lui a refusé "
             "le diplôme parce qu'elle était une femme. Elle est devenue présidente de l'APA en 1905.</li>"
             "<li><strong>Margaret Floy Washburn</strong>, première femme docteure en psychologie aux États-Unis (1894), a fondé "
             "la psychologie comparée moderne.</li>"
             "<li><strong>Mary Ainsworth</strong> a conçu le protocole qui a rendu la théorie de l'attachement mesurable — le nom "
             "retenu reste souvent celui de Bowlby.</li>"
             "<li><strong>Bluma Zeigarnik</strong>, <strong>Anna Freud</strong>, <strong>Melanie Klein</strong>, "
             "<strong>Karen Horney</strong> (qui a contesté très tôt la théorie freudienne de l'envie du pénis), "
             "<strong>Mamie Phipps Clark</strong> (dont les travaux ont pesé sur la fin de la ségrégation scolaire américaine) : "
             "toutes ont produit des contributions majeures.</li>"
             "</ul>"),
            ("Les pages sombres qu'il faut connaître",
             "<p>Une discipline qui ignore ses dérives les reproduit :</p>"
             "<ul>"
             "<li><strong>L'eugénisme</strong> : les tests d'intelligence ont servi à justifier des quotas d'immigration, des "
             "stérilisations forcées (plus de 60 000 aux États-Unis) et des politiques racistes, en détournant complètement "
             "l'intention de Binet.</li>"
             "<li><strong>La lobotomie</strong> : environ 40 000 interventions aux États-Unis, un prix Nobel décerné à son "
             "promoteur en 1949, et des milliers de vies détruites.</li>"
             "<li><strong>Les thérapies de conversion</strong>, fondées sur la classification de l'homosexualité comme trouble "
             "mental jusqu'en 1973 (DSM) et 1990 (OMS).</li>"
             "<li><strong>L'étude de Tuskegee</strong> et d'autres recherches sans consentement, qui ont conduit au rapport "
             "Belmont et aux comités d'éthique modernes.</li>"
             "<li><strong>Les expériences d'isolement sensoriel</strong>, financées puis détournées en techniques d'interrogatoire coercitives.</li>"
             "</ul>"),
        ],
        "mythes": [
            ("Freud a découvert l'inconscient.",
             "L'idée circulait bien avant lui (Leibniz, Schopenhauer, Carus, Janet). Freud en a fait une théorie systématique et une méthode de traitement, ce qui est différent."),
            ("Le behaviorisme est mort en 1959.",
             "Il a perdu son hégémonie théorique, mais ses principes fondent les thérapies comportementales, l'analyse appliquée du comportement et une partie de l'apprentissage automatique."),
            ("La psychologie a progressé de façon linéaire.",
             "Elle avance par ruptures, controverses et retours en arrière. Plusieurs résultats « classiques » des manuels ont été invalidés depuis 2010."),
        ],
        "chiffres": [
            ("1590", "Première apparition du mot « psychologie »"),
            ("180+", "Doctorants formés par Wundt à Leipzig"),
            ("1973", "Retrait de l'homosexualité du DSM"),
            ("1980", "DSM-III : bascule vers des critères opérationnels"),
        ],
        "flashcards": [
            ("Qui fut la première femme présidente de l'APA ?", "Mary Whiton Calkins, en 1905, alors que Harvard lui avait refusé son doctorat."),
            ("Quel médecin médiéval a décrit des troubles anxieux et dépressifs bien avant l'Occident moderne ?", "Al-Balkhi, au IXe siècle, puis Avicenne au XIe siècle."),
            ("Quel prix a récompensé la lobotomie ?", "Le prix Nobel de médecine 1949, attribué à Egas Moniz."),
        ],
    },
    "03-cognitive": {
        "sections": [
            ("Le modèle de la mémoire de travail de Baddeley",
             "<p>La « mémoire à court terme » passive a été remplacée par un système actif à quatre composantes :</p>"
             "<ul>"
             "<li><strong>La boucle phonologique</strong> : stocke et rafraîchit l'information verbale par répétition subvocale. "
             "Sa capacité correspond à ce qu'on peut prononcer en environ 2 secondes — d'où le fait que les mots courts se "
             "retiennent mieux que les mots longs.</li>"
             "<li><strong>Le calepin visuo-spatial</strong> : maintient les images et les positions. Il explique pourquoi on peut "
             "parler au téléphone tout en imaginant un itinéraire, mais difficilement décrire une image en en imaginant une autre.</li>"
             "<li><strong>L'administrateur central</strong> : répartit l'attention, coordonne les deux systèmes précédents, inhibe "
             "les informations non pertinentes. C'est lui qui sature en situation de surcharge.</li>"
             "<li><strong>Le buffer épisodique</strong> (ajouté en 2000) : intègre les informations des différents systèmes et de "
             "la mémoire à long terme en épisodes cohérents.</li>"
             "</ul>"
             "<p>Applications directes : ne pas lire un texte à voix haute pendant que les élèves lisent le même texte (les deux "
             "occupent la boucle phonologique), et présenter les informations complémentaires en image + parole plutôt qu'en "
             "image + texte écrit.</p>"),
            ("Les deux systèmes de pensée",
             "<p>Kahneman a popularisé une distinction devenue centrale :</p>"
             "<ul>"
             "<li><strong>Système 1</strong> : rapide, automatique, parallèle, sans effort, émotionnel, toujours actif. Il reconnaît "
             "un visage, complète « 2 + 2 », détecte l'hostilité dans une voix. Il produit aussi la majorité de nos biais.</li>"
             "<li><strong>Système 2</strong> : lent, séquentiel, coûteux, contrôlé. Il calcule 17 × 24, compare deux contrats, "
             "vérifie un raisonnement. Il est paresseux et accepte volontiers les réponses du système 1.</li>"
             "</ul>"
             "<p>Test classique : une raquette et une balle coûtent 1,10 € ; la raquette coûte 1 € de plus que la balle ; combien "
             "coûte la balle ? Le système 1 répond instantanément 10 centimes. La bonne réponse est 5 centimes. Plus de 50 % des "
             "étudiants des universités les plus sélectives se trompent — non par manque de capacité, mais parce que le système 2 "
             "ne se met pas en marche.</p>"
             "<p>Nuance importante : cette dichotomie est un modèle pédagogique, pas une description anatomique. Il n'existe pas "
             "deux systèmes séparés dans le cerveau.</p>"),
            ("Attention : quatre systèmes distincts",
             "<p>L'attention n'est pas une ressource unique :</p>"
             "<ul>"
             "<li><strong>Attention soutenue</strong> (vigilance) : maintenir la concentration dans la durée. Elle décline "
             "mesurablement après 20 à 30 minutes sur une tâche monotone.</li>"
             "<li><strong>Attention sélective</strong> : filtrer l'information pertinente. C'est elle qui produit la cécité "
             "attentionnelle du gorille invisible.</li>"
             "<li><strong>Attention divisée</strong> : traiter deux sources à la fois. Possible uniquement si l'une des tâches est "
             "automatisée ou si elles mobilisent des modalités différentes.</li>"
             "<li><strong>Attention exécutive</strong> : résoudre les conflits, inhiber une réponse dominante. C'est ce que mesure "
             "l'effet Stroop.</li>"
             "</ul>"
             "<p>Conséquence pratique : dire d'un enfant qu'il « manque d'attention » n'a pas de sens sans préciser laquelle. "
             "Un enfant avec TDAH peut rester six heures sur un jeu — ce n'est pas l'attention qui est déficitaire, c'est sa régulation.</p>"),
            ("Métacognition : savoir ce qu'on sait",
             "<p>La métacognition désigne la connaissance et le contrôle de ses propres processus mentaux. Elle prédit fortement la "
             "réussite des apprentissages, et elle est souvent défaillante.</p>"
             "<p>Le principal piège est l'<strong>illusion de fluence</strong> : un cours bien présenté, relu et surligné donne une "
             "sensation de maîtrise qui ne correspond à rien. Les étudiants privilégient massivement la relecture, la technique la "
             "moins efficace, parce qu'elle procure la sensation la plus agréable. Le rappel actif, inconfortable, est deux fois "
             "plus efficace.</p>"
             "<p>Les <strong>difficultés désirables</strong> (Bjork) formalisent ce paradoxe : ce qui rend l'apprentissage plus "
             "difficile sur le moment — espacer, alterner, se tester, varier les conditions — améliore la rétention à long terme, "
             "au prix d'une performance immédiate plus faible.</p>"),
        ],
        "mythes": [
            ("Nous ne retenons que 10 % de ce que nous lisons et 90 % de ce que nous faisons.",
             "Cette « pyramide de l'apprentissage » n'a aucune source scientifique. Les chiffres ronds ont été inventés et recopiés depuis les années 1960."),
            ("Chacun a un style d'apprentissage (visuel, auditif…) qu'il faut respecter.",
             "L'hypothèse de l'appariement — enseigner selon le style préféré améliore les résultats — a été testée et invalidée à de nombreuses reprises. Varier les modalités aide tout le monde ; s'y enfermer n'apporte rien."),
            ("La mémoire fonctionne comme un enregistrement vidéo.",
             "Elle reconstruit le souvenir à chaque rappel, et le modifie à cette occasion. Se souvenir souvent d'un événement en déforme progressivement le contenu."),
        ],
        "chiffres": [
            ("≈ 4", "Unités réellement maintenues en mémoire de travail (Cowan)"),
            ("2 s", "Capacité de la boucle phonologique en durée de prononciation"),
            ("50 %", "Participants ne voyant pas le gorille invisible"),
            ("20 min", "Durée après laquelle la vigilance décline nettement"),
        ],
        "flashcards": [
            ("Quelles sont les composantes du modèle de Baddeley ?", "Boucle phonologique, calepin visuo-spatial, administrateur central et buffer épisodique."),
            ("Qu'est-ce qu'une difficulté désirable ?", "Une condition qui rend l'apprentissage plus difficile sur le moment mais améliore la rétention à long terme."),
            ("Pourquoi les étudiants préfèrent-ils la relecture ?", "Parce qu'elle produit une illusion de fluence : la facilité ressentie est confondue avec la maîtrise."),
        ],
    },
    "04-sociale": {
        "sections": [
            ("Identité sociale : le moteur du « eux » et du « nous »",
             "<p>Tajfel et Turner ont montré qu'une part de notre estime de soi provient de nos appartenances groupales. D'où trois "
             "processus en chaîne : <strong>catégorisation</strong> (classer le monde en groupes), <strong>identification</strong> "
             "(se définir par l'un d'eux), <strong>comparaison</strong> (avantager son groupe pour valoriser son propre soi).</p>"
             "<p>Les expériences de groupes minimaux montrent que quasiment rien ne suffit : un tirage au sort, une préférence "
             "esthétique déclarée. Les participants distribuent alors les ressources de façon à <strong>maximiser l'écart</strong> "
             "en faveur de leur groupe, quitte à réduire le gain absolu de leur propre camp.</p>"
             "<p>On observe aussi l'<strong>effet d'homogénéité de l'exogroupe</strong> : « ils se ressemblent tous », alors que "
             "notre propre groupe nous paraît riche de nuances. Cet effet suffit à expliquer une grande partie des stéréotypes, "
             "sans même invoquer d'hostilité.</p>"),
            ("Préjugés, discriminations et contact intergroupe",
             "<p>Il faut distinguer trois niveaux : le <strong>stéréotype</strong> (croyance), le <strong>préjugé</strong> "
             "(attitude affective) et la <strong>discrimination</strong> (comportement). On peut discriminer sans hostilité "
             "consciente, par simple application de routines et de normes.</p>"
             "<p>L'<strong>hypothèse du contact</strong> d'Allport reste la piste la mieux validée, sous quatre conditions : statut "
             "égal dans la situation, objectifs communs, coopération plutôt que compétition, et soutien institutionnel. Une "
             "méta-analyse portant sur plus de 500 études confirme un effet réel, et montre qu'il se généralise partiellement à "
             "des groupes non impliqués dans le contact.</p>"
             "<p>Ce qui ne marche pas : les formations à la diversité obligatoires et ponctuelles, qui produisent souvent une "
             "réactance ; et l'exposition à des messages culpabilisants, qui renforce les défenses identitaires.</p>"),
            ("Persuasion : le modèle ELM",
             "<p>Petty et Cacioppo distinguent deux routes de la persuasion :</p>"
             "<ul>"
             "<li><strong>Route centrale</strong> : l'auditeur est motivé et capable de traiter l'argument. Il évalue la qualité du "
             "raisonnement. Les changements d'attitude obtenus sont durables et résistants à la contre-argumentation.</li>"
             "<li><strong>Route périphérique</strong> : faible motivation ou faible capacité de traitement. Ce sont alors les "
             "indices superficiels qui décident : attractivité de la source, nombre d'arguments plutôt que leur qualité, musique, "
             "sentiment de familiarité. Les effets sont rapides mais fragiles.</li>"
             "</ul>"
             "<p>Conséquence directe : toute la publicité grand public vise la route périphérique, tandis qu'un rapport d'expertise "
             "mise sur la route centrale. Pour résister, il suffit souvent d'augmenter délibérément son niveau d'attention et de "
             "se demander : « quel est réellement l'argument ? »</p>"),
            ("Normes, rôles et pouvoir des situations",
             "<p>Les <strong>normes descriptives</strong> (ce que les gens font réellement) sont plus efficaces que les "
             "<strong>normes injonctives</strong> (ce qu'ils devraient faire). Une célèbre campagne hôtelière l'illustre : "
             "« la majorité des clients de cette chambre réutilisent leur serviette » produit plus de réutilisation que « protégez "
             "l'environnement ».</p>"
             "<p>Attention à l'effet pervers : annoncer « beaucoup de gens fraudent » ou « la participation électorale est faible » "
             "normalise le comportement qu'on veut combattre.</p>"
             "<p>Le concept d'<strong>ignorance pluraliste</strong> explique de nombreuses situations paradoxales : chacun désapprouve "
             "en privé une pratique tout en croyant être le seul, parce que personne n'ose l'exprimer. Le silence collectif maintient "
             "alors une norme que presque personne ne soutient réellement.</p>"),
        ],
        "mythes": [
            ("38 témoins ont assisté sans réagir au meurtre de Kitty Genovese.",
             "Le récit fondateur de l'effet du témoin a été largement fabriqué par le New York Times. Plusieurs personnes ont bien appelé la police. L'effet lui-même reste néanmoins solidement démontré en laboratoire."),
            ("L'expérience de Stanford prouve que la situation transforme n'importe qui en bourreau.",
             "Les archives montrent des consignes explicites données aux gardiens et une sélection de volontaires prédisposés. C'est une démonstration marquante, pas une preuve expérimentale."),
            ("Les foules sont irrationnelles et régressives.",
             "La vision de Le Bon a été invalidée. Les études modernes montrent que les foules obéissent à des normes et à des identités sociales, et se comportent souvent de façon coopérative en situation d'urgence."),
        ],
        "chiffres": [
            ("65 %", "Participants allant jusqu'au voltage maximal chez Milgram"),
            ("75 %", "Participants se conformant au moins une fois chez Asch"),
            ("500+", "Études confirmant l'effet du contact intergroupe"),
            ("31 %", "Taux d'intervention avec 5 témoins, contre 85 % seul"),
        ],
        "flashcards": [
            ("Quelles sont les quatre conditions de l'hypothèse du contact ?", "Statut égal, objectifs communs, coopération et soutien institutionnel."),
            ("Quelle norme est la plus efficace pour changer un comportement ?", "La norme descriptive : ce que les gens font réellement."),
            ("Qu'est-ce que l'ignorance pluraliste ?", "Chacun désapprouve une pratique en privé tout en croyant être seul à le faire, ce qui maintient une norme que personne ne soutient."),
        ],
    },
    "05-developpement": {
        "sections": [
            ("Après Piaget : ce que l'on sait aujourd'hui du bébé",
             "<p>Les méthodes modernes — temps de fixation du regard, succion non nutritive, violation d'attente — ont révélé des "
             "compétences bien plus précoces que ne le pensait Piaget :</p>"
             "<ul>"
             "<li><strong>Permanence de l'objet</strong> : dès 3-4 mois avec le paradigme de violation d'attente, contre 8-12 mois "
             "chez Piaget qui exigeait une recherche manuelle.</li>"
             "<li><strong>Numérosité</strong> : des bébés de 5 mois réagissent à une addition impossible (1 + 1 = 1) par un "
             "regard prolongé.</li>"
             "<li><strong>Physique naïve</strong> : ils s'attendent à ce qu'un objet sans support tombe, et qu'un objet solide ne "
             "traverse pas un autre.</li>"
             "<li><strong>Préférences sociales</strong> : à 6 mois, ils préfèrent une marionnette qui en aide une autre à celle qui la gêne.</li>"
             "</ul>"
             "<p>Piaget avait raison sur la logique du développement par étapes et sur la construction active des connaissances ; "
             "il a sous-estimé les compétences précoces parce que ses épreuves exigeaient des capacités motrices et langagières "
             "que le bébé n'a pas encore.</p>"),
            ("L'adolescence : un cerveau en chantier",
             "<p>L'adolescence n'est pas qu'une crise culturelle. Deux systèmes cérébraux se développent à des rythmes différents :</p>"
             "<ul>"
             "<li>Le <strong>système limbique</strong>, sensible à la récompense et à la reconnaissance par les pairs, arrive à "
             "maturité vers 13-15 ans.</li>"
             "<li>Le <strong>cortex préfrontal</strong>, siège du contrôle inhibiteur et de l'anticipation des conséquences, ne "
             "termine sa maturation que vers 25 ans.</li>"
             "</ul>"
             "<p>Ce décalage explique la prise de risque adolescente — qui, c'est important, augmente surtout <strong>en présence "
             "des pairs</strong> : seuls, les adolescents prennent des décisions comparables à celles des adultes.</p>"
             "<p>S'y ajoutent un retard de phase circadienne (l'endormissement se décale physiologiquement de 1 à 2 heures, "
             "ce qui rend les horaires scolaires matinaux réellement problématiques), une sensibilité accrue à l'évaluation "
             "sociale, et une période de forte plasticité qui fait aussi de l'adolescence une fenêtre d'opportunité majeure.</p>"),
            ("L'attachement à l'âge adulte",
             "<p>Hazan et Shaver ont montré que les styles d'attachement se prolongent dans les relations amoureuses, sous la forme "
             "de modèles internes opérants — des représentations de soi (suis-je digne d'être aimé ?) et d'autrui (les autres "
             "sont-ils fiables ?) :</p>"
             "<ul>"
             "<li><strong>Sécure</strong> (≈ 55 %) : à l'aise avec l'intimité et l'autonomie, gère les conflits sans dramatisation.</li>"
             "<li><strong>Anxieux-préoccupé</strong> (≈ 20 %) : besoin de réassurance, peur de l'abandon, hypervigilance aux signaux de rejet.</li>"
             "<li><strong>Évitant-détaché</strong> (≈ 20 %) : valorise l'indépendance, minimise le besoin de proximité, se retire en cas de tension.</li>"
             "<li><strong>Craintif-désorganisé</strong> (≈ 5 %) : désire et redoute simultanément la proximité, souvent lié à des traumatismes précoces.</li>"
             "</ul>"
             "<p>Point essentiel : ces styles ne sont pas des destins. L'<strong>attachement acquis-sécure</strong> désigne les "
             "personnes ayant eu une enfance insécure qui développent un fonctionnement sécure, notamment grâce à une relation "
             "stable ou à une psychothérapie. Le facteur décisif n'est pas ce qui est arrivé, mais la cohérence du récit qu'on "
             "parvient à en faire.</p>"),
            ("Ce qui compte vraiment dans la parentalité",
             "<p>Baumrind a décrit quatre styles parentaux selon deux axes, exigence et chaleur :</p>"
             "<ul>"
             "<li><strong>Démocratique</strong> (exigeant et chaleureux) : règles claires et expliquées, écoute réelle. Associé aux "
             "meilleurs résultats sur presque tous les indicateurs.</li>"
             "<li><strong>Autoritaire</strong> (exigeant, peu chaleureux) : obéissance sans explication. Associé à davantage "
             "d'anxiété et à une moindre autonomie.</li>"
             "<li><strong>Permissif</strong> (peu exigeant, chaleureux) : peu de limites. Associé à des difficultés d'autorégulation.</li>"
             "<li><strong>Négligent</strong> (ni l'un ni l'autre) : associé aux pires résultats.</li>"
             "</ul>"
             "<p>Deux nuances importantes. D'abord, ces catégories sont largement issues de la classe moyenne occidentale : un style "
             "plus directif peut être protecteur dans un environnement dangereux. Ensuite, les études de génétique comportementale "
             "rappellent que l'influence parentale sur les traits de personnalité est plus faible qu'on ne l'imagine — ce qui est "
             "une bonne nouvelle pour les parents rongés par la culpabilité. Ce qui reste solidement établi : la sécurité affective, "
             "la stabilité, l'absence de violence et la qualité du langage adressé à l'enfant.</p>"),
        ],
        "mythes": [
            ("Les trois premières années déterminent toute la vie.",
             "Elles comptent beaucoup, mais la plasticité se poursuit toute la vie. Des enfants issus d'orphelinats très carencés adoptés tardivement montrent des récupérations importantes, surtout avant 2 ans, et des progrès réels après."),
            ("Écouter du Mozart rend les bébés plus intelligents.",
             "L'étude initiale portait sur des adultes, une tâche spatiale précise et un effet qui disparaissait en 15 minutes. Aucun effet durable sur l'intelligence des enfants n'a jamais été démontré."),
            ("Les écrans avant 3 ans provoquent l'autisme.",
             "Aucune donnée ne soutient cette causalité. Les recommandations de limitation des écrans chez le tout-petit reposent sur d'autres raisons : sommeil, langage et interactions."),
        ],
        "chiffres": [
            ("25 ans", "Âge approximatif de maturation du cortex préfrontal"),
            ("≈ 65 %", "Enfants classés en attachement sûr"),
            ("3-4 mois", "Permanence de l'objet détectée par violation d'attente"),
            ("10", "Mots nouveaux acquis par jour pendant l'explosion lexicale"),
        ],
        "flashcards": [
            ("Pourquoi Piaget a-t-il sous-estimé les bébés ?", "Ses épreuves exigeaient des capacités motrices et langagières que le nourrisson ne possède pas encore."),
            ("Pourquoi les adolescents prennent-ils plus de risques ?", "Le système de récompense mûrit avant le cortex préfrontal, et la présence des pairs amplifie fortement la prise de risque."),
            ("Qu'est-ce que l'attachement acquis-sécure ?", "Le développement d'un fonctionnement sécure malgré une enfance insécure, notamment via une relation stable ou une psychothérapie."),
        ],
    },
    "06-personnalite": {
        "sections": [
            ("Le Big Five en détail",
             "<p>Le modèle à cinq facteurs est le plus solide dont dispose la psychologie de la personnalité. Chaque dimension est "
             "un continuum, pas une catégorie :</p>"
             "<ul>"
             "<li><strong>Ouverture à l'expérience</strong> : curiosité, imagination, goût de la nouveauté et des idées abstraites. "
             "Corrèle avec la créativité et les choix de carrière artistiques ou intellectuels.</li>"
             "<li><strong>Conscienciosité</strong> : organisation, persévérance, fiabilité. C'est le meilleur prédicteur de la "
             "réussite professionnelle et scolaire, et même de la longévité.</li>"
             "<li><strong>Extraversion</strong> : sociabilité, énergie, recherche de stimulation. Corrèle avec le niveau d'émotions "
             "positives rapportées.</li>"
             "<li><strong>Agréabilité</strong> : coopération, confiance, empathie. Protège les relations, mais corrèle négativement "
             "avec le niveau de salaire — surtout chez les hommes.</li>"
             "<li><strong>Névrosisme</strong> : tendance aux émotions négatives et à la réactivité au stress. Meilleur prédicteur "
             "des troubles anxieux et dépressifs.</li>"
             "</ul>"
             "<p>Chaque dimension se décompose en facettes : l'extraversion réunit chaleur, grégarité, assertivité, activité, "
             "recherche de sensations et émotions positives. Deux personnes ayant le même score global peuvent avoir des profils "
             "de facettes totalement différents.</p>"),
            ("La personnalité change-t-elle ?",
             "<p>Oui, de façon lente et largement prévisible. Le <strong>principe de maturation</strong> décrit une tendance "
             "universelle, observée dans toutes les cultures étudiées : avec l'âge, la conscienciosité et l'agréabilité augmentent, "
             "le névrosisme diminue, l'ouverture culmine au début de l'âge adulte puis décline légèrement.</p>"
             "<p>Les événements de vie comptent aussi : le premier emploi stable augmente la conscienciosité, une rupture ou un "
             "chômage durable augmente le névrosisme. Des essais cliniques ont même montré que quelques mois de psychothérapie "
             "produisent une baisse du névrosisme équivalente à plusieurs décennies de maturation naturelle — l'un des résultats "
             "les plus encourageants de ce champ.</p>"
             "<p>La <strong>stabilité de rang</strong> reste néanmoins élevée : si vous étiez plus extraverti que 80 % de vos "
             "camarades à 20 ans, vous le serez probablement encore à 50 ans, même si vos deux scores absolus ont évolué.</p>"),
            ("Le débat personne-situation, tranché",
             "<p>En 1968, Walter Mischel a provoqué une crise en montrant que les traits ne prédisent le comportement dans une "
             "situation donnée qu'avec des corrélations d'environ 0,30. Certains en ont conclu que la personnalité n'existait pas.</p>"
             "<p>La résolution est aujourd'hui claire : les traits prédisent mal un comportement isolé, mais très bien des "
             "<strong>agrégats</strong> de comportements dans le temps. On ne peut pas prédire si une personne consciencieuse sera "
             "à l'heure mardi ; on peut prédire qu'elle sera ponctuelle bien plus souvent que la moyenne sur un an.</p>"
             "<p>Mischel a proposé la théorie « si… alors » : la personnalité se manifeste comme un profil stable de réactions "
             "<em>conditionnelles</em> aux situations. « Si on la critique en public, alors elle se retire » est une signature "
             "comportementale plus fidèle qu'un score global d'introversion.</p>"),
            ("Ce que l'on appelle « la triade noire »",
             "<p>Trois traits subcliniques, corrélés entre eux mais distincts, retiennent l'attention de la recherche :</p>"
             "<ul>"
             "<li><strong>Narcissisme</strong> : grandiosité, besoin d'admiration, sentiment d'avoir droit à un traitement particulier.</li>"
             "<li><strong>Machiavélisme</strong> : manipulation stratégique, cynisme, orientation vers l'intérêt personnel à long terme.</li>"
             "<li><strong>Psychopathie subclinique</strong> : faible empathie affective, impulsivité, insensibilité, absence de remords.</li>"
             "</ul>"
             "<p>Leur noyau commun est l'insensibilité au coût infligé à autrui. Ces traits sont associés à des comportements "
             "contre-productifs au travail, mais aussi — à des niveaux modérés — à une progression hiérarchique rapide, ce qui "
             "explique leur persistance. Deux précautions : ces traits sont continus, et une personne désagréable n'est pas un "
             "psychopathe ; le diagnostic clinique relève d'une évaluation spécialisée, pas d'un test en ligne.</p>"),
        ],
        "mythes": [
            ("Il existe des « types » de personnalité.",
             "Les traits se distribuent de façon continue, en courbe de Gauche. Les typologies (MBTI, couleurs, ennéagramme) créent des frontières arbitraires qui font basculer de type des personnes aux scores presque identiques."),
            ("La personnalité est fixée à 25 ans.",
             "Elle continue d'évoluer toute la vie, avec une tendance générale à la maturation. La psychothérapie peut accélérer ces changements."),
            ("L'écriture révèle la personnalité.",
             "La graphologie a été testée à de nombreuses reprises : sa validité prédictive est nulle. Elle reste pourtant utilisée dans certains recrutements en France."),
        ],
        "chiffres": [
            ("5", "Dimensions du modèle le mieux validé (OCEAN)"),
            ("≈ 40-60 %", "Part de variance des traits attribuée à l'héritabilité"),
            ("0,30", "Corrélation trait-comportement isolé (Mischel)"),
            ("18 000", "Mots recensés par Allport pour décrire la personnalité"),
        ],
        "flashcards": [
            ("Quelle dimension du Big Five prédit le mieux la réussite professionnelle ?", "La conscienciosité."),
            ("Qu'est-ce que le principe de maturation ?", "Une tendance universelle à devenir plus consciencieux et agréable et moins névrosé avec l'âge."),
            ("Comment le débat personne-situation a-t-il été résolu ?", "Les traits prédisent mal un comportement isolé mais très bien des agrégats de comportements dans le temps."),
        ],
    },
    "07-emotions": {
        "sections": [
            ("Trois grandes théories de l'émotion",
             "<ul>"
             "<li><strong>James-Lange</strong> (1884) : la perception déclenche une réaction corporelle, et l'émotion est la "
             "perception de cette réaction. « Nous ne pleurons pas parce que nous sommes tristes ; nous sommes tristes parce que "
             "nous pleurons. » Contre-intuitif, partiellement soutenu par les travaux sur le feedback facial.</li>"
             "<li><strong>Cannon-Bard</strong> (1927) : la réaction corporelle et l'expérience émotionnelle surviennent en "
             "parallèle, déclenchées par le thalamus. Argument central : les réactions physiologiques sont trop lentes et trop "
             "peu spécifiques pour différencier les émotions.</li>"
             "<li><strong>Schachter-Singer</strong> (1962) : l'émotion résulte d'une activation physiologique <em>plus</em> une "
             "interprétation cognitive du contexte. Leur expérience de l'injection d'adrénaline montre que la même activation "
             "est vécue comme euphorie ou colère selon le comportement d'un complice présent dans la pièce.</li>"
             "</ul>"
             "<p>La théorie contemporaine de la <strong>construction de l'émotion</strong> (Barrett) va plus loin : il n'existerait "
             "pas de circuit cérébral dédié à chaque émotion de base ; le cerveau construirait l'émotion en catégorisant des "
             "sensations corporelles diffuses à l'aide de concepts appris culturellement.</p>"),
            ("Réguler ses émotions : ce qui marche",
             "<p>Le modèle processuel de James Gross distingue cinq familles de stratégies, selon le moment où elles interviennent :</p>"
             "<ol>"
             "<li><strong>Sélection de la situation</strong> : choisir ou éviter un contexte. Efficace, mais l'évitement systématique "
             "entretient l'anxiété.</li>"
             "<li><strong>Modification de la situation</strong> : agir concrètement sur le contexte.</li>"
             "<li><strong>Déploiement attentionnel</strong> : détourner ou focaliser l'attention. Utile à court terme, "
             "contre-productif s'il devient une distraction chronique.</li>"
             "<li><strong>Changement cognitif</strong> : la <strong>réévaluation</strong> (réinterpréter la situation) est la "
             "stratégie la mieux validée, associée à un meilleur bien-être et à une charge physiologique moindre.</li>"
             "<li><strong>Modulation de la réponse</strong> : agir sur l'expression. La <strong>suppression expressive</strong> "
             "(masquer ce que l'on ressent) est coûteuse : elle ne réduit pas le vécu, augmente l'activation physiologique et "
             "dégrade la qualité des relations.</li>"
             "</ol>"
             "<p>L'<strong>étiquetage affectif</strong> — nommer précisément son émotion — réduit mesurablement l'activité de "
             "l'amygdale. Plus le vocabulaire émotionnel est fin (granularité émotionnelle), meilleure est la régulation : "
             "distinguer agacement, frustration, déception et colère permet des réponses plus ajustées.</p>"),
            ("Motivation : au-delà de la carotte et du bâton",
             "<p>Le modèle dominant est la <strong>théorie de l'autodétermination</strong> (Deci et Ryan) : trois besoins "
             "psychologiques fondamentaux — autonomie, compétence, affiliation — doivent être satisfaits pour qu'une motivation "
             "de qualité se maintienne.</p>"
             "<p>La motivation n'est pas binaire mais forme un continuum d'internalisation : de la régulation externe "
             "(je le fais pour éviter une sanction) à la régulation introjectée (je le fais par culpabilité), identifiée "
             "(je le fais parce que j'en vois l'importance), intégrée (cela correspond à mes valeurs), puis intrinsèque "
             "(je le fais pour le plaisir de l'activité).</p>"
             "<p>Autres apports utiles : la théorie de l'attente-valeur (l'effort dépend de la probabilité perçue de réussir "
             "multipliée par la valeur accordée au résultat), l'importance de la <strong>perception de contrôlabilité</strong> "
             "(attribuer un échec à un manque d'effort est bien plus mobilisateur que l'attribuer à un manque de capacité), et "
             "l'effet délétère des récompenses externes sur les activités déjà appréciées.</p>"),
            ("Alexithymie et intelligence émotionnelle",
             "<p>L'<strong>alexithymie</strong> désigne une difficulté à identifier et décrire ses propres émotions, avec une "
             "pensée tournée vers l'extérieur et une imagination pauvre. Elle concerne environ 10 % de la population générale, "
             "davantage chez les personnes autistes et après certains traumatismes. Ce n'est pas une absence d'émotion mais une "
             "difficulté d'accès et de mise en mots.</p>"
             "<p>L'<strong>intelligence émotionnelle</strong>, au sens de Salovey et Mayer, réunit quatre aptitudes : percevoir, "
             "utiliser, comprendre et gérer les émotions. Mesurée comme une aptitude (test MSCEIT), elle prédit modestement mais "
             "réellement la qualité des relations et la performance dans les métiers relationnels. Mesurée par auto-questionnaire, "
             "elle recoupe largement le Big Five et n'ajoute pas grand-chose. La version popularisée par Goleman, qui en fait un "
             "prédicteur supérieur au QI, dépasse largement les données.</p>"),
        ],
        "mythes": [
            ("Il faut extérioriser sa colère pour l'évacuer.",
             "La théorie de la catharsis est invalidée : frapper un coussin en pensant à la personne qui nous a énervés augmente l'agressivité ultérieure au lieu de la réduire."),
            ("Les émotions nuisent à la décision rationnelle.",
             "Les patients dont les circuits émotionnels sont lésés prennent des décisions catastrophiques malgré une intelligence intacte. L'émotion est une composante de la décision, pas son parasite."),
            ("Il y a six émotions de base universelles, point final.",
             "L'universalité des expressions est réelle mais partielle. Les protocoles de reconnaissance à choix forcé ont surestimé l'accord entre cultures, et le débat reste ouvert."),
        ],
        "chiffres": [
            ("≈ 10 %", "Prévalence de l'alexithymie en population générale"),
            ("6", "Émotions de base selon Ekman"),
            ("4", "Branches de l'intelligence émotionnelle (Salovey & Mayer)"),
            ("≈ 90 s", "Durée de la réponse physiologique brute d'une émotion non alimentée par la rumination"),
        ],
        "flashcards": [
            ("Quelle stratégie de régulation émotionnelle est la mieux validée ?", "La réévaluation cognitive, qui consiste à réinterpréter la situation."),
            ("Pourquoi la suppression expressive est-elle coûteuse ?", "Elle ne réduit pas le vécu émotionnel, augmente l'activation physiologique et dégrade les relations."),
            ("Qu'est-ce que la granularité émotionnelle ?", "La finesse avec laquelle on distingue et nomme ses émotions, associée à une meilleure régulation."),
        ],
    },
    "08-neurosciences": {
        "sections": [
            ("Neuroplasticité : le cerveau se reconfigure",
             "<p>Le dogme d'un cerveau figé après l'enfance est tombé. On distingue plusieurs formes de plasticité :</p>"
             "<ul>"
             "<li><strong>Plasticité synaptique</strong> : renforcement ou affaiblissement des connexions selon leur usage "
             "(potentialisation à long terme, conforme à la règle de Hebb). C'est le substrat de l'apprentissage.</li>"
             "<li><strong>Plasticité structurale</strong> : modification de la densité de matière grise. Les chauffeurs de taxi "
             "londoniens, après des années à mémoriser 25 000 rues, présentent un hippocampe postérieur plus volumineux — et ce "
             "volume augmente avec les années d'expérience, ce qui écarte l'hypothèse d'une prédisposition.</li>"
             "<li><strong>Plasticité de réorganisation</strong> : après une lésion ou une amputation, les régions voisines "
             "colonisent le territoire libéré — mécanisme à l'origine des douleurs du membre fantôme.</li>"
             "<li><strong>Neurogenèse adulte</strong> : la production de nouveaux neurones dans l'hippocampe adulte reste débattue "
             "chez l'humain, avec des études contradictoires publiées la même année dans les meilleures revues.</li>"
             "</ul>"),
            ("Les principaux neurotransmetteurs, sans caricature",
             "<ul>"
             "<li><strong>Dopamine</strong> : n'est pas « la molécule du plaisir » mais le signal d'<em>erreur de prédiction de "
             "récompense</em>. Elle code l'écart entre ce qui était attendu et ce qui arrive, ce qui en fait le moteur de "
             "l'apprentissage et du désir (le <em>wanting</em>), distinct du plaisir (le <em>liking</em>).</li>"
             "<li><strong>Sérotonine</strong> : impliquée dans l'humeur, le sommeil, l'appétit et l'impulsivité. L'hypothèse "
             "simpliste « la dépression est un déficit en sérotonine » a été sérieusement contestée en 2022 ; les antidépresseurs "
             "sérotoninergiques fonctionnent chez une partie des patients, mais leur mécanisme réel reste discuté.</li>"
             "<li><strong>Noradrénaline</strong> : éveil, vigilance, réponse au stress.</li>"
             "<li><strong>GABA</strong> : principal neurotransmetteur inhibiteur, cible des benzodiazépines et de l'alcool.</li>"
             "<li><strong>Glutamate</strong> : principal excitateur, central dans la plasticité et l'apprentissage.</li>"
             "<li><strong>Acétylcholine</strong> : attention, mémoire, jonction neuromusculaire. Cible des traitements anti-Alzheimer.</li>"
             "<li><strong>Ocytocine</strong> : abusivement nommée « hormone de l'amour ». Elle favorise l'attachement au groupe "
             "d'appartenance, mais peut aussi accroître la méfiance envers l'extérieur.</li>"
             "</ul>"),
            ("Ce que mesure vraiment l'IRM fonctionnelle",
             "<p>L'IRMf ne mesure pas l'activité neuronale mais le signal <strong>BOLD</strong>, c'est-à-dire une variation du flux "
             "sanguin oxygéné, avec plusieurs secondes de retard. C'est une mesure indirecte, à résolution temporelle faible.</p>"
             "<p>Les images colorées ne montrent pas « la zone du mensonge » ou « du plaisir » : ce sont des cartes statistiques de "
             "différences entre deux conditions, dont les seuils sont choisis par l'expérimentateur. Une étude devenue célèbre a "
             "détecté une « activité cérébrale » dans un saumon mort, simplement en n'appliquant pas de correction pour "
             "comparaisons multiples.</p>"
             "<p>Deux pièges classiques : le <strong>raisonnement inverse</strong> (« l'insula s'active, donc le sujet ressent du "
             "dégoût » — alors que l'insula s'active dans des dizaines de contextes) et le <strong>neuro-réalisme</strong> "
             "(une explication paraît plus crédible dès qu'elle est illustrée par une image cérébrale, même si l'image n'apporte "
             "aucune information).</p>"
             "<p>Les autres méthodes se complètent : l'EEG a une résolution temporelle de l'ordre de la milliseconde mais une "
             "localisation médiocre ; la MEG combine les deux ; la stimulation magnétique transcrânienne permet, elle, d'établir "
             "une causalité en perturbant temporairement une région.</p>"),
            ("Sommeil et cerveau",
             "<p>Le sommeil n'est pas une interruption de l'activité cérébrale mais un processus actif structuré en cycles de "
             "90 minutes :</p>"
             "<ul>"
             "<li><strong>Sommeil lent profond</strong>, concentré en première partie de nuit : consolidation de la mémoire "
             "déclarative, sécrétion d'hormone de croissance, et activation du système glymphatique qui élimine les déchets "
             "métaboliques, dont les protéines bêta-amyloïdes impliquées dans la maladie d'Alzheimer.</li>"
             "<li><strong>Sommeil paradoxal</strong>, concentré en fin de nuit : consolidation de la mémoire procédurale et "
             "émotionnelle, rêves narratifs, atonie musculaire protectrice.</li>"
             "</ul>"
             "<p>Conséquences concrètes : se coucher tard ampute surtout le sommeil paradoxal, se lever très tôt ampute le sommeil "
             "lent profond. Une nuit blanche réduit la capacité d'apprentissage du lendemain d'environ 40 %. La sieste courte "
             "(10-20 minutes) améliore la vigilance sans inertie ; au-delà de 30 minutes, on se réveille en sommeil profond, "
             "d'où la sensation désagréable.</p>"),
        ],
        "mythes": [
            ("On utilise 10 % de son cerveau.",
             "Aucun fondement. Ce mythe très ancien est parfois attribué à une mauvaise lecture de James, qui parlait de potentiel inexploité, pas de volume cérébral inactif."),
            ("Cerveau gauche rationnel, cerveau droit créatif.",
             "La spécialisation hémisphérique est réelle mais partielle. Aucune étude d'imagerie n'a jamais montré de personnes « à dominance droite » globalement plus créatives."),
            ("Les neurones ne se régénèrent jamais.",
             "La plasticité synaptique et structurale est massive tout au long de la vie. Seule la question de la neurogenèse hippocampique adulte reste réellement débattue."),
        ],
        "chiffres": [
            ("86 milliards", "Neurones dans un cerveau humain adulte"),
            ("20 %", "Part de l'énergie du corps consommée par le cerveau"),
            ("90 min", "Durée d'un cycle de sommeil"),
            ("40 %", "Baisse de capacité d'apprentissage après une nuit blanche"),
        ],
        "flashcards": [
            ("Que code réellement la dopamine ?", "L'erreur de prédiction de récompense, c'est-à-dire l'écart entre ce qui était attendu et ce qui survient."),
            ("Que mesure l'IRM fonctionnelle ?", "Le signal BOLD, une variation indirecte et retardée du flux sanguin oxygéné, pas l'activité neuronale directe."),
            ("Quel rôle joue le sommeil lent profond ?", "Consolidation de la mémoire déclarative et élimination des déchets métaboliques par le système glymphatique."),
        ],
    },
    "09-psychopathologie": {
        "sections": [
            ("Comment fonctionnent les classifications",
             "<p>Deux systèmes coexistent : le <strong>DSM-5-TR</strong> (Association américaine de psychiatrie), très utilisé en "
             "recherche, et la <strong>CIM-11</strong> (OMS), référence officielle pour le codage médical dans la plupart des pays, "
             "dont la France.</p>"
             "<p>Le DSM-III (1980) a opéré une bascule décisive : abandonner les explications théoriques (notamment psychanalytiques) "
             "au profit de <strong>critères opérationnels</strong> observables, afin que deux cliniciens différents posent le même "
             "diagnostic. Ce gain de fidélité s'est fait au prix de critiques sérieuses : multiplication des catégories, frontières "
             "arbitraires avec le normal, comorbidités massives, influence de l'industrie pharmaceutique.</p>"
             "<p>Deux alternatives se développent : le <strong>RDoC</strong> (approche par dimensions neurobiologiques transversales) "
             "et le <strong>HiTOP</strong> (modèle hiérarchique et dimensionnel des troubles). Toutes deux partent du même constat : "
             "les troubles mentaux ne sont probablement pas des catégories naturelles bien séparées.</p>"
             "<p>À retenir : un diagnostic est un outil de communication et d'orientation thérapeutique, pas l'identité d'une personne. "
             "On dit « une personne souffrant de schizophrénie », pas « un schizophrène ».</p>"),
            ("Le modèle vulnérabilité-stress et les facteurs transdiagnostiques",
             "<p>Aucun trouble mental n'a de cause unique. Le modèle dominant articule une <strong>vulnérabilité</strong> "
             "(génétique, neurodéveloppementale, expériences précoces) et des <strong>facteurs de stress</strong> (événements de "
             "vie, précarité, isolement, consommations), modulés par des <strong>facteurs protecteurs</strong> (soutien social, "
             "compétences de régulation, accès aux soins).</p>"
             "<p>Certains mécanismes se retrouvent dans presque tous les troubles — ce sont les <strong>facteurs "
             "transdiagnostiques</strong> :</p>"
             "<ul>"
             "<li><strong>La rumination</strong> et l'inquiétude : pensée répétitive négative, présente dans la dépression, "
             "l'anxiété, les TCA et les addictions.</li>"
             "<li><strong>L'évitement expérientiel</strong> : refus de ressentir certaines émotions, qui les amplifie à terme.</li>"
             "<li><strong>La dysrégulation émotionnelle</strong>.</li>"
             "<li><strong>L'intolérance à l'incertitude</strong>.</li>"
             "<li><strong>Les troubles du sommeil</strong>, à la fois symptôme, facteur de risque et cible thérapeutique.</li>"
             "</ul>"
             "<p>C'est ce constat qui a fait émerger les protocoles transdiagnostiques, comme le protocole unifié de Barlow, "
             "efficaces sur plusieurs troubles à la fois.</p>"),
            ("Évaluer et prévenir le risque suicidaire",
             "<p>Le suicide représente environ 700 000 décès par an dans le monde, et constitue l'une des premières causes de "
             "mortalité chez les 15-29 ans. Quelques repères essentiels :</p>"
             "<ul>"
             "<li><strong>Parler du suicide n'augmente pas le risque.</strong> C'est l'idée reçue la plus dangereuse. Poser la "
             "question directement soulage le plus souvent et ouvre la discussion.</li>"
             "<li><strong>Signaux d'alerte</strong> : évocation directe ou indirecte, sentiment d'être un fardeau, désespoir, "
             "retrait, dons d'objets personnels, apaisement soudain et inexpliqué après une période sombre.</li>"
             "<li><strong>Facteurs de risque</strong> : tentative antérieure (le plus puissant), trouble psychiatrique, accès à un "
             "moyen létal, isolement, douleur chronique, perte récente.</li>"
             "<li><strong>Ce qui protège</strong> : la restriction de l'accès aux moyens (mesure la plus efficace au niveau "
             "populationnel), le lien maintenu, le suivi actif après une hospitalisation, et l'existence d'un plan de sécurité écrit.</li>"
             "</ul>"
             "<p>En France : <strong>3114</strong>, numéro national de prévention du suicide, gratuit, 24 h/24. En cas d'urgence "
             "vitale : 15 ou 112.</p>"),
            ("Stigmatisation : un second fardeau",
             "<p>La stigmatisation aggrave les troubles autant que les symptômes eux-mêmes. Elle opère à trois niveaux : "
             "<strong>publique</strong> (croyances de la population), <strong>structurelle</strong> (accès inégal aux soins, "
             "discrimination à l'embauche, sous-financement de la psychiatrie) et <strong>intériorisée</strong> (la personne "
             "adopte elle-même le regard négatif, ce qui réduit sa demande d'aide et son estime de soi).</p>"
             "<p>Ce qui réduit la stigmatisation : le <strong>contact direct</strong> avec des personnes concernées — de loin le "
             "levier le plus efficace, bien plus que les campagnes d'information — et l'emploi de pairs-aidants dans les équipes "
             "de soin. Ce qui l'aggrave : les messages insistant sur une cause purement biologique, qui augmentent paradoxalement "
             "la perception de dangerosité et d'irréversibilité.</p>"
             "<p>Un chiffre à connaître : les personnes souffrant de troubles psychiques sévères sont bien plus souvent "
             "<strong>victimes</strong> que auteurs de violences.</p>"),
        ],
        "mythes": [
            ("La schizophrénie, c'est le dédoublement de la personnalité.",
             "Contresens issu de l'étymologie. La schizophrénie associe hallucinations, idées délirantes et désorganisation. Le trouble dissociatif de l'identité est une entité distincte et beaucoup plus rare."),
            ("Les troubles mentaux sont rares.",
             "Une personne sur huit dans le monde vit avec un trouble mental, et près d'une sur deux en connaîtra un au cours de sa vie."),
            ("On ne guérit jamais d'un trouble psychique.",
             "La majorité des troubles anxieux et dépressifs répondent bien au traitement. Même pour les troubles sévères, le rétablissement — vivre une vie satisfaisante avec ou sans symptômes résiduels — est un objectif atteignable et documenté."),
        ],
        "chiffres": [
            ("1 sur 8", "Personnes vivant avec un trouble mental dans le monde"),
            ("3114", "Numéro national de prévention du suicide en France"),
            ("11 ans", "Délai moyen entre les premiers symptômes et le premier soin adapté"),
            ("2 à 3×", "Surrisque de mortalité prématurée lié aux troubles psychiques sévères"),
        ],
        "flashcards": [
            ("Qu'est-ce qu'un facteur transdiagnostique ?", "Un mécanisme commun à plusieurs troubles, comme la rumination, l'évitement expérientiel ou la dysrégulation émotionnelle."),
            ("Parler du suicide augmente-t-il le risque ?", "Non. C'est une idée reçue dangereuse : poser la question directement soulage et ouvre la discussion."),
            ("Quel est le levier le plus efficace contre la stigmatisation ?", "Le contact direct avec des personnes concernées, bien plus que les campagnes d'information."),
        ],
    },
    "10-therapies": {
        "sections": [
            ("Les facteurs communs : ce qui soigne dans toute thérapie",
             "<p>Les méta-analyses montrent que la technique employée explique une part limitée du résultat. Les "
             "<strong>facteurs communs</strong> pèsent davantage :</p>"
             "<ul>"
             "<li><strong>L'alliance thérapeutique</strong> — accord sur les objectifs, accord sur les tâches, lien de confiance — "
             "est le prédicteur le plus robuste du résultat, quelle que soit l'approche. Elle prédit le changement, et non "
             "l'inverse.</li>"
             "<li><strong>L'effet thérapeute</strong> : les écarts de résultats entre praticiens d'une même approche sont plus "
             "importants que les écarts entre approches.</li>"
             "<li><strong>Les attentes du patient</strong> et l'espoir suscité.</li>"
             "<li><strong>La réparation des ruptures d'alliance</strong> : les moments de tension, s'ils sont explicitement repris, "
             "sont souvent les plus thérapeutiques de tout le suivi.</li>"
             "</ul>"
             "<p>Cela ne signifie pas que la technique est indifférente : pour le TOC, les phobies ou le TSPT, certains protocoles "
             "sont nettement supérieurs. La bonne formule est : des techniques spécifiques efficaces, portées par une relation de "
             "qualité.</p>"),
            ("Panorama des grandes approches",
             "<ul>"
             "<li><strong>TCC</strong> : structurée, limitée dans le temps, centrée sur les liens entre pensées, émotions et "
             "comportements, avec des exercices entre les séances. Traitement le mieux validé pour l'anxiété, la dépression, "
             "l'insomnie, le TOC et le TSPT.</li>"
             "<li><strong>Thérapies de troisième vague</strong> : ACT (acceptation et engagement vers ses valeurs), MBCT "
             "(pleine conscience, recommandée en prévention de la rechute dépressive), TCD (régulation émotionnelle, référence "
             "pour le trouble borderline), thérapie des schémas (schémas précoces inadaptés).</li>"
             "<li><strong>Approches psychodynamiques</strong> : travail sur les conflits inconscients, les répétitions et le "
             "transfert. Les formes brèves et manualisées disposent de preuves d'efficacité pour la dépression et certains "
             "troubles de la personnalité.</li>"
             "<li><strong>Approches humanistes</strong> : thérapie centrée sur la personne (Rogers), Gestalt-thérapie, focusing. "
             "Bonnes preuves pour les difficultés existentielles et relationnelles.</li>"
             "<li><strong>Thérapies systémiques et familiales</strong> : le symptôme est envisagé dans le système relationnel. "
             "Indication majeure pour l'anorexie de l'adolescent et les troubles du comportement de l'enfant.</li>"
             "<li><strong>EMDR</strong> : retraitement des souvenirs traumatiques par stimulation bilatérale. Recommandée par l'OMS "
             "pour le TSPT, même si le rôle spécifique des mouvements oculaires reste discuté.</li>"
             "</ul>"),
            ("Choisir, commencer, et savoir si ça marche",
             "<p><strong>Comment choisir ?</strong> D'abord selon le trouble (certaines approches ont des indications précises), "
             "ensuite selon la qualification du praticien — en France, le titre de <em>psychologue</em> est protégé et exige un "
             "master ; le titre de <em>psychothérapeute</em> est réglementé ; le mot « thérapeute » seul ne l'est pas du tout. "
             "Un psychiatre est médecin et peut prescrire.</p>"
             "<p><strong>Les premières séances</strong> servent à évaluer, définir des objectifs et vérifier que le courant passe. "
             "Il est légitime de changer de praticien si l'alliance ne s'installe pas après trois ou quatre séances.</p>"
             "<p><strong>Signaux d'alerte</strong> : refus d'expliquer la méthode ou la durée, promesses de guérison garantie, "
             "découragement de tout avis extérieur, dépendance entretenue, transgression des limites professionnelles, coût "
             "disproportionné, isolement vis-à-vis des proches.</p>"
             "<p><strong>Mesurer les progrès</strong> : le <em>feedback-informed treatment</em> consiste à évaluer régulièrement "
             "les symptômes et l'alliance avec de courtes échelles. Les essais montrent que cette pratique simple améliore "
             "significativement les résultats, notamment en repérant tôt les suivis qui se dégradent.</p>"),
            ("Psychotropes : ce qu'il faut savoir",
             "<p>Sans se substituer à un avis médical, quelques repères évitent bien des malentendus :</p>"
             "<ul>"
             "<li><strong>Antidépresseurs</strong> : délai d'action de 2 à 4 semaines, poursuite recommandée au moins 6 mois après "
             "la rémission, arrêt toujours progressif en raison des symptômes de sevrage. Ils ne créent pas de dépendance au sens "
             "des addictions, mais l'arrêt brutal est déconseillé.</li>"
             "<li><strong>Anxiolytiques (benzodiazépines)</strong> : efficaces immédiatement, mais tolérance et dépendance rapides. "
             "Durée recommandée : quelques semaines, pas des années.</li>"
             "<li><strong>Thymorégulateurs</strong> : traitement de fond du trouble bipolaire, avec surveillance biologique.</li>"
             "<li><strong>Antipsychotiques</strong> : indispensables dans les troubles psychotiques, avec une surveillance "
             "métabolique et neurologique nécessaire.</li>"
             "</ul>"
             "<p>Dans les dépressions modérées à sévères, l'association psychothérapie + médicament est supérieure à chaque "
             "traitement isolé, et la psychothérapie protège mieux de la rechute après l'arrêt.</p>"),
        ],
        "mythes": [
            ("La psychothérapie, c'est parler de son enfance sur un divan.",
             "C'est une approche parmi beaucoup d'autres. La plupart des thérapies actuelles sont en face à face, structurées, orientées vers des objectifs concrets et limitées dans le temps."),
            ("Il faut avoir un trouble grave pour consulter.",
             "Une difficulté relationnelle, un deuil, une transition professionnelle ou un besoin de mieux se connaître sont des motifs légitimes."),
            ("Toutes les thérapies se valent.",
             "Le verdict du Dodo décrit une équivalence globale sur des troubles courants, mais certaines approches sont clairement supérieures pour des indications précises : exposition avec prévention de la réponse pour le TOC, exposition pour les phobies."),
        ],
        "chiffres": [
            ("≈ 30 %", "Part du résultat attribuable aux facteurs communs"),
            ("2-4 sem.", "Délai d'action des antidépresseurs"),
            ("12-20", "Nombre de séances d'un protocole TCC standard"),
            ("50 %", "Réduction du risque de rechute dépressive avec la MBCT chez les patients à rechutes multiples"),
        ],
        "flashcards": [
            ("Quel est le meilleur prédicteur du résultat d'une psychothérapie ?", "La qualité de l'alliance thérapeutique."),
            ("Quelle approche est la référence pour le trouble borderline ?", "La thérapie comportementale dialectique (TCD) de Marsha Linehan."),
            ("Quels signaux doivent alerter chez un praticien ?", "Promesse de guérison garantie, refus d'expliquer la méthode, isolement du patient, dépendance entretenue, coût disproportionné."),
        ],
    },
    "11-positive": {
        "sections": [
            ("Le modèle PERMA et ce qui rend heureux",
             "<p>Seligman décrit cinq piliers du bien-être durable :</p>"
             "<ul>"
             "<li><strong>P</strong>ositive emotions : émotions agréables, gratitude, savourer.</li>"
             "<li><strong>E</strong>ngagement : état de flow, absorption dans une activité qui nous dépasse.</li>"
             "<li><strong>R</strong>elationships : relations de qualité — le facteur le plus fortement associé au bien-être.</li>"
             "<li><strong>M</strong>eaning : appartenir à quelque chose qui nous dépasse et y contribuer.</li>"
             "<li><strong>A</strong>ccomplishment : poursuivre et atteindre des objectifs qui comptent pour soi.</li>"
             "</ul>"
             "<p>L'étude longitudinale de Harvard, qui suit des participants depuis 1938 — l'une des plus longues jamais menées — "
             "aboutit à une conclusion d'une simplicité désarmante : ce sont la qualité des relations à 50 ans, et non le "
             "cholestérol ni le revenu, qui prédisent le mieux la santé et la satisfaction à 80 ans.</p>"),
            ("L'adaptation hédonique et comment la contourner",
             "<p>Nous revenons à un niveau de bonheur relativement stable après les événements marquants, positifs comme négatifs. "
             "Les gagnants du loto retrouvent leur niveau antérieur en un à deux ans ; la plupart des personnes devenues "
             "paraplégiques retrouvent une satisfaction de vie bien supérieure à ce qu'elles-mêmes auraient prédit — ce qui "
             "illustre notre incapacité chronique à anticiper nos réactions émotionnelles, ce que Gilbert nomme "
             "l'<strong>erreur de prévision affective</strong>.</p>"
             "<p>Quatre leviers réduisent l'adaptation hédonique : la <strong>variété</strong> (varier les plaisirs plutôt que "
             "répéter), la <strong>gratitude</strong> (qui interrompt la banalisation), les <strong>expériences plutôt que les "
             "biens matériels</strong> (elles s'améliorent en mémoire et se partagent), et la <strong>soustraction mentale</strong> "
             "(imaginer que l'on n'a pas obtenu ce que l'on a), plus efficace que la simple énumération de ce que l'on possède.</p>"),
            ("Interventions validées — et leurs limites",
             "<p>Certains exercices ont montré des effets réels dans des essais contrôlés :</p>"
             "<ul>"
             "<li><strong>Trois bonnes choses</strong> : noter chaque soir trois événements positifs et leur cause. Effets "
             "mesurables jusqu'à six mois dans plusieurs études.</li>"
             "<li><strong>Lettre de gratitude</strong> : écrire et, surtout, lire à voix haute une lettre à quelqu'un qui a compté.</li>"
             "<li><strong>Utiliser une force de caractère d'une nouvelle manière</strong> chaque jour pendant une semaine.</li>"
             "<li><strong>Actes de bienveillance</strong> : plusieurs actes concentrés le même jour sont plus efficaces que dispersés.</li>"
             "<li><strong>Méditation de bienveillance</strong> : effets sur les émotions positives et le lien social.</li>"
             "</ul>"
             "<p>Deux réserves honnêtes. Les tailles d'effet sont modestes et diminuent nettement dans les études les plus "
             "rigoureuses. Et la psychologie positive a été critiquée pour son risque de <strong>positivité toxique</strong> : "
             "imposer l'optimisme à une personne en souffrance, ou faire porter à l'individu la responsabilité de conditions de "
             "vie qui relèvent du social et du politique. Un bon usage complète, sans jamais remplacer, l'action sur les causes réelles.</p>"),
            ("Résilience : ni exception, ni superpouvoir",
             "<p>Les travaux de George Bonanno ont renversé une idée reçue. Après un événement potentiellement traumatique, "
             "la trajectoire la plus fréquente — environ 65 % des personnes — est la <strong>résilience</strong> : une perturbation "
             "brève suivie d'un retour au fonctionnement antérieur. Le TSPT chronique concerne une minorité.</p>"
             "<p>La résilience n'est donc pas une qualité rare réservée à quelques héros, mais la réaction ordinaire du système "
             "humain. Elle dépend davantage des ressources disponibles — soutien social, sécurité matérielle, sens, "
             "flexibilité — que d'un trait de caractère.</p>"
             "<p>La <strong>croissance post-traumatique</strong> désigne les changements positifs rapportés après une épreuve : "
             "relations approfondies, nouvelles priorités, force personnelle perçue. Elle est réelle mais souvent surestimée dans "
             "les mesures auto-rapportées, et n'annule jamais la souffrance. On ne « grandit » pas grâce au traumatisme : "
             "on grandit parfois malgré lui, dans le travail de reconstruction.</p>"),
        ],
        "mythes": [
            ("L'argent ne fait pas le bonheur.",
             "À nuancer : il compte beaucoup jusqu'à ce que les besoins de sécurité soient couverts, puis l'effet s'aplatit sans disparaître totalement. Sortir de la précarité change tout ; passer de confortable à riche change peu."),
            ("Il faut penser positif en toutes circonstances.",
             "L'optimisme rigide empêche d'anticiper les obstacles. Le « contraste mental » — imaginer l'objectif puis les obstacles concrets et planifier la réponse — est bien plus efficace que la seule visualisation positive."),
            ("Le bonheur est un objectif à poursuivre directement.",
             "Le poursuivre explicitement comme un but le rend paradoxalement plus difficile à atteindre : on évalue constamment son propre niveau de bonheur, ce qui le dégrade."),
        ],
        "chiffres": [
            ("1938", "Début de l'étude longitudinale de Harvard, toujours en cours"),
            ("≈ 65 %", "Trajectoire résiliente après un événement potentiellement traumatique"),
            ("5", "Piliers du modèle PERMA"),
            ("24", "Forces de caractère de la classification VIA"),
        ],
        "flashcards": [
            ("Que révèle l'étude longitudinale de Harvard ?", "La qualité des relations, plus que le revenu ou la santé physique à mi-vie, prédit la santé et la satisfaction au grand âge."),
            ("Qu'est-ce que l'adaptation hédonique ?", "Le retour à un niveau de bonheur relativement stable après un événement marquant, positif comme négatif."),
            ("Quelle est la trajectoire la plus fréquente après un événement traumatique ?", "La résilience : une perturbation brève suivie d'un retour au fonctionnement antérieur, chez environ deux tiers des personnes."),
        ],
    },
    "12-travail": {
        "sections": [
            ("Modèles du stress professionnel",
             "<ul>"
             "<li><strong>Modèle de Karasek</strong> : le risque le plus élevé (<em>job strain</em>) combine forte demande "
             "psychologique et faible latitude décisionnelle. Johnson y a ajouté le soutien social : demande forte + autonomie "
             "faible + isolement constitue la situation la plus délétère, avec un surrisque cardiovasculaire documenté.</li>"
             "<li><strong>Modèle de Siegrist</strong> : le déséquilibre efforts/récompenses (salaire, estime, sécurité, "
             "perspectives) prédit indépendamment les troubles de santé. Un effort élevé insuffisamment reconnu use davantage "
             "qu'un effort élevé reconnu.</li>"
             "<li><strong>Modèle Job Demands-Resources</strong> : les exigences épuisent, les ressources (autonomie, soutien, "
             "feedback, sens) protègent et alimentent l'engagement. Deux processus parallèles, pas un continuum unique.</li>"
             "</ul>"
             "<p>Conséquence forte : le burn-out ne se traite pas durablement par des séances de relaxation offertes aux salariés. "
             "Les interventions organisationnelles — charge, autonomie, clarté des rôles, reconnaissance — sont les seules à "
             "produire des effets durables.</p>"),
            ("Recruter sans se tromper",
             "<p>Les méta-analyses classent les méthodes de sélection selon leur validité prédictive de la performance future :</p>"
             "<ul>"
             "<li><strong>Efficace</strong> : tests d'aptitude cognitive, tests d'échantillon de travail, entretiens "
             "<strong>structurés</strong> (mêmes questions, grille de cotation définie à l'avance), tests de jugement situationnel, "
             "conscienciosité mesurée par un instrument validé.</li>"
             "<li><strong>Peu ou pas efficace</strong> : entretien non structuré (fortement soumis à l'effet de halo et aux "
             "préférences personnelles), graphologie (validité nulle), années d'expérience au-delà de quelques années, "
             "âge, et la plupart des typologies de personnalité non validées.</li>"
             "</ul>"
             "<p>Les biais les plus coûteux en recrutement : effet de halo, effet de similarité (préférer qui nous ressemble), "
             "effet de contraste entre candidats successifs, et jugement précoce — plusieurs travaux montrent qu'une décision se "
             "forme dans les premières minutes, le reste de l'entretien servant à la justifier.</p>"),
            ("Motivation, sens et engagement",
             "<p>Le modèle des caractéristiques de l'emploi (Hackman et Oldham) identifie cinq dimensions qui produisent la "
             "motivation interne : variété des compétences, identité de la tâche (réaliser un tout identifiable), signification "
             "de la tâche, autonomie et retour d'information.</p>"
             "<p>Le <strong>job crafting</strong> désigne la manière dont les salariés remodèlent eux-mêmes leur poste — en "
             "modifiant les tâches, les relations ou la perception qu'ils en ont. Des agents d'entretien hospitaliers qui se "
             "considèrent comme contribuant au rétablissement des patients rapportent une satisfaction nettement supérieure à "
             "poste identique.</p>"
             "<p>La <strong>justice organisationnelle</strong> pèse énormément, souvent plus que le niveau absolu de rémunération : "
             "justice distributive (les résultats sont-ils équitables ?), procédurale (les procédures sont-elles justes et "
             "cohérentes ?), interactionnelle (suis-je traité avec respect et informé ?). Le sentiment d'injustice procédurale "
             "est l'un des meilleurs prédicteurs du désengagement et du départ.</p>"),
            ("Télétravail, hybride et santé au travail",
             "<p>Les données accumulées depuis 2020 dessinent un tableau nuancé :</p>"
             "<ul>"
             "<li>Le télétravail partiel (2 à 3 jours) est associé à la meilleure satisfaction ; le télétravail intégral augmente "
             "l'isolement et affaiblit les liens faibles, pourtant essentiels à la circulation de l'information et aux opportunités.</li>"
             "<li>La productivité individuelle sur les tâches de concentration s'améliore ; la créativité collective et "
             "l'intégration des nouveaux arrivants souffrent.</li>"
             "<li>Le <strong>technostress</strong> et l'effacement des frontières entre vie professionnelle et personnelle "
             "constituent les risques principaux. Le droit à la déconnexion, inscrit dans la loi française depuis 2017, répond à "
             "ce constat.</li>"
             "<li>Les réunions vidéo produisent une fatigue spécifique : charge cognitive du contact visuel permanent, "
             "auto-observation continue de sa propre image, mobilité réduite et décalages de synchronisation.</li>"
             "</ul>"),
        ],
        "mythes": [
            ("Un salarié heureux est un salarié productif.",
             "La corrélation entre satisfaction et performance est réelle mais modeste (autour de 0,30), et la causalité va souvent dans l'autre sens : bien réussir rend satisfait."),
            ("Les entretiens permettent de bien juger les candidats.",
             "Les entretiens non structurés ont une validité prédictive faible et introduisent des biais massifs. Les entretiens structurés, eux, font partie des meilleures méthodes."),
            ("Le burn-out concerne les personnes fragiles.",
             "Il touche typiquement les personnes très investies et consciencieuses. C'est un problème d'organisation du travail avant d'être un problème individuel."),
        ],
        "chiffres": [
            ("0,30", "Corrélation satisfaction-performance"),
            ("3", "Dimensions du burn-out selon Maslach"),
            ("2017", "Entrée en vigueur du droit à la déconnexion en France"),
            ("2-3 j", "Rythme de télétravail associé à la meilleure satisfaction"),
        ],
        "flashcards": [
            ("Quelle combinaison décrit le job strain de Karasek ?", "Forte demande psychologique associée à une faible latitude décisionnelle, aggravée par un faible soutien social."),
            ("Quelle méthode de recrutement a une validité nulle ?", "La graphologie, malgré sa persistance dans certaines pratiques."),
            ("Qu'est-ce que le job crafting ?", "La manière dont un salarié remodèle lui-même ses tâches, ses relations et la perception de son travail."),
        ],
    },
    "13-education": {
        "sections": [
            ("Ce que la science de l'apprentissage a réellement établi",
             "<p>Six principes disposent de preuves solides et convergentes :</p>"
             "<ol>"
             "<li><strong>La pratique de récupération</strong> : se tester est deux fois plus efficace que relire, y compris "
             "lorsqu'on échoue au test.</li>"
             "<li><strong>La répétition espacée</strong> : la même durée totale d'étude, répartie dans le temps, produit une "
             "rétention bien supérieure.</li>"
             "<li><strong>L'entrelacement</strong> : alterner les types de problèmes rend l'apprentissage plus lent mais bien plus "
             "transférable, car il force à identifier quelle méthode appliquer.</li>"
             "<li><strong>L'élaboration</strong> : se demander « pourquoi ? » et « comment cela se relie-t-il à ce que je sais ? ».</li>"
             "<li><strong>Les exemples résolus</strong> : pour un débutant, étudier des problèmes déjà résolus est plus efficace "
             "que d'en résoudre soi-même — l'effet s'inverse une fois l'expertise acquise (effet de renversement de l'expertise).</li>"
             "<li><strong>Le double codage</strong> : associer explication verbale et schéma pertinent, en évitant les images "
             "décoratives qui ajoutent de la charge inutile.</li>"
             "</ol>"
             "<p>À l'inverse, les techniques les plus populaires — surligner, relire, résumer passivement — figurent parmi les "
             "moins efficaces, alors qu'elles procurent la plus forte impression de maîtrise.</p>"),
            ("Charge cognitive et conception pédagogique",
             "<p>La théorie de la charge cognitive (Sweller) part d'un constat simple : la mémoire de travail est extrêmement "
             "limitée, la mémoire à long terme ne l'est pas. Enseigner, c'est gérer cette limite.</p>"
             "<ul>"
             "<li><strong>Charge intrinsèque</strong> : complexité propre au contenu. On la réduit en segmentant et en "
             "séquençant des prérequis.</li>"
             "<li><strong>Charge extrinsèque</strong> : celle qu'ajoute une mauvaise présentation. À éliminer.</li>"
             "<li><strong>Charge pertinente</strong> : celle qui sert la construction des schémas mentaux. À favoriser.</li>"
             "</ul>"
             "<p>Trois effets à connaître : l'<strong>effet d'attention partagée</strong> (intégrer le texte dans le schéma plutôt "
             "que le mettre en légende à distance), l'<strong>effet de redondance</strong> (lire à voix haute un texte que les "
             "élèves lisent en même temps nuit à la compréhension), et l'<strong>effet de modalité</strong> (image + commentaire "
             "oral vaut mieux qu'image + texte écrit, car deux canaux distincts sont sollicités).</p>"),
            ("Évaluation, feedback et motivation scolaire",
             "<p>Le feedback est l'un des leviers les plus puissants — mais seulement s'il est bien construit. Il doit porter sur "
             "la <strong>tâche et la stratégie</strong>, pas sur la personne : « ta démonstration saute une étape ici » plutôt que "
             "« tu es bon en maths ». Les éloges portant sur l'intelligence réduisent la persévérance après un échec ; ceux "
             "portant sur l'effort et la méthode l'augmentent.</p>"
             "<p>Le feedback doit aussi être <strong>actionnable</strong> (que faire maintenant ?), <strong>proche dans le "
             "temps</strong>, et suivi d'une occasion de retravailler. Un commentaire accompagné d'une note est largement ignoré : "
             "l'attention se porte sur le chiffre.</p>"
             "<p>Côté motivation, la théorie des buts d'accomplissement distingue les <strong>buts de maîtrise</strong> "
             "(progresser, comprendre), associés à la persévérance et à l'usage de stratégies profondes, et les "
             "<strong>buts de performance</strong> (paraître compétent, ne pas paraître incompétent), associés à l'évitement de "
             "l'effort visible et à l'anxiété d'évaluation.</p>"),
            ("Neuromythes : ce qu'il faut cesser d'enseigner",
             "<p>Des enquêtes internationales montrent qu'une majorité d'enseignants — souvent 80 à 95 % — adhèrent à des "
             "neuromythes solidement invalidés :</p>"
             "<ul>"
             "<li><strong>Les styles d'apprentissage</strong> : l'hypothèse d'appariement a été testée et réfutée à de nombreuses reprises.</li>"
             "<li><strong>Le cerveau gauche/droit</strong> comme profil d'élève : sans fondement.</li>"
             "<li><strong>Les 10 % du cerveau</strong> : faux.</li>"
             "<li><strong>La gymnastique cérébrale (Brain Gym)</strong> : justifications neurologiques inventées.</li>"
             "<li><strong>Les fenêtres critiques fermées après 3 ans</strong> : la plasticité se poursuit toute la vie.</li>"
             "</ul>"
             "<p>Ces croyances ne sont pas anodines : elles détournent du temps, de l'argent et de l'attention au détriment de "
             "pratiques dont l'efficacité est établie.</p>"),
        ],
        "mythes": [
            ("Chaque élève a un style d'apprentissage à respecter.",
             "Le neuromythe le plus répandu. Varier les modalités bénéficie à tous ; enfermer un élève dans un canal ne produit aucun gain mesurable."),
            ("Les jeux d'entraînement cérébral rendent plus intelligent.",
             "Ils améliorent la performance au jeu entraîné, avec un transfert quasi nul vers d'autres tâches ou vers la réussite scolaire."),
            ("Redoubler aide les élèves en difficulté.",
             "Les méta-analyses montrent un effet globalement nul ou négatif sur les apprentissages, et négatif sur l'estime de soi et le décrochage, à niveau initial comparable."),
        ],
        "chiffres": [
            ("2×", "Efficacité du rappel actif comparé à la relecture"),
            ("80-95 %", "Enseignants adhérant à au moins un neuromythe"),
            ("1885", "Courbe de l'oubli d'Ebbinghaus"),
            ("4", "Sessions espacées valant mieux qu'une session massée équivalente"),
        ],
        "flashcards": [
            ("Quelle technique populaire est la moins efficace ?", "Le surlignage et la relecture passive, qui créent une illusion de maîtrise."),
            ("Qu'est-ce que l'effet de redondance ?", "Lire à voix haute un texte que les apprenants lisent simultanément nuit à la compréhension en saturant la boucle phonologique."),
            ("Sur quoi doit porter un bon feedback ?", "Sur la tâche et la stratégie, jamais sur la personne, et il doit être actionnable."),
        ],
    },
    "14-sante": {
        "sections": [
            ("Modifier durablement un comportement de santé",
             "<p>L'information seule ne change presque rien : tout le monde sait que fumer nuit à la santé. Les modèles efficaces "
             "agissent ailleurs.</p>"
             "<p>Le modèle <strong>COM-B</strong> résume les conditions du changement : il faut une <strong>Capacité</strong> "
             "(physique et psychologique), une <strong>Opportunité</strong> (environnement, temps, ressources, norme sociale) et "
             "une <strong>Motivation</strong> (réfléchie et automatique). Intervenir sur la seule motivation, ce que font la "
             "plupart des campagnes, échoue quand l'opportunité manque.</p>"
             "<p>Trois techniques ont des preuves solides :</p>"
             "<ul>"
             "<li><strong>Les intentions de mise en œuvre</strong> : formuler un plan « si… alors » précis (« si c'est mardi 18 h, "
             "alors je vais à la piscine ») double environ la probabilité de passage à l'acte par rapport à une bonne résolution vague.</li>"
             "<li><strong>Le contraste mental</strong> : imaginer le résultat souhaité, puis l'obstacle principal, puis planifier "
             "la réponse à cet obstacle (méthode WOOP).</li>"
             "<li><strong>L'empilement d'habitudes</strong> : rattacher le nouveau comportement à une routine déjà solide.</li>"
             "</ul>"
             "<p>Le modèle transthéorique (précontemplation, contemplation, préparation, action, maintien, rechute) reste utile "
             "cliniquement pour adapter le discours au stade de la personne, même s'il est critiqué sur le plan empirique.</p>"),
            ("Stress, immunité et santé physique",
             "<p>La psychoneuroimmunologie a établi des liens robustes. Le stress chronique maintient l'axe hypothalamo-hypophyso-"
             "surrénalien activé, avec un cortisol durablement élevé : cicatrisation ralentie, réponse vaccinale diminuée, "
             "inflammation de bas grade, risque cardiovasculaire accru.</p>"
             "<p>Deux résultats marquants : des volontaires exposés à un rhinovirus développent d'autant plus souvent un rhume "
             "qu'ils rapportent un stress chronique élevé ; et chez des aidants de personnes atteintes de démence, la "
             "cicatrisation d'une petite plaie standardisée prend en moyenne 24 % de temps en plus.</p>"
             "<p>Nuance essentielle : le stress <strong>aigu</strong> mobilise l'immunité et est adaptatif. C'est la chronicité et "
             "l'absence de contrôle qui nuisent. La façon d'interpréter le stress compte également : les personnes qui le "
             "considèrent comme mobilisateur plutôt que nocif présentent un profil cardiovasculaire plus favorable dans les "
             "études expérimentales.</p>"),
            ("Douleur chronique : un modèle qui a tout changé",
             "<p>La douleur n'est pas un signal proportionnel à la lésion : c'est une <strong>production du cerveau</strong>, "
             "modulée par l'attention, l'émotion, le contexte et les croyances. La théorie du portillon (Melzack et Wall) puis la "
             "théorie de la neuromatrice ont remplacé le modèle du simple câble d'alarme.</p>"
             "<p>Trois faits qui illustrent ce renversement : des IRM du dos réalisées chez des personnes sans aucune douleur "
             "révèlent des hernies discales chez une proportion importante d'entre elles ; des soldats gravement blessés "
             "rapportent parfois une douleur faible, le contexte donnant à la blessure une signification de survie ; et la douleur "
             "du membre fantôme démontre qu'aucun tissu lésé n'est nécessaire pour souffrir.</p>"
             "<p>Ce que cela change en pratique : l'éducation à la neurophysiologie de la douleur réduit réellement l'intensité "
             "ressentie et l'incapacité ; la <strong>catastrophisation</strong> (ruminer, amplifier, se sentir impuissant) est le "
             "meilleur prédicteur psychologique du passage à la chronicité ; l'exposition graduée à l'activité vaut mieux que le "
             "repos prolongé, qui entretient la peur du mouvement (kinésiophobie).</p>"),
            ("Observance, relation de soin et décision partagée",
             "<p>Environ 50 % des traitements chroniques ne sont pas suivis comme prescrits. Les causes sont rarement de la "
             "négligence : effets indésirables, croyances sur le médicament, complexité du schéma, coût, absence de symptômes "
             "ressentis, et surtout qualité de la relation avec le soignant.</p>"
             "<p>Ce qui améliore l'observance : simplifier les schémas, expliquer le rapport bénéfice/risque en valeurs absolues "
             "plutôt qu'en pourcentages relatifs, explorer les croyances du patient sans les juger, et décider ensemble. "
             "La <strong>décision médicale partagée</strong> améliore la satisfaction, l'observance et souvent les résultats "
             "cliniques.</p>"
             "<p>Un chiffre parlant : les médecins interrompent leurs patients en moyenne après une vingtaine de secondes. "
             "Lorsqu'on les laisse terminer, la plupart s'arrêtent d'eux-mêmes en moins de deux minutes — et livrent des "
             "informations diagnostiques essentielles.</p>"),
        ],
        "mythes": [
            ("Le stress donne le cancer.",
             "Aucun lien causal direct établi. Le stress agit indirectement, via des comportements (tabac, alcool, sommeil, dépistage retardé) et l'inflammation chronique."),
            ("Il faut 21 jours pour créer une habitude.",
             "Chiffre issu d'une observation en chirurgie esthétique, jamais d'une étude sur l'habitude. La recherche réelle trouve une médiane d'environ 66 jours, avec une variabilité de 18 à 254 jours."),
            ("La douleur chronique est psychologique.",
             "Faux contresens. La douleur est toujours réelle. Dire que le cerveau la module ne signifie pas qu'elle est imaginaire : cela ouvre au contraire des leviers thérapeutiques efficaces."),
        ],
        "chiffres": [
            ("50 %", "Traitements chroniques non suivis comme prescrits"),
            ("66 j", "Durée médiane d'installation d'une habitude"),
            ("24 %", "Retard de cicatrisation observé chez des aidants stressés"),
            ("≈ 20 s", "Délai moyen avant qu'un médecin interrompe son patient"),
        ],
        "flashcards": [
            ("Que signifie COM-B ?", "Capacité, Opportunité, Motivation — les trois conditions nécessaires au changement de comportement."),
            ("Qu'est-ce qu'une intention de mise en œuvre ?", "Un plan précis « si (situation) alors (action) » qui augmente fortement le passage à l'acte."),
            ("Quel est le meilleur prédicteur psychologique de chronicisation de la douleur ?", "La catastrophisation : ruminer, amplifier et se sentir impuissant face à la douleur."),
        ],
    },
    "15-legale": {
        "sections": [
            ("Fiabilité du témoignage et identification",
             "<p>Le témoignage oculaire est la preuve la plus convaincante pour un jury — et l'une des moins fiables. Aux "
             "États-Unis, sur les premières centaines de personnes innocentées par l'ADN après condamnation, environ "
             "<strong>70 %</strong> l'avaient été sur la base d'une identification erronée par un témoin sincère.</p>"
             "<p>Les facteurs qui dégradent la fiabilité sont bien documentés : le <strong>stress extrême</strong>, la "
             "<strong>focalisation sur l'arme</strong> (l'attention se porte sur le pistolet, pas sur le visage), la durée "
             "d'exposition, le délai, et l'<strong>effet d'autre origine ethnique</strong> (on identifie moins bien les visages "
             "d'un groupe ethnique peu familier).</p>"
             "<p>Les réformes validées par la recherche : procédure d'identification <strong>séquentielle</strong> plutôt que "
             "simultanée (pour éviter la comparaison relative), administration <strong>en double aveugle</strong> (l'agent ignore "
             "qui est le suspect), consigne explicite indiquant que l'auteur peut ne pas figurer parmi les personnes présentées, "
             "et recueil immédiat du <strong>degré de confiance</strong> — car la confiance initiale, avant toute confirmation "
             "extérieure, est bien plus informative que la certitude affichée des mois plus tard à l'audience.</p>"),
            ("Faux aveux et techniques d'interrogatoire",
             "<p>Contre-intuitif mais massivement documenté : des personnes innocentes avouent des crimes qu'elles n'ont pas "
             "commis. On distingue les faux aveux volontaires (recherche de notoriété, protection d'un tiers), "
             "<strong>soumis</strong> (céder pour faire cesser une pression insoutenable) et <strong>internalisés</strong> "
             "(la personne finit par croire elle-même à sa culpabilité).</p>"
             "<p>Les facteurs de risque sont connus : interrogatoires très longs, privation de sommeil, présentation de fausses "
             "preuves (légale aux États-Unis, interdite en France), minimisation morale du crime, jeunesse, déficience "
             "intellectuelle et suggestibilité élevée.</p>"
             "<p>La technique <strong>Reid</strong>, accusatoire et fondée sur la confrontation, est associée à un taux élevé de "
             "faux aveux. La méthode <strong>PEACE</strong>, développée au Royaume-Uni, est non accusatoire, centrée sur le recueil "
             "d'informations et le récit libre ; elle obtient autant de vrais aveux avec bien moins de faux. L'enregistrement "
             "audiovisuel intégral des auditions est la garantie la plus efficace.</p>"),
            ("Évaluer la dangerosité : méthodes et limites",
             "<p>Trois générations de méthodes se sont succédé : le jugement clinique non structuré (peu fiable, à peine meilleur "
             "que le hasard), les instruments actuariels purement statistiques (plus précis mais aveugles au cas particulier), et "
             "le <strong>jugement professionnel structuré</strong> (grilles de facteurs de risque validées, complétées par "
             "l'analyse clinique), aujourd'hui recommandé.</p>"
             "<p>Deux limites majeures doivent être comprises. D'abord, ces outils prédisent des <strong>probabilités de groupe</strong>, "
             "pas des comportements individuels. Ensuite, le problème des <strong>taux de base faibles</strong> : quand un "
             "événement est rare, même un test précis produit une écrasante majorité de faux positifs. Prédire un événement rare "
             "est mathématiquement très difficile, ce qui appelle une grande prudence dans l'usage judiciaire de ces instruments.</p>"
             "<p>Rappel important : les personnes atteintes de troubles psychiques sévères sont statistiquement bien plus souvent "
             "victimes qu'auteurs de violences. Les facteurs de risque les plus prédictifs restent les antécédents de violence, "
             "l'usage de substances et l'instabilité sociale.</p>"),
            ("Psychologie de la décision judiciaire",
             "<p>Les décisions de justice sont soumises aux mêmes biais que les autres décisions humaines :</p>"
             "<ul>"
             "<li><strong>Ancrage</strong> : le réquisitoire du procureur influence la peine prononcée, y compris chez des "
             "magistrats expérimentés à qui l'on présente des réquisitions tirées au sort.</li>"
             "<li><strong>Biais rétrospectif</strong> : une fois l'issue connue, la faute paraît évidente et prévisible.</li>"
             "<li><strong>Effet de croyance en un monde juste</strong> : tendance à chercher ce que la victime « a fait » pour "
             "que cela lui arrive.</li>"
             "<li><strong>Apparence physique</strong> : elle influence les jugements de culpabilité, surtout quand les preuves "
             "sont ambiguës.</li>"
             "</ul>"
             "<p>Les parades sont structurelles plus qu'individuelles : délibération collective organisée, motivation écrite "
             "obligatoire, grilles de référence, formation des professionnels aux biais — dont l'effet est réel mais limité, car "
             "connaître un biais ne suffit pas à s'en préserver.</p>"),
        ],
        "mythes": [
            ("Le détecteur de mensonge est fiable.",
             "Le polygraphe mesure l'activation physiologique, pas le mensonge. Son taux de faux positifs est élevé et ses résultats sont irrecevables devant la plupart des juridictions, dont les tribunaux français."),
            ("Le profilage criminel permet de dresser un portrait précis du coupable.",
             "Les évaluations empiriques montrent que les « profils » sont souvent vagues et faiblement prédictifs. La série télévisée dépasse largement la réalité scientifique."),
            ("Un témoin sûr de lui est un témoin fiable.",
             "La confiance mesurée immédiatement, avant toute confirmation externe, est informative. Celle exprimée des mois plus tard à l'audience a été gonflée par les retours reçus entre-temps."),
        ],
        "chiffres": [
            ("≈ 70 %", "Innocentés par l'ADN ayant été condamnés sur une identification erronée"),
            ("PEACE", "Méthode d'audition non accusatoire de référence"),
            ("1897", "Le Suicide de Durkheim, matrice de la criminologie sociale"),
            ("1876", "L'Homme criminel de Lombroso, théorie aujourd'hui invalidée"),
        ],
        "flashcards": [
            ("Pourquoi la procédure d'identification séquentielle est-elle préférable ?", "Elle empêche la comparaison relative entre personnes présentées et réduit les identifications erronées."),
            ("Qu'est-ce qu'un faux aveu internalisé ?", "Un aveu où la personne finit par croire elle-même à sa culpabilité, souvent après un interrogatoire long et suggestif."),
            ("Quel problème statistique limite la prédiction de la dangerosité ?", "Le taux de base faible : prédire un événement rare produit une majorité de faux positifs, même avec un bon outil."),
        ],
    },
    "16-comparee": {
        "sections": [
            ("Cognition animale : ce que l'on sait vraiment",
             "<p>Les découvertes des trente dernières années ont profondément modifié notre vision :</p>"
             "<ul>"
             "<li><strong>Usage et fabrication d'outils</strong> : chimpanzés, corbeaux de Nouvelle-Calédonie (qui façonnent des "
             "crochets), loutres, et même certains poissons qui utilisent des rochers comme enclumes.</li>"
             "<li><strong>Mémoire épisodique-<em>like</em></strong> : les geais buissonniers se souviennent de <em>quoi</em> ils "
             "ont caché, <em>où</em> et <em>quand</em>, et récupèrent en priorité les aliments périssables.</li>"
             "<li><strong>Test du miroir</strong> : réussi par les grands singes, les dauphins, les éléphants d'Asie, les pies et, "
             "avec un protocole adapté, certains poissons nettoyeurs — ce qui alimente un débat sur ce que ce test mesure réellement.</li>"
             "<li><strong>Culture animale</strong> : des traditions locales de chasse, de nettoyage ou de chants se transmettent "
             "socialement et varient d'un groupe à l'autre chez les chimpanzés, les cétacés et les oiseaux chanteurs.</li>"
             "<li><strong>Coopération et sens de l'équité</strong> : des capucins refusent une récompense pourtant appréciée s'ils "
             "voient un congénère mieux payé pour la même tâche.</li>"
             "</ul>"),
            ("Anthropomorphisme et anthropodéni",
             "<p>Deux erreurs symétriques guettent l'observateur. L'<strong>anthropomorphisme</strong> attribue des états mentaux "
             "humains sans preuve : le chien à la posture basse « culpabilise » — des expériences montrent en réalité qu'il réagit "
             "au ton de son maître, indépendamment de toute bêtise commise.</p>"
             "<p>L'<strong>anthropodéni</strong>, terme de Frans de Waal, est l'erreur inverse : refuser par principe toute "
             "continuité, alors que nous partageons une histoire évolutive, des structures cérébrales et des neurotransmetteurs "
             "avec les autres mammifères. Nier toute forme d'émotion chez un chimpanzé est aussi peu scientifique que lui prêter "
             "des pensées humaines.</p>"
             "<p>Le <strong>canon de Morgan</strong> fournit la règle de prudence : ne pas interpréter un comportement par un "
             "processus mental élevé si un processus plus simple suffit à l'expliquer. Mais « plus simple » ne veut pas dire "
             "« toujours vrai » : chez une espèce proche de nous, l'explication complexe peut être la plus parcimonieuse.</p>"),
            ("Bien-être animal et applications",
             "<p>Le cadre de référence a évolué des « cinq libertés » (absence de faim, d'inconfort, de douleur, de peur, et "
             "liberté d'exprimer un comportement normal) vers les <strong>« cinq domaines »</strong>, qui intègrent explicitement "
             "l'état mental de l'animal, et pas seulement l'absence de souffrance.</p>"
             "<p>Deux notions structurent la recherche actuelle : l'<strong>enrichissement environnemental</strong> (offrir des "
             "possibilités de comportements naturels réduit mesurablement les stéréotypies en captivité) et les "
             "<strong>biais cognitifs comme indicateurs émotionnels</strong> — un animal dans un état affectif négatif interprète "
             "de façon pessimiste un signal ambigu, exactement comme un humain anxieux. C'est aujourd'hui l'un des rares moyens "
             "d'accéder objectivement à l'état émotionnel d'un animal.</p>"
             "<p>Applications pratiques : conception des élevages et des zoos, entraînement par renforcement positif (nettement "
             "supérieur aux méthodes aversives chez le chien, y compris en efficacité), médiation animale, et détection de "
             "maladies par l'olfaction canine.</p>"),
        ],
        "mythes": [
            ("Le chien qui baisse la tête se sent coupable.",
             "Il réagit au ton et à la posture de son maître. Des expériences où le maître gronde un chien innocent produisent exactement la même « mine coupable »."),
            ("Les poissons n'ont que trois secondes de mémoire.",
             "Faux. Des poissons rouges apprennent et retiennent des associations pendant des mois, et certaines espèces utilisent des outils."),
            ("La hiérarchie du loup alpha justifie la domination sur le chien.",
             "Le modèle vient de loups captifs et non apparentés. En milieu naturel, une meute est une famille : les « alphas » sont simplement les parents. Son auteur a lui-même demandé l'abandon du terme."),
        ],
        "chiffres": [
            ("1973", "Nobel de Lorenz, Tinbergen et von Frisch pour l'éthologie"),
            ("5", "Domaines du bien-être animal"),
            ("4", "Questions de Tinbergen sur tout comportement"),
            ("1872", "Publication de L'Expression des émotions de Darwin"),
        ],
        "flashcards": [
            ("Qu'est-ce que l'anthropodéni ?", "Le refus par principe de reconnaître une continuité mentale entre l'humain et les autres animaux, erreur symétrique de l'anthropomorphisme."),
            ("Que mesure le biais de jugement chez l'animal ?", "L'interprétation d'un signal ambigu, révélatrice de son état émotionnel — pessimiste s'il est négatif."),
            ("D'où vient le mythe du loup alpha ?", "D'observations de loups captifs non apparentés ; en nature, la meute est une famille et les « alphas » sont les parents."),
        ],
    },
}
