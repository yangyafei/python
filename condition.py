#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('''
end 
if elif else
''')

# end 将结果输出到同一行，或者在输出的末尾加上不同的字符
a, b =0, 1
while b < 1000:
    print(b, end=', ')
    a, b = b, a+b
print()

# if elif else
a = 60
if a>85:
    print('A')
elif b > 60:
    print('B')
else :
    print('C')

# while
n = 100
sum = 0
cnt = 1
while cnt<=n:
    sum = sum + cnt
    cnt += 1
print('while 循环', sum)

# 无线循环 代码暂时注释掉了
# while 1 ==1 :
#     num = int(input('输入一个数字 :'))
#     print('你输入的数字为: ', num)


# while else
num = 3;
while num<0:
    print('num 小于0')
else:
    print('num 大于0')

# 简单语句组 如果while循环只有一条，可以将语句和while放在一行
flag = 1
# while flag: print('hello python') #死循环

# for 循环
a = [1, 2, 3, 4, 5]
for x in a: print('for 循环', x)

# for else
a = []
for x in a:
    print('for 循环', x)
else:
    print('for else')

# range 生成数列
for i in range(3):
    print('range 生成数列', i)
for i in range(3,5):
    print('range 指定范围', i)
for i in range(3,10, 3):
    print('range 增量', i)

# range结合len
a = [1,2,3]
for i in range(len(a)):
    print('range结合len:', a[i])

# continue break不写demo了

# pass 空语句 保证结果的完整性，不做任何事情 做为占位符
if 1>0:
    pass
    print('pass 空语句')

