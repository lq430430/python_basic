# -*- coding: utf-8 -*-

# @Time    : 2024/4/5 19:34
# @Author  : lily
# @File    : random_modules.py
"""
random模块
"""
import random

ran = random.random()  # 0～1之间的随机小数
print('ran=', ran)

randrange=random.randrange(1,10)  #[1,10) 包含1，不包含10
print('randrange=', randrange)

ranint=random.randint(1,10)  #[1,10]  包含1，10
print('ranint=', ranint)

#随机选择自定义的数据choice
list1=['李岩','水怪','大耀姐']
choice_item=random.choice(list1)
print('choice_item:',choice_item)

#打乱洗牌random.shuffle
list1=['李岩','水怪','大耀姐']
result=random.shuffle(list1)
print(list1)

#生成随机验证码 大小写字母与数字组合
def random_code():
    code=''
    for i in range(4):
        ran1=random.randint(0,9)
        ran2=chr(random.randint(65,90) ) #大写字母,chr将十进制转成对应的 ASCII 字符
        ran3=chr(random.randint(97,122) ) #小写字母,chr将十进制转成对应的 ASCII 字符

        ran=random.choice([ran1,ran2,ran3]) #从三种随机字符中选出一个数，添加到code中
        code+=str(ran)
    return code
print('验证码：',random_code())

#chr ord
print(chr(65)) #Unicode码 ---》str
print(ord('A')) # str ---》Unicode码
print(ord('上')) #中文 对应的Unicode码