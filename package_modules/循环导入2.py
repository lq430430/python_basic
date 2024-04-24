# -*- coding: utf-8 -*-

# @Time    : 2024/4/5 16:48
# @Author  : lily
# @File    : 循环导入2.py
"""
文件说明
"""



def func():
    print('-----循环导入2中的func-------')
    from package_modules.循环导入1 import task1
    task1()
