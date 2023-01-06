from config.settings.base import *

DEBUG = True

# if DEBUG:
#     ALLOWED_HOSTS = ['*']
#     THIRD_PARTY_MIDDLEWARE += [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',  # django debug toolbar middleware
#     ]
# else:
#     ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ASSETS_MEDIA_DIR, 'db.sqlite3'),
    }
}