# -*- coding:utf-8 -*-
# @CreateTime  : 2020/1/3 9:49
# @Author      : Qi

import socket
sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(5)


def f1():
    """
    deal user request and return content
    :param request:
    :return:
    """
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data


def f2():
    return b'f2'


routers = [
    ('/xxx', f1),
    ('/ooo', f2),
]


while True:
    conn, addr = sock.accept()
    data = conn.recv(8096)
    data = str(data, encoding='utf-8')
    headers, bodys = data.split('\r\n\r\n')
    temp_list = headers.split('\r\n')
    nethod, url, protocal = temp_list[0].split(' ')
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    for item in routers:
        if item[0] == url:
            func_name = item[1]
            break

    if func_name:
        response = func_name()
    else:
        response = b'404'
    conn.send(response)
    conn.close()
