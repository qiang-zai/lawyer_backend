# 默认配置文件
class DefaultConfig(object):
    '''默认配置'''
    # 秘钥配置
    SECRET_KEY = 'DKJLSFJDKKDJK'
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/db_lawyer'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发模式配置
class DevelopConfig(DefaultConfig):
    pass


# 生产模式配置
class ProductConfig(DefaultConfig):
    pass


# 入口访问字典
config_dict = {
    'development': DevelopConfig,
    'production': ProductConfig
}
