# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo8.py 
@Author  ：zero 
@Date    ：2023/4/5 22:33  
"""
#再导入带有包的模块时注意事项
import pageage1
import calc
#使用import进行导入时，只能跟包名或者模块名名
from pageage1 import module_A
from pageage1.module_A import a
#使用from...import可以导入包、模块、函数、变量等等