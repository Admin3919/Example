
class BaseConfig(object):

    SECRET_KEY = 'DFGGFDHR'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/script?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1

    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATTONS = True

class ProductionConfig(BaseConfig):
    pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    pass