# -*- coding: utf-8 -*-

# @Time    : 2024/4/5 16:48
# @Author  : lily
# @File    : 循环导入1.py
"""
文件说明
"""
from package_modules.循环导入2 import func


def task1():
    print('---------task1-------')


def task2():
    print('----task2------')
    func()

if __name__=='__main__':
    task1()
    task2()