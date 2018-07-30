#!/usr/bin/env python 
# -*- coding:utf-8 -*-


print('''
set 集合，无序无重复元素的序列
用大括号{}或set函数创建集合, 创建一个空集合必须使用set 因为{}是来创建一个空字典的
''')

# 创建集合 {} set()
set1 = {'name','hang','fei'}
print(set1)
print(set(('11','22')))

# add 添加元素
set1 = set(('yang','26'))
set1.add(11)
print('add 添加元素', set1)

# update 添加元素
set1 = set(('baidu', 'google', 'sina'))
set1.update({'tencent'},{'alibaba'})
set1.update('abc') # 单个字符作为一个元素进行添加，重复的忽略
print('update 添加元素', set1)

# remove 移除元素 如果元素不存在则报错
set1 = {'baidu', 'alibaba', 'tencent'}
set1.remove('baidu')
print('remove 移除元素', set1)

# discard 移除元素 若元素不存在不会报错
set1 = {'baidu', 'alibaba', 'tencent'}
set1.discard('sina')
print('discard 移除元素', set1)

# len 计算元素个数
print('len 计算元素个数', len(set1))

# clear清空集合
set1 = {'baidu', 'alibaba', 'tencent'}
set1.clear()
print('clear 清空元素', set1)

# in 判断元素是否存在
set1 = {'baidu', 'alibaba', 'tencent'}
print('in 判断是否存在', 'baidu' in set1)


