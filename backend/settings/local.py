# Example local settings file

# Leave in debug until sure this is instance running correctly
DEBUG = True
DEBUG_ALIAS = 'lcl'

LOCAL_APPS = [
    'debug_toolbar',
]


# Identify transactions in Braintree as coming from this instance
BRAINTREE_PREFIX = 'rel'

# Custom URLs for this instance
BASE_URL = 'localhost:6000'

# Nginx domains that are allowed to run the site itself
ALLOWED_HOSTS = [
    'localhost:6000',
    'localhost:9002',
    'localhost:6002',
]

# Nginx domains will be allowed to make API calls
CORS_ORIGIN_WHITELIST = [
    BASE_URL,
    'localhost:6000',
    'localhost:9002',
    'localhost:6002',
]

# Redfine the urls which will be sent to the Angular app
# FRONTEND_URL = "http://localhost:3000"
# API_URL = "http://localhost:8000"
# ADMIN_URL = "http://localhost:8001"
# CENTRAL_FRONTEND_URL = "http://localhost:3002"

# Database instance details
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eshop-db',
        # 'NAME': 'livedb-1129',
        'HOST': 'localhost',
        'USER': 'ericwang',
        # 'PASSWORD': 'd<FSpr2G?BmVp.8Z',
    }
}


SHELL_PLUS_PRE_IMPORTS = (
    ('datetime', ['date', 'datetime', 'timedelta']),
    ('random', ['random', 'randint', 'choice']),
    ('decimal', 'Decimal'),
    ('core.mixins.duration', 'to_current_server_timezone'),
    ('core.constants', '*'),
    ('django.db', 'connection'),
    ('django.forms', 'model_to_dict'),
    ('django.core.urlresolvers', 'reverse'),
    ('pprint', 'pprint'),
    ('dateutil.relativedelta', 'relativedelta'),
    'pydash',
)

LOGGERS = {
    # 'common': {
    #     'handlers': ['errorfile'],
    #     'level': 'ERROR',
    # },
    # 'common': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'quotes': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'core': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'users': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'policies': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'claims': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'policies': {
    #     'handlers': ['infofile'],
    #     'level': 'DEBUG',
    # },
    # 'renters': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'cars': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # },
    # 'payments': {
    #     'handlers': ['debugfile'],
    #     'level': 'DEBUG',
    # }
}
