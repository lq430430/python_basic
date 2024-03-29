
"""
实例属性：实例对象的属性
        定义在构造方法中的属性
        公有实例属性：常规属性
        私有实例属性：双下划线开头，只能在自己类中调用

语法：实例名.属性名
类的内部使用：self.属性名   self -- 就是当前对象
私有实例属性：self.__属性名
"""


class Person():

    def __init__(self, name, age, sex, job):
        self.name = name
        self.age = age
        self.__sex = sex
        self.__job = job

    def eat(self):
        print("{} -- 爱吃".format(self.name))

    def work(self):
        print("{} -- 工作： {}".format(self.name, self.__job))

    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job


xiaoming = Person("小明", 88, "women", "teacher")   #私有属性_Person__sex="women"  而不是实例xiaoming.__sex
qiye = Person("七夜", 18, "man", "teacher")

print(Person("小丽", 88, "women", "teacher").name)
print(xiaoming.work())

xiaoming.family='liaoning'
print('xiaoming.family:',xiaoming.family)

# print(xiaoming.__sex)  #AttributeError: 'Person' object has no attribute '__sex'
xiaoming.set_job("worker")
job=xiaoming.get_job()
print(job)