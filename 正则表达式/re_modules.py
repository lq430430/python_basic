# -*- coding: utf-8 -*-

# @Time    : 2024/4/23 15:04
# @Author  : lily
# @File    : re_modules.py
"""
正则表达式re
"""
import re

# msg = '佟丽娅娜扎迪丽热巴'
# pattern = re.compile('佟丽娅')  # compile 编译表达式格式，返回格式对象也就是正则
# result=pattern.match(msg)  # 使用正则去匹配字符串,match没有匹配则返回None，match从头开始匹配
# print(result)
#
# result=re.match('佟丽娅',s)
# print(result)

# s = '娜扎迪丽佟丽娅热巴佟丽娅'
# result = re.search('佟丽娅', s)  # search进行正则字符串匹配方法，匹配的是整个字符串
# print(result)
# print(result.span())  # 返回位置
# print(result.group())  #使用group提取到匹配的内容

# # 用户名可以是字母或数字，不能是数字开头，用户名长度必须6位以上【0-9a-zA-Z】
username='&*)admin01$$'
# username='admin01'

# result1=re.match('[a-zA-Z][0-9a-zA-Z]{5,}',username) #使用username去匹配正式表达式，从开头匹配，匹配成功就返回
# result2=re.match('\w{5,}',username)
#
# print(result1,result2)
#
# result3=re.search('\w{5,}',username)
# result4=re.search('^\w{5,}$',username)
#
# print(result3)
# print(result4)

# #\b的使用
# #匹配.py
# msg='a.py ab.txt bb.py kk.png uu.py apyb.txt .py ss*py'
# #findall匹配所有子串，返回一个列表。
# result1=re.findall(r'\w*.py\b',msg) # r表示字符原义，也可以使用转义字符'\w*.py\\b', 其中.匹配任意字符
# result2=re.findall(r'\w*\.py\b',msg) # r表示字符原义，也可以使用转义字符'\w*.py\\b',将.转义\.表示字符串.
# print(result1)
# print(result2)

#分组 匹配数字0-100数字
# n='0' #不能使用09
# result=re.match('[1-9]?\d',n)

# n='10000'
# result=re.match('[1-9]+\d*',n)

# 正确写法
# n='100'
# result= re.match(r'[1-9]?\d?$|100$',n)
# print(result)

# #验证输入的邮箱 163 126 或者qq
# email='28884325@163.com'
# result=re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)',email)
# print(result)
#
# #qq号码验证 ：5～11位，开头不能是0
# qq='19394'
# qq='29334000008'
#
# result=re.match('^[1-9]\d{4,10}$',qq)
# print(result)
#
# #手机号码匹配 11位1开头
# phone='18600002222'
#
# result=re.match('^1[35789]\d{9}$',phone)
# print(result)
#
#不是以4/7结尾的手机号码（11位）
phone='18600002225'
#方法一：[^] 取非
result=re.match(r'1\d{9}[^47]$',phone)
#方法二：[-]
result=re.match(r'1\d{9}[0-35-689]$',phone)

print(result.group())

#匹配电话号码 爬虫
tel='010-12345678' #区号3位或4位

result=re.match(r'(\d{3}|\d{4})-(\d{8})$',tel)
print(result)
#分别提取
print(result.group(1))
print(result.group(2))

# #在字符串中搜索 a7a, a88c,a78888b 模式的字符
# s='a7aoera88bdfkjds7878a'
#
# result=re.findall('[a-z][0-9]+[a-z]',s)
# print(result)
#
# #起名 ?P<name><pattern>
# #html标签匹配
# msg='<html><h1>abc</h1></html>'
#
# result=re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))

# #分组：不需要引用分组
# msg='<h1>abc</h1>'
#
# result=re.match(r'<\w+>(.+)</\w+>',msg)
# print(result)
# print(result.group(1))
#
# #分组：引用分组匹配内容---number
# msg='<html><h1>abc</h1></html>'
#
# result=re.match(r'<(\w+)><(\w+)>(.+)</\2></\1>$',msg)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
#
# #替换re.sub()
#
# result=re.sub(r'\d+','90','java:100,python:99')
# print(result)

# def func(temp): #匹配到的内容取出，进行计算
#     num=temp.group()
#     num1=int(num)+1
#     return str(num1)
#
# result=re.sub(r'\d+',func,'java:89,python:99')
# print(result)
#
# result=re.split(r'[,:]','java:89,python:99')  #split 切割，正则里表示遇到，或：就切割string
# print(result)

#非贪婪模式
path='<img src="https://imgsa.baidu.com/forum/crop%3D0%2C0%2C500%2C374%3Bwh%3D227%2C170%3B/sign=2fc8d1aa728da9775a60dc6b8d61d429/68dbb6fd5266d0166c7c8cb1962bd40734fa35c5.jpg" width="232" height="174">'

result=re.match(r'<img src="(.+)"',path) # 贪婪模式 “到最后一个”
result=re.match(r'<img src="(.+?)"',path) #非贪婪模式 “开始到第一个”
print(result.group())
image_path=result.group(1) #图片路径

#下载图片
import requests

response=requests.get(image_path)

with open('boy.jpg','wb') as wstream:
    wstream.write(response.content)