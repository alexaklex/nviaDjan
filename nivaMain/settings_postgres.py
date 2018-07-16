DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'auto_bdsm',
        'USER': 'auto_blogs',
        'PASSWORD': '1awdw00DDru',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}