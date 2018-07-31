#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('''
日期处理
time和calendar模块可以用于格式化日期和时间
''')

import time

# time.time() 当前时间戳
# 时间戳用于日期运算，1970年之前不行，2038年之后也不行
print("time.time()当前时间戳", time.time())

# 时间元组 9组数字处理时间
# 4位数年 月1-12 日1-31 小时0-23 分钟0-59 秒0-59 一周的第几日0-6 一年的第几日1-366 夏令时-1,0,1，-1是决定夏令时的旗帜


localtime = time.localtime(time.time())
print("本地时间", localtime)

localtime = time.asctime(time.localtime(time.time()))
print('格式化时间', localtime)

print('time.strftime格式化日期', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print('time.strftime格式化时间', time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# import calendar
# cal = calendar.month(2018, 1)
# print('calendar.month 获取日历\n ', cal)

import time
# time.altzone 返回格林威治西部的夏令时地区的偏移秒数，如果返回负值对夏令时启用的地区才能使用
print('time.altzone 夏令时地区的偏移秒数 %d' % time.altzone)

# time.asctime([tupletime]) 接受一个时间元组返回一个可读的形式为：Tue Dec 11 18:07:14 2008 共24字符的字符串
t = time.localtime()
print('time.asctime(t) %s'% time.asctime(t))

# time.clock() 用以浮点数计算的秒数返回当前CPU时间
def procedure():
    time.sleep(1)
t0 = time.process_time()
procedure()
print('time.clock ', time.process_time() - t0)
t0 = time.time()
procedure()
print(time.time() - t0)

# time.ctime([sec]) 相当于asctime(localtime(sec))
print('time.ctime %s' % time.ctime() )

# time.gmtimes([secs]) 接受时间戳并返回格林威治天文时间下的时间元组t t.tm_isdst始终为0
print('time.gmtimes  ', time.gmtime(1455508609.34375))

# time.localtime([secs]) 接受时间戳并返回当地时间下的时间元组t t.tm_isdst可取0或1 取决于当地当时是不是夏令时
print('time.localtime', time.localtime(1455508609.34375))

# time.mktime(tupletime) 接受时间元组并返回时间戳
t = (2016,2,17,17,3,38,1,48,0)
secs = time.mktime(t)
print('time.mktime %f' % secs)
print('asctime(localtime(secs)) %s' % time.asctime(time.localtime(secs)))

# time.sleep推迟线程的运行
print("start: %s" % time.ctime())
time.sleep(1)
print('end %s' % time.ctime())

# time.strftime(fmt, [tupletime]) 接受时间元组 并返回以可读字符串表示的当前时间，格式由fmt决定
print('time.strftime ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

import time
# time.strptime(str, fmt)使用fmt格式把一个时间字符串解析为时间元组
# struct_time = time.strptime("30 Nov 00", "%d %b %y")
# print('time.strptime', struct_time)

# time.time() 返回时间戳
print('time.time() 时间戳',time.time())

# time,tzset()

