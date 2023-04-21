# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo3.py 
@Author  ：zero 
@Date    ：2023/4/5 21:57  
"""
#from 模块名称 import 函数/变量/类
'''用此方法导入的是该模块中的某一个方法
好处是使用该方法，比如x方法，使用时直接使用x()即可
不用加该模块名字为前缀，如模块c.x()'''
from math import pi
from math import pow
print(pi)
print(pow(2,3))
#print(math.pow(2,3))  #NameError: name 'math' is not defined