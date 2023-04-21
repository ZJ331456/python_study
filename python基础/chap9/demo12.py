# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo12.py 
@Author  ：zero 
@Date    ：2023/3/25 22:51  
"""

#字符串的编码转换
#编码
s='天涯共此时'
print(s.encode(encoding='GBK')) #在GBK编码格式中，一个中文占两个字节
print(s.encode('UTF-8')) #在UTF-8这种格式里面一个中文占三个字节

#解码
byte=s.encode(encoding='GBK')
'''byte是代指一个二进制的数据（字节类型数据）'''
print(byte.decode(encoding='GBK'))
byte1=s.encode('UTF-8')
print(byte1.decode(encoding='UTF-8'))