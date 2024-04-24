# -*- coding: utf-8 -*-

# @Time    : 2024/3/31 14:01
# @Author  : lily
# @File    : modules.py
"""
文件说明
"""


class Article:#文章类
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print('发表文章名字：{}的作者是：{}'.format(self.name,self.author))
class Tag:#标签类
    def __init__(self, name):
        self.name = name