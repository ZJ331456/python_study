# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo10.py 
@Author  ：zero 
@Date    ：2023/4/5 22:46  
"""
import time

#第三方模块的安装以使用
import schedule
def job():
    print('哈哈------------')

schedule.every(3).seconds.do(job)#每隔3秒执行一下job()方法

while True:
    schedule.run_pending()
    time.sleep(1) #休息一秒