#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Employee:
    '所以员工的基类'
    empCount = 0

    # 类的构造方法，实例化的时候调用
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print('name :', self.name, ', salary : ', self.salary)

    # self代表类的实例，self在定义类的方法时是必须有的，虽然调用时不必传入相应的参数
    # 类的方法和普通的函数只有一个特别的区别，他们必须有一个额外的一个参数名称，安装惯例它的名称是self
    #

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()  # <__main__.Test object at 0x00329F30>
t.prt()     # <class '__main__.Test'>
# self代表类的实例，代表当前对象的地址，而self.class则指向类
# self不是python关键词，可以换成其他字符串

print("其他变成语言一般用new关键字来实例化类，但python美元可以直接使用")
print("访问类的属性，需要使用点号连接")

print("hasattr(obj, name) 判断是否有属性")
print("getattr(obj, name) 获取属性的值")
print()