# -*- coding: utf-8 -*-

# @Time    : 2024/2/9 12:44
# @Author  : lily
# @File    : test_tuple.py
"""
元组的使用：元组tuple使用（），元素不能修改
"""
def  define_tuple():
    '''
    元组定义，常见错误
    注意事项：元组中只有一个元素，必须加逗号（'aa',)
    :return:
    '''
    t1=()
    print("{}的类型{}".format(t1,type(t1)))

    t2=('aa')
    print("{}的类型{}".format(t2,type(t2)))

    t3=('aa',)
    print("{}的类型{}".format(t3,type(t3)))

    t4=('a','b','c')
    print("{}的切片t4[0:]:{}".format(t4,t4[0:]))
    print("{}的切片t4[::-1]:{}".format(t4,t4[::-1]))

def tuple_fun():
    t1 = ('a', 'b', 'c','a')
    #tuple.count()统计元素个数
    print("{}的个数：{}".format('a',t1.count('a')))

    #index根据元素获取下标位置
    print("{}的下标位置：{}".format('a',t1.index('a')))
    #注意index（x,1,3)指定查找的位置，末位长度需要大于len+1，否则报错
    # print("{}的下标位置：{}".format('a',t1.index('a',1,3))) #报错
    print("{}的下标位置：{}".format('a',t1.index('a',1,4)))

    #in，not in
    print("{}在元组里{}吗？:{}".format('a',t1,('a'in t1)))
    print("{}在元组里{}吗？:{}".format('e',t1,('e'in t1)))


if __name__=='__main__':
    #元组定义
    # define_tuple()

    #元组常用方法
    tuple_fun()