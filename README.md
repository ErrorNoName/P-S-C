# 🧠 Psyclopédia

**L'encyclopédie vivante et illustrée de la psychologie, en français.**

Un Ebook interactif complet : 17 catégories, 13 livres du domaine public, quiz notés avec corrigés, fiches de
révision et méthodes d'apprentissage — hébergé et accessible directement via GitHub Pages.

## 🚀 Accéder au site

➡️ **[Ouvrir Psyclopédia](https://errornoname.github.io/P-S-C/)** — déjà en ligne, mis à jour automatiquement à chaque push sur `main`.

Ou en local : ouvre simplement [`index.html`](index.html) dans ton navigateur.

## 🔧 Déploiement GitHub Pages

GitHub Pages est déjà activé sur ce dépôt (déploiement automatique depuis `main`, racine `/`). Un workflow
GitHub Actions (`.github/workflows/pages.yml`) redéploie également le site à chaque push, en complément. Aucune
action manuelle n'est nécessaire : tout push sur `main` met le site à jour en 1 à 2 minutes.

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
