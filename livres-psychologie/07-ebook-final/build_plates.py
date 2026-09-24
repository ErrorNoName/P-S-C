# -*- coding: utf-8 -*-
"""PSYCLOPÉDIA — Générateur de planches géométriques, JSON des pensées, page Rappels."""

from __future__ import annotations

import html
import json
import math
import os

from content import CATEGORIES, CATEGORY_TITLE
from data_pensees import COURS_OFFSETS, PENSEES, PLATES_CATEGORIES, PLATES_STATIQUES, SLOTS
from shell import page_header, page_shell

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(BASE, "..", ".."))
SVG_DIR = os.path.join(REPO, "assets-ebook", "plates", "svg")

PAPERS = {
    "cream": {"bg": "#F3E6C8", "ink": "#1C1914", "fill": "#C9C1A8", "soft": "#E4D7B4"},
    "blue": {"bg": "#C4D3EA", "ink": "#1A3358", "fill": "#8EABC9", "soft": "#B0C4DE"},
    "red": {"bg": "#D83A48", "ink": "#F6E4C4", "fill": "#B72E3A", "soft": "#E25A64"},
    "peach": {"bg": "#E8C39A", "ink": "#241C14", "fill": "#D4A06C", "soft": "#F0D4B0"},
    "sage": {"bg": "#D8D6C4", "ink": "#243028", "fill": "#A8B09A", "soft": "#C8C8B2"},
}

W, H = 800, 500
CX, CY = 400, 235


def _write(path, text):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full) if os.path.dirname(full) else BASE, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def _pts(pairs):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in pairs)


def _polar(cx, cy, n, r_fn, turn=0.0):
    out = []
    for i in range(n + 1):
        th = turn + 2 * math.pi * i / n
        r = r_fn(th)
        out.append((cx + r * math.sin(th), cy - r * math.cos(th)))
    return out


def _grid(ink, rings=8, rays=16, rmax=165, opacity=0.28):
    parts = [f'<g stroke="{ink}" fill="none" stroke-width="0.6" opacity="{opacity}">']
    for i in range(1, rings + 1):
        r = rmax * i / rings
        dash = ' stroke-dasharray="2 3"' if i % 2 == 0 else ""
        parts.append(f'<circle cx="{CX}" cy="{CY}" r="{r:.1f}"{dash}/>')
    for i in range(rays):
        th = 2 * math.pi * i / rays
        x = CX + rmax * math.sin(th)
        y = CY - rmax * math.cos(th)
        parts.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}"/>')
    parts.append("</g>")
    return "".join(parts)


def _axes(ink):
    return (
        f'<g stroke="{ink}" fill="none" stroke-width="0.7" opacity="0.45">'
        f'<line x1="140" y1="{CY}" x2="660" y2="{CY}"/>'
        f'<line x1="{CX}" y1="55" x2="{CX}" y2="410"/>'
        f'<path d="M148,{CY - 5} L140,{CY} L148,{CY + 5}"/>'
        f'<path d="M652,{CY - 5} L660,{CY} L652,{CY + 5}"/>'
        "</g>"
    )


def fig_axis_diamond(p, seed):
    ink, fill = p["ink"], p["fill"]
    span = 210 + (seed % 7) * 4
    h = 70 + (seed % 5) * 3
    diamond = [(CX, CY - h), (CX + span, CY), (CX, CY + h), (CX - span, CY)]
    rings = "".join(
        f'<circle cx="{CX}" cy="{CY}" r="{28 + i * 22}" fill="none" stroke="{ink}" '
        f'stroke-width="0.6" opacity="0.35"/>'
        for i in range(5)
    )
    return (
        _axes(ink) + rings
        + f'<polygon points="{_pts(diamond)}" fill="{fill}" fill-opacity="0.55" stroke="{ink}" stroke-width="1.2"/>'
        + f'<circle cx="{CX}" cy="{CY}" r="4" fill="{ink}"/>'
    )


def fig_polar_cardioid(p, seed):
    ink, fill = p["ink"], p["fill"]
    a = 78 + seed % 10

    def r(th):
        return a * (1.05 + 0.95 * math.cos(th))

    pts = _polar(CX, CY + 20, 180, r, turn=math.pi)
    return (
        _grid(ink, rings=9, rays=24, rmax=175)
        + f'<polygon points="{_pts(pts)}" fill="{fill}" fill-opacity="0.2" stroke="{ink}" stroke-width="1.4"/>'
    )


def fig_polar_wheel(p, seed):
    ink, fill = p["ink"], p["fill"]
    rmax = 168
    body = _grid(ink, rings=6, rays=12, rmax=rmax, opacity=0.55)
    gap = (seed % 5) + 2
    body += (
        f'<circle cx="{CX}" cy="{CY}" r="{rmax}" fill="none" stroke="{ink}" stroke-width="1.3"/>'
        f'<circle cx="{CX}" cy="{CY}" r="8" fill="{fill}" stroke="{ink}" stroke-width="0.8"/>'
    )
    # secteur légèrement ouvert, comme une émotion sans nom
    a0 = math.radians(seed * 17)
    a1 = a0 + math.radians(28 + gap * 3)
    x0, y0 = CX + rmax * math.sin(a0), CY - rmax * math.cos(a0)
    x1, y1 = CX + rmax * math.sin(a1), CY - rmax * math.cos(a1)
    body += (
        f'<path d="M{CX},{CY} L{x0:.1f},{y0:.1f} A{rmax},{rmax} 0 0 1 {x1:.1f},{y1:.1f} Z" '
        f'fill="{fill}" fill-opacity="0.22" stroke="none"/>'
    )
    return body


def fig_nested_ovals(p, seed):
    ink, fill = p["ink"], p["fill"]
    parts = []
    for i in range(6, 0, -1):
        rx = 28 * i
        ry = 22 * i + (seed % 4)
        op = 0.08 + i * 0.07
        parts.append(
            f'<ellipse cx="{CX}" cy="{CY + 8}" rx="{rx}" ry="{ry}" fill="{fill}" '
            f'fill-opacity="{op:.2f}" stroke="{ink}" stroke-width="{0.5 + i * 0.12}"/>'
        )
    return "".join(parts)


def fig_tulip_form(p, seed):
    ink, fill = p["ink"], p["fill"]
    k = 3
    a = 118 + seed % 8

    def r(th):
        return a * (0.55 + 0.45 * abs(math.cos(k * th / 2)) ** 1.4)

    pts = _polar(CX, CY + 10, 240, r)
    mesh = _grid(ink, rings=7, rays=14, rmax=150, opacity=0.22)
    notch = (
        f'<path d="M{CX},{CY + 18} l-22,48 h44 Z" fill="{ink}" fill-opacity="0.55"/>'
    )
    return mesh + (
        f'<polygon points="{_pts(pts)}" fill="{fill}" fill-opacity="0.72" '
        f'stroke="{ink}" stroke-width="1.1"/>'
    ) + notch


def fig_stacked_vector(p, seed):
    ink, fill = p["ink"], p["fill"]
    top = fig_axis_diamond(p, seed)
    # décale le losange vers le haut en redessinant un œuf dessous
    egg = "".join(
        f'<ellipse cx="{CX}" cy="{CY + 95}" rx="{40 + i * 18}" ry="{32 + i * 16}" '
        f'fill="{fill}" fill-opacity="0.08" stroke="{ink}" stroke-width="0.7"/>'
        for i in range(5)
    )
    return (
        f'<g transform="translate(0,-70)">{top}</g>'
        + egg
        + f'<line x1="{CX}" y1="70" x2="{CX}" y2="400" stroke="{ink}" stroke-width="0.6" opacity="0.4"/>'
    )


def fig_rose_curve(p, seed):
    ink, fill = p["ink"], p["fill"]
    n = 4 + (seed % 3)
    a = 145

    def r(th):
        return a * abs(math.cos(n * th))

    pts = _polar(CX, CY, 360, r)
    return _grid(ink, rings=6, rays=n * 4, rmax=160, opacity=0.2) + (
        f'<polygon points="{_pts(pts)}" fill="{fill}" fill-opacity="0.35" '
        f'stroke="{ink}" stroke-width="1.15"/>'
    )


def fig_spiral(p, seed):
    ink, fill = p["ink"], p["fill"]
    turns = 4
    n = 280
    pts = []
    for i in range(n):
        t = turns * 2 * math.pi * i / (n - 1)
        r = 8 + t * (22 + seed % 5)
        pts.append((CX + r * math.cos(t), CY + r * math.sin(t)))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return _grid(ink, rings=5, rays=12, rmax=170, opacity=0.18) + (
        f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="1.3"/>'
        f'<circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="4" fill="{fill}" stroke="{ink}"/>'
    )


def fig_vesica(p, seed):
    ink, fill = p["ink"], p["fill"]
    off = 70 + seed % 8
    return _axes(ink) + (
        f'<circle cx="{CX - off}" cy="{CY}" r="130" fill="{fill}" fill-opacity="0.22" stroke="{ink}" stroke-width="1.1"/>'
        f'<circle cx="{CX + off}" cy="{CY}" r="130" fill="{fill}" fill-opacity="0.22" stroke="{ink}" stroke-width="1.1"/>'
        f'<circle cx="{CX}" cy="{CY}" r="3.5" fill="{ink}"/>'
    )


def fig_radiating_field(p, seed):
    ink, fill = p["ink"], p["fill"]
    rays = 18
    parts = [_grid(ink, rings=4, rays=rays, rmax=160, opacity=0.2)]
    for i in range(rays):
        th = 2 * math.pi * i / rays + seed * 0.02
        r0, r1 = 20, 155 + (i % 3) * 8
        x0, y0 = CX + r0 * math.sin(th), CY - r0 * math.cos(th)
        x1, y1 = CX + r1 * math.sin(th), CY - r1 * math.cos(th)
        parts.append(
            f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
            f'stroke="{ink}" stroke-width="{0.6 + (i % 4) * 0.25}"/>'
        )
    parts.append(f'<circle cx="{CX}" cy="{CY}" r="16" fill="{fill}" stroke="{ink}" stroke-width="1"/>')
    return "".join(parts)


FIGURES = {
    "axis_diamond": fig_axis_diamond,
    "polar_cardioid": fig_polar_cardioid,
    "polar_wheel": fig_polar_wheel,
    "nested_ovals": fig_nested_ovals,
    "tulip_form": fig_tulip_form,
    "stacked_vector": fig_stacked_vector,
    "rose_curve": fig_rose_curve,
    "spiral": fig_spiral,
    "vesica": fig_vesica,
    "radiating_field": fig_radiating_field,
}


def render_svg(figure, paper, fig_num, title, seed=0):
    if figure not in FIGURES:
        known = ", ".join(sorted(FIGURES))
        raise ValueError(f"Figure inconnue {figure!r} (attendues : {known})")
    p = PAPERS[paper]
    grain_id = f"g{seed}"
    drawing = FIGURES[figure](p, seed)
    cap = html.escape(f"Fig. {fig_num}.")
    sub = html.escape(title)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{sub}">
  <defs>
    <filter id="{grain_id}" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="{seed}" result="n"/>
      <feColorMatrix type="saturate" values="0"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.16"/>
      </feComponentTransfer>
    </filter>
  </defs>
  <rect width="{W}" height="{H}" fill="{p['bg']}"/>
  <rect width="{W}" height="{H}" filter="url(#{grain_id})" opacity="0.55"/>
  {drawing}
  <text x="{CX}" y="458" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif"
        font-size="22" fill="{p['ink']}">{cap}</text>
  <text x="28" y="484" font-family="Georgia, 'Times New Roman', serif" font-size="9"
        fill="{p['ink']}" opacity="0.45">Psyclopédia · planche {html.escape(str(fig_num))} · {sub}</text>
</svg>
"""


def plate_records():
    records = [dict(p) for p in PLATES_STATIQUES]
    for i, (cat, figure, paper, title) in enumerate(PLATES_CATEGORIES, start=1):
        fig_num = str(30 + i)
        filename = f"cat-{cat}.svg"
        rel = f"assets-ebook/plates/svg/{filename}"
        records.append({
            "id": f"cat-{cat}",
            "fig": fig_num,
            "title": title,
            "file": rel,
            "paper": paper,
            "kind": "categorie",
            "meaning": f"Planche du domaine « {CATEGORY_TITLE.get(cat, cat)} ».",
            "cats": [cat],
            "origin": "svg",
            "figure": figure,
        })
    return records


def write_svgs():
    os.makedirs(SVG_DIR, exist_ok=True)
    n = 0
    for i, (cat, figure, paper, title) in enumerate(PLATES_CATEGORIES, start=1):
        svg = render_svg(figure, paper, str(30 + i), title, seed=i * 13)
        path = os.path.join(SVG_DIR, f"cat-{cat}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        n += 1
    return n


def export_json(plates):
    payload = {
        "slots": [{"id": s, "time": t, "label": lab} for s, t, lab in SLOTS],
        "coursOffsets": [{"minutes": m, "label": lab} for m, lab in COURS_OFFSETS],
        "pensees": [
            {
                "id": pid,
                "kind": kind,
                "slot": slot,
                "text": text,
                "by": by,
                "href": href,
                "plate": plate,
                "keywords": kw,
            }
            for pid, kind, slot, text, by, href, plate, kw in PENSEES
        ],
        "plates": plates,
    }
    path = os.path.join(BASE, "pensees.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
    return path, len(payload["pensees"]), len(plates)


def _plate_card(plate, root_prefix):
    src = root_prefix + plate["file"]
    cats = " · ".join(CATEGORY_TITLE.get(c, c) for c in plate.get("cats") or [])
    origin = {
        "collection": "Collection de référence",
        "created": "Planche créée pour le site",
        "svg": "Gravure générée",
    }.get(plate.get("origin", ""), plate.get("origin", ""))
    return (
        f'<figure class="geo-plate {plate["paper"]}" data-plate-id="{plate["id"]}">'
        f'<img src="{src}" alt="{html.escape(plate["title"])}" loading="lazy">'
        f'<figcaption><span class="geo-fig">Fig. {html.escape(str(plate["fig"]))}.</span>'
        f'<strong>{html.escape(plate["title"])}</strong>'
        f'<em>{html.escape(plate["meaning"])}</em>'
        f'<small>{html.escape(origin)}{(" · " + cats) if cats else ""}</small></figcaption>'
        f"</figure>"
    )


def render_rappels_page(plates):
    n_svg = sum(1 for p in plates if p.get("origin") == "svg")
    n_created = sum(1 for p in plates if p.get("origin") == "created")
    n_col = sum(1 for p in plates if p.get("origin") == "collection")

    header = page_header(
        depth=0,
        breadcrumb=[("Accueil", "../../index.html"), ("Rappels & planches", None)],
        icon="🔔", color="or",
        title="Rappels, pensées et planches",
        subtitle=(
            "Des notifications pour les cours de 50 minutes, des citations qui font "
            "réfléchir dans la journée, et un cabinet de planches de psychologie géométrique."
        ),
        chips=[
            f"🔔 {len(PENSEES)} pensées",
            f"🎓 Rappels de cours",
            f"🖼️ {len(plates)} planches",
        ],
    )

    today_slots = "".join(
        f'<article class="pensee-slot" data-slot-card="{sid}">'
        f'<p class="section-eyebrow">{html.escape(label)} · {time}</p>'
        f'<div data-slot-body="{sid}"><p class="section-desc">La pensée de ce créneau s\'affiche ici.</p></div>'
        f"</article>"
        for sid, time, label in SLOTS
    )

    gallery = "".join(_plate_card(p, "../../") for p in plates)

    body = f"""{header}
<div class="section rappels-page" data-rappels-page>
  <div class="note-box">
    <strong>Comment ça marche.</strong> Les rappels restent dans ce navigateur.
    Ils se déclenchent tant que le site est ouvert dans un onglet. Ce n'est pas
    un soin, ni un coaching : ce sont des piques pédagogiques, et des horaires
    de cours. En détresse, ouvrez <a href="aide.html">Aide</a>.
  </div>

  <div class="rappels-settings panel" data-notify-settings>
    <div class="panel-head"><h3>Réglages des rappels</h3></div>
    <label class="rappels-check"><input type="checkbox" data-opt="thoughts" checked>
      Pensées et citations dans la journée</label>
    <label class="rappels-check"><input type="checkbox" data-opt="cours" checked>
      Me prévenir avant chaque cours (1 h, 15 min, début)</label>
    <label class="rappels-check"><input type="checkbox" data-opt="browser">
      Notifications du navigateur (un onglet du site doit rester ouvert)</label>
    <div class="rappels-quiet">
      <label>Silence de <input type="time" data-opt="quietStart" value="22:00"></label>
      <label>à <input type="time" data-opt="quietEnd" value="08:00"></label>
    </div>
    <div class="cta-row">
      <button type="button" class="btn btn-primary" data-opt-save>Enregistrer</button>
      <button type="button" class="btn btn-secondary" data-opt-test>Envoyer un exemple</button>
    </div>
    <p class="tiny-note" data-opt-status></p>
  </div>

  <div class="section-head" style="margin-top:2.2rem">
    <p class="section-eyebrow">Aujourd'hui</p>
    <h2 class="section-title" style="font-size:1.45rem">Quatre moments, une planche</h2>
  </div>
  <div class="pensee-today" data-pensee-today>{today_slots}</div>

  <div class="cours-next-card" data-cours-next>
    <p class="section-eyebrow">Prochain cours</p>
    <h3 data-cours-next-title>Calendrier en cours de lecture…</h3>
    <p class="section-desc" data-cours-next-meta></p>
    <div class="cta-row" data-cours-next-actions></div>
  </div>

  <div class="section-head" style="margin-top:2.6rem">
    <p class="section-eyebrow">Cabinet de planches</p>
    <h2 class="section-title" style="font-size:1.45rem">Psychologie géométrique</h2>
    <p class="section-desc">Gravures d'inspiration XIXe — grilles polaires, papiers teintés,
    numéros de figure. {n_col} planches de référence, {n_created} planches créées pour
    illustrer les cours, {n_svg} gravures générées, une par domaine.</p>
  </div>
  <div class="geo-gallery">{gallery}</div>
</div>
"""
    _write("rappels.html", page_shell(
        "Rappels & planches", body, depth=0, active="Rappels",
        description=(
            "Rappels de cours, pensées du jour et cabinet de planches de psychologie "
            "géométrique — citations, notifications et illustrations des séances."
        ),
    ))


def render_all():
    n_svg = write_svgs()
    plates = plate_records()
    _path, n_pensees, n_plates = export_json(plates)
    render_rappels_page(plates)
    return n_svg, n_pensees, n_plates, len(CATEGORIES)


if __name__ == "__main__":
    n_svg, n_pensees, n_plates, n_cat = render_all()
    print(f"Planches : {n_svg} SVG, {n_plates} fiches, {n_pensees} pensées, {n_cat} catégories")
