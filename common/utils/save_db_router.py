from pymysql import connect
from flask import current_app


class DBOpenExe(object):
    def __init__(self, sql, lst):
        '''配置初始化信息'''
        self.conn = connect(
            host=current_app.config.get('SLAVE_HOST'),
            port=current_app.config.get('SLAVE_PORT'),
            user=current_app.config.get('SLAVE_USER'),
            password=current_app.config.get('SLAVE_PASSWORD'),
            database=current_app.config.get('SLAVE_DATABASE'),
            charset=current_app.config.get('SLAVE_CHARSET')
        )
        self.cs = self.conn.cursor()
        self.sql = sql
        self.params = lst

    def __enter__(self):
        self.cs.execute(self.sql, self.params)
        return self.cs

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cs.close()
        self.conn.close()


class Queries(object):
    @classmethod
    def fetchone(cls, sql, lst):
        with DBOpenExe(sql, lst) as cs:
            data = cs.fetchone()
            return data

    @classmethod
    def fetchall(cls, sql, lst):
        with DBOpenExe(sql, lst) as cs:
            data = cs.fetchall()
            return data
