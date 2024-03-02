# coding:utf-8
"""
集合 set：没有重复，无序的,无下标
"""
import random
def set_add():
    #集合定义{}
    list1=[1,2,3,1]
    set1=set(list1)
    print('set1:{}:类型：{}'.format(set1,type(set1)))

    set3=set()#空集合

    # 集合添加元素.add() ,.update()
    s1 = {"Google","Runoob","Taobao"}
    s1.add('baidu')
    print("添加元素后的集合：{}:类型：{}".format(s1,type(s1)))
    s1.update([1,2,3])
    print("添加元素后的集合：",s1)
    s1.update({'taobao','google'})
    print("添加元素后的集合：",s1)
    s1.update({'runn':'ss'})
    print("添加元素后的集合：",s1)

def generate_code():
    """
    练习题：产生5组（不允许重复）的验证码,字母和数字组成4位验证码
    :return:
    """
    codes=set()
    flag=True
    while flag:
        str1='abcdedfg1234567890ABCDEFG'
        code=''
        for j in range(4):
            index=random.randint(0,len(str1)-1) #取机取下标
            code+=str1[index]
        codes.add(code)
        if len(codes)==5:
            flag=False
    for i in codes:
        print("验证码：",i)
def set_remove():
    """
    • 集合.pop():随机删除元素
    • 集合.remove(value):指定删除元素，如果元素不存在，则会发生错误
    • 集合.discard(value):指定删除元素，元素不存在，也不会发生错误
    • 集合.clear():清空集合
    :return:
    """
    s1 = {"Google", "Runoob", "Taobao"}
    s1.pop()
    print("pop删除元素后的集合：",s1)
    # s1.remove('baidu')
    # print("remove删除元素后的集合：",s1) #元素不存在则报错：KeyError: 'baidu'
    s1.discard('runn')
    print("discard删除元素后的集合：",s1)
    s1.clear()
    print("clear删除元素后的集合：",s1)

def set_fun():
    """
    1. 交集：集合1 & 集合2 或者 集合1.intersection(集合2)
    2. 并集：集合1 | 集合2 或者 集合1.union(集合2)
    3. 差集：集合1 - 集合2 或者 集合1.difference(集合2)
    :return:
    """
    s1 = {'刘德华','周润发','范冰冰'}
    s2 = {'陈奕迅','周杰伦','刘德华'}
    print("s1和s2使用&的交集",s1&s2)
    print("s1和s2使用.intersection的交集",s1.intersection(s2))

    print("s1和s2使用|的并集",s1|s2)
    print("s1和s2使用.union的交集",s1.union(s2))

    print("s1和s2使用-的差集",s1-s2)
    print("s1和s2使用.difference的交集",s1.difference(s2))

    #对s1的元素去重
    s1=['taobao', 'runn', 'taobao', 'google', 'google', 'Runoob']
    print("s1：",s1)

    s2=set(s1)
    print("s1去重后：",s2)


if __name__=='__main__':
    # #添加集合
    # set_add()

    # #练习题：产生5组（不允许重复）的验证码
    # generate_code()

    # #删除、移除元素
    # set_remove()

    #交集、并集、差集、去重
    set_fun()