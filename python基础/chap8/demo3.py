# 作者：立志成为大神的小白

# 开发时间：2023/3/18 14:43
t=(1,[2,3,4],5)
print(t,type(t))
print(t[0],type(t[0]))
print(t[1],type(t[1]))
# t[0]=11   ------------------>元组里面不可变元素值不可修改
t[1].append(100)
print(t)
t[1].extend([22,33])
print(t)