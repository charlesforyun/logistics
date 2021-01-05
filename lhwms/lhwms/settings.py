import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$4s@qycfn*c%-wf7q-(mz3kpx$b=uef=n2$51d&kzjq^jmvv*t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # 允许所有主机访问，可以设置指定ip，防止黑客攻击


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 

    'user',         # 用户管理
    'master',       # 主数据管理
    'log',          # 日志管理

    'incoming', 	# 入库管理
    'outgoing',     # 出库管理
    'drop',         # 废旧管理
    'transport',    # 调拨管理
    'inventory', 	# 库存管理
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware', 
    # 'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 

    # 'user.middleware.MoudleMiddleware', # 登陆和模块权限中间件
    # 'user.middleware.SyslogMiddleware', # 系统管理日志中间件
    'user.middleware.TestlogMiddleware',  # 测试用登录中间件
]

ROOT_URLCONF = 'lhwms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [], 
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

WSGI_APPLICATION = 'lhwms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'lhwmsdb',
        'USER': 'root', 
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'
USE_I18N = True
USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'STATICFILES'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 获取前端文件上传默认路径
MEDIA_URL = '/media/'   # 访问路径
TEMP_DIR = os.path.join(BASE_DIR, 'temp')

# session和redis缓存设置
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 60 * 30
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache', 
        'LOCATION': 'redis://127.0.0.1:6379/1', 
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient', 
        }
    }
}

# operator调用redis连接信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

PASSWORD_FIRST = '670b14728ad9902aecba32e22fa4f6bd'  # 000000

PROJECT_NAME = '应急物资流动储备管理系统'
COPYRIGHT = 'Copyright © 2020 Synergy Logistics Technology'