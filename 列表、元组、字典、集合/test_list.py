# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 21:57
# @Author  : lily
# @File    : test_list.py
"""
列表 list 添加 删除 修改 查询
1.添加元素：append 追加 类似排队
"""


def list_append():
    # list.append 添加元素
    list3 = [44, 33, 22]
    print("list3:" + str(list3))
    print(list3.append(55))  # 返回 None
    print(list3.append("str1"))  # 返回None
    print(list3.append(2.134))  # 返回 None
    print(list3.append(True))  # 返回 None
    print(list3.append([5, 6]))  # 返回 None
    print("list3:" + str(list3))

    list3=[1, 2, 3, 4, 5, {2, 34, 2}, [4, 5, 6]]
    list3.insert(0, "student")
    print(list3)

def list_extend():
    list2 = ['面包']
    list3 = [44, 33, 22]
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

    # +号连接列表
    list3 = list3 + list2
    print("list3={}".format(list3))

def list_delete():
    """
    列表删除： pop()、remove()、clear()、del
    :return:
    """
    # list删除 pop() 删除最后一个值,pop(索引)删除指定值，下标不要超出范围
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

    list2=list1
    # list.clear()清空列表
    list1.clear()
    print("清空后list1:" + str(list1))
    print(list2)

    # del list[索引] 删除某个值
    list1 = ["python", 1, 2, 34, 99, 0, "python", "xxx", 99234]
    print("list1:" + str(list1))
    del list1[0]
    print("del操作后list1:" + str(list1))
    del list1  # del 列表 删除整个列表，包含列表空间
    # print("del操作后list1:" + str(list1)) # list1已删除，需要重新定

def list_repeat_element_delete():
    # 如果使用循环remove，删除后List下标变化，会造成不能完全删除元素
    # list2 = [2,3,"python","python","python",1, 2, 34, 99, 0, "python", "xxx", 99234]
    # for i in list2:
    #     if i=='python':
    #         list2.remove('python')
    # print(list2)

    # 如果使用循环remove，倒序删除可实现全部删除
    list2 = [2, 3, "python", "python", "python", 1, 2, 34, 99, 0, "python", "xxx", 99234]
    for i in list2:
        if i == 'python':
            list2.remove('python')
    print(list2)

    # 使用while循环，控制下标，可用
    list2 = [2, 3, "python", "python", "python", 1, 2, 34, 99, 0, "python", "xxx", 99234]
    n = 0
    while n < len(list2):
        # 删除元素后，下标不变
        if list2[n] == 'python':
            list2.remove('python')
        else:
            # 未找到元素时，下标后移
            n += 1
    print(list2)

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

def list_slice():
    """
    列表的切片：分割一个列表，只提取其中某一个片段出来
    变量名[start:end:step]
    start：从哪里开始
    end：到哪里结束
    step：步长，每隔几个元素，获取一次 -- 默认为1，并且可以省略
    :return:
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

def list_mutiple():
    """
    购买商品：包括商品名称、价格、数量，要用到列表嵌套
    :return:
    """
    container=[]
    flag=True
    while flag:
        #添加商品
        name=input("商品名称: ")
        price=input("商品价格: ")
        number=input("商品数量: ")
        #每个商品做为列表
        goods=[name,float(price),int(number)]
        #将商品列表做为元素添加到 container购物车
        container.append(goods)
        answer=input("是否继续购物，退出请按'q'或'Q': ")
        if answer.lower()=='q':
            flag=False
    #打印所有购物车商品详细信息及总价
    print('-'*20)
    total=0
    for item in container:
        print("{}: {} * {} ".format(item[0],item[1],item[2]))
        total+=item[1]*item[2]
    print("总价：   {}".format(total))

def list_filter_digitsum(str):
    total=0
    for i in str:
        if i.isdigit():
            total+=int(i)
    if total==0:
        print('0')
    else:
        print("总和：{}".format(total))

def list_modify():
    """
    数组修改操作
    :return:
    """

    # list修改
    list2 = ["python", 1, 2, 34, 99, 0, [5, 6], 2, 2, "python", 44, "python"]

    list2[6][1] = 7
    print("====list2:" + str(list2))

    print("获取list2中value，例如”python“的索引值：" + str(list2.index("python")))
    print("获取list2中包含2的总数" + str(list2.count("python")))

    list2[0] = "java"
    print("====list2:" + str(list2))

def transfer_list():
    '''
    转换为列表：list() 必须可以被循环的元素才能转换为列表。
    ---数值类型-》列表  不支持 数值类型是个不可拆分的整体
    ---字符串-》列表    支持
    ---元组-》列表      支持
    :return:
    '''
    str1 = "soryy,my love"
    print(list(str1))

    tup1 = (4, 2, 3, 2)
    print(list(tup1))

    set1 = {22, 22, 33, 45}
    print(list(set1))

def list_find():
    '''
    1.元素in列表，返回bool类型,  元素 not in 列表
    2.列表.index(元素) ，返回元素的下标位置 ，没有此元素则报错
    3.列表.count(元素)，返回整数，返回值是0则表示不存在此元素，存在则返回个数
    :return:
    '''
    list2 = ["python", 1, 2, 34, 99, 0, [5, 6], 2, 2, "python", 44, "python"]
    result='python' in list2
    print(result)

    result1 = 'python' not in list2
    print(result1)


    print(str(list2.index("python")))

    print(list2.count('python'))
    #统计元素的个数：count(元素具体的值) -- 判断这个元素在我们列表中有几个
    lst3 = [100, 3.14, True, "七夜", [1, 2, 3, 4, 3.14, 3.14]]
    print(lst3.count(3.14))

def list_sort():
    """
    列表排序reverse(),sort()
    :return:
    """
    # list.reverse 数组倒序操作，无返回值
    list1 = [1, 2, 3, 4, 5]
    result=list1.reverse()  # 返回 None,注意list.reverse无返回值
    print(result,list1)

    #sort()数组排序
    list2 = [1, 102, 23, 41, 5]
    result=list2.sort()  # 返回 None,注意list.sort无返回值，默认是升序
    print(result,list2)

    list2 = [1, 102, 23, 41, 5]
    result=list2.sort(reverse=True)  # 降序
    print(result,list2)

def bubble_sort(list):
    '''
    冒泡排序：两两比较，将最大值始终放在最后，
            2层循环，外层循环控制轮次，内层循环控制两两比较，len-1-j 去掉已经比较完的元素
    :param list:
    :return:
    '''
    for i in range(0,len(list)-1):#控制轮次
        for j in range(0,len(list)-1-i):# 两两比较，去掉已经比较完的元素
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
    return list
def list_comprehensions():
    """
    列表推导式
    :return:
    """
    #格式1
    list1=[i for i in range(1,11)]
    print('list1:{}'.format(list1))

    #格式2：[i for i in range if 条件]
    list2 = [i for i in range(1, 11) if i%2==0]
    print('list2:{}'.format(list2))

    #格式3：[i if 条件 else 条件 for i in range ]
    #如果是h开头的，则首字母大写，如果不是h开头的全部转大写
    list2=['hello','kitty','100','hill']
    list3=[word.capitalize() if word.startswith('h') else word.upper() for word in list2]
    print("list3:",list3)

    #格式4：双重循环[ (i,j) for i in range for j in range]
    list4 = [(i*j) for i in range(1, 10) for j in range(1,10)]
    print('list4:',list4)

def comprehensions_exam1():
    """
    练习题1：实现分组将一个list里面的元素，比如[1,2,3....100]变成[[1,2,3],[4,5,6].....]
    :return:
    """
    list1=[i for i in range(1,101)]
    list2=[list1[i:i+3] for i in range(0,len(list1),3)]
    print(list2)

def comprehensions_exam2():
    """
    练习题：找出里面名字含有两个'e'的放到新列表中
    names=[['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe','Celler'],
            ['Alice','Jill','Ana','Wendy','Sherry','Jerrmery']]
    :return:
    """
    names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe', 'Celler'],
             ['Alice', 'Jill', 'Ana', 'Wendy', 'Sherry','Jerrmery']]
    new_list=[name for group in names for name in group if name.count('e')>=2]
    print('new_list: ',new_list)
if __name__=='__main__':

    #append()列表添加元素、追加列表
    # list_append()

    #extend、+ 列表连接
    # list_extend()

    #购物车添加商品，列表嵌套
    # list_mutiple()

    #列表切片
    # list_slice()

    #键盘输入一个字符串，如果里面有数字则进行累加，没有则输出0，输出累加的结果
    # str=input("请输入字符串：")
    # list_filter_digitsum(str)

   #  #列表删除 pop()、remove()、clear()、del
   #  list_delete()
   #
   #  #列表重复元素删除
   #  # list_repeat_element_delete()
   #
   #  #列表元素修改
   #  list_modify()
   #
   #  #列表查找
   #  list_find()
   #
   #  # list取值
   #  list2 = [1, 2, 3, 4, 5, {2, 34, 2}, [4, 5, 6]]
   #  print("list2的长度： " + str(len(list2)))
   #  print("list中元素： " + str(list2[5]))  # 返回set集合{2,34}
   #  # print("list中元素： " + str(list2[5][0]))  # 报错，set没有下标
   #
   # #列表排序 reverse(),sort()
   #  list_sort()
   #
   #  # 转换为列表：list() 必须可以被循环的元素才能转换为列表。
   #  transfer_list()

    # #冒泡排序
    # list=[2,8,3,5,77,15,6]
    # bubble_sort(list)
    # print(list)

    #列表推导式
    # list_comprehensions()

    #列表推导式练习题
    # comprehensions_exam1()
    # comprehensions_exam2()


