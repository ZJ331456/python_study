# 作者：立志成为大神的小白

# 开发时间：2023/3/17 21:41
scores={'张三':100,'李四':80,'王五':40}
'''keys()----->获取字典中所有key'''
key=scores.keys()
print(key)
print(type(key))
print(list(key))


'''values()---------> 获取字典中所有value'''
value=scores.values()
print(value)
print(type(value))
print(list(value))

'''items()---------->获取字典中所有的key,value对'''
item=scores.items()
print(item)
print(type(item))
print(list(item))