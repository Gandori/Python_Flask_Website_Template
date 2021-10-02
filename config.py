SECRET_KEY = "iwugh9w34&%jo"


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = SECRET_KEY

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = SECRET_KEY

class TestingConfig(Config):
    TESTING = True