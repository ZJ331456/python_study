# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo1.py 
@Author  ：zero 
@Date    ：2023/4/5 19:56  
"""
# 1.获取数据
# 2.解析
# 3.提取
# 4.保存

import requests
a=requests.get('https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCw2LDEsMyw0LDUsMiw3LDgsOQ%3D%3D')
with open("D://11//1.jpg","wb")as f:
    f.write(a.content)