# -*- coding: utf-8 -*-

# @Time    : 2024/1/29 21:57
# @Author  : lily
# @File    : test_for.py
"""
for 遍历
1.遍历 -- 复杂的数据结构中，将里面的元素一个个的获取出来
2.循环

语法：
for 变量名 in 可遍历的数据：（可拆分的 -- 字符串，列表... ...)
    循环体逻辑：会在每一次循环的时候把便利的数据一个个的拿出来，并且赋值给这个变量名

循环：
1.循环次数根据可遍历的数据长度决定
2.变量名  获取到可迭代的数据每一个元素
"""
import random


def simple_if():
    """
    if分支简化写法 (if else代码较少时使用)
    :return:
    """

    a = 1
    b = 2
    c = a if a < b else b  # a<b c=a否则 c=b
    print(c)
    print("a<b") if a < b else print("a>b")

def test_find(element,lst):
    """
    lst中是否包含x元素，包含返回True，否则返回False
    :param x:
    :param lst:
    :return:
    """
    lst1 = lst
    for value in lst1:
        if value == element:
            return True
    return False

# j = 0
# for i in lst:
#     if j % 2 == 0:  # 去偶数的j的值
#         # print(i)
#         pass
#     j += 1
#     print("这是第 {} 次循环，其中打印的值为：{}".format(j, i))
#
# # for 循环中的range -- 迭代器，用于生成一个整数的序列
# r = range(10)  # 根据给到的一个数字，生成一个列表 -- 可迭代的对象
# print(list(r))
#
# print(list(range(len(lst))))  # [0, 1, 2, 3, 4, 5]
def Loop_print_list(lst):
    """
    循环打印 list列表，输出循环次数及元素值
    :param lst:
    :return:
    """
    for i in list(range(len(lst))):
        # if i % 2 == 0:
        #     print(lst[i])
        print("这是第 {} 次循环，其中获取到的值是：{}".format(i + 1, lst[i]))

# for i in range(len([1,'a'])):
#     print(i)
#
# a = range(6)
# print(a)
# print(list(range(start=0, end=6)))  # 参数不存在，仅供理解
# print(list(range(0, 6)))
#
# print(list(range(10)))  # 取值的规则？  # 左闭右开， 如果不给初始值，默认从0开始
# print(list(range(4, 10)))
# for i in range(1,10,3):
#     print(i)
#
# for i in "qiyelaoshi":
#     print(i)
#
# for i in range(1, 10):
#     print(i)
#
# for i in range(10):
#     print(i)
#
# """
# 双重循环
# """
# k = 0
# for i in range(1, 10):  # i = [1-9]
#     for j in range(1, 10):
#         k += 1
#
# print(k)  # 81
#
def Multiplication_table():
    """
    # 99乘法表
    # 1 * 1 = 1
    # 1 * 2 = 2, 2 * 2 = 4
    # 1 * 3 = 3, 2 * 3 = 6, 3 * 3 = 9
    # ...
    # 1 * 9 = 9, 2 * 9 = 18, 3 * 9 = 27 ...
    :return:
    """
# print("{} * {} = {}".format(1, 2, 1 * 2))
# 定义变量 i  从1到9进行自动变化
# 定义变量 j  从1到9进行自动变化
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{} * {} = {}".format(j, i, i * j), end="   ")  # print自带换行
        print()  # 起到换行的作用

def login():
    """
    用户名密码登录校验，如果输入错误超过三次，则锁定退出
    :return:
    """
    # err=0
    for i in range(3):
        username=input("请输入用户名：")
        password=input("请输入密码：")
        if username=="admin" and password=='123456':
            print("登录成功")
            break
        print("用户名或密码错误，请重新输入")
            # err += 1
    # if err==3:
    else:
        print("您的账户被锁定")

def dice_game():
    """
    掷骰子

    规则：共 2 个骰子 1～6 数
      1.玩游戏要有金币，无金币不能玩

      2.玩游戏每局赠金币 1 枚

      3.可充值获取金币，10 元的位数，20 个金币

      4.玩游戏消耗 5 个金币

      5.猜大小，超过 6 个则算大，小于等于 6 个则算小，猜对则鼓励 2 枚金币

      6.游戏结束：1.主动退出 2.无金币退出

      7.只要退出则打印金币数，共玩了几局
    :return:
    """
    #金币数
    coins=0
    #游戏次数
    count=0
    if coins<5:
        #提示充值
        print("金币不足请充值")
        while True:
            num=int(input("请充值：（输入10的倍数）"))
            if num%10==0:
                coins+=num//10*20
                print("充值成功")
                answer = input("是否开始游戏(y/n)? ")
                while coins>=5 and answer=='y':
                    print("~~~~~开启游戏之旅~~~~~~")
                    #每局赠送 1 个金币
                    coins+=1
                    #每局消耗 5 个金币
                    coins-=5
                    dice1=random.randint(1,6)
                    dice2=random.randint(1,6)
                    guess=input("请猜大小： ")
                    if (guess=='大' and (dice1+dice2)>6)or(guess=='小' and (dice1+dice2)<=6):
                        print("恭喜你猜对了，奖励 2 金币")
                        coins+=2
                    else:
                        print("猜错了")
                    count+=1
                    answer = input("是否继续游戏(y/n)? ")

                print("您的剩余金币：{},共玩了{}局".format(coins,count))
                break
            else:
                print("不是10的倍数，充值失败")
def print_triangle(number):
    """
    打印正三角图形*图，number为行数
    :param number:
    :return:
    """
    for i in range(number):
        for j in range(i+1):
            print('*', end='')
        print()
def print_Inverted_triangle(number):
    """
    打印number行倒三角*图
    :param number:
    :return:
    """
    for i in range(number,0,-1):
        for j in range(i):
            print('*', end='')
        print()

def print_rectangle_star(line,number):
    """
    打印 line行，每行显示 number的矩形*图形
    :param line:
    :param number:
    :return:
    """
    for i in range(line):
        for j in range(number):
            print('*',end='')
        print()


if __name__=='__main__':
    # simple_if()
    # lst = [1, "七夜", 3, "a", "b", 6]
    # word='七夜1'
    # result=test_find(word,lst)
    # print(result)
    # Loop_print_list(lst)
    # Multiplication_table()
    # login()
    # dice_game()
    # print_triangle(5)
    print_Inverted_triangle(4)
    # print_rectangle_star(3,4)