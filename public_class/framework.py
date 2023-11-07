import requests

# 变量，当做一个函数的参数传递
def excute(case_info): #  函数 url:参数
   rs = requests.request(url=case_info["url"],
                         method=case_info["method"],
                         params=case_info["params"],
                         data=case_info["data"])
   print(rs.text)


case_info = {}

地址 = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
get参数 = {
    "application":"app",
    "applicaiton_client_type":"weixin"
}

参数体数据 = {
    "accounts":"huace_xm",
    "pwd":123456,
    "type":"username"
}
请求方式 = "POST"

地址1 = "http://shop-xo.hctestedu.com/index.php?s=api/goods/favor&token=1ea6f8344253b2cbea6774a9e461bcd1"
参数体数据1 = {
    "id": "12"
}

case_info["url"] = 地址
case_info["method"] = "POST"
case_info["params"] = get参数
case_info["data"] = 参数体数据

case_info2 = {} # 定义一个字典 python数据格式 json数据 key:value
case_info2["url"] = 地址1
case_info2["method"] = "POST"
case_info2["params"] = get参数
case_info2["data"] = 参数体数据1

lst = []
lst.append(case_info) # 向这个中括号放值的方式 单词
lst.append(1)
lst.append(case_info2)
# 循环执行 --可以执行多个不同接口的方法了？
print(lst)
for case in lst:
    excute(case) # 有多少个字典就可以执行多少个接口!

# pytest去执行! -->总结: 如果中途出错，它不会影响后续的我们的接口执行
# pytest 怎么用？ .py文件名 用test_开头 ，函数 test_开头 运行的时候，pycharm会自动用pytest模式去执行代码!
# 所以不再用for循环执行了

# excute(url=地址1,method=请求方式,params=get参数,data=参数体数据1)





