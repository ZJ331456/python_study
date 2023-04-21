# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo11.py 
@Author  ：zero 
@Date    ：2023/4/6 16:37  
"""
#with语句（上下文管理器）
with open('a.txt', 'r', encoding='UTF-8') as file:
    print(file.read())