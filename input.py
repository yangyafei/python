#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# str() 返回一个用户易读的形式
# repr() 返回一个解释器易读的形式

s = 'hello world'
print('str ', str(s)) # 'hello world'
print('repr ', str(s)) # "'hello world'"
print(repr('hello world\n')) # repr 可以转义字符串中的特殊字符
print(repr((1,3))) # repr 参数可以是python的任何对象

# str.format 括号里面的字符会被替换掉
print('{}网站: {}! '.format('python', 'baidu.com'))
print('{name}网站: {site}!'.format(site='badu.com', name='python'))
print('站点列表 {0}, {1}, 和 {other}'.format('baidu','google',other='sina'))

# ‘!a’(使用ascii()) '!s'(使用str())和'!r'(使用repr())可以用于格式化某个值之前对其进行转化
import math
print('常量PI的值近似为: {}'.format(math.pi))
print('常量PI的值近似为: {!r}'.format(math.pi))

# 可选项':'和格式标示符可以跟着字段名 这就允许对值进行更好的格式化
import math
print('常量pi的值近似为 {0:.3f}'.format(math.pi))

# 在:后面传入整数，可以保证该域的宽度，可以美化输出
table = {'google':1, 'baidu':2, 'sina':3}
for name,number in table.items():
    print('(0:10)  ==>  {1:10d}'.format(name, number))

# 如果有一个很长的格式化字符串又不想分开，那么在格式化时通过变量名比位置更好
table = {'google':1, 'baidu':2, 'sina':3}
print('google: {0[google]:d}; baidu: {0[baidu]:d}; sina: {0[sina]:d}'.format(table))
# 通过**也可以实现
print('google: {google:d}; baidu: {baidu:d}; sina: {sina:d}'.format(**table))

# input可以从标准输入读入一行文本，默认的标准输入是键盘
# str = input('请输入: ')
# print('你的输入是： ', str)

