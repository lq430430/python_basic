# -*- coding: utf-8 -*-

# @Time    : 2024/2/24 19:19
# @Author  : lily
# @File    : test_decorator.py
"""
装饰器
"""


def outer():
    a = 100
    def inner():
        b = 200
        # b += a  # 内部函数可以使用外部函数的变量
        nonlocal a  #nonlocal关键字用于指示一个变量是非局部的 ，未定义前不能使用
        a += b  # 报错：内部函数不可以直接修改外部函数的变量
        print('我是内部函数')
        print('a:',a)

    result = locals()  # locals()表示查看当前局部变量,以字典的形式返回
    print(result)
    inner()

def outter(n):
    """
    闭包：
        1.嵌套函数
        2.内部函数引用了外部函数的变量
        3.返回值是内部函数
    :return:
    """
    a=10
    def inner():
        b=a+n
        print('内部函数',b)
    return inner


def decorater1(func):  # 第一步，def decorater加载到内存，但不执行
    '''
    定义装饰器
    :param func:
    :return:
    '''
    print('~~~~~~~~~1')  # 第三步，执行decorater(house)
    def wrapper():  # 加载def wrapper
        func()
        print('刷漆')
        print('精装修房子')

    print('~~~~~~~~~~2')
    return wrapper  # 第四步 返回wrapper给house


@decorater1  # 第二步 @decorater =decorater(house) 并且加载def house
def house():  # 第五步： house=wrapper
    print('毛坯房....')

def decorater(func):
    '''
    定义带参数的装饰器，及带返回值
    :param func: 原函数
    :return:
    '''
    def wrapper(*args,**kwargs):
        #args是一个元组，kwargs是字典
        result=func(*args,**kwargs) #传给func时，*args,**kwargs进行拆包
        print('刷漆')
        print('精装修房子')
        return result

    return wrapper


@decorater
def hotel(name,address,area=40):
    print('酒店的名字是：{},酒店的地址在：{},是一个毛坯房，单间的建筑面积是：{}平米'.format(name,address,area))
    return 5000

def test(cal):
    def do_cal(*args,**kwargs):
        return cal(*args,**kwargs) #需要在这里写return语句，表示调用函数,获取函数的返回值并返回
    return do_cal
@test
def demo(a,b):
    return a+b

def outer_check(time):
    def check_time(action):
        def do_action():
            if time<22:
                return action()
            else:
                return '对不起，您不具有该权限'
        return do_action
    return check_time
@outer_check(23)
def play_game():
    return '玩儿游戏'
if __name__ == '__main__':
    # # 函数嵌套
    # outer()

    # #闭包
    # print(outter(9)) #返回的是inner 函数地址
    # #调用内部函数
    # outter(10)()

    # #装饰器
    # house()  # 第六步：house()=wrapper()
    #
    # #有参数的装饰器
    # hotel('如家酒店','王府井')

    # #有返回值的装饰器
    # r=hotel('如家酒店', '王府井')
    # print('总价格：{}'.format(r))
    # print(demo(1, 2))

    #装饰器带参数
    print(play_game())