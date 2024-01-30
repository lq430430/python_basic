# coding: utf-8
"""
python语言支持一下类型的运算符：算数运算符、比较（关系运算符）、赋值运算符、逻辑运算
符、位运算符、成员运算符、身份运算符、运算符优先级
"""
num1 = 10
num2 = 3
print(num1 / num2)  # 除法，保留小数
print(num1 % num2)  # 取余

# 整数---只会取整数 //
print(num1 // num2)

# 幂计算 **计算
print(num1 ** num2)

# 字符串*数字 ，相乘进行字符串多次输出
str1 = "hello"
num3 = 3
print(str1 * num3)

# float+int ,会出现精准度丢失的情况
data = 3
f1 = 2.222
print(data + f1)  # 5.2219999999999995,出现精准度丢失的情况

# bool型+int
bool1 = True
bool2 = False
num1 = 1
print(bool1 + num1, bool2 + num1)

# 执行顺序： not > and > or
print(True and False or True and not False)  # True
# 执行顺序 ：算符 >比较 >逻辑
print(1 + 1 > 1 + 2 and 3 + 2 < 3 - 1 or 5 and not True)

"""
判断指定内容是否包含在某个内容中 包含关系
in:存在(包含)
not：不存在
"""
str1 ="qiersdffff"

print("sd" in str1)
print("sds" in str1)
print("s d f" in str1)

# num1=12345
# print(1 in num1) #数字不能用于包含语句