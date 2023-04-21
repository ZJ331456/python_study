# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo19.py 
@Author  ：zero 
@Date    ：2023/4/6 22:59  
"""

#os模块里面的walk()方法
import os
path=os.getcwd()
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    '''
    dirpath 所指的是当前正在遍历的这个文件夹的本身的地址  
    dirnames 是一个 list ，内容是该文件夹中所有的目录的名字(不包括目录的子目录)  
    filenames 同样是 list , 内容是该文件夹中所有的文件(不包括子目录下的文件)
    '''
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('------------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print('-----------------')
