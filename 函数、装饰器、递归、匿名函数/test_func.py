# -*- coding: utf-8 -*-

# @Time    : 2024/2/18 14:20
# @Author  : lily
# @File    : test_func.py
"""
函数定义及调用、返回值、参数、注释、嵌套、内置函数、匿名函数
格式：
def 函数名([参数,....]):
    代码
"""
import random
import sys


def generate_code(n=6):
    '''
    练习题：生成n位验证码,无参数时，默认n=6，有n时则传n
    :return:
    '''
    #验证码取值
    s='asdfghjklqwertyuiopzxcvbnm1234567890'
    #random.choices[集群,k=2] 从集群中随机选取k次数据，返回列表
    list1=random.choices(s,k=n)
    code=''.join(list1)#‘’.join(list) 将列表中元素通过''拼接成字符串
    return code

def get_sum(a,b,c=1):
    #判断是否是某类型：isinstance(变量，类型）--》返回bool
    if (isinstance(a,int) and isinstance(b,int)and isinstance(c,int) ) or (isinstance(a,str) and isinstance(b,str) and isinstance(c,str)):
        sum=a+b+c
        print(sum)
    else:
        print('类型不一致')
def borrow_book(bookname,username,number=1,school='library'):
    print('进入{}借书系统'.format(school))
    print('{}要借阅的书名是：{}，借阅数量：{}'.format(username,bookname,number))

def add_book(bookname):
    library.append(bookname)
    print('图书添加成功')
def show_book(books): #形参如果接收是列表，则与实参指向同一个内存地指
    for book in books:
        print(book)
def show_book(**kwargs): #**kwargs装包成字典{参数}
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)
def show_book(*args,**kwargs):
    print(args)
    print(kwargs)
def remove_from_list(library,element):
    """
    删除列表元素，注意删除元素时，下标不变，否则相邻元素漏删
    :param library: 图书馆
    :param element: 书籍名称
    :return: library
    """
    n=0
    while n<len(library):
        if library[n]==element:
            library.remove(element)
        else:
            n+=1
    return library

def get_sum(*args):
    '''
    *args 可变参数，传入时转换成元组
    :param args:
    :return:
    '''
    sum=0
    for i in args:
        sum+=i
    return sum
def get_minmax(list):
    '''
    练习题：使用冒泡法获取最大最小值，并返回最大最小值的元组
    :param list:
    :return: (min,max)
    '''
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]: #判断当前值大于下一个值，则替换
                temp=list[j]
                list[j]=list[j+1]
                list[j + 1]=temp
    min=list[0]
    max=list[-1]
    return min,max
def test_local1():
    name='jim' #name，局部变量，函数内部定义的变量
    print('test_local1中的name:',name)
def test_local2():
    global name #在函数内部使用或修改全局变量需要加global，并且变量是不可变时
    print('test_local2中的global name:', name)
    name='xiaoming'
    age=20
    print('test_local2修改后的global name:', name)

    list1.append(888) #传入全局变量，是可变变量时，不需要加global

def ref_fun():
    """
    引用及函数参数引用
    :return:
    """
    a = 999
    b = a
    c = a
    list1 = [23, 4, 22]
    list2 = list1
    list3 = list1
    # 获取引用数量
    print(sys.getrefcount(c)) #常量引用的数量不定
    print(sys.getrefcount(list3)) #调用sys.getrefcount时也指向了内存地址，所以引用数量+1
    del list1 #删除变量及引用x
    print(sys.getrefcount(list3))
def test1(b):
    '''
    传不可变，则b做为局部变量，传可变变量，则改变其变量本身
    :param b: 变量b一定是一个局部变量，查看传入的是可变还是不可变的变量
    :return:
    '''
    b+=b
    print(b)
if __name__=='__main__':
    #无参数---生成4位验证码函数
    # print(generate_code) #无（）时,打印方法的内存地址
    # code=generate_code() #()调用方法、函数
    # print('验证码： ',code)
    #
    # #有参数---生成n位验证码函数
    # code=generate_code(4) #()调用方法、函数
    # print('验证码： ', code)
    #
    # #多参数函数
    # get_sum(2,3)
    # get_sum('hello','kitty')
    # get_sum(22,'aaa')
    # get_sum(1, 2, 8)

    # #关键字参数
    # borrow_book('狂人日记','小芳')
    # borrow_book('西游记','阿龙',5)
    # borrow_book('草房子', '阿工',school='北大校区')# school为关键字参数

    # #参数是list列表
    # library=['python精通','java语言','java语言','Mysql']
    # add_book('数据结构')
    # show_book(library) #调用时，参数传递列表
    # remove_from_list(library,'java语言')
    # show_book(library)

    # #可变参数*args，元组
    # print(get_sum(1,2))
    # print(get_sum(1,2,3,4,5)) #装包：传递多个参数时，定义函数时加*叫装包,args=(1,2,3,4,5)
    # ran_list=[23,45,22,66,33,2,6,7]
    # # print(get_sum(ran_list)) #报错：传递单个参数时,args=(ran_list,)=([23, 45, 22, 66, 33, 2, 6, 7],)
    # print(get_sum(*ran_list)) #拆包：调用时将参数加* 用作拆包

    # #可变参数**kwargs,字典
    # show_book(bookname='西游记',author='吴承恩',number=5) #传递多个key=value的参数
    # book={'bookname':'红楼梦','author':'曹雪芹','number':5}
    # show_book(**book) #调用函数时，**将book拆包传递
    #
    # #可变参数组合*args,**kwargs
    # book = {'bookname': '红楼梦', 'author': '曹雪芹', 'number': 5}
    # show_book('小明','小芳',**book)

    # #返回值为多个时，返回元组
    # list1=[23,5,6,2,34,25,334,99,1,10]
    # #获取最大最小值
    # min,max=get_minmax(list1)
    # print('min:{},max:{}'.format(min,max))

    # #局部变量和全局变量
    # name='susan' #不可变，全局变量
    # age=18
    # test_local1()
    # print('全局变量name:',name)
    #
    # #传参：可变和不可变类型
    # list1=[2,3,4,5] #可变，全局变量
    # print('list1:', list1)
    # test_local2()
    # print('全局变量name:', name)
    # print('list1:',list1)
    # print('name: {},age: {} ,list1: {}'.format(name, age, list1) )

    #引用及函数参数引用
    ref_fun()
    a=100
    test1(a) #调用函数传入不可变变量，
    print('a:',a) #a仍是全局变量不变
    c=[100,200]
    test1(c) #传入可变变量
    print('c: ',c) #全局变量已改变

