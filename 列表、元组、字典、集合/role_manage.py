# -*- coding: utf-8 -*-

# @Time    : 2024/2/14 12:05
# @Author  : lily
# @File    : role_manage.py
"""
王者荣耀角色管理

角色：姓名、性别、职业
添加角色
修改角色
删除角色
查询角色 --单个角色
显示所有角色
退出系统
"""
print("~~~~~~~~~~~~欢迎进入王者荣耀角色管理系统~~~~~~~~~")
roles=[]
while True:
    option=input("请选择功能：\n1.添加角色\n2.修改角色\n3.删除角色\n4.查询角色\n5.显示所有角色\n6.退出系统\n")
    if option=='1':
        name=input("请输入姓名：")
        sex=input("请输入性别：")
        profession=input("请输入职业：")
        role=[name,sex,profession]
        roles.append(role)
    elif option=='2':
        modify_name=input("请输入要修改的角色姓名：")
        for items in roles:
            if modify_name in items:
                modify_sex = input("请输入要修改的性别：")
                modify_profession = input("请输入要修改的职业：")
                items[1]=modify_sex
                items[2]=modify_profession
                print("修改成功")
                break
        else:
            print("未找到角色姓名，无法修改")
    elif option=='3':
        delete_name = input("请输入要删除的角色姓名：")
        for items in roles:
            if delete_name in items:
                roles.remove(items)
                print("删除成功")
                break
        else:
            print("未找到角色姓名，无法修改")
    elif option=='4':
        print("查询单个角色")
        query_name = input("请输入要查询的角色姓名：")
        for items in roles:
            if query_name in items:
                print(items)
                break
        else:
            print("未找到角色姓名，无法修改")
    elif option=='5':
        print("查看所有角色")
        for items in roles:
            print(items)
    elif option=='6':
        print("已退出系统")
        break