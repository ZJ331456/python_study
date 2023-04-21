# 作者：立志成为大神的小白

# 开发时间：2023/3/17 22:46
'''不可变序列'''
s='hello'
print(id(s))
s+='world'
print(s,id(s))

'''可变序列'''
lst=[1,2,3,4,5]
print(id(lst))
lst.append(3)
print(lst,id(lst))