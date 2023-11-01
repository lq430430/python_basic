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
d4['teacher']=['muzi']
print("嵌套删除后字典为：", d4)

d4['teacher']=['muzi','aaa']
d4['teacher'].
