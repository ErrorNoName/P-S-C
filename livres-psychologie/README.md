# 🧠 Livres de Psychologie — Dossier Complet

Bienvenue dans la **bibliothèque pédagogique de psychologie** : Ebook complet (Psyclopédia), ouvrages du domaine
public, quiz notés et ressources organisées.

## 🚀 Par où commencer ?

| Étape | Action | Fichier |
|-------|--------|---------|
| 1 | **Ouvrir l'Ebook Psyclopédia** (recommandé) | [`../index.html`](../index.html) ou [`07-ebook-final/index.html`](07-ebook-final/index.html) |
| 2 | **Faire un quiz noté** | [`07-ebook-final/quiz/index.html`](07-ebook-final/quiz/index.html) |
| 3 | **Apprendre à apprendre** | [`07-ebook-final/apprendre.html`](07-ebook-final/apprendre.html) |
| 4 | **Bibliothèque de 13 livres complets** | [`07-ebook-final/bibliotheque.html`](07-ebook-final/bibliotheque.html) |
| 5 | *(Ancienne version)* Larousse illustré | [`05-larousse-illustre-complet/index.html`](05-larousse-illustre-complet/index.html) |

## 📂 Structure du dossier

```
livres-psychologie/
├── 00-ACCUEIL/                  Guide de navigation par profil
├── 01-short-cuts-psychologie/   Référence (Wild, EDP Sciences 2023) — non libre de droits
├── 02-petit-larousse-psychologie/  Référence (Larousse 2019) — non libre de droits
├── 03-ressources-gratuites-legales/  Classiques initiaux (première recherche)
├── 04-guide-enrichi-illustre/   Guide original 10 chapitres (conservé)
├── 05-larousse-illustre-complet/  Larousse illustré (10 catégories, version précédente, conservée)
├── 06-pdf-domaine-public/       ★ 13 LIVRES COMPLETS ★ classés par thème
│   ├── psychologie-generale/    James, Binet, Le Bon (éducation)
│   ├── psychologie-sociale/     Le Bon (foules), Durkheim (suicide)
│   ├── psychologie-clinique/    Freud
│   ├── psychopathologie/        Ribot (x2), Janet, Charcot
│   ├── histoire-psychologie/    Taine
│   ├── psychologie-legale/      Lombroso
│   ├── psychologie-comparative/ Darwin
│   └── education/
└── 07-ebook-final/              ★★ EBOOK PRINCIPAL (PSYCLOPÉDIA) ★★
    ├── index.html               Grille des 17 catégories
    ├── categories/*.html        16 fiches enrichies + dictionnaire.html
    ├── quiz/                    Hub + moteur de quiz (10 thèmes, 59 questions)
    ├── apprendre.html           Méthodes d'apprentissage (VARK, rappel actif...)
    ├── bibliotheque.html        Les 13 livres complets, présentés
    ├── data_categories.py       Données sources des 17 catégories (Python)
    ├── data_quiz.py             Données sources des 10 quiz (Python)
    └── build_ebook.py           Générateur du site (relancer après modif des données)
```

Le design (CSS/JS partagés) vit dans [`/assets-ebook`](../assets-ebook) à la racine du dépôt, pour être servi
correctement par GitHub Pages depuis la page d'accueil [`/index.html`](../index.html).

## 📚 Les 13 livres complets du domaine public

| Ouvrage | Auteur | Année | Format | Taille |
|---------|--------|-------|--------|--------|
| Précis de psychologie | William James | 1909 | PDF | ~9 Mo |
| De l'intelligence | Hippolyte Taine | 1870 | PDF | 25 Mo |
| La Suggestibilité | Alfred Binet | — | HTML | Complet |
| Psychologie des foules | Gustave Le Bon | 1895 | PDF | 13 Mo |
| Le Suicide : étude de sociologie | Émile Durkheim | 1897 | PDF | 15 Mo |
| Les maladies de la volonté | Théodule Ribot | 1883 | PDF | ~9 Mo |
| Les maladies de la mémoire | Théodule Ribot | 1898 | PDF | 6,3 Mo |
| Les névroses | Pierre Janet | 1909 | PDF | 2 Mo |
| Leçons sur les maladies du système nerveux | Jean-Martin Charcot | 1884 | PDF | 38 Mo |
| L'interprétation des rêves | Sigmund Freud (trad. fr.) | 1900 | HTML | Complet |
| Psychologie de l'éducation | Gustave Le Bon | — | HTML | Complet |
| L'homme criminel | Cesare Lombroso | 1887 | PDF | 35 Mo |
| L'expression des émotions chez l'homme et les animaux | Charles Darwin (trad.) | 1877 | PDF | 15 Mo |

**Sources :** [Gallica BnF](https://gallica.bnf.fr/), [Project Gutenberg](https://www.gutenberg.org/),
[Internet Archive](https://archive.org/), [Classiques UQAM](https://classiques.uqam.ca/),
[Darwin Online](https://darwin-online.org.uk/), [BabordNum](https://www.babordnum.fr/).
Tous ces ouvrages sont dans le domaine public (auteurs décédés depuis plus de 70 ans).
Le texte de Lombroso est conservé pour sa valeur historique et documentaire — sa thèse du « criminel-né » est
aujourd'hui scientifiquement réfutée (voir la fiche *Psychologie légale* pour le contexte critique).

## 🖼 Illustrations

Toutes les illustrations proviennent de **[Wikimedia Commons](https://commons.wikimedia.org/)** (domaine public) :
schémas du cerveau, 17 portraits de figures historiques (Freud, Jung, Piaget, Skinner, Pavlov, Binet, Le Bon,
Ribot, Janet, Durkheim, Charcot, Lombroso, Darwin, Wundt, Rogers, James, Lorenz), planche de Rorschach, pyramide de
Maslow, neurone.

## ⚠️ Livres commerciaux (photos)

Les ouvrages **Short Cuts Psychologie** et **Petit Larousse Psychologie** (photos) ne sont **pas** disponibles
gratuitement en intégralité pour des raisons de droit d'auteur. Voir dossiers `01-` et `02-` pour l'accès légal
(extraits, librairies partenaires, emprunt en bibliothèque).

## 🎮 Comment utiliser Psyclopédia

1. Choisis une **catégorie** qui t'intéresse (ou suis l'ordre suggéré)
2. Lis la fiche illustrée et ses objectifs d'apprentissage
3. Ouvre le **livre complet** associé si tu veux aller plus loin
4. Teste-toi avec les **flashcards** (rappel actif, sans regarder la réponse d'abord)
5. Passe le **quiz noté** de la catégorie — ton meilleur score est sauvegardé
6. Reviens dans quelques jours pour réviser (répétition espacée) — voir la page
   [Apprendre efficacement](07-ebook-final/apprendre.html)

---

*Dossier mis à jour le 18 septembre 2026 — Usage éducatif, contenu pédagogique original + œuvres du domaine public.*
