
print('''__init__py 作用是将文件夹变成一个python模块，python中每个模块的包中都有__init__.py文件''')

print('''__name__这个系统变量显示了当前模块执行过程中的名称，
如果当前程序运行在整个模块中，__name__的名称就是__main__，如果不是则为整个模块的名称''')

print('''
__main__一般作为函数入口，类似于C语言，尤其在大型工程中，常常有if __name__ == "__main__"来表明整个工程开始的入口
''')
def nameMain() :
    if __name__ == '__main__' :
        print('当前文件调用执行')
    else :
        print('其他的文件程序调用执行')

# dict(key, default) 获取字典中值，为找到返回默认值default
dict1 = {'name':'yang'}
print('dict.get 获取值', dict1.get('age'))