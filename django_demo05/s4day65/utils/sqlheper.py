# -*- coding:utf-8 -*-
# @CreateTime : 2020/1/5 21:43
# @Author     : Qi

import pymysql


def c_connect():
    global conn
    global cursor
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='s4db65',)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


def c_close():
    cursor.close()
    conn.close()


def get_list(sql, args):
    c_connect()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    c_close()

    return result


def get_one(sql, args):
    c_connect()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    c_close()

    return result


def modify(sql, args):
    c_connect()
    cursor.execute(sql, args)
    conn.commit()
    c_close()


def create(sql, args):
    c_connect()
    cursor.execute(sql, args)
    conn.commit()
    last_row_id = cursor.lastrowid
    c_close()
    
    return last_row_id


# class SqlHelper(object):
#     def __init__(self):
#         # todo 读取配置文件
#         self.connect()

#     def connect(self):
#     self.conn = pymysql.connect(host='127.0.0.1', port=3306,
#                            user='root', passwd='root', db='s4db65',)
#     self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#     def get_list(self, sql, args):
#         self.cursor.execute(sql, args)
#         result = self.cursor.fetchall()
#         return result

#     def get_one(self, sql, args):
#         self.cursor.execute(sql, args)
#         result = self.cursor.fetcone()
#         return result

#     def modify(self, sql, args):
#         self.cursor.execute(sql, args)
#         self.conn.commit()

#     def multiple_modify(self, sql, args):
#         # 'inster into bd(id, name) values(%s, %s)', [(1, 'alex'), (2, 'eric'), ]
#         self.cursor.executemany(sql, args)
#         self.conn.commit()

#     def create(self, sql, args):
#         self.cursor.execute(sql, args)
#         self.conn.commit()
#         return self.cursor.lastrowid

#     def close():
#         self.cursor.close()
#         self.conn.close()
