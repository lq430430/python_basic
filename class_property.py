"""
对象的封装
封装原则：
• 将不需要对外提供的内容都隐藏起来；
• 把属性都隐藏，提供公共方法对其访问。
"""


class Account():
    def __init__(self, account, name, money):
        self.__account = account
        self.__name = name
        self.__money = money
        print("欢迎来到银行，您的卡号：{}，姓名：{}，余额：{}".format(self.__account, self.__name, self.__money))

    # 方式一：访问接口一般是由set()/get()方法来表示，get()方法是提供接口的访问通道，而set()方法是提供接口的修改通道。
    def get_money(self):
        # 查询余额
        return self.__money

    def set_money(self, money):
        self.__money += money

    @property
    def money(self):
        return self.__money  # 查询余额

    @money.setter
    def money(self, money):
        self.__money += money

"""
方式二 @property
用@property装饰器装饰的方法，就相当于把方法被变成了类中的一个属性，属性名即方法名，属性命名不可以重复。
使用和赋值就跟类中属性的操作一致。
1. 在get方法加上@property，方法名与私有属性名一致
2. 在set方法上方加上@xxx.setter，方法名与私有属性名一致，其中xxx与方法名一致
"""

# 方法一
ff = Account("10001","芳芳",800)
print("余额是：{}".format(ff.get_money()))
ff.set_money(90)
print("修改后余额是：{}".format(ff.get_money()))

#方法二
xm = Account("10002","晓明",666)
print("余额是：{}".format(xm.money))
xm.money=-66
print("修改后余额是：{}".format(xm.money))


