# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo17.py 
@Author  ：zero 
@Date    ：2023/4/6 22:26  
"""

#os.path模块操作目录相关函数
import os.path
print(os.path.abspath('demo13.py')) #用于获取文件或目录的绝对路径

print(os.path.exists('demo13.py'), os.path.exists('demo18.py')) #用于判断文件或目录是否存在，如果存在返回True，否则返回False

print(os.path.join('/python基础/chap15', 'demo18.py'))
#将目录与目录或者文件名拼接起来

print(os.path.split("/python基础/chap15/demo18.py"))
#将目录与文件名分离

print(os.path.splitext("/python基础/chap15/demo18.py"))
#分离文件名和扩展名

print(os.path.basename("/python基础/chap15/demo18.py"))
#从一个目录中提取文件名

print(os.path.dirname("/python基础/chap15/demo18.py"))
#从一个路径中提取文件路径，不包括文件名

print(os.path.isdir("/python基础/chap15/demo18.py"))
print(os.path.isdir("/python基础/chap15"))
#用于判断是否为路径，注意路径不包括文件名