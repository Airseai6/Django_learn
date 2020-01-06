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
