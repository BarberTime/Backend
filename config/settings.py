"""
Configuración de Django para el proyecto.
"""

from pathlib import Path

# Directorios base
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de seguridad
SECRET_KEY = 'django-insecure-s#7qu5(s_r0))@oozlc)(g)1kea_l=4dm-zr+1v7jmv1ofai5l'
DEBUG = True
ALLOWED_HOSTS = ['web-production-94b30.up.railway.app']

# Configuración de Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dcld4chdx',
    'API_KEY': '983364344456282',
    'API_SECRET': 'Th8gojntsJ8biyOxYqQ7SPE5ldU'
}

# Configuración de archivos estáticos
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

# Configuración CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend local
    "https://web-production-94b30.up.railway.app/",  # Dominio Railway
]
CORS_ALLOW_ALL_ORIGINS = True

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'apps.categoria',
    'apps.cita',
    'apps.horario',
    'apps.negocio',
    'apps.servicio',
    'apps.cliente',
    'apps.usuario',
    'apps.resenia', 
    'apps.rol',
    'apps.pago',
    'apps.metodos_pago',
    'apps.imagenes_negocio',
    'apps.empleados',
    'apps.ciudad',
    'apps.authLogin',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs
ROOT_URLCONF = 'config.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'tDxufPPrHTjygjuvdnlRNhaVQTlegiSN',
        'HOST': 'nozomi.proxy.rlwy.net',  
        'PORT': '50928',      
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Configuración de archivos estáticos y medios
STATIC_URL = '/static/'



# Configuración para producción
if not DEBUG:
    # Configuración de archivos estáticos
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    
    # Configuración de almacenamiento de archivos
    DEFAULT_FILE_STORAGE = 'storages.backends.minio.MinioStorage'
    STATICFILES_STORAGE = 'storages.backends.minio.MinioStaticStorage'
    
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


