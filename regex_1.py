#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('''
正则 模块re
compile函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象，该对象拥有一系列方法用于正则表达式匹配和替换
re模块提供了与这些方法完全一致的函数，这些函数使用一个模式字符串作为他们的第一个参数
''')

import re

# re.match(pattern, string, flags=0)
# pattern 正则表达式
# flags 标志位，用于控制正则表达式的匹配方式 如是否区分大小写 多行匹配
# 匹配失败返回None，成功返回一个匹配的对象
# 可以使用group(num)或groups()匹配对象函数来获取匹配表达式
print('re.match ', re.match('www', 'www.baidu.com').span())
print('re.match ', re.match('com', 'www.baidu.com'))
line = 'Cats are smarter than dogs'
obj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if obj:
    print('re.match group()', obj.group())
    print('re.match group(1)', obj.group(1))
    print('re.match group(2)', obj.group(2))
    print('re.match groups()', obj.groups())
else :
    print("No Match")

# re.search(pattern, string, flags=0)
# 匹配失败返回None，成功返回一个匹配的对象
# 可以使用group(num)或groups()匹配对象函数来获取匹配表达式
print('re.match ', re.search('www', 'www.baidu.com').span())
print('re.match ', re.search('com', 'www.baidu.com'))
line = 'Cats are smarter than dogs'
obj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
if obj:
    print('re.search group()', obj.group())
    print('re.search group(1)', obj.group(1))
    print('re.search group(2)', obj.group(2))
    print('re.search groups()', obj.groups())
else :
    print("No search")

# re.match和re.search的区别
print('''
re.match只匹配字符串的开始，如果开始不符合正则表达式，则匹配失败，返回None
re.search匹配整个字符串，直到找到一个匹配的
''')


# re.sub(pattern,repl,string,count=0) 替换字符串中的匹配项
# repl替换的字符串，也可以是函数
# count替换的最大次数，0 表示所有
phone = '2004-959-559 # 这是一个电话号码'
# 删除注释
num = re.sub(r'#.*$', '', phone)
print('re.sub 替换', num)
# 移除非数字内容
num = re.sub(r'\D', '', phone)
print('re.sub 替换', num)
# repl是一个函数
def double(matched):
    value = int(matched.group('value'))
    return str(value*2)
s = 'A23G4HFD567'
print('re.sub 替换repl为函数', re.sub('(?P<value>\d+)', double, s))

# compile(pattern, [flags])
pattern = re.compile(r'\d+') # 匹配至少一个数字
m = pattern.match('one123two')
print('compile', m)
m = pattern.match('one12two',2,5) # 从'e'开始匹配
print('compile', m)
m = pattern.match('one12two',3,5) # 从'1'开始匹配
print('compile', m)
print('compile group', m.group(0))
print('compile start', m.start(0))
print('compile end', m.end(0))
print('compile span', m.span())
# group([group1, ...]) 方法用于获取一个或多个分组匹配的字符串，当要获得整个字符串的时候，可直接使用group()或group(0)
# start(group) 方法是获取分组匹配的子串在整个字符串的起始位置，参数默认值是0
# end(group) 方法是获取分组匹配的子串在整个字符串的结束位置，参数默认值是0
# span(group) 方法是获取(start(group), end(group))
pattern = re.compile(r'([a-z+]+) ([a-z]+)', re.I) # re.I表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m) # 匹配成功返回一个match对象
print('m.group(0)', m.group(0)) # 返回匹配成功的整个子串
print('m.span(0)', m.span(0)) # 返回匹配成功的整个子串的索引
print('m.span(1)', m.span(1)) # 返回第一个分组匹配成功的整个子串的索引
print('m.group(1)', m.group(1)) # 返回第一个分组匹配成功的子串
print('m.span(2)', m.span(2)) # 返回第二个分组匹配成功的整个子串的索引
print('m.group(2)', m.group(2)) # 返回第二个分组匹配成功的子串
print('m.groups()', m.groups()) # 等价于 (m.group(1), m.group(2), ...)


# findall(string,[pos],[end])
# 在字符串中找到正则表达式所匹配的索所有字符，并返回一个列表，如果没有找到匹配的，则返回空列表
# match和search是匹配一次，findall是匹配所有
pattern = re.compile(r'\d+')
result1 = pattern.findall('python  12 python 23', 0, 20)
print('findall 匹配所有', result1)


# re.finditer(pattern,string,flags=0)
# 跟findall类似，查找匹配的所有子串，并作为一个迭代器返回
it = re.finditer(r'\d+', 'asd12gsdg23asd89bghr00')
for match in it:
    print('re.finditer 匹配所有子串', match.group())

# re.split(pattern,string,[maxsplit=0, flags=0])
# maxsplit分割次数，默认0不限制次数
# 按照匹配的字符分割后返回列表
print('re.split 分割字符串', re.split('\W+','python, php, java'))

# re.compile 返回正则对象RegexObject

# 正则表达式修饰符- 可选标志， 多个标志用或|间隔
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

print('''
正则表达式模式
字母和数字表示他们本身，一个正则表达式模式中的字母和数字匹配同样的字符串
多数字母和数字前加反斜杠会有不同的含义
标点符号只有被转义时才匹配自身，否则他们表示其他含义
反斜杠本身需要反斜杠转义
由于正则表达式都包含反斜杠，所以最好使用原始字符串来表示他们，模式元素如r'\t',等价于\\t匹配相应的特殊字符
''')
# ^	匹配字符串的开头
# $	匹配字符串的末尾。
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# re*	匹配0个或多个的表达式。
# re+	匹配1个或多个的表达式。
# re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
# re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
# re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b	匹配a或b
# (re)	G匹配括号内的表达式，也表示一个组
# (?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
# (?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
# (?: re)	类似 (...), 但是不表示一个组
# (?imx: re)	在括号中使用i, m, 或 x 可选标志
# (?-imx: re)	在括号中不使用i, m, 或 x 可选标志
# (?#...)	注释.
# (?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
# (?> re)	匹配的独立模式，省去回溯。
# \w	匹配数字字母下划线
# \W	匹配非数字字母下划线
# \s	匹配任意空白字符，等价于 [\t\n\r\f]。
# \S	匹配任意非空字符
# \d	匹配任意数字，等价于 [0-9]。
# \D	匹配任意非数字
# \A	匹配字符串开始
# \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
# \z	匹配字符串结束
# \G	匹配最后匹配完成的位置。
# \b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \n, \t, 等。	匹配一个换行符。匹配一个制表符, 等
# \1...\9	匹配第n个分组的内容。
# \10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

print('python 匹配"python"')
print('[Pp]ython 匹配"Python"或"python"')
print('[0-9] 匹配任何数字')
print('[a-z] 匹配任何小写字母')
print('[^aeiou] 匹配除aeiou外的所有字符')
print('[^0-9] 匹配除数字外的所有字符')

# .	    匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d	匹配一个数字字符。等价于 [0-9]。
# \D	匹配一个非数字字符。等价于 [^0-9]。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
