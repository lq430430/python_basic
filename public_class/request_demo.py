# _*_ coding:utf-8 -*_
import requests, jsonpath

# 域名地址
gateway = "http://shop-xo.hctestedu.com/index.php?s="

# 公共参数 其他接口都通用
params = {
    "application": "app",
    "application_client_type": "ios",
}


def test_login():  # 账号登录
    url = "api/user/login"
    data = {
        "accounts": "lily888",
        "pwd": "123456",
        "verify": "",
        "type": "username"
    }
    rs = requests.request(url=gateway + url,
                          method="POST",
                          params=params,
                          data=data)
    # print(rs.text)
    token = jsonpath.jsonpath(rs.json(), "$..token")  # $..token取字典中所有token放到list，rs.json()反序列化，将json格式字符串转成字典
    return token[0]


def test_search_index(token):  # 获取商品id及spec规格
    url = "api/search/index"
    data = {
        "page": "1"
    }
    rs = requests.request(url=gateway + url + "&token=" + token,
                          method="POST",
                          params=params,
                          data=data)
    goods_id = jsonpath.jsonpath(rs.json(), "$.data.data[0].id")
    # print("商品id:" + goods_id[0])
    spec_base = jsonpath.jsonpath(rs.json(), "$.data.data[0].spec_base")
    # print("商品spec:" + str(spec_base[0]))
    return goods_id[0], spec_base[0]


def test_cart(token, goods_id, spec):  # 加入购物车
    url = "api/cart/save"
    data = {
        "goods_id": goods_id,
        "spec": spec,
        "stock": 1
    }
    rs = requests.request(url=gateway + url + "&token=" + token,
                          method="POST",
                          params=params,
                          data=data)
    print(rs.text)


if __name__ == '__main__':
    test_login()
    token = test_login()
    print("token = " + token)
    goods_list = test_search_index(token)
    test_cart(token, goods_list[0], goods_list[1])
