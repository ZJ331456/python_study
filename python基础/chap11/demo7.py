# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo7.py 
@Author  ：zero 
@Date    ：2023/3/28 16:53  
"""
#python中常见的异常类型
#（1）数学运算的异常
'''print(10/0)
ZeroDivisionError'''
#(2)IndexError
'''lst=[1,2,3,4]
print(lst[4])'''
#(3)KeyError: 'gender'
'''dic={'name':'张三','age':18}
print(dic['gender'])'''
#(4)NameError
'''print(num)'''
#(5)SyntaxError---->python语法错误
'''int a=20'''
#(6)ValueError----->传入无效的参数
a=int('hello')