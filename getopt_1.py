#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/8/30
    author:yafei9 
"""

'''
getopt分析输入的参数，根据不同的参数输入不同的命令


'''
import sys
import getopt

'''
getopt.getopt( [命令行参数列表], "短选项", "长选项列表" )
getopt这个函数，就是用来抽取sys.argv获得用户输入来确定后续操作的
getopt是一个模块，而这个模块里面又有getopt函数，
函数返回2个值 opts 和 args
opts是一个存有所有选项及其输入值的元组，当输入确定后，这个值就不能更改了
'''

