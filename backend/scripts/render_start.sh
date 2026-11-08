#!/bin/sh
# Arranque del backend en Render (plan gratuito, un solo contenedor).
# Prepara la base y los archivos estaticos, levanta Celery (worker + beat) en
# segundo plano y deja gunicorn como proceso principal en el puerto de Render.
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

celery -A config worker -B -l info -c 1 &

exec gunicorn config.wsgi:application --bind "0.0.0.0:${PORT:-10000}" --workers 2
