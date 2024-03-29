# -*- coding: utf-8 -*-

# @Time    : 2024/3/11 21:25
# @Author  : lily
# @File    : class_inherit_isa.py
"""
继承  is a
"""
class Person:  #基础类中的name和age，其他子类有相同属性时可直接继承基础类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name+'正在吃饭。。。。')
class Student(Person):
    def __init__(self,name,age,clazz): #重写
        super().__init__(name,age)
        self.clazz = clazz
    def eat(self,food): #重写
        super().eat()
        print('吃的是：'+food)

    # def eat(self):
    #     print(self.name+'正在吃饭。。。。吃的是：')
class Employee(Person):
    def __init__(self,name,age,employer,salary): #报阴影
        # 如何调用父类__init__
        super().__init__(name,age)
        self.employer = employer
        self.salary = salary

class Doctor(Person):
    def __init__(self,name,age,patients):
        super(Doctor,self).__init__(name,age) #super(type, obj) -> bound super object; requires isinstance(obj, type)
        self.patients=patients


s=Student('jim',18,'一班')
e=Employee('tom',23,'employer','1000')
lists=['张三','丽萨','李明']
d=Doctor('mary',22,lists)
s.eat('面条')
e.eat()
d.eat()