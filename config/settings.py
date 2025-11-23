import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# [ ... (resto de tu configuración, SECRET_KEY, etc.) ... ]

# IMPORTANTE: Permitir acceso desde cualquier lugar (necesario para Azure)
# NOTA: En producción real, esto debe ser el nombre de tu Web App:
# ALLOWED_HOSTS = ['tuappdjangounico.azurewebsites.net']
ALLOWED_HOSTS = ['*']

# [ ... (resto de INSTALLED_APPS, MIDDLEWARE, etc.) ... ]

WSGI_APPLICATION = 'config.wsgi.application'


# ----------------------------------------------------------------------
# CONFIGURACIÓN DE BASE DE DATOS (AZURE POSTGRESQL vs. LOCAL)
# ----------------------------------------------------------------------

# 1. Intenta conectarse a PostgreSQL usando variables de entorno de Azure.
#    Si las variables de Azure existen, usa la configuración de la nube.
#    Esto es automático y más seguro que usar USAR_NUBE = True/False.

DB_HOST = os.environ.get('DB_HOST')

if DB_HOST:
    # --- CONFIGURACIÓN PARA AZURE POSTGRESQL ---
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': DB_HOST, # Usamos el valor de la variable de entorno
            'PORT': os.environ.get('DB_PORT', '5432'),
            # CRÍTICO: Azure PostgreSQL requiere conexión SSL
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    }
    
    # 2. CONFIGURACIÓN DE SEGURIDAD PARA LA NUBE
    # Usar esto en Azure para que los estáticos sean manejados correctamente
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    
    # IMPORTANTE: DEBUG debe ser False en la nube para proteger la información sensible.
    DEBUG = False
    
else:
    # --- CONFIGURACIÓN LOCAL (SQLite) ---
    # Si las variables de Azure no existen (estás trabajando localmente), usa SQLite.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
    # 3. CONFIGURACIÓN DE SEGURIDAD LOCAL
    DEBUG = True


# ----------------------------------------------------------------------
# FIN CONFIGURACIÓN DE BASE DE DATOS
# ----------------------------------------------------------------------


# [ ... (resto de AUTH_PASSWORD_VALIDATORS, Internationalization, etc.) ... ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Directorio adicional para estáticos (importante para que encuentre tus imágenes localmente)
STATICFILES_DIRS = [
    BASE_DIR / "web/static",
]

# El STATIC_ROOT se define en la sección de la nube para evitar conflictos locales.

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'