# coding:utf-8

list1 = [1, 2, 3, 4, 5]

print("list1的长度： " + str(len(list1)))

# list取值
list2 = [1, 2, 3, 4, 5, {2, 34, 2}, [4, 5, 6]]
print("list2的长度： " + str(len(list2)))
print("list中元素： " + str(list2[5]))  # 返回set集合{2,34}
# print("list中元素： " + str(list2[5][0]))  # 报错，set没有下标

# list.reverse 数组倒序操作，无返回值
list1 = [1, 2, 3, 4, 5]

list1.reverse()
print(list1)
list2 = [1, 2, 3, 4, 5, 6]
print(list2.reverse())  # 返回 None,注意list.reverse无返回值

# list.append 添加元素
list3 = [44, 33, 22]
print("list3:" + str(list3))
print(list3.append(55))  # 返回 None
print(list3.append("str1"))  # 返回 None
print(list3.append(2.134))  # 返回 None
print(list3.append(True))  # 返回 None
print(list3.append([5, 6]))  # 返回 None
print("list3:" + str(list3))

# list.insert()
list3.insert(0, "student")

# list连接使用+ /list.extend()
print("list3:" + str(list3))
print("list2+list3= " + str(list2 + list3))
list3.extend(list2)
print("list3:" + str(list3))

list4 = {4, 5, 6}
list5 = (999, 888)
list3.extend(list4)
print("list3:" + str(list3))

list3.extend(list5)
print("list3:" + str(list3))

"""
list删除 pop() 删除最后一个值,pop(索引)删除指定值
"""
list1 = ["python", 1, 2, 34, 99, 0, "python", "xxx", 99234]
list1.pop()
print("list1:" + str(list1))
list1.pop(3)
print("list1:" + str(list1))

# list.remove(元素值)
list1.remove(1)
print("====list1:" + str(list1))
list1.remove("python")  # 如果有重复的，从左到右找到第一个删除
print("====list1:" + str(list1))

# list.clear()清空列表
list1.clear()
print("清空后list1:" + str(list1))

# del list[索引] 删除某个值
list1 = ["python", 1, 2, 34, 99, 0, "python", "xxx", 99234]
print("list1:" + str(list1))
del list1[0]
print("del操作后list1:" + str(list1))
del list1  # del 列表 删除整个列表，包含列表空间
# print("del操作后list1:" + str(list1)) # list1已删除，需要重新定


# list修改
list2 = ["python", 1, 2, 34, 99, 0, [5, 6], 2, 2, "python", 44, "python"]

list2[6][1] = 7
print("====list2:" + str(list2))

print("获取list2中value，例如”python“的索引值：" + str(list2.index("python")))
print("获取list2中包含2的总数" + str(list2.count("python")))

# list2[0] = "java"
# print("====list2:" + str(list2))


# 删除List2中所有的指定元素,例如删除所有'python'
del list2[list2.index("python")]
print("del第一次list2:" + str(list2))

list2.remove("python")
print("del第二次list2:" + str(list2))

del list2[list2.index("python")]
print("del第三次list2:" + str(list2))

list1 = []  # list 其中0，空值（空字符串、空列表、空数组、空字典、空集合等） === False
if list1:
    print("list1非空")
else:
    print("list1是个空列表")
"""
转换为列表：list() 必须可以被循环的元素才能转换为列表。
---数值类型-》列表  不支持 数值类型是个不可拆分的整体
---字符串-》列表    支持 
---元组-》列表      支持
"""
str1 = "soryy,my love"
print(list(str1))

tup1 = (4, 2, 3, 2)
print(list(tup1))

set1 = {22, 22, 33, 45}
print(list(set1))


"""
列表的切片：分割一个列表，只提取其中某一个片段出来
变量名[start:end:step]
start：从哪里开始
end：到哪里结束
step：步长，每隔几个元素，获取一次 -- 默认为1，并且可以省略
"""

lst3 = [100, 3.14, True, "七夜", [1, 2, 3, 4]]

print(lst3[0:2])  # [100, 3.14]
print(lst3[0:4])  # [100, 3.14, True, "七夜"]
print(lst3[1:4])  # [3.14, True, '七夜']
print(lst3[1:1])

print(lst3[:3])  # 默认从0开始
print(lst3[0:])  # 不写end,默认取全部值
print(lst3[0::2])  # 取偶数下标对应的值，步长的概念


lst1 = [1, 2, 3, 4]
# lst2 = lst1  # 切记不要直接变量赋值给变量，会出现问题
lst2 = lst1[0:]
lst2.append(5)
print(id(lst1))
print(id(lst2))

"""
统计元素的个数：
count(元素具体的值) -- 判断这个元素在我们列表中有几个
"""
lst3 = [100, 3.14, True, "七夜", [1, 2, 3, 4, 3.14, 3.14]]
print(lst3.count(3.14))

"""
字符串可以当做一个列表用
切片：变量名[start:end:step]
"""
str1 = "hello python"
res = str1[0]
print(res)

# 负数？ --  在python中，就是反序的意思，倒过来数第几个
res = str1[-1]
print(res)

for i in str1:
    print(i)

# 切片

res = str1[0:5:2]
print(res)

