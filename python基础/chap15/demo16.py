# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo16.py 
@Author  ：zero 
@Date    ：2023/4/6 22:13  
"""

#os模块操作目录相关函数
import os
#print(os.getcwd()) #返回当前工作目录

# lst=os.listdir('../chap15') #返回指定路径下的文件和目录信息
# print(lst)

# os.mkdir('newdir') #创建新目录

# os.makedirs('A/B/C/D') #创建多级目录

# os.rmdir('newdir')  #删除目录
#os.rmdir('A') #OSError: [WinError 145] 目录不是空的。: 'A'----->不能删除多行目录

# os.removedirs('A/B/C/D')  #删除多级目录

os.chdir("/python基础/chap15") #将path设置为当前工作目录
print(os.getcwd())