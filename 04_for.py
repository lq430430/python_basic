# coding:utf-8

"""
for 遍历
1.遍历 -- 复杂的数据结构中，将里面的元素一个个的获取出来
2.循环

语法：
for 变量名 in 可遍历的数据：（可拆分的 -- 字符串，列表... ...)
    循环体逻辑：会在每一次循环的时候把便利的数据一个个的拿出来，并且赋值给这个变量名

循环：
1.循环次数根据可遍历的数据长度决定
2.变量名  获取到可迭代的数据每一个元素
"""

lst = [1, "七夜", 3, "a", "b", 6]

for value in lst:
    if value == "七夜":
        print("请叫我七夜老师")
    print(value)



j = 0
for i in lst:
    if j % 2 == 0:  # 去偶数的j的值
        # print(i)
        pass
    j += 1
    print("这是第 {} 次循环，其中打印的值为：{}".format(j, i))

# for 循环中的range -- 迭代器，用于生成一个整数的序列
r = range(10)  # 根据给到的一个数字，生成一个列表 -- 可迭代的对象
print(list(r))

print(list(range(len(lst))))  # [0, 1, 2, 3, 4, 5]
for i in list(range(len(lst))):
    # if i % 2 == 0:
    #     print(lst[i])
    print("这是第 {} 次循环，其中获取到的值是：{}".format(i + 1, lst[i]))

for i in range(len(lst)):
    print(i)

a = range(6)
print(a)
print(list(range(start=0, end=6)))  # 参数不存在，仅供理解
print(list(range(0, 6)))

print(list(range(10)))  # 取值的规则？  # 左闭右开， 如果不给初始值，默认从0开始
print(list(range(4, 10)))

for i in "qiyelaoshi":
    print(i)

for i in range(1, 10):
    print(i)

for i in range(10):
    print(i)

"""
双重循环
"""
k = 0
for i in range(1, 10): # i = [1-9]
    for j in range(1, 10):
        k += 1

print(k) # 81

"""
练习：
99乘法表
1 * 1 = 1
1 * 2 = 2, 2 * 2 = 4
1 * 3 = 3, 2 * 3 = 6, 3 * 3 = 9
...
1 * 9 = 9, 2 * 9 = 18, 3 * 9 = 27 ...
"""

# print("{} * {} = {}".format(1, 2, 1 * 2))
# 定义变量 i  从1到9进行自动变化
# 定义变量 j  从1到9进行自动变化
for i in range(1, 10):
    for j in range(1, i+1):
        print("{} * {} = {}".format(j, i, i * j), end="   ")  # print自带换行
    print()  # 起到换行的作用
