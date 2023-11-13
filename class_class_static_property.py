"""
classmethod可以设置修改类属性；也可以实例化对象；
staticmethod无法访问类或对象的数据，所以可把它当作一个辅助功能方法用，里面包含一些与该类有关的逻辑代码。比如validate(*args)
"""

"""
需求：

从本地文件中(txt, csv, json等等)读取数据，生成一个对象。
比如，本地有一个data.json文件，里面包含了每个学生的姓名及对应的考试成绩。现在要求读取该数据，生成一个class对象。

思路：

__init__方法中，清晰的声明对象的属性
用一个classmethod：load_json，专门用于读取data_file，获取数据，实例化对象
用一个staticmethod：validate，来对要初始化数据进行有效性检查

"""


class Class:
    def __init__(self, names, grades):
        self._names = names
        self._grades = grades

    @classmethod
    def load_json(cls, data_file):
        # 读取数据,获得names,grades
        cls.validate(names, grades)
        return cls(names, grades)

    @staticmethod
    def validate(names, grades):
        # 检查数据有效性
        pass
