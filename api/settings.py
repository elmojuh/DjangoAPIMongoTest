import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Usar variável de ambiente para SECRET_KEY
SECRET_KEY = os.getenv('SECRET_KEY', 'sua-secret-key-aqui-dev-only')

# Melhorar DEBUG
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# Hosts mais seguros
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0').split(',')

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'animals',  # Nosso app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'api.urls'  # Agora aponta para api.urls

TEMPLATES = []

WSGI_APPLICATION = 'api.wsgi.application'  # Corrigir referência

DATABASES = {}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações MongoDB
MONGODB = {
    'HOST': os.getenv('MONGO_HOST', 'localhost'),
    'PORT': int(os.getenv('MONGO_PORT', 27017)),
    'USERNAME': os.getenv('MONGO_USER', 'root'),
    'PASSWORD': os.getenv('MONGO_PASSWORD', 'senha-forte-docker'),
    'DATABASE': os.getenv('MONGO_DB', 'animal_db'),
}

# Configuração básica de Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'animals': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}