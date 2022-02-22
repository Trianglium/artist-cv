"""
Django settings for cv project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import logging
import configurations
from configurations import values
import dj_database_url



# https://django-configurations.readthedocs.io/en/stable/
# https://12factor.net/config

class Dev(configurations.Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Django settings module for wsgi and googledrivestorage
    DJANGO_SETTINGS_MODULE = 'cv.settings'


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-@lo4umkwl5_w35h^j@&ojqie-oc1zrrvcw3&1!ii3x#jazw$=('

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['LDixon.pythonanywhere.com']

    # Admin Settings
    ADMINS = [("Luke Dixon", "L.DegenDixon@gmail.com")]


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.humanize',
        # Extensions
        'crispy_forms',
        'crispy_bootstrap5',
        'django_extensions',
        'taggit',
        'ckeditor',
        'ckeditor_uploader',
        # Custom User Auth app
        'cvuser_auth.apps.CvuserAuthConfig',
        # Project apps
        'projects.apps.ProjectsConfig',
        'blog.apps.BlogConfig',
        'about.apps.AboutConfig',
        'resume.apps.ResumeConfig',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]


    ROOT_URLCONF = 'cv.urls'

    TEMPLATE_BASE_DIR = os.path.dirname(__file__)
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(TEMPLATE_BASE_DIR, 'templates'),],
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

    WSGI_APPLICATION = 'cv.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/4.0/ref/settings/#databases

    DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")


    # Password Hashing
    # https://docs.djangoproject.com/en/4.0/topics/auth/passwords/#using-argon2-with-django
    PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

    # Custom User Auth

    AUTH_USER_MODEL = "cvuser_auth.User"

    # Password validation
    # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/4.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value("UTC")

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.0/howto/static-files/

    STATIC_URL = 'static/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # default static files settings for PythonAnywhere.
    # see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

    # Django-CKEditor
    # https://django-ckeditor.readthedocs.io/en/latest/#required-for-using-widget-with-file-upload
    CKEDITOR_UPLOAD_PATH =  os.path.join(MEDIA_ROOT, 'uploads')

    # Bootstrap 5 & Crispy forms config
    CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
    CRISPY_TEMPLATE_PACK = 'bootstrap5'

    # For Taggging (Tags have alternative names in Projects app)
    TAGGIT_CASE_INSENSITIVE = True

    # Max upload size default = 2mb
    # 5 mb = 5242880
    MAX_UPLOAD_SIZE = "5242880"



# Production settings
class Prod(Dev):
    DEBUG = False
    #SECRET_KEY = values.SecretValue()
