# coding:utf-8
"""
python中 包(package)和模块(module)
包：python的文件夹
模块：我们的文件名（不包含.py)
import math
"""
import time

# 定时提醒：别人设置时间，时间到了自动弹窗
print("时间戳：",time.time())

print("格式化时间：",time.strftime('%Y-%m-%d %H:%M:%S'))
print("结构化时间：",time.localtime())
print("结构化时间——年：",time.localtime().tm_year)
print("结构化时间——月：",time.localtime().tm_mon)
print("结构化时间——天：",time.localtime().tm_mday)
print("结构化时间——时：",time.localtime().tm_hour)
print("结构化时间——分：",time.localtime().tm_min)
print("结构化时间——秒：",time.localtime().tm_sec)
print("结构化时间——星期：",time.localtime().tm_wday)

# t1=time.time()
t1=1699523086.7697074
print("时间戳---转换成---格式化时间：",time.strftime('%Y-%m-%d %H:%M:%S'),t1)
print("时间戳---转换成---格式化时间：",time.ctime(t1))

def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

"""
from ... import...
from 模块名 import 函数名
"""
from time import time

print(time())
