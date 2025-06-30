from pathlib import Path
import os

# ====== المسار الأساسي ======
BASE_DIR = Path(__file__).resolve().parent.parent

# ====== الأمان ======
SECRET_KEY = 'django-insecure-استبدل_هذا_المفتاح_في_الإنتاج'
DEBUG = True
ALLOWED_HOSTS = []

# ====== التطبيقات ======
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'complexes',
    'units',
    'residents',
    'payments',
    'maintenance',
    'office',
]

# ====== الوسطاء ======
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ====== إعدادات URL ======
ROOT_URLCONF = 'abd95.urls'

# ====== إعدادات القوالب ======
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← مجلد القوالب الرئيسي
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

# ====== إعدادات WSGI ======
WSGI_APPLICATION = 'abd95.wsgi.application'

# ====== قاعدة البيانات ======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ====== اللغة والتوقيت ======
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ====== الملفات الثابتة ======
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'abd95' / 'static',
]

# ====== ملفات الوسائط ======
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ====== النظام الافتراضي للمفاتيح الأساسية ======
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
