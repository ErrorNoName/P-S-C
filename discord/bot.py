#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bot Discord Psyclopédia — rôles d'accueil, slash commands, embeds.

Dépendance : discord.py >= 2.3 (voir requirements.txt).

    python3 -m pip install -r discord/requirements.txt
    DISCORD_BOT_TOKEN=… python3 discord/bot.py

Intents à activer sur le portail développeur :
  • Server Members Intent (attribution de 🌱 Nouveau)
  • Message Content Intent n'est pas requis

Le jeton ne doit jamais être commité. Le serveur reste lisible sans le bot :
les embeds d'orientation sont déjà postés par deploy_server.py.
"""

from __future__ import annotations

import json
import logging
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from blueprint import LINKS, ROLES, SITE
from deploy_server import load_guild_id, load_token
from embeds import COMMAND_EMBEDS, mentionize

try:
    import discord
    from discord import app_commands
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "discord.py est requis pour le bot long-courrier.\n"
        "  python3 -m pip install -r discord/requirements.txt"
    ) from exc


STATE_PATH = HERE / "deploy_state.json"
READY_PATH = Path(os.environ.get("PSYC_BOT_READY", "/tmp/psyc-bot.ready"))
LOG = logging.getLogger("psyclopedia")
INTEREST_KEYS = [r["key"] for r in ROLES if r.get("interest")]
LEVEL_KEYS = ["nouveau", "apprenant", "licence", "master"]


def _load_state():
    if not STATE_PATH.is_file():
        return {}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def _ids():
    return (_load_state().get("channels") or {})


def _role_id(guild, key):
    state = _load_state()
    stored = (state.get("roles") or {}).get(key)
    if stored:
        role = guild.get_role(int(stored))
        if role:
            return role
    spec = next(r for r in ROLES if r["key"] == key)
    return discord.utils.get(guild.roles, name=spec["name"])


def _embed(name):
    return mentionize(COMMAND_EMBEDS[name], _ids())


def _discord_embed(payload):
    embed = discord.Embed(
        title=payload.get("title"),
        description=payload.get("description"),
        color=payload.get("color"),
        url=payload.get("url"),
    )
    for field in payload.get("fields") or []:
        embed.add_field(
            name=field["name"],
            value=field["value"],
            inline=field.get("inline", False),
        )
    footer = payload.get("footer") or {}
    if footer.get("text"):
        embed.set_footer(text=footer["text"])
    return embed


class RoleView(discord.ui.View):
    def __init__(self, guild):
        super().__init__(timeout=180)
        levels = [
            (key, next(r["name"] for r in ROLES if r["key"] == key))
            for key in LEVEL_KEYS
        ]
        interests = [
            (key, next(r["name"] for r in ROLES if r["key"] == key))
            for key in INTEREST_KEYS
        ]
        self.add_item(LevelSelect(levels))
        self.add_item(InterestSelect(interests))


class LevelSelect(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="Votre niveau d'études…",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(label=label, value=key)
                for key, label in options
            ],
        )

    async def callback(self, interaction: discord.Interaction):
        assert interaction.guild and interaction.user
        chosen = self.values[0]
        member = interaction.user
        to_remove = []
        to_add = None
        for key in LEVEL_KEYS:
            role = _role_id(interaction.guild, key)
            if not role or role >= interaction.guild.me.top_role:
                continue
            if key == chosen:
                to_add = role
            elif role in member.roles:
                to_remove.append(role)
        if to_remove:
            await member.remove_roles(*to_remove, reason="Psyclopédia /roles")
        if to_add and to_add not in member.roles:
            await member.add_roles(to_add, reason="Psyclopédia /roles")
        await interaction.response.send_message(
            f"Niveau enregistré : **{to_add.name if to_add else chosen}**.",
            ephemeral=True,
        )


class InterestSelect(discord.ui.Select):
    def __init__(self, options):
        super().__init__(
            placeholder="Vos champs d'intérêt (plusieurs possibles)…",
            min_values=0,
            max_values=min(6, len(options)),
            options=[
                discord.SelectOption(label=label, value=key)
                for key, label in options
            ],
        )

    async def callback(self, interaction: discord.Interaction):
        assert interaction.guild and interaction.user
        member = interaction.user
        wanted = set(self.values)
        add, remove = [], []
        for key in INTEREST_KEYS:
            role = _role_id(interaction.guild, key)
            if not role or role >= interaction.guild.me.top_role:
                continue
            has = role in member.roles
            if key in wanted and not has:
                add.append(role)
            elif key not in wanted and has:
                remove.append(role)
        if add:
            await member.add_roles(*add, reason="Psyclopédia /roles")
        if remove:
            await member.remove_roles(*remove, reason="Psyclopédia /roles")
        names = [r.name for r in add] or ["aucun nouveau"]
        await interaction.response.send_message(
            "Intérêts mis à jour : " + ", ".join(names) + ".",
            ephemeral=True,
        )


class Psyclopedia(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        guild_id = load_guild_id()
        guild = discord.Object(id=int(guild_id))
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    async def on_ready(self):
        READY_PATH.write_text(f"{int(time.time())} {self.user}\n", encoding="utf-8")
        LOG.info("Connecté %s · %s serveur(s)", self.user, len(self.guilds))
        print(f"Connecté : {self.user} · {len(self.guilds)} serveur(s)")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="les cours de 50 min · /guide",
            )
        )

    async def on_member_join(self, member: discord.Member):
        role = _role_id(member.guild, "nouveau")
        if role and role < member.guild.me.top_role:
            try:
                await member.add_roles(role, reason="Accueil automatique Psyclopédia")
            except discord.HTTPException:
                pass
        channel_id = _ids().get("bienvenue")
        if not channel_id:
            return
        channel = member.guild.get_channel(int(channel_id))
        if not isinstance(channel, discord.TextChannel):
            return
        try:
            await channel.send(
                content=f"{member.mention} — bienvenue. Lisez les règles, puis le guide.",
                embed=_discord_embed(_embed("guide")),
                allowed_mentions=discord.AllowedMentions(users=True, roles=False),
            )
        except discord.HTTPException:
            pass


client = Psyclopedia()


def _slash(name):
    async def _inner(interaction: discord.Interaction):
        await interaction.response.send_message(
            embed=_discord_embed(_embed(name)),
            ephemeral=True,
        )

    return _inner


client.tree.command(name="guide", description="Mode d'emploi du serveur")(_slash("guide"))
client.tree.command(name="regles", description="Règles communautaires")(_slash("regles"))
client.tree.command(name="planning", description="Planning des cours de 50 min")(_slash("planning"))
client.tree.command(name="site", description="Liens du site Psyclopédia")(_slash("site"))
client.tree.command(name="aide", description="Numéros d'aide et cadre")(_slash("aide"))
client.tree.command(name="cours", description="Cursus, lecteur et archives")(_slash("cours"))


@client.tree.command(name="ressource", description="Une ressource Psyclopédia ou un fonds ouvert")
async def ressource_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Ressources",
        description=(
            f"[Site]({SITE}) · [Cours]({LINKS['cours']}) · [Fiches]({LINKS['fiches']}) · "
            f"[Bibliothèque]({LINKS['bibliotheque']}) · [Aide]({LINKS['aide']})\n"
            "[Collège de France](https://www.college-de-france.fr/fr) · "
            "[Canal-U](https://www.canal-u.tv/) · [HAL](https://hal.science/) · "
            "[OpenEdition](https://www.openedition.org/) · [Gallica](https://gallica.bnf.fr/)"
        ),
        color=0x50A67E,
    )
    embed.set_footer(text="Psyclopédia — Encyclopédie vivante de la psychologie")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@client.tree.command(name="roles", description="Choisir niveau et intérêts")
async def roles_cmd(interaction: discord.Interaction):
    if not interaction.guild:
        await interaction.response.send_message("À utiliser sur le serveur.", ephemeral=True)
        return
    await interaction.response.send_message(
        "Choisissez votre **niveau** et vos **champs**. Les rôles 🏛️ et 🛡️ restent manuels.",
        view=RoleView(interaction.guild),
        ephemeral=True,
    )


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    token = load_token()
    # Garde-fou : ne jamais imprimer le jeton.
    if len(token) < 50 or "." not in token:
        raise SystemExit("Jeton Discord invalide (longueur).")
    client.run(token)


if __name__ == "__main__":
    main()
