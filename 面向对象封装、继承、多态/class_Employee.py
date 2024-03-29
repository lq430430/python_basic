# -*- coding: utf-8 -*-

# @Time    : 2024/3/12 00:27
# @Author  : lily
# @File    : class_Employee.py
"""
编写一个简单的工资管理程序
系统可以管理以下四类人：工人worker、销售员salesman、经理manager、销售经理salemanager
所有员工都具有员工号、姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
1）工人：工人具有工作小时数和时薪的属性，工资计算方法：工作小时数*时薪
2）销售员：具有销售额和提成比例的属性，工资计算方法：销售额*提成比例
3）经理：具有固定月薪的属性，工资计算方法：固定月薪
4）销售经理：工资计算方法：销售额*提成比例+固定月薪
请根据以上要求设计合理的类，完成以下功能：
1）添加所有类型的人员
2）计算月薪
3）显示所有人的工资情况信息
"""


class Employee():
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def set_name(self, name):
        self.name = name

    def get_salary(self):
        return self.salary

    def __str__(self):
        msg = "员工号：{},姓名:{},本月工资：{}".format(self.id, self.name, self.salary)
        return msg


class Worker(Employee):
    def __init__(self, id, name, salary, hours, per_salary):
        super().__init__(id, name, salary)
        self.hours = hours
        self.per_salary = per_salary

    def get_salary(self):
        money = self.hours * self.per_salary
        self.salary+=money
        return self.salary
class Salesman(Employee):
    def __init__(self, id, name, salary, salemoney, percent):
        super().__init__(id, name, salary)
        self.salemoney = salemoney
        self.percent = percent
    def get_salary(self):
        money = self.salemoney * self.percent
        self.salary += money
        return self.salary

class Manager(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)

w=Worker('0001','jack',2000,80,20)
print('{}的基本工资：{}'.format(w.name,w.salary))
money=w.get_salary()
print(w)

s=Salesman('0002','luck',3000,200,80)
print('{}的基本工资：{}'.format(s.name,s.salary))
money=s.get_salary()
print(s)

m=Manager('0003','bai',5000)
print('{}的基本工资：{}'.format(m.name,m.salary))
money=m.get_salary()
print(m)