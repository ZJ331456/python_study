# 作者：立志成为大神的小白

# 开发时间：2023/3/19 20:44
#字符串劈分操作
'''1、split()方法--------->从字符串的左边开始劈分，默认的劈分字符是空格字符，劈分返回的是一个列表
而且可以指定参数sep来指定劈分字符串所用的劈分符
可以通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大劈分次数的时候就会停止继续劈分，剩余的子串会单独作为一部份'''
s='hello world hello python'
lst=s.split()
print(lst)
print(s.split(sep='o'))
print(s.split(sep='o',maxsplit=3))

print('--------------------------------------------------')
'''2、rsplit()方法--------->从字符串的右边开始劈分，默认的劈分字符是空格字符，劈分返回的是一个列表 
而且可以指定参数sep来指定劈分字符串所用的劈分符 
可以通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大劈分次数的时候就会停止继续劈分，剩余的子串会单独作为一部份'''
s='hello world hello python'
lst=s.rsplit()
print(lst)
print(s.rsplit(sep='o'))
print(s.rsplit(sep='o',maxsplit=3))