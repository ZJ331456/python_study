# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo14.py 
@Author  ：zero 
@Date    ：2023/4/6 21:56  
"""

#优化图片复制方法
with open('wit.png', 'rb') as src_img:
    with open('copy2wit.png', 'wb') as target_img:
        target_img.write(src_img.read())