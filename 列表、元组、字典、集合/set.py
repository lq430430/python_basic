# coding:utf-8
"""元组,有序不可变"""

tup1=("Google","Runoob","Taobao")

print("元组中‘Taobao’数量：",tup1.count("Taobao"))
print("元组元素：",tup1[1])
print("元组\"Google\"元素索引值：",tup1.index("Google"))

"""===========================集合============================================="""
"""集合的各项操作，无序可变"""

#集合添加元素.add() ,.update()
s1 = {"Google","Runoob","Taobao"}
s1.add('baidu')
print("添加元素后的集合：",s1)
s1.update([1,2,3])
print("添加元素后的集合：",s1)
s1.update({'taobao','google'})
print("添加元素后的集合：",s1)
s1.update({'runn':'ss'})
print("添加元素后的集合：",s1)

"""
• 集合.pop():随机删除元素
• 集合.remove(value):指定删除元素，如果元素不存在，则会发生错误
• 集合.discard(value):指定删除元素，元素不存在，也不会发生错误
• 集合.clear():清空集合
"""
s1.pop()
print("pop删除元素后的集合：",s1)
s1.remove('baidu')
print("remove删除元素后的集合：",s1)
s1.discard('runn')
print("discard删除元素后的集合：",s1)
s1.clear()
print("clear删除元素后的集合：",s1)

"""
1. 交集：集合1 & 集合2 或者 集合1.intersection(集合2)
2. 并集：集合1 | 集合2 或者 集合1.union(集合2)
3. 差集：集合1 - 集合2 或者 集合1.difference(集合2)
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


