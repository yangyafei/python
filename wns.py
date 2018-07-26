#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import config
import urllib.request
import re


url = config.url_wns
response = urllib.request.urlopen(url)
code = response.getcode()
print(code)

# src="/Content/common/images/lottery/Images/Ball_4/10.png"
#regex = '(src)="/Content/common/images/lottery/Images/Ball_4/"(\d+)'
#matches = re.finditer(regex, response)

print(response)
#print(matches[0,10])