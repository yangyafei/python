#!/usr/bin/env python 
# -*- coding:utf-8 -*-


var = 'hello python'
print('var: ', var)
print('var[0]:', var[0])
print('var[1,3]', var[1:3])
print('修改var: ', var[0:5] + ' world')

# \在行尾时，可以表示续行符
# \\反斜杠
# \e转义
# \oyy 八进制数 yy表示字符
# \xyy 十六进制数 yy表示字符
# \other 其他字符以普通格式输出

# + 字符串连接
print('+字符串连接', 'hello' + 'yyfer')

# * 重复输出
print('*重复输出')

# [] 通过索引获取字符串中字符
print('[]索引检索字符: ', var[1])

# [:] 截取字符一部分
print('[:]截取字符: ', var[0:6])

# in 判断字符串中是否有给定字符
print('in判断字符串是否有给定字符: ', 'a' in 'bac')

# not in 判断字符串中没有给定字符
print('not in判断字符串么偶有给定字符: ', 'e' not in 'bca')

# r/R 原始字符串，所以字符都按照给定字符使用
print('r/R 原始字符串: ', r'\n')

# % 格式化字符
# %c 字符
# %d 整数
# %s 字符串
# %u 无符号整数
# %o 八进制
# %x 十六进制
# %X 十六进制，大写
# %f 浮点数 可指定小数点后尾数
# %e 科学计数法
# %E 同%e
# %g %f和%e的简写
# %G %f和%E的简写
# %p 十六进制格式化变量的地址
# * DIN定义宽度或者小数点精度
# - 左对齐
# + 在正数前面显示+号
# <sp> 在正数前显示空格
# # 在八进制显示零'0' 在十六进制前面显示'0x'或'0X'
# 0 显示的数字前面填充0
# % %%输出一个单一的%
# (var) 映射变量(字典参数)
# m,n m是显示的最小宽度 n是小数点后位数

# '''三引号允许字符串多行

# 在python中所以字符都是unicode

# capitalize 将字符串的第一个字符转换成大写
print('capitalize 将字符串首字符改成大写: ', 'hello'.capitalize())

# center(width, fillchar) 返回一个指定的宽度width居中的字符串 fillchar是字符不是字符串
print('center 扩充字符串: ', 'hello'.center(12,'-'))

# count(str, beg=0, end=len(str)) 返回str出现的次数
print('count返回str出现的次数: ', 'ahaadhaanaaahdddaazaa'.count('aaa'))

# bytes.decode(encoding=utf-8, errors='strict') 解码 默认utf-8
str = 'hello'.encode()
print('bytes.decode解码: ', str.decode())

# encode(encoding=utf8) 编码
print('encode编码: ', 'hello'.encode())

# endswith(suffix, beg=0, end=len(string)) 判断是否以suffix结尾
print('endswith 判断是否以某字符串结尾: ', 'hello world'.endswith('ld'))

# expandtabs(tabsize=8) 把字符串的tab转换为空格，默认是8个
print('expandtabs tab转空格:', 'hello\tworld'.expandtabs())

# find(str,[beg],[end]) 查找str出现的索引位置 否则返回-1
print('find查找子串的索引位置: ', 'hello world'.find('world'))

# index(str,[beg],[end]) 同find, 但没找到的话报异常
print('index查找子串位置，同find ', 'hello world'.index('world'))

# isalnum判断字符串至少一个且所有字符都是字母或数字则返回true
print('isalnum 判断字符串是不是由字母和数字组成', 'hello2018'.isalnum())

# isalpha 判断字符串都是字母
print('isalpha 判断字符串是不是都是字母','hello'.isalpha())

# isdigit() 判断都是数字
print('isdigit 判断都是数字', '2018'.isdigit())

# islower() 判断字母都是小写
print('islower判断字母都是小写', 'hello 2018'.islower())

# isnumeric() 判断字符串只有数字
print('isnumeric 判断字符串只有数字', 'hello2018'.isnumeric())

# isspace() 判断只包含空白
print('isspace判断只包含空白','  '.isspace())

# istitle() 判断是否标题化(所有字母首字母大写)
print('istitle判断是否标题化', 'Title'.istitle())

# isupper() 判断字母都是大写
print('isupper 判断字母都是大写', 'HELLO2018'.isupper())

# join(seq) 将序列以字符串分割进行拼接新的字符串, 序列元素需要都是字符串
print('join将序列拼接成字符串', '-'.join(['a','b']))

# len(strgin) 求字符串长度
print('len取字符串长度:', len('hello'))

# ljust(width,fillchar) 左对齐填充字符
print('ljust左对齐填充字符串', 'hello'.ljust(10,'*'))

# lower将字母转换成小写
print('lower字母转小写','HeLlo'.lower())

# lstrip()截掉左侧空格或指定字符
print('lstrip截掉左侧空格或指定字符','***hello'.lstrip('*'))

# maketrans 创建字符映射表，第一个参数是字符串，第二个参数是要转换的目标
intab = 'aeiou'
outtab = '12345'
#trantab = str.maketrans(intab, outtab)
test = 'this is string example ... wow!'
#print('maketrans 字符映射表',test.translate((trantab)))

# max 取字符串中最大的字母 区分大小写
print('max 取字符串中最大的字母', max('AaZz'))

# min 取最小的字母 区分大小写
print('min 取最小的字母', min('AaZz'))

# replace(old, new, [max]) 替换
print('replace 替换', 'aabbaallaakk'.replace('aa','--',1))

# rfind(str, beg, end) 从右边开始查找
print('rfind 从右边开始查找', 'aa---aa--ddaa--kk'.rfind('aa'))

# rindex(str, beg, end) 从右边开始查找
print('rindex 从右边开始查找', 'aa--bb--'.rindex('--'))


# rjust(width, fillchar) 右对齐
print('rjust右对齐补全', 'hello'.rjust(10,'*'))

# rstrip删除末尾空格
print('rstrip删除末尾空格', 'hello   '.rsplit())

# splitlines([keepends]) 按照行(\n,\r,\r\n)分割，返回列表
print('splitlines按照行分配', 'a\nbv\rad\r\nzz'.splitlines())

# startswith(str,beg,end)判断以str开始
print('startswith判断以str开始', 'hello ___'.startswith('he'))

# strip() 删除行首位空格
print('strip 删除首位空格', '  hello  '.strip())

# swapcase大小写转换
print('swapcase 大小写转换', 'Hello World'.swapcase())

# title 标题化
print('title 标题化', 'hello world'.title())

# translate 映射表相关

# upper 转换大写
print('upper 转换大写', 'hello'.upper())

# zfill(width) 右对齐补零
print('zfill右对齐补零', 'hello'.zfill(10))

# isdecimal() 判断只包含10进制
print('isdecimal判断只包含', '0x12'.isdecimal())

print('字符串操作经常用到，还是都写写demo才熟悉的快！！！')