import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    
class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DB_CONNECTION_STRING = 'dbname=mydb user=jonathan password=jonathan host=localhost'
class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    DB_CONNECTION_STRING = 'dbname=mydb user=jonathan password=jonathan host=localhost'

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}