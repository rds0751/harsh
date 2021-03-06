import os

from django.utils.translation import ugettext_lazy as _

from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR, get_core_apps


# Django settings for oscar project.
PROJECT_DIR = os.path.dirname(__file__)
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x
)

DEBUG = True

WSGI_APPLICATION = 'wsgi.application'

USE_TZ = True

ALLOWED_HOSTS = ['softsmart.herokuapp.com', '*']

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://pusikvmqntkjtl:5e3ee148fdd048cc77c1cdf14c8e419d6c06a3799056fbedf4e6a004b9300f2e@ec2-54-225-121-235.compute-1.amazonaws.com:5432/d6lkfpssp98htu',
        conn_max_age=600)}


ATOMIC_REQUESTS = True

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

gettext_noop = lambda s: s
LANGUAGES = (
    ('en-gb', gettext_noop('British English')),
    ('zh-cn', gettext_noop('Simplified Chinese')),
    ('nl', gettext_noop('Dutch')),
    ('it', gettext_noop('Italian')),
    ('pl', gettext_noop('Polish')),
    ('ru', gettext_noop('Russian')),
    ('sk', gettext_noop('Slovak')),
    ('pt-br', gettext_noop('Brazilian Portuguese')),
    ('fr', gettext_noop('French')),
    ('de', gettext_noop('German')),
    ('ko', gettext_noop('Korean')),
    ('uk', gettext_noop('Ukrainian')),
    ('es', gettext_noop('Spanish')),
    ('da', gettext_noop('Danish')),
    ('ar', gettext_noop('Arabic')),
    ('ca', gettext_noop('Catalan')),
    ('cs', gettext_noop('Czech')),
    ('el', gettext_noop('Greek')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/s/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')
MEDIA_URL = '/m/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$)a7n&o80u!6y5t-+jrd3)3!%vh&shg$wqpjpxc!ar&p#!)n1a'

MIDDLEWARE = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
)

OSCAR_SHOP_NAME = "PTE | IELTS | CELPIP"

INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('templates'),
            os.path.join(OSCAR_MAIN_TEMPLATE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    # Apps from oscar
    'rzpay',
    'compressor',
    'widget_tweaks',
    # Vendor apps
    'bootstrap4',
    'contact',
    'demo',
]

DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap-responsive.html'


TREE_TYPES = (
    ('Marketing.LevelTree', 'LevelTree'),
)

INSTALLED_APPS = INSTALLED_APPS + get_core_apps([
    'apps.shipping'])

DEFAULT_FROM_EMAIL = 'noreply@example.com'

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

LOGIN_REDIRECT_URL = '/accounts/'
APPEND_SLASH = True

# Oscar settings
OSCAR_ALLOW_ANON_CHECKOUT = True

OSCAR_SHOP_TAGLINE = 'SoftSmart'

# Add Razorpay dashboard stuff to settings
OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('Razorpay'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Razorpay transactions'),
                'url_name': 'razorpay-list',
            },
        ]
    })

OSCAR_DEFAULT_CURRENCY = "INR"

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

RAZORPAY_API_KEY = 'rzp_test_v8svbaXtB5wQc4'
RAZORPAY_API_SECRET = 'C5kTaAnwmigWuDKgSq2Z5gHI'
RAZORPAY_CURRENCY = "INR"

# Put your own sandbox settings into an integration.py modulde (that is ignored
# by git).
try:
    from integration import *  # noqa
except ImportError:
    pass
