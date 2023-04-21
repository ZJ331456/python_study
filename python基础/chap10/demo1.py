# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo1.py 
@Author  ：zero 
@Date    ：2023/3/27 17:26  
"""
#函数的定义
#函数调用
def calc(a,b):        #a、b为形参，形参的位置是在函数定义处
    c=a+b
    return c
result=calc(10,20)  #10、20成为实参，位置在函数的调用处
print(result)

result1=calc(b=20,a=10)   # =左侧的变量的名称为关键字参数
print(result1)