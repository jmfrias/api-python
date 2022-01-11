class BaseConfig(object):
    DEBUG = False
    PYTHONDONTWRITEBYTECODE=1
    JSON_SORT_KEYS = False
    
class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True

class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False