# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo9.py
@Author  ：zero 
@Date    ：2023/3/27 21:44  
"""


#递归函数
def fac(num):
    if num==1:
        return 1
    else:
        return num*fac(num-1)
sum=fac(6)
print(sum)