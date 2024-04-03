# -*- coding: utf-8 -*-

# @Time    : 2024/3/29 19:46
# @Author  : lily
# @File    : class_singleton.py
"""
单例模式
运行整个程序时，只创建一个实例对象，重复使用,节省内存。
"""
class Singleton:
    __instance = None  # 类属性，用于保存唯一的实例

    def __new__(self):
        if self.__instance is None: #判断类属性是否已被创建
            print('-----1-----')
            self.__instance = object.__new__(self)
        else:
            print('-----2-----')
        return self.__instance
    def __init__(self):
        pass

one=Singleton()
two=Singleton()
print(id(one))  # 内存空间一致
print(id(two))
print(one == two)   # True
print(one is two)   # True

ValueError