# -*- coding: utf-8 -*-

# @Time    : 2024/2/14 13:05
# @Author  : lily
# @File    : test_dictionary.py
"""
字典常用方法：添加、修改、删除、遍历、获取
"""
def dict_add():
    """
    字典添加操作：setdefault() 类似dict[key]=value,
                update 将两个字典合并
    :return:
    """
    dic1= {'class': 'v211'}
    dic1.setdefault('name','jim')
    print('setdefault操作后dic1:{}'.format(dic1))

    dic2={'class': '999a', 'teacher': ['muzi', 'aa']}
    dic1.update(dic2) #key重复，则会覆盖
    print('update后dic1:{}'.format(dic1))

    d4 = {'class': 'v211','des': 'hahaha'}
    d4['des'] = [{"name": "mary", "age": 12}, {"name": "sunny", "age": 34}]  # 如果key值重复则覆盖
    print("嵌套增加后字典为：", d4)

    # 嵌套修改
    d4['des'][1] = "bbb" # 如果key值重复则覆盖
    print("嵌套修改后字典为：", d4)

    #构建新字典fromkeys,用序列中元素做字典的键，value=None
    dict2={}
    seq=('青','红','黄','绿')
    dict2=dict2.fromkeys(seq)
    print("dict2:",dict2)

    dict3=dict.fromkeys(['name','age'],['lily',18]) # 注意使用的是dict调用方法
    print('dict3:',dict3)
def dict_delete():
    '''
    字典删除操作：pop()、popitem()，del dic[key]、clear()
    :return:
    '''
    # 删除字典
    d4 = {'class': 'v211', 'teacher': ['muzi', 'aa'], 'vip': {1: '张三', 2: '李四'}, 'sub': ('python'), 'des': 'hahaha'}
    print("原字典为：", d4)

    # 嵌套删除
    d4['teacher'] = ['muzi']
    print("嵌套删除后字典为：", d4)

    d4['teacher'] = ['muzi', 'aaa']
    d4['teacher'].remove('muzi')
    print("嵌套删除后字典为：", d4)

    result=d4.pop('teacher')
    print("pop删除后字典为：{},返回值：{}".format(d4,result))

    # popitem()删除最后一个键值对
    result=d4.popitem()
    print("popitem删除后字典为：{},返回值：{}".format(d4,result))

    del d4['class'] #类似pop(key)
    print("del删除后字典为:{},返回值：{}".format(d4,result))
    # 清空
    result=d4.clear()
    print("clear删除后字典为：{},返回值：{}".format(d4,result))

    # 删除字典
    del d4
    # print("del删除字典为：", d4)  #d4已删除，需要重新定义

def dict_list():
    """
    字典转成List
    其他类型转型为字典
    ---数字-》字典    不支持
    ---字符串-》字典  不支持
    ---元组-》字典    支持
    ---列表-》字典    支持
    :return:
    """
    str1 = (('name', '小明'), ('age', 12))
    list1 = [['name', '小明'], ['age', 99]]
    dic1 = dict(str1)
    dic2 = dict(list1)
    print(dic1, '\n', dic2)
def dict_get():
    """
    字典查询操作：
    dict.get(key):根据Key获取value值
    dict[key] :根据Key获取value值

    区别：get(key)中key如果不存在则返回None,同时get(key,默认值)可以设置默认值
         dict[key]中key如果不存在则报keyerror错误。
    :return:
    """
    book={'书名':'《三体》','价格':15,'作者':'刘慈欣'}
    value = book.get('书名')
    value1 = book.get('书名1','默认值') #使用get方法，不会报错，查不到key时显示默认值
    print("value:{},value1:{}".format(value,value1))
def dict_fun():
    """
    • 字典名.items()：返回可遍历的（键，值）元组数组
    • 字典名.keys()：返回一个字典所有的键，返回一个迭代器，可以使用 list() 来转换为列表
    • 字典名.values()：返回一个字典所有的值，返回一个迭代器，可以使用 list() 来转换为列表
    :return:
    """
    d4 = {'class': 'v211',
          'teacher': ['muzi', 'aa'],
          'vip': {1: '张三', 2: '李四'},
          'sub': ('python'),
          'des': 'hahaha'}
    print("输出所有字典的键值对:{}，类型：{}".format(d4.items(),type(d4.items())))
    print("输出所有字典的key:{}，类型：{}".format(d4.keys(),type(d4.keys())))
    print("输出所有字典的value:{}，类型：{}".format(d4.values(),type(d4.values())))

    for i in d4.items():
        print(i)

    for k,v in d4.items():
        print('key:',k,end=' ')
        print('value:',v)
def book_add():
    """
    添加3本书名不重复的书，每本书包括书名，作者，价格
    :return:
    """
    books=[]
    while len(books)<3:
        name=input("请输入书名：")
        for book in books:
            if name in book.get('name'):
                print("书名重复")
                break
        else:
            author=input("请输入作者：")
            price=input("请输入价格：")

            books.append({
                'name':name,
                'author':author,
                'price':float(price)

            })
    print(books)

if __name__=='__main__':
    # #字典增加操作
    # dict_add()
    #
    # # 字典删除操作
    # dict_delete()
    #
    # #字典查询
    # dict_get()
    #
    # #字典转成List
    # dict_list()
    #
    # #字典遍历
    # dict_fun()

    #例子：添加3本不重复的书
    book_add()