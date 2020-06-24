import logging
from logging.handlers import RotatingFileHandler


def log_file(log_lv):
    '''记录日志信息'''
    # 设置哪些日志信息等级要被记录
    logging.basicConfig(level=log_lv)
    # 创建日志记录器,指明日志保存的路径,每个日志文件的最大大小,保存的日志文件个数
    file_log_handler = RotatingFileHandler('logs/log.txt', maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式,日志等级,输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

