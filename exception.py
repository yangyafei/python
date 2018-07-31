#!/usr/bin/env python
# -*- coding:utf-8 -*-

print('''
python错误：语法错误和异常
语法错误：指出出错的一行且在错误位置加上小箭头
异常：异常类型和错误信息，错误信息的前部分显示移除发生的上下文并以调用栈的形式显示具体信息
''')

# try except 异常处理
try:
    f = open('ta.txt', 'r')
    f.close()
except :
    print('try except 异常处理')

# raise 抛出异常
try:
    f = open('ff.txt', 'r')
    f.close()
except :
    print('raise 抛出异常')
    # raise

# try except finally finally里面的语句不管如何都会执行

def temp_conver(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print('参数没有包含数字\n', Argument)
