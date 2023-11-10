# import decorator
from decorator import fun1
# decorator.fun1()
"""
 python模块（文件）也不一定非要你主动调用它才执行的。只是模块中的函数部分的定义不会在 import 时立即执行，而非函数部分的其它脚本是可以在导入时就执行的

只有下面的写法在导入时才不会执行:
def fun1():
    print("hello")
if __name__ == "__main()__"
   fun1()

如果py文件作为模块被导入(import)，那么__name__就是该py文件的文件名(也称 模块名)；
如果py文件直接运行时(Ctrl+Shift+F10)，那么__name__默认等于字符串”__main__”;

"""
fun1()