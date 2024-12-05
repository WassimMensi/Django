from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
 
# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-votre-clé-secrète'
DEBUG = True
ALLOWED_HOSTS = []
 
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Nécessaire pour gérer les langues
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
 
ROOT_URLCONF = 'blog_projet.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
 
WSGI_APPLICATION = 'blog_projet.wsgi.application'
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbDjango',  # Nom de la base de données
        'USER': 'django_user',  # Nom de l'utilisateur
        'PASSWORD': 'password',  # Mot de passe
        'HOST': 'localhost',  # Adresse de la base de données (ou IP du serveur)
        'PORT': '5432',  # Port de PostgreSQL (par défaut 5432)
    }
}

 
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
 
LANGUAGE_CODE = 'fr-fr'
LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
    ('it', 'Italiano'),
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True
USE_L10N = True
 
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
LOGIN_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'post_list'
LOGOUT_REDIRECT_URL = 'post_list'

# Créez le dossier log s'il n'existe pas
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp': {  # Logger pour une application spécifique
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}