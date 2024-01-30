# -*- coding: utf-8 -*-

# @Time    : 2024/1/30 22:19
# @Author  : lily
# @File    : str_fun.py
"""
字符串常用方法
1.查找内容：find,index,rfind,rindex
2.获取长度： len
3.计算出现次数：count
4.判断：startswith,endswith,isalpha,isdigit,isalnum,isspace,isupper,islower
5.替换内容：replace
6.切割字符串：split,rsplit,splitlines,partiton,rpartition
7.拼接字符串：join()
8.修改大小写：capitalize,title,upper,lower
9.空格处理：ljust,rjust,center,lstrip,rstrip,strip
"""
import random
def find_url_filename(path):
    """
    查找内容 find，index，从左往右找，找到第一个即返回
    反向查找 rfind,rindex 从右往左找，找到第一个即返回
    :param path:
    :return:
    """
    #xfind 从右往左找，返回元素在字符串或列表的下标值
    i=path.rfind('.')
    file_type=path[i+1:]
    print("文件扩展名：{}".format(file_type))
    j=path.rindex('/')
    image_name=path[j+1:]
    print("文件名：{}".format(image_name))
    return image_name

def upload_file():
    """
    模拟文件上传，键盘输入上传文件的名称，判断文件名是否大小 6 位以上，扩展名是否是：jpg,gif,png格式，
    如果不是则提示上传失败，如果名字不满足条件，而扩展名满足条件则随机生成一个 6 位数字组成的文件名
    :return:
    """
    file=input("请输入上传文件：")
    #判断扩展名是否是：jpg,gif,png格式
    if file.endswith(('jpg','gif','png')):
        #判断文件名是否大小 6 位以上
        i=file.rfind('.')
        name=file[:i]
        if len(name)>= 6:
            print("{}上传成功".format(file))
        else:
            #文件名小于 6 位时，随机生成一个 6 位数字组成的文件名
            # filename=str(random.randint(100000,999999))
            file_name=generate_verification_code(6)
            #将文件名和扩展名拼接
            print("{}上传成功".format(file_name+file[i:]))
    else:
        print("上传失败，文件类型错误")
def generate_verification_code(number):
    """
    生成验证码： 随机产生number位的数字+字母的字符串
    :param number:
    :return:
    """
    file_name=''
    s='abcdedfg1234567890ABCDEFG'
    for i in range(number):
        index=random.randint(0,len(s)-1) #随机产生下标
        file_name+=s[index] #获取下标匹配到的字母，拼接到 file_name
    return file_name

if __name__=='__main__':
    path='https://www.baidu.com/img/flexible/logo/pc/peak-result.png'
    #find查找url中的文件名称
    find_url_filename(path)

    print(path.find('$')) # find找不到则返回-1

    #count()统计某个字符的个数
    print("'/'在字符串中出现的次数：{}".format(path.count('2')))

    #len()返回长度
    print("返回字符串长度：{}".format(len(path)))

    """
    判断startswith,endswith,isalpha,isdigit,isalnum,isspace
    """
    s='e32348sfwerjjjsdf.gif'
    result=s.startswith("e") #判断是否以xxx开头
    print("{}字符串是否以e开头：{}".format(s,result))

    result=s.endswith('.gif')
    print("{}字符串是否以.gif结尾：{}".format(s,result))

    #模拟文件上传功能
    upload_file()

    #生成验证码
    code=generate_verification_code(4)
    print("生成的验证码:{}".format(code))

    #isalpha() 判断是否全部为字母
    str1='hello'
    result=str1.isalpha()
    print("{}是否为全部字母:{}".format(str1,result))

    #isdigit() 判断字符串内容是否全部为数字
    str='hello'
    result=str1.isdigit()
    print("{}是否为全部数字:{}".format(str1,result))

    #isalnum() 判断字符串内容是否为数字和字母
    str1 = 'hello123'
    result = str1.isalnum()
    print("{}是否为数字+字母:{}".format(str1, result))

    #isspace() 判断字符串是否为空串
    str2=' a     '
    result = str2.isspace()
    print("{}是否为空白字符串:{}".format(str2, result))

    #isupper() 判断字符串内容是否全部为大写字母
    str2='FJFDLF'
    result = str2.isupper()
    print("{}是否全部为大写字母:{}".format(str2, result))

    #islower() 判断字符串内容是否全部为小写字母
    str2='asdf'
    result = str2.islower()
    print("{}是否全部为小写字母:{}".format(str2, result))
