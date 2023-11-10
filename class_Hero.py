"""
王者游戏 -- 英雄为单位的话？ 100-200? 每一个英雄都具备自己的技能和属性

封装  --  继承 --  多态
"""
import time

class Hero(object):  # 类 -- 留在实例化的时候，具体去生成不同的英雄
    name = "任意名字"
    desc_01 = "英雄技能_01"
    desc_02 = "英雄技能_02"
    desc_03 = "英雄技能_03"
    hero_type = "英雄属性"

    # 构造方法 -- 类中的内置方法 -- 个性化
    # 实例化的时候，一定会先去执行的函数__init__
    def __init__(self, name, desc_01, desc_02, desc_03, hero_type):  # 在类中的self表示什么意思？ -- 当前对象
        self.name = name
        self.desc_01 = desc_01
        self.desc_02 = desc_02
        self.desc_03 = desc_03
        self.hero_type = hero_type

    def flat_a(self):
        print("{} -- 使用了平A".format(self.name))

    def skill_01(self):
        print("{} -- 使用了 -- {}".format(self.name, self.desc_01))

    def skill_02(self):
        print("{} -- 使用了 -- {}".format(self.name, self.desc_02))

    def skill_03(self):
        print("{} -- 使用了 -- {}".format(self.name, self.desc_03))

    def return_city(self):
        print("{} -- 进行了回城操作".format(self.name))

# Dian_Wei = Hero()
"""
实例化时自动调用 __init__()，缺少入参
TypeError: __init__() missing 5 required positional arguments: 'name', 'desc_01', 'desc_02', 'desc_03', and 'hero_type'
"""
Anqila=Hero("安琪拉","火球术","混沌火种","炽热光辉","法师")
Dian_Wei = Hero("典韦", "发疯", "加速", "踩一脚", "力量")
Kai = Hero("凯", "飞刀", "砍一刀", "变身", "力量")

print("第一回合：")
Anqila.skill_01()
Dian_Wei.skill_01()
time.sleep(3)
print("第二回合：")
Anqila.flat_a()
Kai.flat_a()
time.sleep(3)
print("回城：")

Anqila.return_city()
Dian_Wei.return_city()
Kai.return_city()