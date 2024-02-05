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

def forum():
    """
    模拟论坛框架搭建
    :return:
    """
    print("遇到个漂亮的小姐姐，要不要表白？")
    print('*'*50)
    print("以下为回复内容：")
    while True:
        #输入昵称
        name=input("姓名： ")
        while True:
            # 输入回复内容
            comment = input("评论: ")
            #回复内容去除左右空格
            comment=comment.strip()
            #验证回复内容是否为空
            if len(comment)!=0:
                #验证内容长度是否超过 20个字符
                if len(comment)<=20:
                    #敏感词汇进行替换
                    comment=comment.replace('tmd','**')
                    #计算剩余可输入长度
                    remain=20-len(comment)
                    #发表评论内容
                    print("{}:\n\t{}\n（已输入{}个字符，剩余{}个字符可输入）".format(name,comment,len(comment),remain))
                    #回复成功后，退出评论
                    break
                else:
                    print("回复内容超过20个字符！")

            else:
                print("回复内容不能为空！")
        answer=input('exit?Q')
        if answer.lower()=='q':
            break

if __name__=='__main__':
    # path='https://www.baidu.com/img/flexible/logo/pc/peak-result.png'
    # #find查找url中的文件名称
    # find_url_filename(path)
    #
    # print(path.find('$')) # find找不到则返回-1
    #
    # #count()统计某个字符的个数
    # print("'/'在字符串中出现的次数：{}".format(path.count('2')))
    #
    # #len()返回长度
    # print("返回字符串长度：{}".format(len(path)))
    #
    # """
    # 判断startswith,endswith,isalpha,isdigit,isalnum,isspace
    # """
    # s='e32348sfwerjjjsdf.gif'
    # result=s.startswith("e") #判断是否以xxx开头
    # print("{}字符串是否以e开头：{}".format(s,result))
    #
    # result=s.endswith('.gif')
    # print("{}字符串是否以.gif结尾：{}".format(s,result))
    #
    # #模拟文件上传功能
    # upload_file()
    #
    # #生成验证码
    # code=generate_verification_code(4)
    # print("生成的验证码:{}".format(code))
    #
    # #replace(old,new,count)替换内容：默认全部替换，也可以通过count指定次数
    # s='lily来唱歌,lily来跳舞,lily来化妆,john鼓掌！！！'
    # result1=s.replace('lily','mebal')
    # print('完全替换:\n{}----{}'.format(s,result1))
    # result2=s.replace('lily','mebal',2)
    # print('指定次数替换:\n{}----{}'.format(s, result2))
    #
    # #replace使用正则表达式进行替换多个元素
    # """
    # 第一个参数是匹配模式，对于被替换数据，使用正则表达式将其分为多个捕获组，即分别用小括号标注起来，
    # 其中，第一个小括号内的.*?代表不限长度的任何字符，
    # 第二个小括号内代表只能有一个字符（因为只有一个中括号）该字符只能是千或者万，
    # 通过这个正则表达式就把数据匹配拆分成了需要的两组。
    # replace方法的第二个参数前加r表示这是一个row字符串，配合第三个参数regex=True也可以被识别为正则表达式
    # 添加一个"***"字符串，匹配到的第二组字符串放在"***"字符串后面，直接不要第一组字符串
    # """
    # import re
    # str1="'1.1万', '8.5千', '0.9万', '6.5千', '22.0万'"
    # #(.*?)([千｜万])匹配 2 组，其中\2是指千或万,\1指匹配到的数字或任意字符
    # str2=re.sub('(.*?)([千｜万])',r"'***\2',",str1)
    # print('替换多个元素:\n{} 替换后： {}'.format(str1, str2))
    #
    # #split,rsplit splitlines分割字符串转成列表
    # s='千 百 万'
    # result1=s.split() #分割所有空格，返回列表
    # print('全部切割:\n{}----{}'.format(s,result1))
    # result2=s.split(' ',1) #使用空格分隔符，切一次
    # print('从左开始切割1次:\n{}----{}'.format(s,result2))
    # result3=s.rsplit(' ',1)#使用空格分隔符，从右边开始切一次
    # print('从右开始切割1次:\n{}----{}'.format(s,result3))
    #
    # #splitlines按行切割，转成列表
    # s="""lily来唱歌,
    # lily来跳舞,
    # lily来化妆,
    # john鼓掌,
    # """
    # result4=s.splitlines()
    # print('按行切割:\n{}----{}'.format(s,result4))
    #
    # #partition 使用分隔符切割，包括分隔符转换成元组
    # s = '千 百 万'
    # result1=s.partition(' ')
    # print('分割符左切割:\n{}----{}'.format(s,result1))
    # result2 = s.rpartition(' ')
    # print('分割符从右切割:\n{}----{}'.format(s, result2))
    #
    # #isalpha() 判断是否全部为字母
    # str1='hello'
    # result=str1.isalpha()
    # print("{}是否为全部字母:{}".format(str1,result))
    #
    # #isdigit() 判断字符串内容是否全部为数字
    # str='hello'
    # result=str1.isdigit()
    # print("{}是否为全部数字:{}".format(str1,result))
    #
    # #isalnum() 判断字符串内容是否为数字和字母
    # str1 = 'hello123'
    # result = str1.isalnum()
    # print("{}是否为数字+字母:{}".format(str1, result))
    #
    # #isspace() 判断字符串是否为空串
    # str2=' a     '
    # result = str2.isspace()
    # print("{}是否为空白字符串:{}".format(str2, result))
    #
    # #isupper() 判断字符串内容是否全部为大写字母
    # str2='FJFDLF'
    # result = str2.isupper()
    # print("{}是否全部为大写字母:{}".format(str2, result))
    #
    # #islower() 判断字符串内容是否全部为小写字母
    # str2='asdf'
    # result = str2.islower()
    # print("{}是否全部为小写字母:{}".format(str2, result))
    #
    # #title()所有单词首字母大写，其余小写
    # str2 = 'hello world'
    # result = str2.title()
    # print("{} 转成:{}".format(str2, result))
    #
    # # capitalize() 只对第一个单词首字母大写，其余小写
    # str2 = 'hello world'
    # result = str2.capitalize()
    # print("{} 转成:{}".format(str2, result))
    #
    # #upper()所有字母大写
    # str2 = 'hello world'
    # result = str2.upper()
    # print("{} 转成:{}".format(str2, result))
    #
    # #lower所有字母小写
    # str2 = 'HELLO WORLD'
    # result = str2.lower()
    # print("{} 转成:{}".format(str2, result))
    #
    # #lstrip,rstrip,strip去除空格
    # s='  admin     '
    # print(len(s))
    # result1=s.strip() #去除左右两边空格
    # result2=s.lstrip() #去除左边空格
    # result3=s.rstrip() #去除右边空格
    # print("{}的长度：{}\n{}的长度：{}\n{}的长度：{}".format(result1,len(result1),result2,len(result2),result3,len(result3)))
    #
    # #ljust,rjust,center 空格对齐
    # s='space aline'
    # result1 = s.center(30)  # 共30个字符，添加空格字符串居中对齐
    # result2 = s.ljust(30)  # 共30个字符，字符串靠左对齐
    # result3 = s.rjust(30)  # 共30个字符，字符串靠右对齐
    # print("{}\n{}\n{}".format(result1,result2,result3))

    #模拟论坛
    forum()

