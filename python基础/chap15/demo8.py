# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo8.py 
@Author  ：zero 
@Date    ：2023/4/6 16:15  
"""
file=open('c.txt', 'w', encoding='UTF-8')
# file.write('hello')
lst=['java','go','python']
file.writelines(lst)
file.close()