# coding:utf-8
"""dictionary 字典操作"""

# 删除字典
d4 = {'class': 'v211', 'teacher': ['muzi', 'aa'], 'vip': {1: '张三', 2: '李四'}, 'sub': ('python'), 'des': 'hahaha'}
print("原字典为：", d4)

d4.pop('teacher')
print("pop删除后字典为：", d4)

# popitem()删除最后一个键值对
d4.popitem()
print("popitem删除后字典为：", d4)

del d4['class']
print("del删除后字典为：", d4)
# 清空
d4.clear()
print("clear删除后字典为：", d4)

# 删除字典
del d4
# print("del删除字典为：", d4)  #d4已删除，需要重新定义

# 字典转成List
dict1 = {"name": "mary", "age": 22}
print(list(dict1.items()))
print(list(dict1.values()))
print(list(dict1.keys()))

d4 = {'class': 'v211',
      'teacher': ['muzi', 'aa'],
      'vip': {1: '张三', 2: '李四'},
      'sub': ('python'),
      'des': 'hahaha'}
print("原字典为：", d4)

# 嵌套修改
d4['teacher'][1] = "bbb"
print("嵌套修改后字典为：", d4)

# 嵌套增加
d4['des'] = [{"name": "mary", "age": 12}, {"name": "sunny", "age": 34}]  # 如果key值重复则覆盖
print("嵌套修改后字典为：", d4)

# 嵌套删除
d4['teacher'] = ['muzi']
print("嵌套删除后字典为：", d4)

d4['teacher'] = ['muzi', 'aaa']
d4['teacher'].remove('muzi')
print("嵌套删除后字典为：", d4)

# 字典常用方法
"""
• 字典名.items()：返回可遍历的（键，值）元组数组
• 字典名.keys()：返回一个字典所有的键，返回一个迭代器，可以使用 list() 来转换为列表
• 字典名.values()：返回一个字典所有的值，返回一个迭代器，可以使用 list() 来转换为列表
"""
print("输出所有字典的键值对:", d4.items())
print("输出所有字典的key:", d4.keys())
print("输出所有字典的value:", d4.values())

# 获取值class的值，如果没有class，则给定默认值vip_211
res=d4.get('class1', "vip_211")
print(res)

"""
其他类型转型为字典
---数字-》字典    不支持
---字符串-》字典  不支持
---元组-》字典    支持
---列表-》字典    支持
"""
# num1=101
str1=(('name','小明'),('age',12))
list1=[['name','小明'],['age',99]]
dic1=dict(str1)
dic2=dict(list1)
print(dic1,'\n',dic2)

