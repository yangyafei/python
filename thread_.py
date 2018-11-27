#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/11/27
    author:yafei9 
"""
from threading import Thread
import time

def fun():
    cnt = 0
    for i in range(10000000):
	    cnt += 1
    return True

def test1():
    s = time.time()
    for i in range(2):
	    t = Thread( target=fun )
	    t.start()
	    t.join()
    e = time.time()
    print(e - s)

def test2():
    ret = {}
    s = time.time()
    for i in range(2):
	    t = Thread( target=fun )
	    t.start()
	    ret[i] = t

    for i in range(2):
	    ret[i].join()

    e = time.time()
    print(e - s)

test1()
test2()
