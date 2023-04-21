# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo8.py 
@Author  ：zero 
@Date    ：2023/3/28 17:00  
"""
#异常处理模块-------->traceback模块
import traceback
try:
    print('---------------')
    print(1/0)
except:
    traceback.print_exc()