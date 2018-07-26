#!/usr/bin/env python


import config
import urllib.request
# import http.cookiejar
import re
import parser
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


url = config.url_wns
response = urllib.request.urlopen(url).read().decode('utf-8')
# code = response.getcode()
# print(response)



regex = '/Content/common/images/lottery/Images/Ball_4/(\d+).png'
matches = re.finditer(regex, response)

print(matches)
sum = 0
ans = []
temp = []
for match in matches:
    a = match.group(1)
    print(a)
    sum+=1
    temp.append(a)
    if sum%10 == 0 :
        ans.append(temp)
        print(temp)
        temp  = []
print(sum)