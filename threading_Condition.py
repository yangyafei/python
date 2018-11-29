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
    Condition条件变量通常与一个锁关联，需要在多个condition中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个Rlock实例
    可以认为，除了Lock带有的锁定池外，Condition还有一个等待池，池中的进程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进程锁定池等待锁定
    acquire([timeout])/release()：调用关联的锁的相应方法
    wait([timeout])：调用这个方法将使线程进入Condition的等待池等候通知，并释放锁，使用前线程必须已获得锁定，否则抛出异常
    notify()：调用这个方法从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获取锁定(进入锁定池),其他线程仍在等待池，调用这个方法不会释放锁，使用前线程必须已获得锁定，否则抛出异常
    notifyAll()：调用这个方法通知等待池中的所有线程，这些线程进入锁定池并尝试获取锁定，调用这个方法线程必须已获得锁定，否则抛出异常
''')


# 生产者消费者模式
cnt = 0
LIMIT_NUM = 2
product = None #商品
con = threading.Condition() # 条件变量
def produce():#生产者方法
    global product, cnt, LIMIT_NUM
    if con.acquire():
        while True:
            if product is None:
                cnt += 1
                print('produce...')
                product = 'angthing'

                con.notify()# 通知消费者商品已生产
            con.wait() # 等待通知
            time.sleep(2)
            if cnt>LIMIT_NUM :
                break
def consume():#消费者方法
    global product, cnt, LIMIT_NUM
    if con.acquire():
        while True:
            if product is not None:
                print('consume...')
                product = None

                con.notify() # 通知生产者商品没有了
            con.wait() # 等待通知
            time.sleep(2)
            if cnt>LIMIT_NUM+1:
                break
t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t1.start()
t2.start()
# 如果不加cnt限制会一直生产消费下去

time.sleep(5)

condition = threading.Condition()
products = 0
class Producer(threading.Thread):
    def run(self):
        global products, LIMIT_NUM
        while True:
            if condition.acquire():
                if products<LIMIT_NUM:
                    products += 1
                    print('Producer(%s):deliver one now products is %s' % (self.name, products))
                    condition.notify() # 不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print('Producer(%s):already limit num, stop deliver, now products is %s' % (self.name, products))
                    condition.wait() # 自动释放锁定
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global products, LIMIT_NUM
        while True:
            if condition.acquire():
                if products>1:
                    products -= 1
                    print('Consumer(%s):consume one, now products is %s' % (self.name, products))
                    condition.notify()
                    condition.release()
                else:
                    print('Consumer(%s):only 1, stop consume, products is %s' % (self.name, products))
                    condition.wait()
                time.sleep(2)
for p in range(2):
    p = Producer()
    p.start()
for c in range(2):
    c = Consumer()
    c.start()
