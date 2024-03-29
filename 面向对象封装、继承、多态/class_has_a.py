# -*- coding: utf-8 -*-

# @Time    : 2024/3/11 20:30
# @Author  : lily
# @File    : class_has_a.py
"""
继承 ：is a,has a
"""

"""
练习题1：has a举例
公路(Road):
     属性：公路名称，公路长度
  车(Car)：
    属性：车名，时速
       方法：1.求车名在那条公路上以多少的时速行驶了多长时间
      get_time(self,road)
      2.初化车属性信息__init__方法
      3.打印对象显示车的属性信息
"""
class Road():
    # roadname='京沈高速'
    # length=1000
    def __init__(self,roadname,length):
        self.roadname=roadname
        self.length=length
class Car():
    def __init__(self,carname,speed):
        self.carname = carname
        self.speed = speed
    def get_time(self,road):#road=r 接收的是对象，指向同一个地址空间
        return '{} 在{} 公路上以 {}km/时速 行驶了 {}km'.format(self.carname,road.roadname,self.speed,road.length)

    def __str__(self): #打印对象时自动调用
        return '{}品牌的速度：{}km/时'.format(self.carname,self.speed)

r=Road('京沈高速','12000')
r.roadname='京藏高速' #改变对象属性
p=Car('奔驰','10')
print(p.get_time(r)) #传的r是对象
print(p)