#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('''
一些标准库
''')

import os
print('getcwd获取目录', os.getcwd())
print('dir 读取模块信息', dir(os))
print('help 读取信息', help(os))

# glob模块提供了一个函数用于从目录通配符搜索中生成文件信息
# glob支持3种通配符：*表示0或多个字符；?表示一个字符; []指定范围内的字符如[0-9]匹配数字
import glob
print('glob.glob', glob.glob('*.py'))
print('glob.glob', glob.glob('*[0-9].py'))

# 命令行参数，在命令行执行python脚本，传递的参数在sys.argv中

