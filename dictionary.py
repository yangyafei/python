#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('''
dictionary 字典
字典是一个可变容器模型 且可存储任意类型的对象
字典元素以key:value形式，字典使用花括号{}
''')

dict = {1:3, 4:5}
print('dict:', dict)
print('访问字段的值', dict[1])

dict[1] = 111
print('修改字典:', dict)

del dict[1]
print('删除字典元素', dict)

print('''
字典的value可以是任何python对象，可以是标准对象，可以是用户定义，但是键不行
不允许出现重复的键名，如果出现，后者覆盖前者
键不可变，可以是数字，字符串，元组，不能是列表
''')

# Len 长度
dict = {1:1, 2:4, 3:6}
print('len 长度', len(dict))

# str 输出字典 以可打印的字符串表示
dict = {1:1, 2:4, 'a':'yyf'}
print('str 输出', str(dict))

# type 返回变量类型
print('type 类型', type(dict))

# dict.clear() 删除字典元素
dict.clear()
print('clear 清楚字典元素', dict)

# copy 复制
dict1 = {1:2, 3:'a'}
dict2 = dict1.copy()
print('copy 复制', dict2)

# fromkeys(seq, val) 以seq元素为键，val为值，创建新的字典
dict1 = dict.fromkeys([1,2,3],555)
print('fromkeys 创建字典', str(dict1))

# dict.get(key,[default=None]) 获取指定键的值，找不到默认None
dict1 = {'name':'yang', 'age':'26'}
print('dict.get获取指定键的值', dict1.get('name'))

# in 判断key是否在dict中

# items 返回可遍历的(键，值) 元组
dict1 = {'name':'yang', 'age':'26'}
for i,j in dict1.items():
    print('items返回可遍历的元组: ', i, '\t', j)

# keys 返回列表形式的键名
dict1 = {'name':'yang', 'age':26}
print('keys返回列表形式的键', dict1.keys())

# dict.setdefault(key, default=None) 跟get一样，如果找不到，加入键，并设置默认值，default
dict1 = {'name':'yang'}
dict1.setdefault('age',26)
print('dict.setdefault 跟get一样，没有的话添加', dict1)

# dict.update(dict2) 将字典添加到字典中
dict1 = {'name':'yang'}
dict1.update({'age':26})
print('dict.update 将字典添加到字典', dict1)

# dict.values 返回序列形式value值

# pop(key, default)删除指定键名的元素，如果没找到返回default
dict1 = {'name':'yang', 'age':26}
dict1.pop('name')
print('dict.pop 删除指定元素', dict1)

# dict.popitem() 随机返回一组元素并从字典删除, 一般是最后一个
dict1 = {'name':'yang', 'age':26, 'sex':'1'}
print('dict.popitem 随机返回并删除一组元素', dict1.popitem(), dict1)
