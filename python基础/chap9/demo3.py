# 作者：立志成为大神的小白

# 开发时间：2023/3/19 19:58
#字符串的大小写转换操作
s='HelloWORLD'
print(s.upper(),id(s),id(s.upper()))  #upper()方法--------》将字符串中所有字符都转化成大写字母

print(s.lower(),id(s),id(s.lower()))   #lower()方法------》字符串中所有字符都转化成小写字母

print(s.swapcase(),id(s),id(s.swapcase()))  #swapcase()方法----》将字符中所有大写字母转成小写，所有小写转成大写

print(s.capitalize(),id(s),id(s.capitalize()))  #capitalize()方法-----------》将第一个字符转成大写，其余字符转成小写

a='hello,world'
b='helloworld'
print(a.title(),b.title())  #title()方法---------》把每个单词的第一个字符转化为大写，把每个单词的剩余字符转化为小写
s='s19'
print(s.upper())
print(a.capitalize())