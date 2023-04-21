# 作者：立志成为大神的小白

# 开发时间：2023/3/7 19:42
#输出数字
print(1111)
#输出字符
print("你好")
print('hello')

#含有运算符的表达式
print(2*9)
print(1+3)

#将数据输出文件中
#注意点：1、所制定盘符存在 2、使用file=fp
fp=open('D:/first.txt','a+')#a+意思就是如果文件不存在就会新创建一个文件，如果存在就在源文件后面追加
print('helloworld',file=fp)
fp.close()

#不进行换行输出
print('a','b','c')