import logging

from flask import Flask

from common.settings.default import config_dict
from common.utils.logger import log_file


def create_app():
    '''工厂方法'''
    # 创建app对象
    app = Flask(__name__)
    # 加载配置
    config = config_dict.get(app.config.get('ENV'))
    app.config.from_object(config)
    # 加载数据库配置
    from common.models import db
    db.init_app(app)
    # 记录日志信息
    log_file(config.LOG_LV)
    # redis集群加载
    from rediscluster import RedisCluster
    app.redis_cluster = RedisCluster(startup_nodes=app.config.get('REDIS_CLUSTER'))
    # redis哨兵,主从配置
    from redis.sentinel import Sentinel
    sentinel = Sentinel(app.config.get('REDIS_SENTINELS'))
    app.redis_master = sentinel.master_for(app.config.get('REDIS_SENTINEL_SERVICES_NAME'))
    app.redis_slave = sentinel.slave_for(app.config.get('REDIS_SENTINEL_SERVICES_NAME'))
    # 注册用户蓝图到app中
    from .resources.users import user_blue
    app.register_blueprint(user_blue)
    return app
