# -*- coding: utf-8 -*-

# @Time    : 2024/3/24 20:58
# @Author  : lily
# @File    : class_multiple_inherit.py
"""
多重继承,Python3查找顺序是广度优先
"""
import inspect

# class Base(object):  #新式类
#     def test(self):
#         print("-------base------")

class Base: #经典类
    def test(self):
        print("-------base------")
class A(Base):
    def test(self):
        print("-------AAAAAAAAAAAA------")
class B(Base):
    def test(self):
        print("-------BBBBBBBBBBB------")
class C(A,B):
    pass

c=C()
c.test()
# print(inspect.getmro(C)) #返回搜索顺序的一个元组
print(C.__mro__)  #返回搜索顺序的一个元组
