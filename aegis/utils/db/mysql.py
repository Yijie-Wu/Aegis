# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
Date: 2020/5/14 14:53
"""
import pymysql


class MysqlBaseHandler(object):
    def __init__(self, host, user, password, db):
        self.db = db
        self.host = host
        self.user = user
        self.password = password
        self.conn = pymysql.connect(self.host, self.user, self.password, self.db)

    def execute(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            print('Get DB Data failed at:', str(e))
            return False

    def query(self, sql, fetch_one=False):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            if fetch_one:
                data = cursor.fetchone()
            else:
                data = cursor.fetchall()
            return data
        except Exception as e:
            print('Get DB Data failed at:', str(e))
            return False

    def close_db(self):
        self.conn.close()
