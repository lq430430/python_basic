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
import os.path


def file_tell_seek():
    with open(r"/Users/lilicui/PycharmProjects/python_basic/temp/demo1.txt", encoding="utf-8", mode="r") as file:
        print("打开文件时指针位置", file.tell())
        print(file.readlines())
        # file.tell() 查看指针当前位置
        print("读完后指针位置",file.tell())
        # file.seek() 移动文件读取指针到指定位置。
        file.seek(0)
        file.seek(28)
        print(file.readline())
        print("seek(28)当前指针位置",file.tell())

    #添加新内容后，如果再次读取文件中的所有内容
    with open(r"/Users/lilicui/PycharmProjects/python_basic/temp/demo1.txt", encoding="utf-8", mode="a+") as file:
        # file.read()
        file.write("\n新增内容----------")  #write后，指针位置是文件尾
        print("write后指针位置：",file.tell())
        file.seek(0)
        print("移动指针至文件开头位置：",file.tell())
        print("读取文件中的所有内容：",file.read())

def copy_file():
    # 打开源文件
    import os
    with open(r'/Users/lilicui/Pictures/a.jpeg', mode='rb') as stream:
        content = stream.read()  # 读取文件内容

        # 获取源文件路径stream.name
        file = stream.name
        # 取路取中文件名，2种方式
        # name=file[file.rfind('/')+1:] #rfind,字符串从右侧寻找/返回索引，取/后面的所有值
        list1 = file.split('/')  # 字符串拆分
        name = list1[-1]
        print(name)

        # 获取当前路径os.path.dirname(__file__)
        path = os.path.dirname(__file__)
        # 拼结路径及文件名，为目标文件
        filename = os.path.join(path, name)

        # 打开目标文件
        with open(filename, mode='wb') as stream2:
            stream2.write(content)

def os_func():
    #os.path.isabs判断是否是绝对路径
    r=os.path.isabs(r'/Users/lilicui/Pictures/a.jpeg')
    r1=os.path.isabs(r'Pictures/a.jpeg')
    r2=os.path.isabs(r'../../Pictures/a.jpeg')
    print(r,r1,r2)

    #abspath()获取绝对路径
    path=os.path.abspath('a.jpeg')
    print('a.jpeg文件绝对路径：',path)

    current=os.path.abspath(__file__) #当前文件的绝对路径
    print('当前文件的绝对路径：',current)

    #os.path.dirname(__file__)获取当前文件的目录
    print('当前文件目录：',os.path.dirname(__file__))
    #os.getcwd()获取当前文件的目录
    print('当前文件目录：', os.getcwd())

    #os.path.split(path)拆分路径及文件名
    path=os.path.abspath(__file__) #获取当前文件绝对路径
    result=os.path.split(path) #分隔路径与文件名
    print('result:{},文件名：{}'.format(result,result[1]))

    #os.path.splitext(path) 分隔文件与扩展名
    result=os.path.splitext(path) #分隔文件与扩展名
    print('result:{},扩展名：{}'.format(result,result[1]))

    #获取文件大小 单位字节
    size=os.path.getsize(path)
    print('文件大小：',size)

    #获取所有文件及文件夹名称，保存到列表中
    all=os.listdir(os.getcwd())#返回指定目录下所有的文件及文件夹名称，保存到列表中
    print('当前目录下所有文件列表:',all)

    #创建文件目录
    if not os.path.exists(os.path.abspath('dir1')):
        os.mkdir('dir1')#返回值None
        print('dir1目录创建成功')
    #dir1下创建文件
    with open(os.path.abspath('dir1')+'/aa.txt',mode='w') as file:
        file.write('aaaaaa')
    # # os.rmdir('dir1') #目录不为空，删除报错
    #删除文件
    os.remove(os.path.abspath('dir1/aa.txt'))

    #判断目录下文件是否存在
    if not os.path.exists(os.path.abspath('dir1/aa.txt')):
        os.rmdir('dir1')#返回值None 只能删除空文件夹
        print('dir1目录删除成功')

    #切换目录
    print('当前目录',os.getcwd())
    os.chdir(os.path.abspath('/Users/lilicui/PycharmProjects/python_basic/temp'))
    print('切换后当前目录',os.getcwd())
def copy_dir(src_path,dest_path):
    """
    复制文件夹，将文件夹中所有文件及文件夹复制到目标文件夹
    :param src_path: 源文件夹路径
    :param dest_path: 目标文件夹路径
    :return:
    """
    #获取源文件夹下所有文件及文件夹
    paths=os.listdir(src_path)
    for path in paths:
        #判断是文件还是文件夹
        result_list=os.path.splitext(os.path.abspath(path)) #拆分路径
        #判断是拆分后元素是扩展名还是空串，#判断不为空是文件，为空时是文件夹
        if result_list[1]!='': #是文件时，复制文件 os.path.isdir(path)判断是否是文件夹
            #打开源文件，读文件
            with open(src_path + '/' + path, mode='rb') as stream:
                content=stream.readlines()
            #打开目标文件，写文件
            with open(dest_path+'/'+path,mode='wb') as file:
                file.writelines(content)
        else:#是文件夹时
            #判断目标文件夹是否存在,不存在则创建文件夹
            if not os.path.exists(os.path.abspath(dest_path+'/'+path)):
                os.chdir(dest_path)
                os.mkdir(path)
            #递归调用复制文件夹
            copy_dir(src_path + '/' + path, dest_path + '/' + path)

if __name__=='__main__':
    # #文件指针：当前位置及移动
    # file_tell_seek()

    # #文件复制
    # copy_file()

    # #os操作
    # os_func()

    #复制文件夹
    copy_dir('/Users/lilicui/PycharmProjects/python_basic/temp','/Users/lilicui/PycharmProjects/python_basic/temp1')

