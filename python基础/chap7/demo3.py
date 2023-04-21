# 作者：立志成为大神的小白

# 开发时间：2023/3/17 21:28


'''key的判断'''
scores={'张三':100,'李四':80,'王五':40}
print('张三' in scores)
print('张三' not in scores)


#字典的删除操作
del scores['张三']
print(scores)
# del scores
# print(scores)
scores.clear()  #清空整个字典
print(scores)
#字典的添加操作
scores['陈六']=99
print(scores)

#字典的修改操作
scores['陈六']=66
print(scores)
