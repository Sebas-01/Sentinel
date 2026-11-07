from .production import *  # noqa: F403
from .production import ALLOWED_HOSTS, DATABASES, env

# Settings para el despliegue gratuito en Render con la base en Neon.
# Hereda todo lo de produccion (DEBUG apagado, HTTPS, HSTS) y solo agrega lo
# que depende de Render: el host publico que Render asigna al servicio y los
# origenes de confianza para formularios (admin) servidos desde el frontend.

# Render inyecta esta variable con el dominio publico del servicio
# (p. ej. sentinel-api.onrender.com), asi no hay que escribirlo a mano.
RENDER_EXTERNAL_HOSTNAME = env('RENDER_EXTERNAL_HOSTNAME', default='')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [*ALLOWED_HOSTS, RENDER_EXTERNAL_HOSTNAME]

# El frontend (sitio estatico) reenvia /api y /admin a este backend desde otro
# dominio; Django exige declarar ese origen para aceptar el login del admin.
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])

# Neon cierra conexiones inactivas: se reutilizan pero se verifican antes de usarlas.
DATABASES['default']['CONN_MAX_AGE'] = 60
DATABASES['default']['CONN_HEALTH_CHECKS'] = True
