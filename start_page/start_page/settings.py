"""
Django settings for start_page project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from sys import flags

DATABASE_HOST = None
DATABASE_PASSWD = None

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tc!0p@qwkav04&9rap@o&vp%dexiz=iq%8om$6_z-^kuy-4sf='


ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'shuangchen.info'
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",  # 本地测试的接口
    "https://shuangchen.info"  # 正式接口
]


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware' ,  # 注册中间件
    'django.middleware.common.CommonMiddleware' ,
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'start_page.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': ['frontend/dist'], # 搜索前端的打包目录
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

WSGI_APPLICATION = 'start_page.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'start_page', # 数据库名 与项目名相同
        'USER': 'root',
        'PASSWORD': DATABASE_PASSWD,
        'HOST': DATABASE_HOST,
        'PORT': '3306' # 默认为3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'

# 使用nginx管理静态资源 不使用django，所有也就没必要为django指定静态资源目录
# django对静态资源的请求只适合在DEBUG模式下对应用做调试用，web请求适合交给web服务器
# 这是一种设计模式,参考：
# 　在这种方式中，我们的通常做法是，将nginx作为服务器最前端，它将接收web的所有请求，统一管理请求。
#   nginx把所有静态请求自己来处理（这是nginx的强项）。
#   然后，nginx将所有非静态请求通过uwsgi传递给django，由django来进行处理，从而完成一次web请求。

# DEBUG 模式关闭uwsgi 使用runservere即可
# 在DEBUG模式下需要解除注释
STATIC_URL = "/static/"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SESSION_COOKIE_SAMESITE = None