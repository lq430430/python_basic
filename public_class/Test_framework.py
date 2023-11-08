import requests,pytest,jsonpath
from xToolkit import xfile
from string import Template

# 变量，当做一个函数的参数传递
# 把之前定义的变量，拿走, 只需要一样的可以生成一个 [{}，{}]的数据就可以继续去执行测试了!
# 放的这个地方 能够清晰明了 第一时间看到它的结构
"""
# 特定的单词，会让计算机做特定的事情
1. 读到excel的数据，让它能够和我们写for循环一样，[{},{}]
2. 让pytest来帮我们执行这个函数! -- 循环执行，每次循环都读取一个dict --就一行代码！！@pytest.mark.parametrize() 
前一个参数,传递给函数的变量名，后一个参数是 需要解析的list 
3. eval是让这个格式的数据变成对应的类型! --DDT 数据驱动 参数化
4.理解了Template之后 ，只要干两件事 -- 有$符号的就去替换 ，登录之后吧值拿出来，保存在字典

"""
test_data = xfile.read("模拟接口测试用例.xls").excel_to_dict(sheet=1)
print(test_data)

dic ={}

@pytest.mark.parametrize("case_info",test_data) #  自动循环执行!
def test_excute(case_info): #  函数 url:参数
   url = case_info["接口URL"]
   if "$" in url:
        url = Template(url).substitute(dic)

   rs = requests.request(url=url,
                         method=case_info["请求方式"],
                         params=eval(case_info["URL参数"]),
                         data=eval(case_info["JSON参数"]))
   print(rs.text)


   #  问题： 我怎么判断需不需要提取返回值的东西呢？ -- 每个接口到底要不要提取值需要确定下来!
   if case_info["提取参数"]: # 不为空就是true 为空就是false
       rlst = jsonpath.jsonpath(rs.json(),'$..'+case_info["提取参数"]) # $..token $..goods_id
       dic[case_info["提取参数"]] = rlst[0]



# 让pytest去运行
if __name__ == '__main__': # 固定写法！！！ 复制粘贴
    pytest.main(["-vs"]) # pytest运行的固定命令








# pytest去执行! -->总结: 如果中途出错，它不会影响后续的我们的接口执行
# pytest 怎么用？ .py文件名 用test_开头 ，函数 test_开头 运行的时候，pycharm会自动用pytest模式去执行代码!
# 所以不再用for循环执行了

# excute(url=地址1,method=请求方式,params=get参数,data=参数体数据1)





