# -*- coding: utf-8 -*-

# @Time    : 2024/4/5 18:26
# @Author  : lily
# @File    : time_module.py
"""
time模块
"""
import time
#时间戳
t=time.time()
print(t)

#时间戳转成字符串
s=time.ctime(t)
print(s)

#将时间戳转成元组
t1=time.localtime(t)
print(t1)
print(t1.tm_year)

#将元组转成时间戳
t2=time.mktime(t1)
print(t2)

#将元组的时间转成格式化字符串
tt=time.strftime('%Y-%m-%d %H:%M:%S',t1) #将元组转字符串
print(tt)
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S')) #默认将当前时间戳转成格式化字符串

#将字符串转成元组的方式
r=time.strptime('2445','%y%m%d')
print(r)