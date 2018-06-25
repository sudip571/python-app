
class BaseConfig(object):
    """ 
    Common configuration that are used across all environment
    """
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """
    development configuration
    """
    DEBUG=True
    TESTING = True
    # setting this to True helps us with debugging by allowing SQLAlchemy to log errors
    SQLALCHEMY_ECHO = True
    ENV = 'dev'

class ProductionConfig(BaseConfig):
    """
    Production configuration
    """
    DEBUG=False
    ENV = 'prod'

app_config = {

    'development': DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
    }

