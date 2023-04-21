# 作者：立志成为大神的小白

# 开发时间：2023/3/8 22:30
#布尔运算符

a,b=1,2
print(a==1 and b==2)
print(a==1 and b==3)
print(a==2 and b!=2)
'''
and(并且)只有当两个值都为真时结果才为真
or（或者）有一个真的时候结果就为真
not（对bool类型取反），真--》假//假--》真
'''
print(not a==1)
print(not a!=1)

print('--------in与not in的区别-----------')
s='hello world'
print('h' in s)
print('q' in s)
print('h' not in s)
print('q' not in s)
'''
in表示某字符是否在该字符串中
not in表示某字符是否不在该字符串中
'''