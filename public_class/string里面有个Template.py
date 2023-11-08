from string import Template
"""
用一个字符串，去Template一个字典 
如果字符串有特殊符号 ${} 花括号里面有单词
Template会自动拿字典里的value 去替换掉 与花括号单词相同的key
"""
url = "http://111.111.222.333:101?token=${token}"
params = "{'token':${token},'xx':'xxx'}"
ss = {"token":"xiaoming"}
print(url)
print(Template(params).substitute(ss))
