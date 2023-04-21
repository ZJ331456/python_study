# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：练习1.py 
@Author  ：zero 
@Date    ：2023/4/17 14:11  
"""
#定义函数，根据总两数计算几斤零几两
def count_liang(num):
    #1 斤=10 两
    total_jin=num//10
    remain_liang=num%10
    print(f'{num}两的东西共{total_jin}斤，余{remain_liang}两')
num=int(input('请输入有多少两>:'))
count_liang(num)