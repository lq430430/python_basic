# -*- coding: utf-8 -*-

# @Time    : 2024/3/30 20:07
# @Author  : lily
# @File    : calculate.py
"""
用于导入测试的模块，主要用于加减乘除运算
包括全局变量、函数、类
"""
__all__=['add','number','Calculate']  #限制其他模块导入*时，限制获取的内容

number=100
name='calculate'
def add(*args):
    """
    加法运算
    :param args: *args装包：将多个数据组成一个元组
    :return: sum 求和总数
    """
    if len(args)>1:
        sum=0
        for num in args:
            sum+=num
        return sum
    else:
        print('至少要传入两个参数')

def minus(*args):
    """
    减法运算
    :param args: *args装包：将多个数据组成一个元组
    :return:
    """
    if len(args)>1:
        sub=0
        for num in range(len(args)):
            if num==0:
                sub=args[num]
            else:
                sub-=args[num]
        return sub
    else:
        print('至少要传入两个参数')
def mutiply(*args):
    '''
    乘法运算
    :param args: *args装包：将多个数据组成一个元组，进行乘积
    :return:
    '''
    if len(args)>1:
        muti=0
        for num in args:
            muti*=num
        return muti
    else:
        print('至少要传入两个参数')
def divide(*args):
    """
    除法运算
    :param args: *args装包：将多个数据组成一个元组
    :return:
    """
    if len(args)>1:
        sub=0
        for num in range(len(args)):
            if num==0:
                sub=args[num]
            else:
                sub//=args[num]
        return sub
    else:
        print('至少要传入两个参数')

class Calculate:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print('{} is calculating'.format(self.name))

    @classmethod
    def classfunc(cls):
        print('------>Calculate的类方法')

    @staticmethod
    def staticfunc():
        print('------>Calculate的静态方法')

def test():
    print('--------自动加载test方法')



# print('模块名 __name__:',__name__)

if __name__=='__main__':
    test()