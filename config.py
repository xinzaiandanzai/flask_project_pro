# 日志模块
import logging
# redis 数据库模块
from redis import StrictRedis


class Config(object):
    "项目的配置"
    # 下行代码是用来防止csrf侵入
    # jhl;

    CSRF_ENABLED = True
    SECRET_KEY = 'iECgbYWReMNxkRprrzMo5KAQYnb2UeZ3bwvReTSt+VSESW0OB8zbglT+6rEcDW9X'
    #   mysql数据库进行配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/information27'
    # TODO 是否跟踪修改显示数据库修改是否提示
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #     redis数据库的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # 此行设置session的保存选择设置
    SESSION_USE_SINGER = 'redis'
    # TODO 开启session签名
    SESSION_USE_SIGNER = True
    #    指定session的具体redis保存
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    #     设置是否过期
    SESSION_PERMANENT = False
    # 设置过期时间  86400是1天此处设置过期时间是两天
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    #   设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """继承config  开发环境的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESTING = True


# 下方设置一个字典用来在manage文件中选择配置环境
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
