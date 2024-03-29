"""
1.录入商品的功能
2.查询商品的功能
3.退出系统的功能
"""
print("--->欢迎使用七夜老师的烤鸭店计算器<---")
pro_dic = {}  # 定义了一个空的字典


def input_goods():
    """录入商品的功能"""
    print(">>>> 准备开始录入商品 <<<<")
    pro_list = []  # 定义了一个空的列表
    loat_txt = ["请输入商品的名称：", "请输入商品的成本价：", "请输入商品的出产地：", "请输入商品的生产日期：",
                "其他商品属性-1", "其他商品属性-2"]
    for i in loat_txt:
        name1 = input("{}".format(i))
        pro_list.append(name1)
    pro_dic[pro_list[0]] = pro_list  # 希望这个字典的key是商品的名称


def select_goods():
    """查询商品的功能"""
    print(pro_dic)
    # 需要让客户通过商品名称完成查询
    po_name = input("请输入您要查询的商品名称：")
    print(pro_dic[po_name])


while True:
    # 转义字符：键盘上有一部分键，不能在代码中显示
    # 用英文去代替特殊键位
    # \n :换行
    oper_type = input("1 - 录入商品\n2 - 查询商品\n3 - 退出系统\n请做出您的选择：")
    if oper_type == "1":
        # 在这里，我想要调用录入商品的函数，怎么办？
        input_goods()  # 调用录入商品的函数
    elif oper_type == "2":
        # 在这里，我想调用查询商品的函数，怎么办？
        select_goods()  # 调用查询商品的函数
    elif oper_type == "3":
        # 退出系统的功能
        break
    else:
        print("系统无法识别你的操作，即将关闭系统~")
        break
