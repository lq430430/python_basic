# coding:utf-8
"""
文件基本操作
python 能够直接读取计算机内的文件 -- txt
file 对象 -- 把txt文件的内容写入到程序中来

open 函数 -- 用来读取文件
1.打开文件 open("文件路径"， mode（方式）)--->返回值：stream(管道)
mode: r 读  w写（覆盖写入）  a 追加写入（加在原有的内容之后）
    rb   wb   ab  二进制（IO流，或者图片）
    r+  w+  a+ 读写
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    ========= ===============================================================
2.文件操作 -- 读 写
    stream.read()---->读取管道中的内容
"""
# # 默认打开方式：rt
# stream=open(r"/Users/lilicui/Pictures/壁纸/os进程.jpg")
# container=stream.read() #报错UnicodeDecodeError 编码格式错误，
# #读取图片使用rb
# stream=open(r"/Users/lilicui/Pictures/壁纸/os进程.jpg",mode="rb")
# container=stream.read()
# print(container)

# file = open(r"/Users/lilicui/PycharmProjects/python_basic/temp/demo1.txt", encoding="utf-8", mode="r")

# #readable()判断是否可读
# result=file.readable()
# print('文件是否可读：',result)

# #read()：的弊端就是当文件很大的时候,将文件中的内容全部读取,存放在内存中这样会导致内存崩溃。
# msg = file.read()  # 全部读取
# print(msg)
# print(type(msg))  # str
# file.close()

# #readline() 读取出来的数据在后面都有一个\n，读取之后会自动换行
# msg = file.readline()  # 只读取一行内容，str类型
# print(msg)
# print(type(msg))

# #readline()循环读取全部
# while True:
#     line=file.readline()
#     print(line)
#     if not line:
#         break
# file.close()
# #readlines() 读取所有行内容，返回List 如果文件很大，占内存，容易崩盘。
# content = file.readlines() #保存到列表中[]
# print(content)
# print(type(content))
# #循环打印所有行
# for line in content:
#     print(line)
# file.close()
#
# #大文件读取
# file = open(r"/Users/lilicui/PycharmProjects/python_basic/temp/demo1.txt", encoding="utf-8", mode="r")
# for line in file:
#     print(line)
# file.close()
#
# """
# 覆盖写入：w
# 追加写入：a
# """
file = open(r"/Users/lilicui/PycharmProjects/python_basic/temp/demo1.txt", encoding="utf-8", mode="a")

# n = 0
# while n < 5:
#     file.write("mary正在输入第{}行\n".format(n+1))
#     n += 1
# file.close()

# writelines(Iterable) #没有换行效果
file.writelines(['hello','word','marry'])
file.close()


