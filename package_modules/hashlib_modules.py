# -*- coding: utf-8 -*-

# @Time    : 2024/4/20 15:21
# @Author  : lily
# @File    : hashlib_modules.py
"""
加密算法hashlib
md5,sha1,sha256都是单向算法，不可逆
base64 双向算法，可加密解密
"""
import hashlib

msg='我要玩游戏'
md5=hashlib.md5(msg.encode('utf-8')) #md5不能直接对字符串加密，需要编码。生成哈希值
print('md5加密后：',md5.hexdigest()) #hexdigest() 用16进制查看哈希值

sha1=hashlib.sha1(msg.encode('utf-8'))
print('sha1加密后：',sha1.hexdigest())

sha256=hashlib.sha256(msg.encode('utf-8'))
print('sha256加密后：',sha256.hexdigest())

#密码加密后存储到数据库中
password='123456'
list1=[]
sha256=hashlib.sha256(password.encode('utf-8')) #将密码使用sha256进行加密
list1.append(sha256.hexdigest())


#解密
pwd=input('输入密码:')
sha256=hashlib.sha256(pwd.encode('utf-8'))
pwd=sha256.hexdigest()
#循环访问数据库，匹配密码
for i in list1:
    if pwd ==i:
        print('登录成功')