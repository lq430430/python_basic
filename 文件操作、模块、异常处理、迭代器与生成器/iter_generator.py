# -*- coding: utf-8 -*-

# @Time    : 2024/3/2 21:15
# @Author  : lily
# @File    : iter_generator.py
"""
迭代器：是一个可以记住遍历的位置的对象。
"""


def iter_1():
    list1=[x*3 for x in range(10) if x%3==0]
    print(type(list1))
    print(list1)
    # 方法1：通过推导式得到生成器
    g=(x*3 for x in range(10))
    print(type(g))
    print(g)

    #方法2 iter()
    g=iter(list1)
    print(type(g))
    print(g)

    #方式1：通过__next__()得到元素
    print(g.__next__())
    print(g.__next__())

    #方式2：next()通过系统内置函数
    print(next(g))
    print(next(g))
    # print(next(g)) #StopIteration 超出元素个数

def yield_fun():
    """
    只要函数中出现了yield关键字，函数就不是函数而是生成器了
    :return:
    """
    n=0
    while True:
        n+=1
        yield n # 等于return n 并且暂停，下次还从此处开始

def gen():
    i=0
    while i<5:
        temp=yield i
        print('temp:',temp)
        for x in range(temp):
            print('--------',x)
        print('*************')
        i+=1
    return '没有更多数据了'
from collections import Iterable
def Iterator_fun():
    list1=[1,2,5,6,7]
    print(isinstance(list1,Iterable))
if __name__ == '__main__':
    # # 得到生成器方法1
    # iter_1()

    #Iterator
    Iterator_fun()

    # #yield 生成器
    # g=yield_fun()
    # print(next(g)) #调用next(g)时，才调用yield_fun()方法
    # print(next(g))

    # #yield +send()
    # g=gen()
    # g.send(None)
    # g.send(3)
    # g.send(5)

