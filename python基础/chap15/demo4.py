# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo4.py 
@Author  ：zero 
@Date    ：2023/4/6 15:46  
"""
#常用的文件打开模式
file=open('b.txt', 'w', encoding='UTF-8')
file.write('Python')
file.close()
'''w---->将需要输入的内容填写到指定文件中去
如果该文件不存在，则重新创建一个新的文件
如果该文件存在且有内容，新内容会覆盖旧内容'''


