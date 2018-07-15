DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'auto_bd',
        'USER': 'auto_blog',
        'PASSWORD': '1awdw00DDru84#2',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}