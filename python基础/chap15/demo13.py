# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo13.py 
@Author  ：zero 
@Date    ：2023/4/6 21:52  
"""
#模拟上下文管理器
class MyContentMgr(object):
    def __enter__(self):
        print('调用了enter方法')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('调用了exit方法')
    def show(self):
        print('调用了show方法')

with MyContentMgr() as file:
    file.show()