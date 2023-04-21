# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo9.py 
@Author  ：zero 
@Date    ：2023/3/25 22:08  
"""

#字符串的切片操作
s='hello,python'
print(s[:5:])
print(s[6::])

print('-------------------------切片[start:end:step]-----------------------------')
print(s[::2])
print(s[::-1])
print(s[-6::])
print(s[-1:-7:-1])

'''
切片操作的话，start默认为0，end默认为字符串位后一位，sep默认为1
当sep为负数时，是从后往前遍历，此时start为最后一个输出字符的位置，end为第一个输出的位置
而且当start/end为负数时，是从后往前数的索引------->可知字符串有两套索引确定方式
如：  p   y   t   h   o   n
索引：0   1    2   3   4  5
     -6 -5   -4  -3  -2 -1
'''
