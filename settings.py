INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'testapp',
)

SECRET_KEY = 'ASDFjklö123456890'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}
