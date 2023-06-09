# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：杨辉三角.py
@Author  ：zero 
@Date    ：2023/3/25 22:38  
"""

print('%10d'%99)
print('%d'%666)
'''%10d里面的10表示宽度'''
print('%.3f'%3.1415926)
'''%.3f里面的.3表示保留下小数点后3位'''
print('%10.3f'%3.1415926)
'''同时表示宽度和精度
10.3f表示总宽度为10，保留小数点后3位'''

print('============================================================')
print('{0:.3}'.format(3.1415926))
'''.3表示的是保留一共3位数'''
print('{0:.3f}'.format(3.1415926))
'''.3f表示的是小数点后保留三位'''
print('{0:10.3f}'.format(3.1415926))