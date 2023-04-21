# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：创建进程.py 
@Author  ：zero 
@Date    ：2023/4/21 15:17  
"""


#创建一个进程

#1.导入包
import multiprocessing

import time

#制定任务函数
def task1():
    for i in range(10):
        print('A--',i+1)
        time.sleep(1)

def task2():
    for i in range(10):
        print('B--',i+1)
        time.sleep(1)

if __name__ == "__main__":
    #创建进程子对象
    p1=multiprocessing.Process(target=task1)
    p2=multiprocessing.Process(target=task2)
    #启动子进程
    p1.start()
    p2.start()


'''

multiprocessing简介 
multiprocessing是python自带的多进程模块，可以大批量的生成进程，在服务器为多核CPU时效果更好，类似于threading模块。
相对于多线程，多进程由于独享内存空间，更稳定安全，在运维里面做些批量操作时，多进程有更多适用的场景  
multiprocessing包提供了本地和远程两种并发操作,有效的避开了使用子进程而不是全局解释锁的线程，
因此，multiprocessing可以有效利用到多核处理  

Process类 在multiporcessing中，通过Process类对象来批量产生进程，使用start()方法来启动这个进程
'''