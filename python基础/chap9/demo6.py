# 作者：立志成为大神的小白

# 开发时间：2023/3/19 21:03
#判断字符串的操作方法
'''isidentifier()方法，判断指定的字符串是不是合法的标识符'''
s='hello,world'
print('1',s.isidentifier())
s1='hello world'
print('2',s1.isidentifier())
s2='helloworld'
print('3',s2.isidentifier())
print('4','张三'.isidentifier())
print('5','张三11'.isidentifier())
print('6','张三_'.isidentifier())
print('7','ss*'.isidentifier())
'''isspace()方法判定指定的字符串是否全部由空白字符串组成（回车、换行，水平制表符）'''
print('8','\n'.isspace())
print('9',' '.isspace())
print('10','1'.isspace())
'''isalpha()方法定指定的字符串是否全部由字母组成'''
print('11','hello'.isalpha())
print('12','w1'.isalpha())
print('13','张三'.isalpha())
'''isdecimal()方法定指定的字符串是否全部由十进制的数字组成'''
print('14','1234'.isdecimal())
print('15','12w'.isdecimal())
print('16','一'.isdecimal())
'''isnumeric()方法定指定的字符串是否全部由数字组成'''
print('17','123'.isnumeric())
print('18','一二三'.isnumeric())
print('19','IIIIIIIV'.isnumeric())
print('20','①②③'.isnumeric())
'''isalnum()方法定指定的字符串是否全部由字母和数字组成'''
print('21','张三66'.isalnum())
print('22','IIIIIIIV'.isalnum())
print('23','①②③'.isalnum())