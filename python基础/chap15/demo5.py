# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo5.py 
@Author  ：zero 
@Date    ：2023/4/6 15:51  
"""
file=open('b.txt', 'a', encoding='UTF-8')
file.write('Python')
file.close()
'''a------>会在原有内容之后追加'''