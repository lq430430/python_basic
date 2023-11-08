# coding:utf-8

"""
1.录入商品功能
2.查询商品功能
3.退出系统功能
"""
print("-------->欢迎使用烤鸭计算器<--------")
pro_list = []
while True:
    # 转义字符用英文代替特殊键位例如 \n 换行 \t制表位 \r回车
    oper_type = input("1 - 录入商品\n2 - 查询商品\n3 - 退出系统\n请做出您的选择：")
    # 录入商品
    if oper_type == "1":
        pro = {}

        pro['name'] = input("请输入商品名称：")
        pro['price'] = input("请输入商品成本价：")
        pro['addr'] = input("请输入商品产地：")
        pro['date_time'] = input("请输入商品生产日期：")
        pro_list.append(pro)
    # 查询商品
    elif oper_type == "2":
        name = input("请输入查询商品名称：")
        flag = 0
        print(pro_list)
        for item in pro_list:
            if item['name'] == name:
                print("商品信息如下：", item)
                flag = 1
        if flag == 0:
            print("无此商品")

    # 退出系统
    elif oper_type == "3":
        break
    else:
        print("系统无法识别您的操作，即将关闭系统")
