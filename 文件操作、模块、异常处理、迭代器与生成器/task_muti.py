# -*- coding: utf-8 -*-

# @Time    : 2024/3/3 00:39
# @Author  : lily
# @File    : task_muti.py
"""
协程
"""

def task1(n):
    for i in range(n):
        print("正在搬第{}块砖".format(i))
        yield None

def task2(n):
    for i in range(n):
        print("正在听第{}首歌".format(i))
        yield None

if __name__=='__main__':
    g1=task1(5)
    g2=task2(5)

    while True:
        try:
            g1.__next__()
            g2.__next__()
        except:
            break