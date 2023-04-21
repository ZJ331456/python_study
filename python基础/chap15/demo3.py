# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo3.py 
@Author  ：zero 
@Date    ：2023/4/6 15:29  
"""
#文件读写
file=open('a.txt', 'r', encoding='UTF-8')
print(file.readlines())
file.close()