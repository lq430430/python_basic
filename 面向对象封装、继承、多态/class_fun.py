"""
类的方法分为方法则有构造方法，实例方法，类方法，静态方法和属性方法5种
1. 构造方法：__init__,python自带，用作实例对象的初始化，在实例对象时默认调用此方法
2. 实例方法：跟普通方法基本一致，默认第一个参数为self，self 代表的是实例对象，且只能被实例对象
调用。
3. 类方法：由@classmethod来装饰的方法，默认第一个参数为cls，cls表示这个类本身，可以被类或类
的实例对象调用；
4. 静态方法：由@staticmethod装饰的方法,没有默认参数，可以被类或类的实例对象调用；
5. 属性方法：由@property装饰的方法，默认第一个参数为self，将方法当做属性来使用。

***@classmethod 和@staticmethod节省内存空间，不需要实例化，直接使用类名.方法
"""


class Girlfriend:
    age = 22
    sex = '女'

    def __init__(self, hair, bra):  # 初始化魔术方法
        self.hair = hair
        self.bra = bra
        print('初始化--------')

    # def __new__(cls, *args, **kwargs):  # 覆盖了默认的object的__new__ 方法,向内在要空间--》new
    #     print('实例化--------')
    #     position = object.__new__(cls)  # 申请内存空间：0x107aa1390
    #     print(position)
    #     return position

    def __call__(self, name):  # 对象调用魔术方法
        print('-------call')
        print('执行对象得到参数是：', name)

    # def __del__(self):  # 析构方法，执行所有方法后调用方法回收空间，一般不用自定义
    #     print('--------删除')

    def __str__(self): #打印对象的时候调用__str__
        return '头发是：' + self.hair + '----bra:' + self.bra

    def about_me(self):
        print('年芳{0}，性别{1}，身材{2}棒棒哒，一头{3}'.format(self.age, self.sex, self.size, self.hair))

    def run(self, name):  # 实例方法 可以定义非初始化的参数
        print('{}is run------'.format(name))
        self.about_me()

    @staticmethod
    def bio():
        print('全心全意为主人服务!')
        print('静态方法能够访问类属性：', Girlfriend.age)
        print('静态方法能够访问类方法：', Girlfriend.cls_name())
        # print('静态方法能够访问对象方法：',Girlfriend.about_me()) #静态方法不能访问对象方法

    @classmethod
    def cls_name(cls):  # 返回值 None
        print('当前使用模具是{0}'.format(cls.__name__))
        print('age:', Girlfriend.age)
        print(cls)

    @property
    def size(self):
        return self.bra

    @size.setter
    def size(self, size):
        self.bra = size
        print('丰胸手术完成！')


lulu = Girlfriend("黑长直", 'c')  # 先调用__new__申请内在空间，创建对象空间，再调用__init__对象进行初始化
# lulu('lulu')  # 将对象当成函数使用时调用call
# lulu.about_me()
print(lulu)  #打印对象的时候调用__str__，打印更多对象的信息
# lulu.bio()
# lulu.cls_name()
# print(Girlfriend.cls_name()) #类方法直接用类名调用，节省空间
# print(Girlfriend.bio()) #静态方法直接用类名调用，节省空间
# print(Girlfriend.bra) #类不能使用实例属性

# print("lulu的size：",lulu.size)
# lulu.size='E'
# print("修改后lulu的size：",lulu.size)
