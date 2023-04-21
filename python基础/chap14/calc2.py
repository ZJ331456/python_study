# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：calc2.py 
@Author  ：zero 
@Date    ：2023/4/5 22:12  
"""
def add(a,b):
    return a+b




if __name__ == '__main__':
    print(add(10, 20))
'''只有点击运行calc2的时候才会执行add(10, 20)运算
即在calc2被别的py文件调用的时候是不会执行add(10,20)这个操作'''