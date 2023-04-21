# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo4.py 
@Author  ：zero 
@Date    ：2023/4/3 22:15  
"""

class A(object):
    pass

class B(object):
    pass

class C(A,B):
    pass

'''A和B都继承object类，C继承A，B'''