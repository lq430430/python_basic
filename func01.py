
"""
函数：将一段公式/逻辑  定义在一个特定的 标题下面，通过一块，或者一行代码来执行固定好的逻辑，而这些代码只有在函数被调用的时候才会执行

这种行为在计算机中理解为简单的封装

函数 -- 定义
def 函数名(参数)：  -- 函数的语法

函数的调用：函数名()  -- 如果括号内有参数，就需要传参数
参数：参数可以简单的理解为在函数中使用的变量
这个变量是由调用函数的时候去给变量赋值
"""

m = 1
n = 2
s = (m + n) * 2

def add_01(m, n):
    s = (m + n) * 2
    return "七夜老师真帅，m:{}, n:{}".format(m, n)


print(add_01(2, 3))

# 如何获取函数的返回结果，也就是return的值
# 第一种： 定义变量接收值
a = add_01(2, 3)
print(a)

# 第二种方式：直接用print（）打印函数调用的结果
print(add_01(2, 3))

"""
return 关键字
如果说某些函数执行的时候，需要将执行的结果传递给调用函数的位置
就可以使用return这个关键字来返回我们的执行结果
函数可以不写return，如果不写，那么这个函数就不会与调用的地方产生更多的联系

总结：
1.他可以把结果传递出来，外面可以用两种方式接收
2.return一定标志着一个函数的结束，也就是意味着return后面的代码一定不会执行
3.一个函数如果有return，return也可以不带值，这个时候就意味着函数返回的是个None
4.一个函数也可以没有return，那么他返回的结果一定是None
"""

"""
函数的参数：
定义函数的时候，可以有参数，也可以没有参数
参数的形式有这么几种：
1.位置参数：调用函数的传递，按照函数规定的位置，来一一对应
2.指定参数：写明参数名 = 值，这个顺序是随意
3.缺省参数：定义函数的时候，直接给参数一个默认值
4.不定长参数：* 和 ** 表示当前参数是不定长的
"""


def pp():
    print("打印一句话")
    return "你好呀！"


pp()  # 打印了print（）
str1 = pp()  # 有打印print（）
print(str1)  # 打印的是return

print(pp())

def ddd(m, n, k):
    print("m:{}".format(m))
    print("n:{}".format(n))
    print("k:{}".format(k))


# 方式1：
ddd(1, 2, 3)

# 方式2：
ddd(n=10, k=30, m=1)

# 不去主动获取return的结果，是不会打印None

def fun1(*args):  # *表示传入的是元祖
    print(args)
    print(type(args))
    print(args[0])


fun1(1, 2, 3, 4, 5)

def fun2(**kwargs): #  传入的值是一个字典
    print(kwargs)
    print(type(kwargs))
    print(kwargs["name"])


fun2(name="七夜", addr="长沙")




"""
函数的注释 -- 与普通的注释有一定的区别，它是用来说明当前函数的参数含义
:param  参数的诠释
:return  函数的返回结果是什么？
通过这样的方式在调用的时候，能够更加直观的去理解函数的参数含义，以及函数的返回值含义
"""

"""
因为自己的英文不太好，习惯性的直接书写，导致了顺序错乱
函数1：left    实际的效果：右
函数2：right   实际的效果：左
函数3：up
函数4：down 
"""


def login(u1, p1):
    """
    :param u1:  请输入你的用户名：
    :param p1:    请输入你的密码：
    :return:    返回登录成功或者失败
    """
    if u1 == "root" and p1 == 123:
        return "登录成功！"
    else:
        return "登录失败！"


print("欢迎来到七夜老师的课堂，请进行登录操作~")


# 怎么获取函数的return结果？
# 方式1：
a = login(u1="root", p1=123)
print(a)

# # 方式2：
print(login(u1="root", p1=123))

# ctrl + 左键 进行点击  mac：command + 左键 点击
print(login.__doc__)  # 可以打印函数的注释
print(print.__doc__)


"""
一个函数内可以直接调用另一个函数
"""

# 程序会陷入死循环
def fun1():
    print("七夜老师最帅！")
    fun2()


def fun2():
    print("小明老师最丑！")
    fun1()  # 对fun1函数进行调用


fun2()

"""
python中 函数内可以定义函数，不仅可以定义，还可以直接调用
"""


def fun3():
    print("欢迎来到华测教育~~~")

    def fun4():
        print("七夜老师非常的专业~~~")

    fun4()  # 调用fun4函数
    print("请告诉我，fun3调用后，会打印几句话？")


fun3()  # 调用fun3函数

