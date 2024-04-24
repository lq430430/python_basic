# -*- coding: utf-8 -*-

# @Time    : 2024/3/31 14:07
# @Author  : lily
# @File    : package_modules.py
"""
使用包的方法
"""
#使用包中模块中的User类
# from user import modules
#
# user1=modules.User('lily',234534)
# user1.login('admin',123456)

# from user.modules import User #from 包.模块 import 类 方法  变量
# user2=User('admin',123456)
# user2.login('admin',123456)
#
# from article.modules import Article
# a=Article('三国传','罗贯中')
# a.show()

# from user.modules import version
# print(version)
# user2=User('admin',123456)
# user2.show()

import user  #-----user的__init__
from user import *  #from 包名 import * 需要在__init__文件中加__all__=【】
u=modules.User('admin',123456)
u.show()

print(test.Max) # 访问包中模块里定义的变量