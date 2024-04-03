from pathlib import Path
import os
from decouple import config

from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['127.0.0.1',]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'accounts',
    'vendor',
    'menu',
    'marketplace',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'accounts.middleware.logging.LoggingMiddelware',
    'accounts.middleware.is_ajax_middleware.AjaxMiddleware',
]

ROOT_URLCONF = 'foodOnline_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.get_vendor',
                'marketplace.context_processors.get_cart_counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'foodOnline_main.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        }
}

AUTH_USER_MODEL='accounts.user'
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT=BASE_DIR /'static'
STATICFILES_DIRS=[
    'foodonline_main/static'
]
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR /'media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# Email Configuration

EMAIL_HOST= config('EMAIL_HOST')
EMAIL_PORT= 587#config('EMAIL_PORT', cast=int) 
EMAIL_HOST_USER= config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL="foodOnline Marketplace <prabhatidubey@outlook.com>"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
#email sample code
# import os
# import smtplib
# from email.message import EmailMessage

# #credentials
# email_user = 'prabhatidubey@outlook.com'
# email_pass = 'God@1110'
# contacts = ['vivekchauhan14@hotmail.com']
# sender = email_user
# to = contacts

# msg = EmailMessage()
# msg['Subject'] = 'Subject...............E'
# msg['From'] = sender
# msg['To'] = ', '.join(contacts)
# msg.set_content('YOUR EMAIL MESSAGE HERE')

# try:
#     with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
#         smtp.starttls()
#         smtp.login(email_user, email_pass)
#         print("after login ........................")
#         smtp.send_message(msg)
# except Exception as e:
#     print(e)



