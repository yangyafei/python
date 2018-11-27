#!/usr/bin/env python
# coding: utf-8

import urllib.request
# import http.cookiejar
import re
import parser
import sys
import codecs
import datetime
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

url_wns='https://www.678922.cc/Lottery/syspk10List/?classid=109&chinese=%E6%9E%81%E9%80%9F%E8%B5%9B%E8%BD%A6%E6%9E%81%E9%80%9F%E8%B5%9B%E8%BD%A6'
url = url_wns
response = urllib.request.urlopen(url).read().decode('utf-8')
# code = response.getcode()
# print(response)


# 号码
regex_num = '/Content/common/images/lottery/Images/Ball_4/(\d+).png'
matches_num = re.finditer(regex_num, response)

# 期号
now = datetime.datetime.now().strftime("%Y%m%d")
regex_no = '<td>'+ now +'(\d+)</td>'
matches_no = re.finditer(regex_no, response)

tmax = []
tmin = []
todd = []
teven = []
for i in range(20):
    print(i)
    tmax.append(0)
    tmin.append(0)
    todd.append(0)
    teven.append(0)


sum = 0
temp = []
ans = []
for match in matches_num:
    a = match.group(1)
    sum+=1
    #a = int(a)
    temp.append(a)
    if sum%10 == 0 :
        print(temp)
        ans.append(temp)
        temp  = []



# for match in matches_no:
#     print(now+match.group(1))


def fun(pos):
    ll_max = 0
    ll_min = 0
    ll_odd = 0
    ll_even = 0


    for num in ans:
        if int(num[pos]) > 5:
            ll_max +=1
            if ll_min !=0 :
                tmin[ll_min] += 1
                ll_min = 0
        if int(num[pos]) < 6:
            ll_min +=1
            if ll_max !=0 :
                tmax[ll_max] += 1
                ll_max = 0
        if int(num[pos]) %2 == 0:
            ll_even +=1
            if ll_odd !=0 :
                todd[ll_odd] += 1
                ll_odd = 0
        if int(num[pos]) %2 == 1:
            ll_odd +=1
            if ll_even!=0 :
                teven[ll_even] +=1
                ll_even = 0

for i in range(0,10):
    fun(i)
    print(i+1, ': ', tmax)
    

