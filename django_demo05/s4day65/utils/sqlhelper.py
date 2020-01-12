# -*- coding:utf-8 -*-
# @CreateTime : 2020/1/12 21:51
# @Author     : Qi

import pymysql


class SqlHelper(object):
    def __init__(self):
        # todo 读取配置文件
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                            user='root', passwd='root', db='s4db65',)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def get_one(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def modify(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multiple_modify(self, sql, args):
        # 'inster into bd(id, name) values(%s, %s)', [(1, 'alex'), (2, 'eric'), ]
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def create(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()
