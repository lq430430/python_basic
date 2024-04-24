# -*- coding: utf-8 -*-

# @Time    : 2024/4/5 18:45
# @Author  : lily
# @File    : datetime_module.py
"""
datetime模块
"""
import datetime
import time

print(datetime.time.hour) #对象datetime.time的hour属性

#因为date是类，所以要创建对象并初始化后传给d
d=datetime.date(2024,4,5)
print(d)
#格式化日期
print(datetime.date.ctime(d))
print(datetime.date.day)
t=time.time()
print(t)
print(datetime.date.today())

#时间差timedelta
timedel=datetime.timedelta(days=2) #时间差
timedel1=datetime.timedelta(weeks=1,hours=4) #时间差

d=datetime.datetime.now() #当前时间
print(d)
print(d-timedel) #当前时间-时间差
print(d+timedel1) #当前时间-时间差

