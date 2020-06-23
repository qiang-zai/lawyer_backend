from flask import Flask

from common.settings.default import config_dict


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
    return app
