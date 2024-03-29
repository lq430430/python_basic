"""
类的定义
class 类名():
    属性（特征）
    函数（功能）
"""
class Person():
    name = "lily"
    age = 18

    def eat(self):
        print("吃东西")   #没写return 返回空
        # pass
        # return "吃东西"

    def order_food(self):
        print("我喜欢吃XXX菜")

    def person(self):
        print("self的真正身份：",self)

Xman = Person()  # 实例化
print("Xman实例对象：",Xman)
print("Person类本身：",Person)
print(Xman.person()) #调用实例方法后，打印方法返回值None（无返回值时）
print('Person():',Person()) #实例对象
print(Person.person(Person())) #只要类加()，即实例化，传入了创建的对象Person()

a=Xman.eat()
print(a)        #None

name=Xman.name
Xman.name="mary" #只影响实例的name
print("修改之前的值：{},修改之后的值:{}".format(name, Xman.name))
#
xiaoming = Person()
lily=Person()
xiaoming.name="sunxiaoming"
Person.name="uuuuu"
print(Person.name)
print(xiaoming.name)
print(lily.name)



