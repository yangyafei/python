#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/11/27
    author:yafei9 
"""
# 装饰器

def a(func):
    print('a out start')
    def wrapper():
        print('a in start')
        func()
        print('a in end')

    print('a out end')
    return wrapper()

def b(func):
    print('b out start')
    def wrapper():
        print('b in start')
        func()
        print('b in end')

    print('b out end')
    return wrapper()
@a
@b
def test():
    print('test')

test()

# 装饰器多个 由近至远依次执行
