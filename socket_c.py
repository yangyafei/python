#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/8/1
    author:yafei9 
"""

'''
客户端
socket.connect(hostname,post)方法打开一个TCP链接到主机hostname和端口port的服务商,
连接后从服务端获取数据，记住，操作完成后需要关闭链接
'''

import socket
s = socket.socket()

host = socket.gethostname()
port = 12345

s.connect((host, port))
print('收到服务端信息', s.recv(1024))
s.close()