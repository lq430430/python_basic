# -*- coding: utf-8 -*-

# @Time    : 2024/3/29 17:10
# @Author  : lily
# @File    : class_mutiform.py
"""
多态应用
多态是指同一个方法可以在不同的对象上产生不同的行为。
通过多态性，我们可以使用父类的引用来调用子类对象的方法。这使得我们可以轻松地扩展系统，添加新类型的商品，而无需修改现有的代码。

例：假设我们正在开发一个电子商务网站，我们需要计算不同商品的价格（包括折扣）。
    有些商品具有固定的折扣，而其他商品可能有不同的折扣方式。我们可以使用多态来解决这个问题。
"""


class Product:  #定义父类 Product，包含商品的基本信息和计算价格的方法：
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def calculate_price(self):
        return self.price

class DiscountedProduct(Product): #固定折扣商品
    def __init__(self,name,price,discount):
        super().__init__(name,price)
        self.discount=discount

    def calculate_price(self): #DiscountedProduct类通过固定的折扣方式计算价格
        discounted_price=self.price-(self.price*self.discount) #折扣价=原价-（原价*折扣率）
        return discounted_price
class FlexibleProduct(Product): #灵活折扣商品 允许使用自定义的折扣函数来计算价格。
    def __init__(self,name,price,discount_function):
        super().__init__(name,price)
        self.discount_function=discount_function

    def calculate_price(self): #允许使用自定义的折扣函数来计算价格。
        discount_price=self.discount_function(self.price)
        return discount_price

#自定义折扣方法
def custom_discount(price):
    return price-100

product1=DiscountedProduct('化妆品',1500,0.2)
product2=FlexibleProduct('switch',1500,custom_discount)

print('{}的价格：{}'.format(product1.name,product1.calculate_price()))
print('{}的价格：{}'.format(product2.name,product2.calculate_price()))