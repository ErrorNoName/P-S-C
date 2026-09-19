#!/usr/bin/env bash
# Relance le bot Discord tant qu'il s'arrête. Aucun jeton dans ce fichier.
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="${PSYC_BOT_LOG:-$DIR/bot.log}"
PIDFILE="${PSYC_BOT_PID:-/tmp/psyc-bot.pid}"
READY="${PSYC_BOT_READY:-/tmp/psyc-bot.ready}"
export PYTHONUNBUFFERED=1
export PYTHONPATH="$DIR${PYTHONPATH:+:$PYTHONPATH}"

load_token() {
  if [[ -n "${DISCORD_BOT_TOKEN:-}" ]]; then
    return 0
  fi
  if [[ -f /tmp/.psyc_discord_token ]]; then
    DISCORD_BOT_TOKEN="$(tr -d '[:space:]' < /tmp/.psyc_discord_token)"
    export DISCORD_BOT_TOKEN
    return 0
  fi
  if [[ -f "$DIR/.env" ]]; then
    # shellcheck disable=SC1091
    set -a
    # Ne source que les lignes KEY=VALUE sans imprimer.
    while IFS= read -r line; do
      case "$line" in
        DISCORD_BOT_TOKEN=*|DISCORD_GUILD_ID=*) eval "$line" ;;
      esac
    done < "$DIR/.env"
    set +a
    export DISCORD_BOT_TOKEN DISCORD_GUILD_ID
    return 0
  fi
  echo "Jeton Discord introuvable (DISCORD_BOT_TOKEN ou /tmp/.psyc_discord_token)." >&2
  return 1
}

already_running() {
  if [[ -f "$PIDFILE" ]]; then
    local old
    old="$(cat "$PIDFILE" 2>/dev/null || true)"
    if [[ -n "$old" ]] && kill -0 "$old" 2>/dev/null; then
      return 0
    fi
  fi
  return 1
}

loop() {
  load_token || exit 1
  cd "$DIR" || exit 1
  echo $$ > "$PIDFILE"
  echo "$(date -Is) superviseur démarré pid=$$" >> "$LOG"
  while true; do
    echo "$(date -Is) lancement bot.py" >> "$LOG"
    python3 "$DIR/bot.py" >> "$LOG" 2>&1
    code=$?
    echo "$(date -Is) bot arrêté code=$code — relance dans 8s" >> "$LOG"
    rm -f "$READY"
    sleep 8
  done
}

if [[ "${1:-}" == "--daemon" ]]; then
  if already_running; then
    echo "Bot déjà actif (pid $(cat "$PIDFILE"))."
    exit 0
  fi
  load_token || exit 1
  nohup "$0" >> "$LOG" 2>&1 &
  echo $! > "$PIDFILE"
  echo "Superviseur lancé en arrière-plan (pid $!)."
  exit 0
fi

loop
