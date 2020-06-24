import logging

from flask import current_app

from common.utils.save_db_router import DBOpenExe, Queries
from lawyer import create_app

app = create_app()


@app.route('/')
def hello_world():
    # sql = """select * from user_basic where mobile=%s;"""
    # lst = ['13423682841']
    # with DBOpenExe(sql, lst) as cs:
    #     data = cs.fetchall()
    # print(data)
    sql = """select * from user_basic where mobile=%s;"""
    lst = ['13423682841']
    user = Queries.fetchone(sql, lst)
    print(user)
    # 测试日志
    logging.debug('这是日志信息debug')
    logging.error('这是日志信息error')
    # 集群测试
    # current_app.redis_cluster.set('name', 'qiangzai')
    # print(current_app.redis_cluster.get('name'))
    # 测试主从
    # current_app.redis_master.set('age', 10)
    # print(current_app.redis_master.get('age'))
    return 'hello world!'
