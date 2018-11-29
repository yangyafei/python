#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/11/29
    author:yafei9
"""

import threading

print('''
Timer定时器，是Thread的派生类，用于在指定时间后调用一个方法
    构造方法Timer(interval, function, args=[], kwargs={})
    interval： 指定的时间

    Timer从Thread派生，没有增加实例方法
''')

def func():
    print('hello timer')

timer = threading.Timer(5, func)
timer.start()
