# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Génération du sitemap.xml et du robots.txt à la racine du dépôt."""

import os
import time

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
SITE = "https://errornoname.github.io/P-S-C"

# Les dossiers 03, 04 et 05 sont des versions antérieures conservées pour archive :
# seules leurs illustrations sont encore utilisées par le site courant.
EXCLUS = ("livres-psychologie/03-", "livres-psychologie/04-", "livres-psychologie/05-",
          "livres-psychologie/06-")


def _priorite(rel):
    if rel == "index.html":
        return "1.0", "weekly"
    if rel.endswith(("/index.html", "/plan.html", "/emploi-du-temps.html")):
        return "0.9", "weekly"
    if "/cours/" in rel:
        return "0.8", "weekly"
    if "/categories/" in rel or "/references/" in rel:
        return "0.8", "monthly"
    if "/fiches/" in rel or "/laboratoire/" in rel:
        return "0.6", "monthly"
    return "0.7", "monthly"


def _pages():
    pages = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", ".github", "__pycache__")]
        for name in filenames:
            if not name.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, "/")
            if rel.startswith(EXCLUS):
                continue
            pages.append(rel)
    return sorted(pages, key=lambda r: (r != "index.html", r))


def render_sitemap():
    today = time.strftime("%Y-%m-%d")
    pages = _pages()
    urls = "\n".join(
        f"  <url>\n    <loc>{SITE}/{rel}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        for rel, (prio, freq) in ((p, _priorite(p)) for p in pages)
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{urls}\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

    robots = ("User-agent: *\n"
              "Allow: /\n"
              "Disallow: /livres-psychologie/03-ressources-gratuites-legales/\n"
              "Disallow: /livres-psychologie/04-guide-enrichi-illustre/\n"
              "Disallow: /livres-psychologie/05-larousse-illustre-complet/categories/\n"
              "Disallow: /livres-psychologie/05-larousse-illustre-complet/jeux/\n"
              f"\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    return len(pages)
