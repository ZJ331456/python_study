# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：进程注意事项1_主进程会等待子进程执行完.py 
@Author  ：zero 
@Date    ：2023/4/21 16:33  
"""
import multiprocessing
import time

def task1():
    for i in range(5):
        print('task1 -',i+1)
        time.sleep(0.5)

if __name__ == '__main__':
    p=multiprocessing.Process(target=task1)

    #方式二： 设置守护进程
    #注意：设置进和时，需要开始进程之前设置
    p.daemon =  True
    p.start()
    time.sleep(0.5)

    #方式一：
    #再主进程结束之前，手动调用方法结束子进程
    # p.terminate()

    print('Main Process Over')