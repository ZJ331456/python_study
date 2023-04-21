# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：元素养提优.py 
@Author  ：zero 
@Date    ：2023/4/8 11:51  
"""
'''
A+B=13
B+C+D=13
D+E+F=13
F+I+J=13
J+K=13
'''
lst=[i for i in range(1,10)]
for A in lst:
    for B in lst:
        for C in lst:
            for D in lst:
                for E in lst:
                    for F in lst:
                        for G in lst:
                            for H in lst:
                                for I in lst:
                                    for J in lst:
                                        for K in lst:
                                            if(A!=B and B!=C):
                                                pass
