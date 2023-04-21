# 作者：立志成为大神的小白

# 开发时间：2023/3/17 21:11
'''字典元素的获取'''
#1.使用[]，如：scores['张三']
scores={'张三':100,'李四':80,'王五':40}
print(scores['张三'])
# print(scores['麻七'])


print('------------------------')
#2、get()方法，如：scores.get('张三')
print(scores.get('张三'))
print(scores.get('麻七'))
print(scores.get('麻七',90))