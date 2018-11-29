#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/11/28
    author:yafei9 
"""
import threading
import time

# Thread使用1：将要执行的方法作为参数传给Thread的构造方法
# threading.currentThread() 返回当前的线程变量
# Thread.getName 获取线程名
def action(args):
    time.sleep(1)
    print ('the first thread start and name is %s\r' % threading.currentThread().getName())
    print('the first thread arg is:%s\r' % args)

for i in range(4):
    t = threading.Thread(target=action, args=(i,))
    t.start()
print('first thread end')


time.sleep(5)


# Thread使用2：从Thread继承并重写run()
class MyThread(threading.Thread):
    def __init__(self, arg):
        # 注意一定要显示调用父类的初始化函数
        super(MyThread, self).__init__()
        self.arg = arg
    # 定义每个线程运行的函数
    def run(self):
        time.sleep(1)
        print('the second thread start and name is %s\r' % threading.currentThread().getName())
        print('the second arg is:%s\r' % self.arg)
for i in range(4):
    t = MyThread(i)
    t.start()
print('\n\nsecond thread end')
time.sleep(5)

# setDeamon 主线程执行完毕之后，后台线程不管成功与否都结束
def action(arg):
    time.sleep(1)
    print('the third thread start and name is %s \r' % threading.currentThread().getName())
    print('the third arg is %s\r' % arg)
for i in range(4):
    t = threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    t.start()
time.sleep(5)
print('\n\nthird thread end')



# join堵塞，主线程等待子线程全部执行完成后或者子线程超时后，主线程才结束
def action(arg):
    time.sleep(1)
    print('the fouth thread start and name is %s\r' % threading.currentThread().getName())
    print('the fouth arg is %s\r' % arg)
thread_list = []
for i in range(4):
    t = threading.Thread(target=action, args=(i,))
    t.setDaemon(True)
    thread_list.append(t)
for t in thread_list:
    t.start()
for t in thread_list:
    t.join()
time.sleep(2)
print('\n\nfouth thread end')




# join堵塞 每个进程都都被上个进程的join堵塞，失去多线程的意义
def action(arg):
    time.sleep(1)
    print('the fiveth thread start and name is %s\r' % threading.currentThread().getName())
    print('the five arg is %s\r' % arg)
for i in range(4):
    t = threading.Thread(target=action, args=(i,))
    t.setDaemon(True)
    t.start()
    t.join()
time.sleep(2)
print('\n\nfive thread end')







