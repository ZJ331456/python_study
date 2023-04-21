# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo4.py 
@Author  ：zero 
@Date    ：2023/3/28 16:43  
"""
try:
    a = int(input('请输入第一个正数：'))
    b = int(input('请输入第二个正数：'))
    resurt = a / b
    print('结果为：', resurt)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')