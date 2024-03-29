"""
类的属性有类属性，成员属性（实例属性），内置属性三种。
1. 类属性：是定义在类中且在方法外面的变量，相当于类中全局变量。有公有和私有两种，私有类属性是
以两个下划线开头的。
2. 成员属性（实例属性）：也叫对象属性，是定义在构造方法里面的变量。该属性也有公有和私有两种。
3. 内置属性：python自定义的一些属性，通过调用来获取对应类的相关属性信息。常见的有：
• [类名].__dict__:打印类的所有属性与方法(包括继承自基类的属性和方法)（包括内置属性和方法）
• [对象].__dict__:打印对象的所有属性（私有和公有）

"""


class Demo(object):
    # 类属性：是定义在类中且在方法外面的变量，相当于类中全局变量。
    var = "demo"  # 类属性，公有
    __num = 100  # 类属性，私有

    def __init__(self, name="lily", age=19):
        self.name = name  # 实例属性，公有
        self.__age = age  # 实例属性，私有

    # 类属性调用
    def fun1(self):
        print("本类中定义的公有类属性：var =", Demo.var)
        print("本类中定义的私有类属性：__num=", Demo.__num)

    def fun2(self):
        Demo.var = "已修改"
        Demo.__num = 1314
        print("修改后的公有类属性：var =", Demo.var)
        print("修改后的私有类属性：__num:", Demo.__num)

    def fun3(self):
        self.name = "John"
        self.__age = 66
        print("修改后的公有实例属性：name =", self.name)
        print("修改后的私有实例属性：__age:", self.__age)

    def fun4(self):
        print("类的内置属性，类名：", Demo.__name__)  # 内置属性，自带
        print("类的内置属性，类的所有属性：", Demo.__dict__)  # 内置属性，自带


d = Demo()
print(d)
print(d.name)
# print(Demo.name)#报错，类本身不能使用init中定义的实例属性
# print(d.age)  #报错，私有实例属性不能在类外面调用，AttributeError: 'Demo' object has no attribute 'age'
print('类公有属性：',Demo.var)
print('类公有属性：',Demo.__num) #报错,私有类属性不能在类外调用type object 'Demo' has no attribute '__num'
d.fun1()
d.var = "mm"
print("在类外修改类公有属性var:", d.var)
# print("在类外修改类私有属性__num:",d._num) #报错：AttributeError: 'Demo' object has no attribute '_num'
d.fun2()
d.name = "类外name"
print("在类外修改实例公有属性var:", d.name)
# print("在类外修改实例私有属性__age:",d.__age) #报错：AttributeError: 'Demo' object has no attribute '__age'
d.fun3()
d.fun4()
# print("在类外调用对象的内置属性:类名", d.__class__)
