
import math
"""
作用域：我们定义的变量和函数在哪个范围内可用
文件和文件之间定义的东西，一般不能直接用
函数内定义的东西，不能在文件中直接使用，哪怕是同一个文件也不行

类中定义的东西，只在类的内部生效，不能在文件中直接使用

变量：
    全局变量 -- 在当前文件内定义的变量，可以在文件任何地方使用
    局部变量 -- 在有效范围内可以调用，出了范围就失效了
    类声明的变量也是一样，类的概念后面说
    局部变量在定义的时候可以直接声明为 全局变量
"""

def fun1():
    a = 10

print(a) # 是否能够打印出a的值？不能直接调用这个a变量，因为这个a只在fun1内部生效


a = 10  # 全局变量




def add():
    b = 5 # 局部变量
    print(a)

add()

def add():
    b = 5
    global c  # 声明为全局变量，一定要先声明，后赋值
    c = 4
    print(a)

add()
print(c)

# 循环

aa = 1
while True:
    aa = 10  # 注意：如果在循环内重新定义变量，那么这个全局变了的值就失效了
    break

print(aa)

"""
会用就行
abs()  绝对值
divmod()  返回商和余数
round() 四舍五入（银行家算法）
pow() 次方
sum() 求和
min() 最小值
max() 最大值
"""

# 绝对值
res = abs(-1)
print(res)

# 返回商和余数
x = int(input("输入一个值："))
a, b = divmod(x, 2)  # 传入两个参数，一个是被除数，一个是除数，返回值也是两个，商和余数
print(a)  # 商
print(b)  # 余数

# 四舍五入（银行家算法）规则：分奇偶数，奇数：四舍五入；偶数：直接舍弃 -- 只存在0.5这个区间
print(round(1.5))  # 2
print(round(2.5))  # 2
print(round(3.5))  # 4
print(round(4.5))  # 4

print(round(5.5))  # 6
print(round(6.5))

print(round(4.6))
print(round(4.51))
print(round(4.49))

# 次方
res = pow(10, 2)
print(res)

# 求和
lst1 = [1, 2, 3, 4, 5, 6, 7]
print(sum(lst1))

# 最大值
print(max(lst1))

# 最小值
print(min(lst1))

"""
匿名函数：就是没有名字的函数
python lambda表达式实现你们函数
lambda 参数: 逻辑
结果就是返回表达式的结果
"""


p = math.pi
print(p)  # 可以打印圆周率

def fun(r):
    res = lambda r: pow(r, 2) * math.pi  # 返回的res的函数本体
    return res(r)  # res()完成对res函数的调用 并且吧fun接收的r值给到的res函数


print(fun(r=5))  # 打印出fun函数执行后的结果，也就是res函数执行后的结果

res = lambda r: pow(r, 2) * math.pi
print(res)
print(res(r=5))



"""
python中可以把函数当做变量传递
所以这种情况下，可以直接执行被传入的函数
函数的引用  和调用
"""


def fun1():
    print("sdasfas")


# fun1()  # 调用就是加一个小括号 -- 函数的执行结果

# 如果说不加小括号呢？
# print(fun1)  # 会返回函数所在的内存地址 -- 函数的本体

def fun2(fun_name):
    print("你好，我是第二个函数的打印")
    fun_name()  # 在这个地方等同于fun1()


fun2(fun_name=fun1)

"""
函数的调用与引用：
调用：在函数后面加一个小括号()--语法规则设定,就是在执行对应的函数，跑函数里面的代码

引用：不加小括号，直接写函数名，这个东西称之为函数的本体
"""

"""
小口诀：有小括号叫调用，没有小括号叫引用
"""

"""
import 关键字：导入已经写好的python内容
"""
# import time
# import math



