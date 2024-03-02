# -*- coding: utf-8 -*-

# @Time    : 2024/2/25 01:37
# @Author  : lily
# @File    : test_lambda.py
"""
匿名函数使用场景/高阶函数
"""
from functools import reduce

sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print('value of total:%d' % sum(10, 20))


# 匿名函数组合使用场景
def func1(a, func):
    print('+++++++>', a)
    r = func(a)
    print('========>', r)


func1(8, lambda x: x ** 2)


# 高阶函数：函数做为另一个函数的参数
def test(age, action):
    if age < 18:
        print('您还没满十八岁，请退出')
    action()  # 把参数action直接当做一个函数来调用


def smoke():
    print('我已经年满十八岁了，我想抽烟')


my_action = smoke  # 定义一个变量my_action，让它指向smoke函数
test(20, my_action)  # 将my_action传给test函数做为它的参数

m=max([2,3,4,35,34,])
print(m)

list1=[('tom',19),('tony',20),('rose',26)]
m=max(list1,key=lambda x:x[1]) #key=func,x[1]取的是（，值）
print(m)

s=sorted(list1,key=lambda x:x[1],reverse=True)
print(s)

#filter(function or None, iterable) ，filter要求匿名函数返回值必须是bool类型，只有结果为True的都是符合过滤条件的
result=filter(lambda x:x[1] >20,list1)  #filter返回值是迭代器，使用list进行转换
print(list(result))

#map() 提取/映射数据
list1=[('tom',19),('tony',20),('rose',26)]
result=map(lambda x:x[0].title(),list1)  #map返回值是迭代器，使用list进行转换
print(list(result))

#reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates((((1+2)+3)+4)+5)
r=reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(r)

#zip()
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 返回一个对象
print(zipped)  #<zip object at 0x1049e1600>
print(list(zipped) ) # list() 转换为列表 [(1, 4), (2, 5), (3, 6)]

print(list(zip(a,c)) )             # 元素个数与最短的列表一致,[(1, 4), (2, 5), (3, 6)]

a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
print(list(a1)) #[1, 2, 3]
print(list(a2)) #[4, 5, 6]
