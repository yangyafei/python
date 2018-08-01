#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('tuple元组中的数据不能更改, 使用小括号')

tup1 = (1,2,3,4,5,6,7,8,9,0)
print('tuple', tup1)

tup1 = ()
# tuple只有一个元素的时候，需要在元素后加逗号， 否则括号会被当做运算符使用
tup1 = (1)
print(type(tup1))
tup1 = (1,)
print(type(tup1))

# tuple(a[:b]) 通过下表访问
tup1 = [1,2,3,4,5,6,7]
print('元组访问', tup1[1:5])

# + 元组连接， 元组不能修改，但可以连接生产新元组
tup1 = [1,2]
tup2 = [3,4]
print('+ 连接元组', tup1+tup2)

# del tuple删除元组, 元组不能修改，只能全部删除
print('del tuple 删除元组')

print('Len 计算元素个数')
print('max 取最大值')
print('in 判断是否在元组中')
print('*n 复制')
print('for 遍历')
print('tuple 强制转换')