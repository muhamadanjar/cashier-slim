from django.conf import settings

DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'siberalam',
        'USER': "postgres",
        'PASSWORD': "xcWI3128",
        'PORT': 5432
    }
}