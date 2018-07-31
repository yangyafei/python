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
print("python中的类支持继承")
# class DerivedClassName(modname, BaseClassName)
# class DClassName(BaseName1,BaseName2) 多继承
print("在子类中可以重写父类的方法")


# __private_attrs 2个下划线开头的，声明属性私有，不可在类外部使用和访问，在类内部使用self.__private_attrs
# 类方法必须包含参数self，且为第一个参数，self表示的是类的实例，也可使用this，但按照约定用self
# __private_method 2个下划线开头的，声明该方法为私有方法，只能在类的内部调用,self.__private_method
class JustCounter:
    __secretCount = 0   # 私有变量
    publicCount = 0     # 共有变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print("私有变量 __secretCount", self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print("公有变量", counter.publicCount)
# print("私有变量", counter.__secretCount) #报错， 实例不能访问私有变量

# 类的专有方法
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __div__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

# 运算符重载
class Ver:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Ver (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Ver(self.a+other.a, self.b+other.b)
v1 = Ver(2,10)
v2 = Ver(5,-2)
print(v1+v2)

class StrVer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "这个人名字是%s 已经有%d岁了" %(self.name, self.age)
a = StrVer('yang',26)
print(a)