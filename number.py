#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import math
import random


print('pass 空语句，作为占位符')
if 1 :
    pass
    print('this is pass block')

print('number存储数值')
print('数据类型不允许改变，若改变Number数据类型的值意味着将重新分配内存空间')
print('del 可以删除一些Number对象引用')
b = 1
c = 2
print(b)
print(c)
del b,c

print('python数值类型 整型 浮点型 复数')

# int(string, [base]) 强制类型转换，base进制
# long(string, [base])
# float(string)

a = '21'
print('21用int强制转换的8进制形式:', int(a, 8))
# complex(real, [imag]) 创建一个复数
print('complex创建一个复数: ', complex(2,3))

# str(2) 将对象转换成字符串
a = 2323
print('str强制转换: ', str(a))

# repr 将对象转换成表达式字符串
a = ['hello', 'world']
print('repr转换成表达式字符串: ', repr(a)) #将list转换成字符串

# eval 将字符串转换成表达式字符 跟repr相反
a = "['hello', 'world']"
print('eval将字符串转换成对象:', eval(a))

# tuple 将序列s转换成元组
a = [1,2,3]
print('tuple将序列转换成元组: ', tuple(a))

# list 将序列转换成列表
a = (1,23,4)
print('list将序列转换成列表: ', list(a))

# chr(x) 整型转字符
a = 65
print('chr将整型转换成字符: ', chr(a))

# unichr(x) 将整型转换成unicode字符 python3没有该语法
a = 65
# print('unichr整型转换成Unicode: ', unichr(a))



# / 除法运算总是返回一个浮点数
print('除法总是返回一个浮点数: ', 8/5)

# // 除法向下取整
print('//除法向下取整: ', 8//5)
# // 不一定返回整型，跟分母分子的类型有关，分子或分母为浮点型则返回为浮点型
print('//不一定返回整型: ', 8//5.0)
print('//不一定返回整型: ', 8.0//5)

# **幂运算
print('**幂运算: ', 2**3)

# 不同类型的数值混合运算时最好结果为浮点型
print('不同类型的数值混合运算时最后结果为浮点型: ', 2*3.0/2)

# _在交互模式中，最后输出的表达式结果被赋值给变量_ 且_为只读变量
price = 6
tax = 1.5
print(price * tax)
# print('交互模式中，最后输出的表达式结果被赋值给变量_: ', _)

# abs(x) 取绝对值
print('abs取绝对值: ', abs(-10))

# ceil(x) 向上取证 需要math模块
print('ceil向上取整: ', math.ceil(18.1))

# cmp(x,y) 比较大小 x<y,-1; x=y,0; x>y,1; python3已废弃，使用(x>y)-(x<y)替换

# exp(x) 求e的x次幂 需要math
print('exp求e的幂: ', math.exp(2))

# fabs(x) 取绝对值
print('fabs取绝对值: ', math.fabs(1.1))

# floor(x) 向下取整
print('floor向下取整: ', math.floor(1.6))

# log(x) 取e的指数
print('log取e的指数: ', math.log(2))

# log10(x) 取10的指数
print('log10取10的指数: ', math.log10(100))

# max(v1, v2, ...) 参数可以是序列
print('max取最大值: ', max([1,3,4,10]))

# min(v1, v2, ...) 参数可以是序列
print('min取最小值: ', min([10,3,-10]))

# modf(x) 返回小数的整数和小数部分，2部分符号和x相同
print('modf取浮点数的整数和小数: ', math.modf(2.34))

# pow(x,y) x**y的运算
print('pow 幂运算:', pow(2,3))

# round(x,[n]) 浮点数四舍伍入
print('round浮点数四舍五入: ', round(8.31264,3))

# sqrt(x) 求平方跟
print('sqrt求平方根:', math.sqrt(16))

# choice(seq) 随机从序列取元素
print('choice 随机从序列取元素: ', random.choice([1,3,4,5]))

# randrange([start], stop, [step]) step递增基数
print('randrange给定范围和递增基数取随机值 ', random.randrange(0, 100, 7))

# random() 随机生成一个实数在[0,1)
print('random 随机生成实数: ', random.random())

# seed([x]) 改变种子生成器的种子seed
#print('seed 改变种子生成器的种子seed:', random.seed())

# shuffle(seq) 序列元素随机排序
a = [13,4,1,5,131,5,66]
random.shuffle(a)
print('shuffle 序列元素随机排列: ', a)

# uniform(x,y) [x,y]范围随机生成实数
print('uniform随机生成范围内实数:', random.uniform(2,10))

# pi

print('累死啦 其他三角函数不写了!!!')