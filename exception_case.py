# 异常处理--多分支
# 例1： try/except/finally
dict = {"name": "mary", "age": 14}
try:
    sum = dict["name"] + dict["age"]
# except TypeError:
#     print("类型不一致，无法计算")
except KeyError:
    print("字典中不存在KEY值")
except TypeError as e:
    print(e)
finally:
    print("统一类型后计算===")

# 例2 try/except/else
str = "sorry"
try:
    for i in range(len(str)):
        print(str[i])
except IndexError as e:
    print(e)
else:
    print("输入成功，结束！")
