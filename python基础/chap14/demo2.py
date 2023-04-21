# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo2.py 
@Author  ：zero 
@Date    ：2023/4/5 21:52  
"""
#创建模块

#导入模块
#import 模块名称 [as 别名]
'''使用该方法之后可以使用该模块中所有的功能，但是在使用时必须加上模块名的前缀
使用as就是把模块名暂时定位你所想使用的名字'''
'''import math  #关于数学运算的模块
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('----------------------------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))
print(math.ceil(9.001))#找接近的最大整数
print(math.floor(9.999))'''
import math as m
print(m)
print(m.pi)