# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo9.py 
@Author  ：zero 
@Date    ：2023/4/6 16:16  
"""
file=open('c.txt', 'r', encoding='UTF-8')
file.seek(2)
print(file.read())
print(file.tell())
file.close()