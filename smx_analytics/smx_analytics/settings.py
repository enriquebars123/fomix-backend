import os
import datetime
from decouple import config
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vhdiu3w+91bzm@3h731m-n36vnks3d*j3azekdor53gjmdmu%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
   config('LC3000'), #"http://localhost:3000"
   config('LC8000'), # "http://localhost:8000"
   config('LC8080'), # "http://localhost:8080"
]

TIME_ZONE = 'America/Monterrey'    # HORA REAL 17:37
#TIME_ZONE = 'America/Mexico_City'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'djcelery',
    'django_celery_beat',
    'django_celery_results',
    'django_filters',
    'rest_framework',
    'corsheaders',
    'apps_analytics.referencias',
    'apps_analytics.relacion',
    'apps_analytics.regla',
    'apps_analytics.catalogo',
    'apps_analytics.variables',
    'apps_analytics.metodo',
    'apps_analytics.contacto',
    'apps_analytics.recoveryTable',
    'apps_user.smxAnalitica_user',
    ]


AUTH_USER_MODEL = 'smxAnalitica_user.user'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'smx_analytics.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR, 'media')],
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

WSGI_APPLICATION = 'smx_analytics.wsgi.application'


# Database
VARIABLES = {
      'IS_PRODUCTION_ENV': config('IS_PRODUCTION_ENV'),
                        }

if VARIABLES['IS_PRODUCTION_ENV'] == "False":

    DATABASES = {
     'default': dj_database_url.config(default=config('DB_URL')
         ),
     'redis': dj_database_url.config(default=config('DB_URL_REDIS')
         ),
     }
    #print('IS_PRODUCTION_ENV: False')

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('POSTGRES_DB_NAME', 'db_analytics'), # noqa
            'USER': os.environ.get('POSTGRES_DB_USER', 'postgres'), # noqa
            'PASSWORD': os.environ.get('POSTGRES_DB_PASSWORD', 'galileo.1564'), # noqa
            #'HOST': os.environ.get('POSTGRES_SERVICE_HOST', '10.0.75.1'), # noqa
            #'HOST': os.environ.get('POSTGRES_SERVICE_HOST', 'localhost'), # noqa
            'HOST': os.environ.get('POSTGRES_SERVICE_HOST', '172.16.100.34'), #  --4
            #'PORT': os.environ.get('POSTGRES_SERVICE_PORT', 65432), # noqa
            'PORT': os.environ.get('POSTGRES_SERVICE_PORT', 5432), # noqa
        },
        'redis': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('REDIS_DB_NAME', 'db_analytics'), # noqa
            'USER': os.environ.get('REDIS_DB_USER', 'postgres'), # noqa
            'PASSWORD': os.environ.get('REDIS_DB_PASSWORD', 'galileo.1564'), # noqa
            #'HOST': os.environ.get('REDIS_SERVICE_HOST', '10.0.75.1'), # noqa
            'HOST': os.environ.get('REDIS_SERVICE_HOST', 'localhost'), # noqa
            'PORT': os.environ.get('REDIS_SERVICE_PORT', 6379), # noqa
        },
     }
    #print('IS_PRODUCTION_ENV: entre al else')

DATOS_CONFIG                = DATABASES['redis']
HOST_REDIS                  = DATOS_CONFIG['HOST']  # Utilizar el mismo puerto de la base de datos para leer redis
PORT_REDIS                  = DATOS_CONFIG['PORT']
CELERY_BROKER_URL           = 'redis://'+str(HOST_REDIS)+':'+str(PORT_REDIS)
CELERY_RESULT_BACKEND       = 'redis://'+str(HOST_REDIS)+':'+str(PORT_REDIS)
CELERY_ACCEPT_CONTENT       = ['application/json']
CELERY_TASK_SERIALIZER      = 'json'
CELERY_RESULT_SERIALIZER    = 'json'
CELERY_TIMEZONE             = TIME_ZONE
CELERY_SEND_TASK_SENT_EVENT = True

CELERY_IMPORTS              = ('smx_analytics.tasks',)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = '/backend/static/'

#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


#STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')
#STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
#ADMIN_MEDIA_PREFIX = '/static/admin/' 
#MEDIA_ROOT = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.dirname(os.path.dirname(__file__))
MEDIA_URL = '/media/'
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# configuracion SMTP

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # servicio de correo smtp
EMAIL_HOST_USER = 'noti.daimler@sisamex.com.mx' # id de correo electrónico
EMAIL_HOST_PASSWORD = 'Sisamex.20203' #password
EMAIL_PORT = 25
EMAIL_USE_TLS = True
