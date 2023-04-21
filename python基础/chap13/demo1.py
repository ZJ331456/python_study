# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo1.py 
@Author  ：zero 
@Date    ：2023/4/3 21:42  
"""
class car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print(self.brand + '汽车正在启动中')

car1=car('奔驰')
car1.start()