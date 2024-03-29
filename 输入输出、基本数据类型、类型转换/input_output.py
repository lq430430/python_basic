# coding=utf-8
"""输入输出、基本数据类型、类型转换"""

# 换行输出使用\,或使用（）[]{}

num1 = 1 \
       + 2 \
       + 3

num2 = (10
        + 20
        + 30)
print(num1, num2)

"""input()返回值是字符串"""
a = input("请输入数字")
b = 1
print(int(a) + b)


# 特殊字符：具有特定的效果，如：\n 换行 \t 制表符 \r 回车
str2 = "\t今天是星期一吗?不是吧\r 我觉得是\n " #回车符（\r）表示将光标移动到当前行的开头，可以用来实现在同一行上进行覆盖输出的效果。
print(str2)

# 对于特殊字符，我们不想要他有特定的效果，只想按照原样输出，把特殊字符变成普通的字符来使用，可以用r/R或者斜杠（\）来处理
str3 = "今天是’星期三‘\n"
str4 = r"今天是’星期三‘\n"
str5 = "今天是\"星期三\""
print(str3, str4 + '\n', str5)


"""格式化输出"""
# 方式一：使用 %d %s %f 来进行占位，具体显示什么值，我们来决定
# %d == 整数
# %s == 字符串
# %f == 小数
print("""
       =======自我介绍======
       name: %s,
       age: %d,
       addr: %s,
       sal: %f
       """ % ("lily", 18, "shenyang", 500.55))

# 方式二 ,str.format() 格式化输出
print("""
       =======自我介绍======
       name: {},
       age: {},
       addr: {},
       sal: {}
       """.format("lily", 18, "shenyang", 500.55))

name='lily'
score_math=100
score_chinese=85

print("{0}本次考试：数学分数={1}, 语文分数={2},英语分数={1},恭喜{0}".format(name,score_math,score_chinese))



"""
烤鸭店利润计算器
计算这个烤鸭店每天的利润是多少？ -- 怎么计算？
收入 - 成本 = 利润
进货价  售卖价  鸭子数量
利润 = （售卖价 - 成本价） * 鸭子数量
1.提示界面友好
2.让老板自己输入价格，鸭子数量
"""

print("--->欢迎使用烤鸭店计算器<---")
price1 = int(input("请输入你的进货价："))  # input传递出来的值，都是str！！！
price2 = int(input("请输入你的售卖价："))
num1 = int(input("请输入鸭子数量："))

result = (price2 - price1) * num1
print("今天获得的总利润为: {} 元".format(result))
