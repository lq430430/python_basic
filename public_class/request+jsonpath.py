# -*- coding:utf-8 -*-
"""requests请求demo"""

import requests, jsonpath

params = {
    "application": "app",
    "applicaiton_client_type": "weixin"
}

data = {
    "accounts": "huace_xm",
    "pwd": 123456,
    "type": "username"
}

rs = requests.request(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",
                      method="POST",
                      params=params,
                      data=data)  # 请求四要素
# print(rs.text) #text返回响应的内容，unicode 类型数据
# print(type(rs.text))
# 取响应内容中的指定内容做变量
# print(rs.json())  # 返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误),rs.json()反序列化：将json格式字符串转化成字典
# print(type(rs.json()))
# 方法1 字典取值
token = rs.json()["data"]["token"]
# print(token)
# 方法2 复杂字典 根据key对字典取值
token1 = jsonpath.jsonpath(rs.json(), '$..token')  # $根目录，$..toekn取所有token，返回list
print("登录后token= "+token1[0])

# 接口需要登陆后才能访问!
"""
接口访问的时候，如果是需要登录后的接口才有权限，那么访问本接口的时候，必须带上你已经登录的信息！！
登录的信息是什么？ -- token字段表示你已经登录了。。。
token令牌信息~~ 请求头里？  后端代码准备在哪里拿token ，你前端就放哪里!
接口请求：单点登录! 每次登录就会生成一个新的token 
session是会话 --存放东西 
结论：token不能写死值！随着登录变化而变化!! --> 接口测试的时候，如果有关联怎么办？ --> 变量去处理!
以token为例!

接口测试的时候，如果有关联 且 我不知道这个值，在返回结果的哪一层？怎么办？ 复杂：JSONPATH
它的取值方式
"""
data2 = {
    "id": "12"
}
rs1 = requests.request(url="http://shop-xo.hctestedu.com/index.php?s=api/goods/favor&token=" + token1[0],
                       method="POST",
                       params=params,
                       data=data2)
print("登录后收藏响应："+rs1.text)
