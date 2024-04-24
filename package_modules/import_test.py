# -*- coding: utf-8 -*-

# @Time    : 2024/3/30 20:39
# @Author  : lily
# @File    : import_test.py
"""
导入模块：自定义模块导入用法
1. import 模块名
  用的时候使用：模块名.类，模块名.变量，模块名.函数
2. from 模块名 import 变量｜函数｜类
"""
# import calculate
#
# list1=[100,2,5]
# #使用模块中的函数
# result=calculate.divide(*list1)
# print('除法的结果：result={}'.format(result))
#
# #使用模块中的全局变量
# print('calculate模块中number={},name={}'.format(calculate.number,calculate.name))
#
# #使用模块中的类
# calculate.Calculate.classfunc()  #调用类方法 calculate(模块名）.Calculate（类名）.classfunc()(类方法）
# calculate.Calculate.staticfunc() #调用静态方法，不需要创建对象，不需要传参
# person=calculate.Calculate('jack') #创建对象
# print('调用Calculate类的方法')
# person.speak()
# print('类的变量name：{}'.format(person.name))

# from calculate import number,name,add,minus,Calculate
from calculate import *
#使用模块中的函数
list1=[100,2,5]
result=add(*list1)
print('加法的结果：result={}'.format(result))

#使用模块中变量
total=result+number #number是calculate模块中的全局变量
print('totla=',total)

#使用模块中的类
p=Calculate('lily') #因为导入文件限制*限制的内容
p.speak()
p.classfunc()
p.staticfunc()