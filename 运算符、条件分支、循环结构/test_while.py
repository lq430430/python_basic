# -*- coding: utf-8 -*-

# @Time    : 2024/1/27 22:56
# @Author  : lily
# @File    : test_while.py
"""
while循环及应用，练习题
"""
import random
def iter_print(start,end):
    """
    while基础用法:循环打印 start~end的数字
    :return:
    """
    # 初始值
    n = start
    # 结束条件
    while n <= end:
        print(n)
        # 变量要有变化
        n += 1

def mod3(start,end):
    """
    练习
    1.打印 start~end之间能被3整除的数字
    :return:
    """
    num = start
    while num <= end:
        if num % 3 == 0:
            print(num)
        num += 1
def sum(start,end):
    """
    打印 start~end之间数字的累加和,并返回总和
    :param start:
    :param end:
    :return:sum
    """
    n = start
    sum = 0
    while n <= end:
        sum += n
        n += 1
    print("sum={}".format(sum))
    return sum
def market_count():
    """
    超市购物
    有价格和数量，可选择多项，计算所有商品的总额,商品总数量
    :return:
    """
    total = 0
    numbers = 0
    while True:
        price = float(input("请输入价格："))
        number = int(input("请输入数量："))
        # 金额累加
        total += price * number
        # 数量累加
        numbers += number
        #判断是否退出
        answer = input("当前商品总额：{},是否继续添加其他商品(退出请按'q'):".format(price * number))
        if answer == 'q':
            break
    print("商品总数量：{},商品总额：{},".format(numbers, total))

def guess_number():
    """
    猜数字游戏
    生成随机数，可以猜多次，直到猜对为止，猜错时需要给出错误提示
    (1)统计猜了几次
    (2)猜中时 如果 1 次，提示 1，如果 2-5次，提示 2，否则提示 3
    :return:
    """
    ran = random.randint(1,10)
    num1=1
    while True:
        guess = int(input("请猜拳输入1～10的任意数字："))
        if guess == ran:
            if num1==1:
                print("恭喜你猜对了,运气爆棚，快去买彩票")
            elif num1>2 and num1<6:
                print("恭喜你猜对了,运气不错")
            else:
                print("恭喜你猜对了")
            break
        elif guess > ran:
            print("大了")
        elif guess < ran:
            print("小了")
        else:
            print("输入格式不正确，请输入数字！")
    num1+=1

def guessing_game():
    """
    猜拳游戏
    共 3 局，石头（0）剪刀（1）布（2），三局两胜制
    :return:
    """
    n=0 #次数
    person_num=0 #人猜对次数
    machine_num=0 #机器猜对次数
    while n<3:
        machine=random.randint(0,2)
        guess=int(input("请猜拳：石头（0）剪刀（1）布（2）"))
        #每轮判断输赢
        if (guess==0 and machine==1)or(guess==1 and machine==2)or(guess==2 and machine==0):
            print("本局赢了")
            person_num+=1
        elif (guess==0 and machine==2)or(guess==1 and machine==0)or(guess==2 and machine==1):
            print("本局输了")
            machine_num+=1
        else:
            print("平局")
        n += 1
    #判断人机赢的次数
    if person_num>machine_num:
        print("三局两胜，恭喜你获胜")
    else:
        print("输了，再见")

def print_trigle_star(number):
    n=1
    while n<=number:
        print('*'*n)
        n+=1


if __name__=='__main__':
    # iter_print(1,5)
    # mod3(1,10)
    # sum(1,10)
    # market_count()
    # guess_number()
    # guessing_game()
    print_trigle_star(5)

