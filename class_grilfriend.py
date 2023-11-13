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

    def __init__(self, hair):
        self.hair = hair
        self.bra = 'C'

    def about_me(self):
        print('年芳{0}，性别{1}，身材{2}棒棒哒，一头{3}'.format(self.age, self.sex, self.size, self.hair))

    @staticmethod
    def bio():
        print('全心全意为主人服务!')

    @classmethod
    def cls_name(cls):
        print('当前使用模具是{0}'.format(cls.__name__))

    @property
    def size(self):
        return self.bra

    @size.setter
    def size(self, size):
        self.bra = size
        print('丰胸手术完成！')

lulu=Girlfriend("黑长直")
lulu.about_me()
lulu.bio()
lulu.cls_name()
print("lulu的size：",lulu.size)
lulu.size='E'
print("修改后lulu的size：",lulu.size)
