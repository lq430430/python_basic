"""
通过使用with...as...不用手动关闭文件。当执行完内容后，自动关闭文件。with open(路径，模式) as 变量：

r  只读，指针在开头
rb 以二进制格式打开一个文件用于只读。一般用于非文本文件如图片等
r+ 读+写，指针在开头

w  写入，文件不存在时创建，文件存在时清空，刚打开文件时，指针在开头
wb 以二进制格式打开一个文件只用于写入
w+ 写+读。如果文件存在，清空文本内容再写入，否则新建文件后写入内容

a  打开文件追加内容，存在文件，在文件原内容后增加，否则新建写入
a+ 打开一个文件用于读写。存在文件，在文件原内容后增加，否则新建用于读写
ab 以二进制格式打开一个文件用于追加，存在文件，在文件原内容后增加，否则新建写入
ab+ 以二进制格式打开一个文件用于读写。存在文件，在文件原内容后增加，否则新建用于读写

"""
# with open(r"C:\Users\lq430\PycharmProjects\python_basic\temp\demo1.txt", encoding="utf-8", mode="r") as file:
#     print(file.readlines())
#     # file.tell() 查看指针当前位置
#     print("读完后指针位置",file.tell())
#     # file.seek() 移动文件读取指针到指定位置。
#     file.seek(0)
#     file.seek(28)
#     print(file.readline())
#     print("seek(0)当前指针位置",file.tell())

#添加新内容后，如果再次读取文件中的所有内容
with open(r"C:\Users\lq430\PycharmProjects\python_basic\temp\demo1.txt", encoding="utf-8", mode="a+") as file:
    # file.read()
    file.write("\n新增内容----------")  #write后，指针位置是文件尾
    print("write后指针位置：",file.tell())
    file.seek(0)
    print("移动指针至文件开头位置：",file.tell())
    print("读取文件中的所有内容：",file.read())