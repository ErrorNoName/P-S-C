# 🧠 Psyclopédia

**L'encyclopédie vivante et illustrée de la psychologie, en français.**

Un Ebook interactif complet : 17 catégories, 13 livres du domaine public, quiz notés avec corrigés, fiches de
révision et méthodes d'apprentissage — hébergé et accessible directement via GitHub Pages.

## 🚀 Accéder au site

➡️ **[Ouvrir Psyclopédia](https://errornoname.github.io/P-S-C/)** *(une fois GitHub Pages activé, voir ci-dessous)*

Ou en local : ouvre simplement [`index.html`](index.html) dans ton navigateur.

## 🔧 Activer GitHub Pages (une seule fois)

Ce dépôt contient un workflow GitHub Actions (`.github/workflows/pages.yml`) qui déploie automatiquement le site à
chaque push sur `main`. Il ne reste qu'à activer la source une fois, dans le repo GitHub :

1. **Settings** → **Pages**
2. Sous **Build and deployment**, choisir **Source : GitHub Actions**
3. Le site se déploie automatiquement au prochain push (ou déclenche manuellement l'action *Déployer Psyclopédia sur GitHub Pages*)

## 📚 Contenu

| Ressource | Lien |
|-----------|------|
| **Accueil Ebook** | [`index.html`](index.html) |
| **17 catégories** | [`livres-psychologie/07-ebook-final/index.html`](livres-psychologie/07-ebook-final/index.html) |
| **Quiz (10 thèmes, 59 questions)** | [`livres-psychologie/07-ebook-final/quiz/index.html`](livres-psychologie/07-ebook-final/quiz/index.html) |
| **Méthodes d'apprentissage** | [`livres-psychologie/07-ebook-final/apprendre.html`](livres-psychologie/07-ebook-final/apprendre.html) |
| **Bibliothèque de 13 livres complets** | [`livres-psychologie/07-ebook-final/bibliotheque.html`](livres-psychologie/07-ebook-final/bibliotheque.html) |
| **Dictionnaire A-Z (64 notions)** | [`livres-psychologie/07-ebook-final/dictionnaire.html`](livres-psychologie/07-ebook-final/dictionnaire.html) |
| **Guide détaillé du dossier** | [`livres-psychologie/README.md`](livres-psychologie/README.md) |

## ✨ Points clés

- **17 catégories** couvrant tous les grands champs de la psychologie (fondamentaux, cognitive, sociale,
  développement, personnalité, émotions, neurosciences, psychopathologie, thérapies, positive, travail, éducation,
  santé, légale, comparée…)
- **13 livres complets du domaine public** hébergés directement (Le Bon, James, Binet, Freud, Durkheim, Ribot,
  Janet, Charcot, Taine, Lombroso, Darwin…)
- **10 quiz thématiques notés sur 20**, avec corrigé complet et explication de chaque réponse
- **Flashcards de révision** (rappel actif) sur chaque catégorie
- **Progression gamifiée** sauvegardée localement (localStorage) : score de maîtrise, niveau, meilleurs quiz
- **Adapté à 4 styles d'apprentissage** (visuel, auditif, lecture/écriture, kinesthésique)
- **100 % en français**, design original inspiré d'une charte graphique moderne (Noto Serif JP + palette
  vert/or/rose/gris)

## 🗂 Structure

```
/
├── index.html                     Page d'accueil Ebook (dashboard de progression)
├── assets-ebook/                  CSS + JS partagés du design system
├── .github/workflows/pages.yml    Déploiement automatique GitHub Pages
└── livres-psychologie/
    ├── 07-ebook-final/            ★ EBOOK PRINCIPAL ★ (catégories, quiz, apprendre, bibliothèque)
    ├── 06-pdf-domaine-public/     13 livres complets, classés par thème
    ├── 05-larousse-illustre-complet/  Version précédente (Larousse illustré, conservée)
    ├── 04-guide-enrichi-illustre/     Guide original 10 chapitres (conservé)
    ├── 01-.. / 02-.. / 03-..      Fiches sur les ouvrages commerciaux + ressources initiales
    └── README.md                 Guide complet du dossier
```

Toutes les sources des livres du domaine public (Gallica BnF, Internet Archive, Project Gutenberg, Classiques UQAM,
Darwin Online) sont créditées dans la [bibliothèque](livres-psychologie/07-ebook-final/bibliotheque.html). Les
illustrations proviennent de Wikimedia Commons. Les fiches pédagogiques, quiz et flashcards sont des contenus
originaux rédigés pour ce projet.
