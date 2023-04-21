# 作者：立志成为大神的小白

# 开发时间：2023/3/19 20:16
#字符串内容对齐操作
'''1、center()居中对齐，有两个参数，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，
不过不填默认是空格。如果设置宽度小于实际宽度则返回原字符'''
s='hello,python'
print(s.center(20,'*'))
print(s.center(10))
print(s.center(20))


print('-----------------------------')
'''2、ljust()方法------>左对齐(在字符串最右边填充指定填充符)，有两个参数，第一个参数指定宽度，第二个参数指定填充符，
第二个参数可选， 不过不填默认是空格。如果设置宽度小于实际宽度则返回原字符'''
s='hello,python'
print(s.ljust(20,'*'))
print(s.ljust(10))
print(s.ljust(20))


print('---------------------------------')
'''2、rjust()方法------>右对齐(在字符串最左边填充指定填充符)，有两个参数，第一个参数指定宽度，第二个参数指定填充符， 
第二个参数可选， 不过不填默认是空格。如果设置宽度小于实际宽度则返回原字符'''
s='hello,python'
print(s.rjust(20,'*'))
print(s.rjust(10))
print(s.rjust(20))


print('---------------------------')
'''zfill()方法--------->右对齐，左边用0填充，该方法只接受一个参数，
用于指定字符串宽度，如果指定的宽度小于等于字符串长度，返回字符串本身'''
s='hello,python'
s1='-1024'
s2='f-1024'
s3='%ppp'
print(s.zfill(20),'\n',s1.zfill(10),'\n',s2.zfill(10))

print(s1.rjust(20))
print(s3.zfill(9))
'''注意：zfill()和rjust()方法的区别在于，如果字符串首位为非字母类和数字类符号（+-#%等符号）填充的数字0会在首个字符之后，
而rjust()方法不会，它总是在字符串之前填充'''