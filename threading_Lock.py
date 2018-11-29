#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/11/29
    author:yafei9 
"""

import threading
import time

print('''
Lock指令锁是可用的最低级的同步命令，Lock处于锁定状态，不被特定的线程拥有。Lock有锁定和非锁定两个状态
可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池，池中的线程处于状态图中的同步阻塞状态
Rlock可重入锁是一个可被同一线程请求多次的同步指令，Rlock使用”拥有的线程“和”递归等级“的概念，处于锁定状态时，Rlock被某个线程拥有，拥有Rlock的线程可以再次调用acquire()，释放锁时需要调用相同次数的release()
可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用acquire/release，计数器+1/-1，为0时处于未锁定状态
简言之，Lock是全局的，RLock属于线程
''')

# 不使用锁，多次运行可能产生混乱，这种场景适合使用锁
gl_num = 0
def show(arg):
    global gl_num
    time.sleep(1)
    gl_num += 1
    print(gl_num)
for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()
print('the first thread stop')

time.sleep(5)
gl_num = 0
lock = threading.RLock()
def show(arg):
    lock.acquire()
    global  gl_num
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    lock.release()
for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()
print('the two thread stop')
# 全局变量每次在操作时需要先获取锁，才能操作，因此保证了共享数据的安全性



# Lock和RLock
lock = threading.Lock()
try:
    lock.acquire()
    lock.acquire()
    lock.release()
    lock.release()
except RuntimeError:
    print('Lock Error')
else:
    print('Lock success')

lock = threading.RLock()
try:
    lock.acquire()
    lock.acquire()
    lock.release()
    lock.release()
except RuntimeError:
    print('RLock error')
else:
    print('RLock success')



