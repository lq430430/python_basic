"""
日志模块：记录程序运行时的流程是否正常
在实际的工作中，python脚本是放在哪里运行的？-- 服务器上执行的
日志其实就是记录下来当前程序的运行，协助我们定位问题
"""
import logging

"""
logging 模块是 Python 内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等；相比 print，具备如下优点：

可以通过设置不同的日志等级，在 release 版本中只输出重要信息，而不必显示大量的调试信息；
print 将所有信息都输出到标准输出中，严重影响开发者从标准输出中查看其它数据；logging 则可以由开发者决定将信息输出到什么地方，以及怎么输出；
和 print 相比，logging 是线程安全的。
"""
logging.basicConfig(level=logging.DEBUG)


def fun1():
    logging.debug("这是debug级别日志")
    logging.info("这是info级别日志")
    logging.warning("这是warning级别日志")
    logging.error("这是error级别日志")


# fun1()

"""

装饰器：python重点 解释器简化掉所有流程， 增强函数，不改变原有函数，只要遇到@符号，就去找同名函数，如果有的话就先去执行同名函数


"""


def log_info(fun_name):
    def wrapper():
        logging.info("当前这个函数执行了")
        return fun_name()  # 可以写函数本体，也可以写函数调用后的结果

    return wrapper


@log_info       # @log_info后，会默认把fun2当做参数传给log_info，会默认去调用wrapper这些是装饰器的规则.
def fun2():
    print("fun2代码执行....")


def fun3():
    print("fun3代码执行....")


# m1 =log_info(fun_name=fun2) # 返回wrapper本体
# # print(method) # 返回wrapper本体，并打印wrapper引用的地址
# # method()  #调用wrapper函数，打印及返回fun2本地，fun2引用的地址
# m2 = m1() # 获取fun2的本体
# m2() # 等于fun2()

# 第一种：
# wrapper = log_info(fun_name=fun2) # 返回wrapper本体
# f2= wrapper() # 获取fun2的本体
# f2() #等于fun2

# 第二种：
# log_info(fun2)() #wrapper()
# log_info(fun2)()() # fun2()

# 第三种
# fun2()
"""
装饰器中的参数是不定长定参数，可以使用*args,**kwargs接收不定量的参数
"""
def log(fun_name):
    def wrapper(*args,**kwargs):
        logging.info("{}函数正在执行...".format(fun_name.__name__))
        return fun_name(*args,**kwargs)
    return wrapper

@log
def fun4():
    print("fun4函数正在执行")

@log
def fun5(name,addr):
    print("姓名：{}，地址：{}".format(name,addr))

# fun4()
# fun5("lily","shenyang")