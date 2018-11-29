#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/11/29
    author:yafei9
    local是一个小写字母开头的类，用于管理thread-local(线程局部的)数据，对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换
    可以把local看成一个"线程-属性字典"的字典，local封装了从自身使用线程作为key检索对应的属性字典，再使用属性名作为key检索属性值的细节
"""
import threading
import time

local = threading.local()
local.name = 'main'

def func():
    local.name = 'not main'
    print(local.name)

t1 = threading.Thread(target=func)
t1.start()
t1.join()

print(local.name)