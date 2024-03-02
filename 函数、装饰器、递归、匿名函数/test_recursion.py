# -*- coding: utf-8 -*-

# @Time    : 2024/2/25 00:44
# @Author  : lily
# @File    : test_recursion.py
"""
递归函数：如果一个函数在内部不调用其他的函数，而是调用自己本身的话，这个函数就是递归函数。
"""
def test1(i):
    """
    累加1-5的和
    :param i:
    :return:
    """
    if i==5:
        return 5
    else:
        return i+test1(i+1)
def test2(i):
    """
    阶乘
    :param i:
    :return:
    """
    if i==5:
        return 5
    else:
        return i*test2(i+1)
def fibo(n):
    """递归函数实现斐波那契数列"""
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n -2)


if __name__ == '__main__':
    #累积和，使用递归函数
    r=test1(1)
    print(r)

    #阶乘，5！=1*2*3*4*5
    print(test2(1))

    #斐波那契数列: 1，1，2，3，5，8，13，21，34......
    n = int(input("请输入数列的项数："))
    res = fibo(n)
    print(res)