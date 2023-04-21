# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：获取进程编号.py 
@Author  ：zero 
@Date    ：2023/4/21 15:24  
"""

#导入包
import multiprocessing
import time
import os

#创建任务
def task1():
    # 获取当前进程对象
    mp = multiprocessing.current_process()
    print(mp)
    print(f"任务1的PID是{os.getpid()},父进程的PID是{os.getppid()}")
    time.sleep(1)

def task2():
    # 获取当前进程对象
    mp=multiprocessing.current_process()
    print(mp)
    print(f"任务1的PID是{os.getpid()},父进程的PID是{os.getppid()}")
    time.sleep(1)


if __name__=="__main__":
    print(f"主任务的PID是{os.getpid()},父进程的PID是{os.getppid()}")

    #创建子进程
    p1=multiprocessing.Process(target=task1,name='p2')
    p2=multiprocessing.Process(target=task2,name='p1')
    '''name的作用是给当前进程命名'''
    #获取当前进程对象
    mp=multiprocessing.current_process()
    print(mp)
    '''
    <_MainProcess name='MainProcess' parent=None started>
    '''
    print(p1)
    print(p2)
    '''
    <Process name='Process-1' parent=3440 initial> 
    <Process name='Process-2' parent=3440 initial>
    '''

    #启动子进程
    p1.start()
    p2.start()

    print(p1)
    print(p2)
    '''
    <Process name='Process-1' pid=2956 parent=6688 started> 
    <Process name='Process-2' pid=13780 parent=6688 started>
    '''


    '''
    获取当前进程编号os.pid()
    获取当前进程的父进程编号os.ppid()
    获取当前进程对象multiprocessing.current_process()
    '''