#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/8/1
    author:yafei9 
"""

'''
服务端
使用Socket模块的Socket函数来创建一个Socket对象，Socket对象可以通过调用其他函数来设置一个Socket服务
通过调用bind(hostname,port)函数来指定服务的端口
然后调用socket对象的accept方法，该方法等待客户端的连接，并返回connection对象，表示已连接到客户端
'''

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port ))

s.listen(5)
while True:
    c, addr = s.accept()
    print('连接地址 ', addr)
    c.sendall(b'welcome python ')
    c.close()