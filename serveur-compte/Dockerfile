FROM python:3.12-slim

WORKDIR /app
COPY serveur-compte/compte_server.py /app/serveur-compte/compte_server.py
COPY serveur-compte/data/.gitkeep /app/serveur-compte/data/.gitkeep

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PSYCLOPEDIA_COMPTE_HOST=0.0.0.0
ENV PSYCLOPEDIA_COMPTE_DB=/data/compte.sqlite

EXPOSE 8787
CMD ["sh", "-c", "mkdir -p /data && python3 /app/serveur-compte/compte_server.py --host 0.0.0.0 --port ${PORT:-8787} --db ${PSYCLOPEDIA_COMPTE_DB}"]
