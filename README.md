# 🧠 Psyclopédia

**L'encyclopédie vivante et illustrée de la psychologie, en français.**

Un site d'apprentissage complet et autonome : 26 catégories rédigées, plus de 1 100 fiches consultables
(références, théories, courants, cas cliniques, débats, méthodes, pratique, métiers), 13 ouvrages du domaine
public lisibles directement en ligne, une recherche globale instantanée, 26 quiz notés avec corrigés, un
laboratoire d'expériences jouables, un système de révision espacée, un **cursus annuel de 60 cours**
de 50 minutes (emploi du temps, replays YouTube francophones, fiches synchronisées) et des parcours
guidés — le tout hébergé sur GitHub Pages.

## 🚀 Accéder au site

➡️ **[Ouvrir Psyclopédia](https://errornoname.github.io/P-S-C/)** — en ligne, mis à jour automatiquement à chaque push sur `main`.

En local, un simple double-clic sur [`index.html`](index.html) suffit pour la quasi-totalité du site. Seule la
**recherche globale** a besoin d'un serveur web, car elle charge un index JSON (les navigateurs bloquent
`fetch` sur le protocole `file://`) :

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000/
```

## ✨ Ce que contient le site

### Un moteur de recherche intelligent

Accessible partout par <kbd>Ctrl</kbd> + <kbd>K</kbd> (ou la touche <kbd>/</kbd>), il interroge un index de
**1 695 entrées** couvrant catégories, chapitres, notions, expériences, auteurs, théories, courants, troubles,
biais, tests, cas cliniques, débats, idées reçues, questions fréquentes, fiches pratiques, métiers, expériences
du laboratoire, termes anglais, dates, livres, quiz et cours magistraux. Il ignore les accents, accepte plusieurs mots,
**tolère les fautes de frappe** (distance de Levenshtein bornée), classe les résultats par pertinence de champ,
les regroupe par type, surligne les correspondances et se pilote entièrement au clavier.

### Un lecteur de livres intégré

Plus besoin de télécharger quoi que ce soit : [`lecteur.html`](livres-psychologie/07-ebook-final/lecteur.html)
affiche les ouvrages page par page avec PDF.js, et propose

- l'**extraction du texte** de la page, affiché côte à côte avec l'image ;
- la **reconnaissance optique** (Tesseract.js, modèle français) pour les pages qui ne sont que des images —
  planches gravées, pages de titre, tableaux. Elle s'exécute entièrement dans le navigateur : aucun fichier
  n'est envoyé sur un serveur ;
- la **modernisation du français du XIXe siècle** : réécriture des formes anciennes (« étoit » → « était »,
  « enfans » → « enfants », « s » long) et surlignage d'un glossaire de près de cent termes de psychologie
  d'époque, avec leur équivalent actuel en info-bulle ;
- une **traduction** de la page affichée vers six langues, pour les lecteurs non francophones ;
- le zoom, la navigation au clavier et un **marque-page** par ouvrage.

### 26 catégories rédigées

Chaque fiche comporte un sommaire latéral qui suit la lecture, une barre de progression, des objectifs
pédagogiques, des chapitres de fond, des **chiffres clés**, une rubrique **« idées reçues »** qui corrige les
neuromythes les plus répandus, des planches commentées, les expériences fondatrices du domaine, les ouvrages
sources lisibles en ligne, des flashcards de rappel actif et un quiz noté.

| # | Domaine | # | Domaine |
|---|---------|---|---------|
| 01 | Fondamentaux et méthodes | 14 | Psychologie de la santé |
| 02 | Histoire et grands courants | 15 | Psychologie légale et criminologie |
| 03 | Psychologie cognitive | 16 | Psychologie comparée et éthologie |
| 04 | Psychologie sociale | 17 | Psychologie interculturelle |
| 05 | Psychologie du développement | 18 | Psycholinguistique et langage |
| 06 | Personnalité et différences individuelles | 19 | Psychométrie et mesure |
| 07 | Émotions et motivation | 20 | Psychologie du sport et performance |
| 08 | Neurosciences et psychologie biologique | 21 | Psychologie du consommateur |
| 09 | Psychopathologie | 22 | Psychologie du numérique |
| 10 | Thérapies et interventions | 23 | Psychologie évolutionniste |
| 11 | Psychologie positive et bien-être | 24 | Vieillissement et gérontopsychologie |
| 12 | Psychologie du travail | 25 | Psychologie environnementale |
| 13 | Psychologie de l'éducation | 26 | Psychologie politique et croyances |

### Une base de références filtrable

| Rubrique | Contenu |
|---|---|
| [Expériences célèbres](livres-psychologie/07-ebook-final/references/experiences.html) | 46 études : protocole, résultat, portée **et critiques** |
| [Grandes figures](livres-psychologie/07-ebook-final/references/auteurs.html) | 72 biographies : apport décisif, parcours, œuvre, citation |
| [Répertoire des troubles](livres-psychologie/07-ebook-final/references/troubles.html) | 36 tableaux cliniques : signes, mécanismes, prises en charge validées |
| [Biais cognitifs](livres-psychologie/07-ebook-final/references/biais.html) | 58 biais : définition, exemple concret, **parade** |
| [Tests psychométriques](livres-psychologie/07-ebook-final/references/tests.html) | 27 instruments : ce qu'ils mesurent, passation, interprétation, limites |
| [Chronologie](livres-psychologie/07-ebook-final/references/chronologie.html) | 83 dates réparties en six grandes périodes |
| [Théories et modèles](livres-psychologie/07-ebook-final/references/theories.html) | 73 modèles : l'idée, le mécanisme, les usages **et les limites** |
| [Cas cliniques célèbres](livres-psychologie/07-ebook-final/references/cas.html) | 30 histoires singulières qui ont fait basculer la théorie |
| [Débats et controverses](livres-psychologie/07-ebook-final/references/debats.html) | 20 dossiers : chaque camp au meilleur de ses arguments, puis l'état des données |
| [Les grands courants](livres-psychologie/07-ebook-final/references/courants.html) | 14 écoles : postulat, méthode, apports, critiques, héritage |
| [Idées reçues et neuromythes](livres-psychologie/07-ebook-final/references/mythes.html) | 50 affirmations très répandues, avec leur origine et leur part de vérité |

### Comprendre comment on sait ce qu'on sait

- **[Méthodes et statistiques](livres-psychologie/07-ebook-final/methodes.html)** — 12 chapitres et 50 notions :
  plans de recherche, valeur *p*, taille d'effet, puissance, biais, éthique, crise de la réplication et lecture
  critique d'un article.
- **[5 auto-évaluations pédagogiques](livres-psychologie/07-ebook-final/auto-evaluations.html)** — cinq grands
  facteurs, chronotype, méthodes d'apprentissage, régulation émotionnelle, procrastination. Les 80 affirmations
  ont été **rédigées pour ce site** afin d'illustrer la construction d'une mesure (items inversés, échelle de
  Likert, score par dimension) : elles ne reproduisent aucun instrument publié et **n'ont aucune valeur
  diagnostique**. Rien n'est enregistré ni transmis.
- **[Laboratoire](livres-psychologie/07-ebook-final/laboratoire.html)** — 7 expériences classiques rejouables
  dans le navigateur (Stroop, empan mnésique, temps de réaction, Müller-Lyer, position sérielle, flanker,
  ancrage), avec vos propres résultats chiffrés puis leur explication.

### Passer à la pratique

- **[Psychologie appliquée](livres-psychologie/07-ebook-final/pratique.html)** — 41 fiches action : apprendre,
  procrastiner moins, dormir, décider, communiquer, gérer le stress, chacune avec l'état de la recherche, un
  protocole en étapes et le piège classique.
- **[Métiers et études](livres-psychologie/07-ebook-final/metiers.html)** — 20 métiers décrits de l'intérieur et
  les quatre étapes du cursus français.
- **[Lexique anglais-français](livres-psychologie/07-ebook-final/lexique.html)** — 158 termes traduits et 18 faux
  amis, pour lire les articles scientifiques sans contresens.
- **[Aide et ressources](livres-psychologie/07-ebook-final/aide.html)** — numéros d'urgence et d'écoute (France,
  Belgique, Suisse, Canada), parcours de soin, remboursement, à quoi ressemble une première séance, comment
  aider un proche, et où lire la recherche en accès libre.
- **[Questions fréquentes](livres-psychologie/07-ebook-final/faq.html)** — 50 questions, avec des réponses qui
  précisent aussi ce qu'on ignore encore.

### Retenir durablement

- **[Révision espacée](livres-psychologie/07-ebook-final/revision.html)** — 1 000 cartes tirées de tout le site,
  replanifiées automatiquement selon vos réponses (algorithme inspiré de SM-2), réparties en 33 paquets.
- **[26 fiches de révision imprimables](livres-psychologie/07-ebook-final/fiches/index.html)** — l'essentiel de
  chaque domaine sur une page, plus une fiche unique regroupant tout le programme.
- **[Plan du site et index A-Z](livres-psychologie/07-ebook-final/plan.html)** — toutes les pages et 941 entrées
  classées alphabétiquement.

### Et aussi

- **[Dictionnaire A-Z](livres-psychologie/07-ebook-final/dictionnaire.html)** — 365 notions définies, chacune
  reliée à la catégorie qui l'approfondit, avec filtre texte et navigation alphabétique.
- **[26 quiz notés sur 20](livres-psychologie/07-ebook-final/quiz/index.html)** — 207 questions, corrigé complet
  et explication du raisonnement pour chaque réponse, y compris les bonnes. Un examen final de 20 questions.
- **[6 parcours guidés](livres-psychologie/07-ebook-final/parcours.html)** — « je pars de zéro », « mieux me
  comprendre », « comprendre la souffrance psychique », « réviser un examen », « psychologie au travail »,
  « les frontières de la discipline ». Les étapes déjà faites se cochent toutes seules.
- **[Guide d'apprentissage](livres-psychologie/07-ebook-final/apprendre.html)** — les cinq techniques validées
  par la science cognitive, les erreurs de révision les plus coûteuses, et un plan concret sur 30 jours.
- **[Emploi du temps & cours](livres-psychologie/07-ebook-final/emploi-du-temps.html)** — cursus annuel
  2026-2027 (2 semestres × 15 semaines × CM + TD) : 60 séances de 50 minutes découpées en Exposition /
  Démonstration / Cas clinique / Synthèse & quiz flash. Calendrier semaine ou mois, compte à rebours avant
  le prochain cours, assiduité et notes de quiz dans le navigateur.
- **[Lecteur de cours](livres-psychologie/07-ebook-final/cours/lecteur.html)** — iframe YouTube 100 %
  francophone (Collège de France, universités, archives), panneau de fiches synchronisé sur une timeline
  JSON, surlignage des notions au moment où elles sont nommées, notes exportables en Markdown ou PDF.
  Si les sous-titres YouTube sont inaccessibles, la timeline du cours prend le relais.
- **[Cours & archives](livres-psychologie/07-ebook-final/cours/index.html)** — tous les replays filtrables
  par catégorie, thème et intervenant.
- **[Bibliothèque](livres-psychologie/07-ebook-final/bibliotheque.html)** — 13 ouvrages du domaine public.
- **[Crédits et sources](livres-psychologie/07-ebook-final/credits.html)** — chaque illustration avec son
  fichier d'origine sur Wikimedia Commons et sa licence exacte, vérifiés un par un via l'API de Commons.
- **Progression enregistrée** localement (localStorage) : score de maîtrise, catégories lues, meilleurs scores.

## 🗂 Structure du dépôt

```
/
├── index.html                          Accueil (généré par build_home.py)
├── sitemap.xml, robots.txt             Générés par build_sitemap.py
├── assets-ebook/
│   ├── css/style.css + v2 v3 v4 + cours.css
│   └── js/app.js, search.js,           Progression, recherche, lecteur, interface,
│          lecteur.js, ui-v2.js,        laboratoire, révision, auto-évaluations, cours
│          quiz-engine.js, laboratoire.js,
│          revision.js, autoeval.js, cours.js
└── livres-psychologie/
    ├── 07-ebook-final/                 ★ LE SITE ★
    │   ├── build_ebook.py              Point d'entrée du générateur
    │   ├── shell.py, content.py        Coque commune, fusion des données
    │   ├── build_*.py                  Générateurs (catégories, références, pages, accueil, index)
    │   ├── data_*.py                   Toutes les données du site
│   ├── categories/, references/,   Pages générées
│   │   quiz/, fiches/, laboratoire/,
│   │   auto-evaluations/, *.html
│   ├── search-index.json           Index de recherche généré
│   └── revision-cards.json         Cartes de révision espacée générées
    ├── 06-pdf-domaine-public/          13 ouvrages, classés par thème
    ├── 05-larousse-illustre-complet/   Version précédente + bibliothèque d'illustrations
    ├── 04-guide-enrichi-illustre/      Guide original 10 chapitres
    └── 01-.. / 02-.. / 03-..           Fiches sur les ouvrages commerciaux et ressources initiales
```

## 🔧 Régénérer le site

Tout le contenu HTML est produit à partir des fichiers `data_*.py`. Pour modifier un texte, une définition
ou une question de quiz, on édite la donnée puis on relance le générateur :

```bash
cd livres-psychologie/07-ebook-final
python3 build_ebook.py
```

Le script régénère l'intégralité du site — 98 pages : les 26 fiches de catégorie, le dictionnaire, les onze
pages de références, les pages de savoirs (méthodes, pratique, lexique, métiers), les repères (courants, idées
reçues, questions fréquentes, aide), les auto-évaluations, le laboratoire, la révision espacée, les fiches
imprimables, les quiz, la bibliothèque, le lecteur, les parcours, le guide d'apprentissage, les crédits, le plan
du site, la page d'accueil, l'index de recherche, `sitemap.xml` et `robots.txt` — et affiche un récapitulatif
chiffré.

Deux vérifications utiles après une modification :

```bash
python3 -c "import json; print(len(json.load(open('search-index.json'))))"   # index de recherche
node --check ../../assets-ebook/js/autoeval.js                               # syntaxe d'un script
```

## 📖 Déploiement

GitHub Pages est actif sur ce dépôt (déploiement depuis `main`, racine `/`). Le workflow
[`.github/workflows/pages.yml`](.github/workflows/pages.yml) redéploie également à chaque push. Aucune action
manuelle n'est nécessaire : le site est à jour une à deux minutes après un `git push`.

## ⚖️ Licences et avertissement

Les fiches, notices, définitions, flashcards, questions de quiz et affirmations des auto-évaluations sont des
**contenus originaux** rédigés pour ce projet. Aucun instrument psychométrique publié n'est reproduit. Les ouvrages sont dans le domaine public et proviennent d'Internet Archive, Gallica (BnF), du Project
Gutenberg, des Classiques des sciences sociales (UQAC) et de Darwin Online. Les illustrations viennent de
Wikimedia Commons, sous domaine public ou licence libre (CC0, CC BY, CC BY-SA) ; le détail fichier par fichier
figure sur la [page de crédits](livres-psychologie/07-ebook-final/credits.html).

⚠️ Psyclopédia est un contenu **pédagogique de vulgarisation**. Il ne remplace ni un diagnostic, ni un avis
médical, ni un suivi psychologique professionnel. En cas de souffrance, adressez-vous à un médecin ou à un
psychologue. Urgence en France : **3114** (prévention du suicide, gratuit, 24 h/24) ou **15**.
