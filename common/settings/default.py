# 默认配置文件
import logging


class DefaultConfig(object):
    '''默认配置'''
    # 秘钥配置
    SECRET_KEY = 'DKJLSFJDKKDJK'
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3307/db_lawyer'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 数据库主从配置
    SLAVE_HOST = '127.0.0.1'
    SLAVE_PORT = 3308
    SLAVE_USER = 'root'
    SLAVE_PASSWORD = 'mysql'
    SLAVE_DATABASE = 'db_lawyer'
    SLAVE_CHARSET = 'utf8'
    # 默认日志级别
    LOG_LV = logging.DEBUG
    # redis集群
    REDIS_CLUSTER = [
        {'host': '127.0.0.1', 'port': '7000'},
        {'host': '127.0.0.1', 'port': '7001'},
        {'host': '127.0.0.1', 'port': '7002'},
    ]
    # redis主从
    REDIS_SENTINELS = [
        ('127.0.0.1', '16380'),
        ('127.0.0.1', '16381'),
        ('127.0.0.1', '16382'),
    ]
    REDIS_SENTINEL_SERVICES_NAME = 'mymaster'


# 开发模式配置
class DevelopConfig(DefaultConfig):
    pass


# 生产模式配置
class ProductConfig(DefaultConfig):
    # 生产模式日志级别
    LOG_LV = logging.ERROR


# 入口访问字典
config_dict = {
    'development': DevelopConfig,
    'production': ProductConfig
}
