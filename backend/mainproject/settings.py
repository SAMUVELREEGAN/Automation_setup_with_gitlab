import os
from pathlib import Path

# -----------------------------
# Base Directory
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent  # backend/mainproject

# -----------------------------
# Secret & Debug
# -----------------------------
SECRET_KEY = 'django-insecure-msfx49se3=!x@te)melvq_d5xq@(-+#10%i%)s=(oep6@(7y56'
DEBUG = True
ALLOWED_HOSTS = []

# -----------------------------
# Installed Apps
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# URL config
# -----------------------------
ROOT_URLCONF = 'mainproject.urls'

# -----------------------------
# Templates (React build)
# -----------------------------
FRONTEND_BUILD_DIR = os.path.join(BASE_DIR.parent, 'frontend', 'build')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONTEND_BUILD_DIR],
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

# -----------------------------
# WSGI
# -----------------------------
WSGI_APPLICATION = 'mainproject.wsgi.application'

# -----------------------------
# Database
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------
# Password Validators
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# Localization
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# Static files
# -----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(FRONTEND_BUILD_DIR, 'static'),  # React static files
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# -----------------------------
# Default auto field
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------
# Debug check (optional)
# -----------------------------
print("React build folder:", FRONTEND_BUILD_DIR)
print("index.html exists:", os.path.exists(os.path.join(FRONTEND_BUILD_DIR, 'index.html')))
