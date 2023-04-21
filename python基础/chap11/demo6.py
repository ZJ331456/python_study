# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo6.py 
@Author  ：zero 
@Date    ：2023/3/28 16:51  
"""
try:
    a = int(input('请输入第一个正数：'))
    b = int(input('请输入第二个正数：'))
    resurt = a / b
except BaseException as e:
    print('出错了',e)
else:
    print(resurt)
finally:
    print('谢谢你的使用')