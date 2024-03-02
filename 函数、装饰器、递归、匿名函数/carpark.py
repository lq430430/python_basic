# -*- coding: utf-8 -*-

# @Time    : 2024/2/24 18:08
# @Author  : lily
# @File    : carpark.py
"""
停车计费系统：
    进入停车场记录进入时间 ，如果出去则记录出去时间，停车时间是：出去-进入时间
    停车场的数据结构是：
    [{'车牌':[进入时间,0]},{'车牌':[进入时间,出去时间]}.....]
    15分钟 1块
    1小时   4块
    停车场变量-->全局变量
"""
import random
def enter():
    """
    进入停车场
    :return:
    """
    car={}
    #扫描车牌号
    plate=input("请输入车牌：")
    #将车牌当成Key,进入时间是0做为车牌进场时间
    car[plate]=[0]
    #将车加入车辆列表
    car_park.append(car)
    print("已进场")

def go_out():
    '''
    离开停车场
    :return:
    '''
    print("离开停车场扫描车牌")
   #扫描车牌号
    plate = input("请输入车牌：")
    #判断汽车是否进场
    for car in car_park:
        if plate in car:
            # 记录结束时间
            time=random.randint(0,24)
            #获取车辆对应时间列表
            time_record=car.get(plate)
            #将出场时间加入时间列表
            time_record.append(time)
            #计算花费
            total=time*4
            print('{}停车{}小时，应缴费:{}'.format(plate,time,total))
            break
    else:
        print("您的车未进场！")

if __name__=='__main__':
    car_park = []
    enter()
    enter()
    enter()
    go_out()