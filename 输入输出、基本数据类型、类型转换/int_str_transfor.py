# -*- coding: utf-8 -*-

# @Time    : 2024/1/27 15:32
# @Author  : lily
# @File    : int_str_transfor.py
"""
基本数据类型、类型转换、变量应用
"""

"""
数字类型：
       整数：0-9 int
       浮点数：整数+小数点+小数 float
       布尔值：真或假 True:1 False:0 --非 0 则为 True
       复数：  实数+虚数 0.99j
"""
# type
print(type(9))
print(type(9.9))
print(type(1 > 2))
print(type(9 + 0.99j))

# 布尔型，非0即为真
b = 99999999
print(bool(b))

"""
str字符串
定义：只要是引号（单、双）括起来的内容 ，都是字符串
"""
print(type("hello"))
print(type("你好"))
print(type("9.0"))
print(type("True"))
print(type(True))

# 字符串的float不能直接转换成int
str1 = "3.1444444444"
# print(int(str1))
print(int(float(str1)))

# 字符串转布尔型，空字符串转为布尔值为False，非空字符串永远为True
str = ""
str1 = "only"
print(bool(str), bool(str1))

bol=True
print(str(bol))
print(type(str(bol)))
print(bol)
print(type(bol))

"""===================变量赋值=================="""
"""多个变量连续定义与赋值,多个变量获得同一个初始值"""
a = b = c = 10
print(a, b, c)
# id()内存地址
print(id(a), id(b), id(c))

"""is 比较变量内存地址"""
s1='hello'
s2=s1
s3='hello'
s4='hello1'
print(s1 is s2)
print(s1 is s3)
print(s1 is s4)

"""多个变量连续定义与赋值,多个变量分别获取不同的初始值"""
c, d, e = 3, 2, 1
print(c, d, e)
print(id(c), id(d), id(e))

"""回收机制，一个变量接受多个值 使用*接收"""

*a, b, c = 1, 2, 3, 4, 5, 6
print(a, b, c)
print(type(a), type(b))

"""切片格式：字符串变量[start:end]"""
s='ABCDEFG'
print(s[1:4])
print(s[0:5])
print(s[:5])
print(s[-3:])
print(s[::-1])
print(s[-1:-8:-1])

x=s[:]
print('x={}'.format(x))
print('s={}'.format(s))
print(id(x),id(s))

