# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo6.py 
@Author  ：zero 
@Date    ：2023/4/6 15:57  
"""
src_file=open('wit.png', 'rb')

target_file=open('copywit.png', 'wb')

target_file.write(src_file.read())

target_file.close()

src_file.close()