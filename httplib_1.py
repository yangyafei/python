#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/8/1
    author:yafei9 
"""


'''
httplib是一个相对底层的HTTP请求模块，其上有专门的包装模块，如URLlib内建模块，goto等第三方魔力
但是封装越多越不灵活，比如urllib模块里请求错误时就不会返回结果页的内容，只有头信息，
对于某些需要检测错误请求的场景不适合，所以就得用httplib模块
'''

# httplib.HTTPConnection(host,[port, [strict, [timeout]]]) 创建一个http类型的请求链接
# host 请求地址，不能带http://开头
# port 端口，
# strict是否严格检查请求的状态行，就是http1.0/1.1协议版本的那一行 默认FALSE，为TRUE时检查错误会抛出异常
# timeout 单次请求超时时间，没有时默认使用httplib模块内的全局的超时时间
# http.client.HTTPConnection(...) python3没有httplib，使用import http.client

# httplib.HTTPSConnection底层的socket模块是支持SSL的编译模式，即编译时SSL选项是否开启
# 创建一个https链接，必须保证
# ket_file 一个包含PEM格式的私钥文件
# cert_file 一个包含PEM格式的认证文件

# HTTPConnection.request(method,url,[body, [headers]])
# method请求方法 GET POST HEAD PUT DELETE
# body 请求是否带数据，该参数是一个字典
# headers 是否带头部信息，该参数是一个字典，不过键的名称是指定的http头关键字

# HTTPConnection.getresponse() 获取一个http响应对象HTTPResponse，相当于执行最后2个空格

# HTTPConnection.close() 关闭指定的httpconnect连接

# HTTPResponse.read([amt]) 获取http响应的内容部分，即网页源码
# amt读取指定长度的字母，默认为空，读取全部

# HTTPResponse.getheaders([name,[default]]) 获取所有的响应头内容，是一个元组列表
# 可以传递name, 获取某一个

# HTTPResponse.fileno() 获取fileno

# HTTPResponse.msg() 获取所有头部信息跟getheaders一样，只不过这个是原始未处理的字符串

# HTTPResponse.status() 请求状态，即状态码

# HTTPResponse.version() 请求的http版本 10是http1.0 11是http1.1

# HTTPResponse.reason() 请求的表述内容，200是OK，404是Not Found，即状态码的文字描述



import http.client
import urllib
def sendHttp():
    data = urllib.parse.urlencode({'wd':'python'})
    headers = {
        "Content-type": 'application/x-www-form-urlencoded',
        "Accept": 'text/plain'
    }

    conn = http.client.HTTPConnection('news.baidu.com')
    conn.request('POST', '/', data, headers)
    httpres = conn.getresponse()

    print(httpres.status)
    print(httpres.reason)
    print(httpres.read())



if __name__ == '__main__':
    sendHttp()