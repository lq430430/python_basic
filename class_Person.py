"""
类的定义
class 类名():
    属性（特征）
    函数（功能）
"""
class Person():
    name = "lily"
    age = 18
    sex = "woman"
    addr = "shenyang"

    def eat(self):
        print("吃东西")   #没写return 返回空
        # pass
        # return "吃东西"

    def order_food(self):
        print("我喜欢吃XXX菜")

    def person(self):
        print("self的真正身份：",self)


Xman = Person()  # 实例化
print(Xman.person())
print("Xman实例对象：",Xman)
print("Person类本身：",Person)
print(Person.person(Person()))
print(Xman.name)
# print(Xman.eat())
a=Xman.eat()
print(a)        #None

name=Xman.name
Xman.name="mary" #只影响实例的name
print(Xman.name)

print("修改之前的值：{},修改之后的值:{}".format(name, Xman.name))
print("这个对象中的name值:{}".format(Xman.name))

xiaoming = Person()
lily= Person()
print(xiaoming.name)
print(Person.name)

xiaoming.name="sunxiaoming"
Person.name="uuuuu"
print(xiaoming.name)
print(Person.name)
print(lily.name)

