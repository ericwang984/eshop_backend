from base import *
import sys
from datetime import timedelta

ROOT_URLCONF = 'urls.api'

APP_NAME = 'API'

MIDDLEWARE_CLASSES += [
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'users.auth.QuerystringJSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
       'rest_framework.permissions.AllowAny',
    ),
    # 'EXCEPTION_HANDLER': 'common.server_errors.graceful_exception_handler',
}

if not DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(minutes=JWT_AUTHENTICATION['TIMEOUT_MINUTES']),
    'JWT_ALLOW_REFRESH': True,
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.auth.jwt_response_payload_handler',
}

CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST + [
]


# In test mode, disable database migrations
TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

if TESTING:
    print("===================================")
    print("In TEST Mode - Disabling Migrations")
    print("===================================")

    class DisableMigrations(object):

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return "notmigrations"

    MIGRATION_MODULES = DisableMigrations()
