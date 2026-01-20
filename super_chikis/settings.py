import os
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# --- CONFIGURACIÓN DE SEGURIDAD ---
SECRET_KEY = 'django-insecure-r9_-!$%_t6#v_6i6e#i#^v#2g+dr2ve6k3y86txqdoxex_=*ue'

# Cambiar a False en producción (Railway/VPS)
DEBUG = True 

# Permitir dominios de Railway y localhost
ALLOWED_HOSTS = ['*', '.railway.app', 'localhost', '127.0.0.1']

# --- DEFINICIÓN DE APLICACIONES ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lista', # Tu aplicación de la lista del súper
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'super_chikis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'super_chikis.wsgi.application'

# --- BASE DE DATOS (PERSISTENCIA) ---
# Si Railway detecta un volumen montado, usamos esa ruta para no perder datos
RAILWAY_VOLUME = os.getenv('RAILWAY_VOLUME_MOUNT_PATH')

if RAILWAY_VOLUME:
    DB_PATH = os.path.join(RAILWAY_VOLUME, 'db.sqlite3')
else:
    DB_PATH = BASE_DIR / 'db.sqlite3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_PATH,
    }
}

# --- VALIDACIÓN DE CONTRASEÑAS ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- LOCALIZACIÓN (COSTA RICA) ---
LANGUAGE_CODE = 'es-cr'
TIME_ZONE = 'America/Costa_Rica' #
USE_I18N = True
USE_TZ = True

# --- ARCHIVOS ESTÁTICOS (CSS, JS) ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static', # Donde está tu admin_custom.css
]

# --- ARCHIVOS MEDIA (FOTOS DE PRODUCTOS) ---
MEDIA_URL = '/media/'

# Aseguramos que las fotos también se guarden en el volumen persistente
if RAILWAY_VOLUME:
    MEDIA_ROOT = os.path.join(RAILWAY_VOLUME, 'media')
else:
    MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    'https://web-production-9ce9c.up.railway.app'
]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('/app/data', 'media') # Si tu volumen está en /app/data
# Crea la carpeta si no existe (truco de ingeniería para evitar el Error 500)
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)