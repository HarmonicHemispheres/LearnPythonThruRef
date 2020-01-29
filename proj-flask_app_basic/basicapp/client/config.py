
class Config(object):
    DEBUG = False
    TESTING = False
    SERVER_NAME = '127.0.0.1:6060'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    # CACHE_TYPE = "null"


class TestingConfig(Config):
    TESTING = True
