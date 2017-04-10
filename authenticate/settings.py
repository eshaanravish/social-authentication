import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^i_4lrb=*b%kpwi#w+k*m+k$@iv8^$#6ohnfnt_4i9f(93cu9@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Google API details

GOOGLE_CLIENT_ID = '459600573348-f8ng5ifjugc14t8afnhhcphjml8nckir.apps.googleusercontent.com'

GOOGLE_CLIENT_SECRET = 'NbxNp6yZtN1QiBY-vUQ9zMot'

API_KEY = 'AIzaSyDnsRUXtIvbvp4zCkzj7BUbA3xzoTIof6k'

#Facebook API Details

FACEBOOK_CLIENT_ID = '237086353424892'

FACEBOOK_CLIENT_SECRET = '71e32063afaf632812e138a2785591ac'

FACEBOOK_ACCESS_TOKEN = '237086353424892|IhanNpMQj-dlOkF_Yabj5n8iwA4'

# Instagram API Details

INSTAGRAM_CLIENT_ID = '629ffae177374707a40ec22dca4f9c0b'

INSTAGRAM_CLIENT_SECRET = 'c49b1b0fc897463aa90a6c21af7a7aa7'

# LinkedIn API Details

LINKEDIN_CLIENT_ID = '81s11folma544z'

LINKEDIN_CLIENT_SECRET = 'Y8vBMwEaYewWVsDD'

# Twitter API Details

TWITTER_AUTHORIZATION = 'rk8bKoS10u2fuF31V8lpcSmuU:FR8oWM3k9BiN6KYUIvG8NaPfPwh3JfnAhR7ro7DfiV8eDC3AEc'

TWITTER_TOKEN = 'rk8bKoS10u2fuF31V8lpcSmuU'

TWITTER_SECRET = 'FR8oWM3k9BiN6KYUIvG8NaPfPwh3JfnAhR7ro7DfiV8eDC3AEc'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social',
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

ROOT_URLCONF = 'authenticate.urls'

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


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

WSGI_APPLICATION = 'authenticate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CSRF_COOKIE_SECURE=False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/login/'
