# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo18.py 
@Author  ：zero 
@Date    ：2023/4/6 22:53  
"""

#列出指定目录下的所有py文件
import os
path=os.getcwd()
lst=os.listdir(path)
print(lst)
print('----------------------------')
for filename in lst:
    if filename.endswith('.py'):  #endswith()方法-------->用于判断字符串后缀是否是某几个字符串，返回值为布尔类型bool（true|false）。
        print(filename)