# -*- coding: utf-8 -*-

# @Time    : 2024/3/31 14:41
# @Author  : lily
# @File    : test.py
"""
导入包：模块包导入分为三种类型：
类型一：
    导入的py文件在同一文件夹下
类型二：
    py文件同导入的文件夹同一目录
类型三：
    导入的包在另外一个文件夹下
练习：用户发表文章
1.创建用户类
2.创建文章类
3.用户发表文章

"""
# from package_modules.user.modules import User  # 导入的py文件在同一文件夹下，也需要编写完整路径 项目下的文件夹/包/模块
from .modules import User  #导入的py文件在同一文件夹下,当前目录下的模块导入
from package_modules.article.modules import Article  # 导入的包在另外一个文件夹下，也需要编写完整路径 项目下的文件夹/包/模块

user = User('admin', 123456)  # 创建用户

article1 = Article('西游记', '吴承恩')  # 创建文章

user.publish_article(article1)

#导入包的外部文件
from package_modules.calculate import *

list1=[8,7,6,5]
print('sum= ',add(*list1))

Max=100