#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('''
文件读写
''')

# open(filename, mode) 返回一个file对象
f = open('ttt.txt', 'w')
f.write('python is good\n keep study on\n please')
f.close()

# f.read() 读取一个文件的内容 调用f.read(size)将读取一定数目的数据 然后将字符串或字节对象返回
# size 是一个可选的数字类型的参数，当size被忽略了或者为负，那么该文件的所有内容都将被读取并且返回
f = open('ttt.txt','r')
str = f.read()
print('read 读取文件内容 ', str)
f.close()

# f.readline单独读取一行，若返回空字符串说明已经读取到最后一行
f = open('ttt.txt','r')
str = f.readline()
print('readline读取一行', str)
f.close()

# f.readlines返回文件所有行 如果设置size，将进行分割
f = open('ttt.txt', 'r')
str = f.readlines()
print('readlines读取所有行',str)
f.close()

# 迭代文件对象读取每行
f = open('ttt.txt', 'r')
for line in f:
    print('迭代读取文件每行', line )
f.close()

# write 如果写入一些不是字符的东西，需要先进行转换
# f = open('ttt.txt', 'r')
# value = ['python is good\n keep study on\n please', 14]
# value = str(value)
# f.write(value)
# f.close()

# f.tell返回文件对象当前所处的位置 它是从文件开头开始算起的字节数
# f.seek(offset, form_what) 改变文件当前的位置
# from_what如果是0表示开头，1表示当前位置，2表示文件结尾
# seek(x, 0) 从起始位置即文件首行开始移动x个字符
# seek(x, 1) 从文件当前位置开始移动x个字符
# seek(x, 2) 从文件结尾往前移动x个字符

f = open('ttt.txt', 'rb+')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))
f.close()

# close关闭文件
# 当处理里面文件with关键字是非常好的方式，在结束时会帮你正确关闭文件，且比try-finally块简洁
with open('ttt.txt') as f:
    pass
print('with 自动关闭文件',f.closed)

# pickle模块实现基本的数据序列和反序列
# 通过pickle的序列化操作可以将程序中运行的对象保存到文件中，永久保存
# 通过pickle的反序列化操作，可以从文件中创建上一次程序保存的对象

import pickle
data1 = {
    'name': 'yang',
    'age': 26,
    'company': 'sina',
    'work': 'it'
}
list1 = [1,2,3,4]
with open('ttt.txt','wb') as f:
    pickle.dump(data1, f)
    pickle.dump(list1, f, -1)

import pickle,pprint
with open('ttt.txt','rb') as f:
    data1 = pickle.load(f)
    pprint.pprint(data1)

    data2 = pickle.load(f)
    pprint.pprint(data2)

# flush 刷新缓冲区，即将缓冲区的数据立刻写入文件且清空缓冲区，不需要被动的等待输出缓冲区写入
# 一般情况下，文件关闭后自动刷新缓冲区，但有时需要在关闭前刷新它，这时需要使用flush
with open('ttt.txt','wb') as f:
    print('flush 刷新缓冲区 文件名', f.name)
    f.flush()

# fileno 返回一个整型的文件描述符file descriptor FD整型，可用于底层操作系统的IO
with open('ttt.txt','wb') as f:
    print('fileno 输出整型的文件描述符', f.fileno())

# isatty 检测文件是否连接到一个终端设备
with open('ttt.txt',"wb") as f:
    print('isatty 检测文件是否连接到一个终端设备', f.isatty())

# truncate([size]) 从文件首行开始截取
with open('ttt.txt','wb+') as f:
    print('读取行:', f.readline())

    f.truncate(2)
    print('truncate 文件截取', f.read())

# writelines 文件写入字符串序列
with open('ttt.txt','w') as f:
    seq = ['paython is good\n', 'keep study on\n', 'please\n']
    f.writelines(seq)

    print('writelines写入字符串序列')
