#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('''
函数 def    
''')

def area(width, height):
    return width*height
print('函数调用', area(2, 5))

# 可更改mutable和不可更改immutable
print('''
在python中，string。tuple和numbers是不可更改的对象，list和dict等是可更改的对象

不可变类型：变量赋值a=5后再赋值a=10，这里实际是新生成一个int值对象10，再让a指向他，而5被丢弃，不是改变a的值，而是新生成
可变类型，变量赋值a=[1,2]后再赋值a[0]=5，其实是修改a的元素，a本事没有动，只是改变其中一部分

python参数传递
不可变类型：类似值传递，如整数字符串元组如fun(a)，传递a的值
可变类型：类似引用传递，如列表字典
''')

# 函数调用时传递的参数顺序可以跟函数定义的顺序不一致
def info(name, age):
    print('年龄: ', age)
    print('姓名:', name)
info(age=26,name='yang')

# 不定长参数
# 加了星号*的参数会以元组的形式导入
def info2(name, *age):
    print('name:', name)
    print('age:', age)
info2('yang',1,1,10)
# 加了2个星号**的参数会以字典的形式导入
def info3(name, **age):
    print('name:',name)
    print('age:',age)
info3('yang',a=1,b=3)


# 匿名函数 lambda
sum = lambda arg1, arg2: arg1 + arg2
print('lambda匿名函数:', sum(1,3))

# global 修改全局变量
num = 1
def info4():
    global num;
    print('global 修改全局变量num:', num)
    num = 123
    print('global 修改全局变量num:', num)
info4()
print('global 修改全局变量num ', num)

# nonlocal嵌套作用域使用变量
def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print('nonlocal嵌套作用域使用变量num', num)
    inner()
    print('nonlocal嵌套作用域使用变量num:', num)
outer()

# dir 找到模块内定义的所以名称
import sys
print('dir函数 ', dir(sys))
