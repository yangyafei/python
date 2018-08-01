#!/usr/bin/env python 
# -*- coding:utf-8 -*-

list = [1, 2, 3, 4, 5, 6]

print('访问索引值: ', list[1])
print('列表截取： ', list[1:3])

list[0] = 0
print('更新列表值: ', list)

del list[5]
print('删除列表值: ', list)

# len求list长度
print('list 长度 ', len(list))

# + 列表组合
print('+ 列表组合 ', [1,2] + [3,4])

# *列表重复
print('*列表重复 ', [2,3]*2)

# in 判断是否在列表中
print('in 判断是否在其中 ', 1 in list)

# for 迭代
for x in [1,2,3]:
    print(x, end=', ')

# max min 对列表一样适用
print("list 强制转换 通常适用于元祖:")

# list.append(obj) 在列表尾部追加元素
list1 = [1,3,4]
list1.append(3)
print('list.append尾部追加元素', list1)

# list.count统计某个元素在列表中出现的次数
list1 = [1,3,4,5,6,3]
print('list.count()统计出现的次数', list1.count(3))

# list.extend(seq) 尾部追加序列
list1 = [1,3,4,5]
list1.extend(range(4))
print('list.extend(seq)尾部追加序列', list1)

# list.index(obj) 查找某个值的索引位置
print('list.index(obj) 查找某个值的索引位置', [1,3,1].index(1))

# list.insert(index.obj) 在某个位置插入元素
list1 = [1,2,3]
list1.insert(1,44)
print('list.insert(index. obj) 某个位置插入元素',  list1)

# list.pop([index=-1]) 移除某个位置的元素，默认是最后一个
list1 = [1,2,3,4]
list1.pop(1)
print('list.pop([index=-1]) 移除某个位置的元素', list1 )

# list.remove(obj) 移除某个元素, 只移除第一个匹配到的
list1 = [1,2,1,3,1]
list1.remove(1)
print('list.remove(obj)移除某个元素', list1)

# list.reverse(0) 翻转
list1 = [1,2,3,4]
list1.reverse()
print('list.reverse翻转', list1)

# list.sort(cmp=none, key=none, reverse=false) 排序
# cmp指定参数，可以写方法名
# key比较的元素
# reverse 默认false升序
def takeSecond(elem):
    return elem[1]
random = [(2,2), (3,4), (4,1), (1,3)]
random.sort(key=takeSecond)
print('list.sort排序', random)

# list.clear() 清空
list1 = [1,2]
list1.clear()
print('list.clear 清空', list1)

# list.copy() 复制列表
list1 = [1, 2, 3]
list2 = list1.copy()
print('list.copy 复制', list2)


