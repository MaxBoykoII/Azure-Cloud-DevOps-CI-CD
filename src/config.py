class BaseConfig:
    TESTING = False
    SECRET_KEY = "SECRET"


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
