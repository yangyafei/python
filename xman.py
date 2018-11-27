#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/11/23
    author:yafei9 
"""
class Decorator(object):
    def __init__(self, f):
        self.f = f
    def __call__(self):
        print("decorator start")
        self.f()
        print("decorator end")

@Decorator
def func():
    print("func")

func()

