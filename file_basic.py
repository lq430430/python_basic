# coding:utf-8
"""
python 能够直接读取计算机内的文件 -- txt
file 对象 -- 把txt文件的内容写入到程序中来

open 函数 -- 用来读取文件
1.打开文件 open("文件路径"， mode（方式）)
mode: r 读  w写（覆盖写入）  a 追加写入（加在原有的内容之后）
    rb   wb   ab  二进制（IO流，或者图片）
    r+  w+  a+ 读写
2.文件操作 -- 读 写
"""
file = open(r"C:\Users\lq430\PycharmProjects\python_basic\temp\demo1.txt", encoding="utf-8", mode="r")

#read()：的弊端就是当文件很大的时候,将文件中的内容全部读取,存放在内存中这样会导致内存崩溃。
msg = file.read()  # 全部读取
print(msg)
print(type(msg))  # str

#readline() 读取出来的数据在后面都有一个\n，读取之后会自动换行
msg = file.readline()  # 只读取一行内容，str类型
print(msg)
print(type(msg))

#readlines()读取所有行内容，返回List 如果文件很大，占内存，容易崩盘。
content = file.readlines()
print(content)
print(type(content))

for text in content:  # 循环list每行文本
    print(text)
    print(type(text))
file.close()

#大文件读取
file = open(r"C:\Users\lq430\PycharmProjects\python_basic\temp\demo1.txt", encoding="utf-8", mode="r")
for line in file:
    print(line)
file.close()

"""
覆盖写入：w
追加写入：a
"""
file = open(r"C:\Users\lq430\PycharmProjects\python_basic\temp\demo1.txt", encoding="utf-8", mode="a")

n = 0
while n < 5:
    if n == 0:
        file.write("mary正在输入第一行\n")
    else:
        file.write("mary正在输入第N行\n")
    n += 1
file.close()