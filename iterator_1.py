#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import sys
print('''
iterator 迭代器 是访问集合元素的一种方式
迭代器是一个可以记住遍历的位置的对象
迭代器从第一个元素开始访问，直到所有的被访问结束，只能向后不能向前
基本方法 iter() next()
字符串 列表 元组对象都可以用于迭代器
''')

list1 = [1,2,3,4]
it = iter(list1) # 创建迭代器
print('迭代器遍历', next(it))
print('迭代器遍历', next(it))

# 迭代器跟for结合;
list1 = [1, 2, 3]
it = iter(list1)
for i in it:
    print('迭代器和for结合', i)

list1 = [1,3,4]
it = iter(list1)
while True:
    try:
        print(next(it))
    except StopIteration:
        break;

# 生成器 generator
print('''
在python中，使用了yield的函数被称为生成器
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，即生成器就是一个迭代器
在调用生成器运行的时候，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next方法时从当前位置继续运行
''')

def fibonacci(n): # 生成器 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n :
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10) # f是一个迭代器，由生成器返回
while True:
    try:
        print(next(f), end=', ')
    except StopIteration:
        break


