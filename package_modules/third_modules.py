# -*- coding: utf-8 -*-

# @Time    : 2024/4/20 15:51
# @Author  : lily
# @File    : third_modules.py
"""
第三方模块
"""
import requests

rs=requests.get('http://www.12306.cn')
print(rs.text)