# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demp10.py 
@Author  ：zero 
@Date    ：2023/3/25 22:22  
"""

#格式化字符串
#1、使用%做占位符号 ----->%s：字符串 ， %i或%d：整数 ， %f：浮点数
name='张三'
age=18
print('我的名字是%s,今年%d岁了'%(name,age))
#2、设置{}作占位符
print('我的名字是{0},今年{1}岁了,我的名字真叫{0}哦'.format(name,age))
'''{}里面数字代表formate()函数里面参数的索引'''

#3、f-string
print(f'我的名字是{name},今年{age}岁了')