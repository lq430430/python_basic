# -*- coding: utf-8 -*-

# @Time    : 2024/3/31 14:02
# @Author  : lily
# @File    : modules.py
"""
文件说明
"""
# __all__=['User']  #针对from包.模块 import * 限制导入内容
# version='1.1'
class User:  # 用户类
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('登录成功')
        else:
            print('登录失败')

    def publish_article(self,article):
        print(self.username,'发表了文章：',article)
    def show(self):
        print(self.username,self.password)

if __name__=='__main__':
    print('------user-----')