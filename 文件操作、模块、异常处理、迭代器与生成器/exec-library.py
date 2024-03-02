# -*- coding: utf-8 -*-

# @Time    : 2024/3/2 19:05
# @Author  : lily
# @File    : exec-library.py
"""
图收馆管理系统--持久化保存至文件（用户信息）：用户注册，用户登录
"""
import os.path


def register():
    """
    用户注册
    :return:
    """
    username=input('请输入用户名：')
    password=input('请输入密码：')
    repassword=input('请输入确认密码：')

    #判断用户名是否存在
    with open(os.path.dirname(__file__)+'/'+'user.txt',mode='r') as file:
        for line in file.readlines():
            if username in line:
                print('用户名已存在，注册失败')
                break
        else:
            #判断密码与确认密码一致
            if password == repassword:
                #将用户名及密码写入user.txt文件
                with open(os.path.dirname(__file__) + '/' + 'user.txt', mode='a') as file:
                    file.write('{} {}\n'.format(username,password))
            else:
                print('密码与确认密码不一致，注册失败')
def login(user,passwd):
    '''
    登录
    :param user: 用户名
    :param passwd: 密码
    :return:
    '''
    #判断用户名及密码是否在文件中
    with open(os.path.dirname(__file__)+'/'+'user.txt',mode='r') as file:
        #按行读取文件
        line=file.readline()
        list1=line.strip().split(' ')
        print(list1)
        if list1[0]==user and list1[1]==passwd:
            print('登录成功')
        else:
            print('用户名或密码错误')
if __name__=='__main__':
    #用户注册
    register()
    #用户登录
    login('lily','111111')