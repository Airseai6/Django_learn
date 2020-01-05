# -*- coding:utf-8 -*-
# @CreateTime : 2020/1/5 21:43
# @Author     : Qi

import pymysql


def get_list(sql, args):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='s4db65',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result


def get_one(sql, args):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='s4db65',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result


def modify(sql, args):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='',
        db='s4db65',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()