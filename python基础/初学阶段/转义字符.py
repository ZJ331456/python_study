# 作者：立志成为大神的小白

# 开发时间：2023/3/7 20:18

#转义字符
print('hello\nworld')  #\+转义字符的首字母 如\n表示换行
print('hello\tworld')  #如\t与tab键相同
print('helloooo\tworld')  #不过\t是按第一个字节来的，从第一个字符到\t是4的倍数（理解的话）
print('h\tworld')
print('hello\rworld')  #\r是对前面内容的覆盖
print('hello\bworld')  #\b是向前退一格

print('老师说:\'大家好\'')
print('http:\\\\baidu.com')

#原字符--不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或者R
print(r'hello\nworld')
#注意：使用原字符最后一个字符不能是反斜杠\
#print(r'hello\nworld\')