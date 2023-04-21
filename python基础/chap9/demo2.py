# 作者：立志成为大神的小白

# 开发时间：2023/3/18 21:42
#字符串的常用操作
#字符串的查询操作
#1、index()-------------》查找子串第一次出现的位置
s='helloworld,helloworld'
print(s.index('world'))
# print(s.index('q')) 若查找子串不存在时，会抛出ValueError: substring not found异常

#2、rindex()-------------》查找子串最后一次出现的位置
print(s.rindex('world'))
# print(s.rindex('www')) 若查找子串不存在时，会抛出ValueError: substring not found异常


#3、find()---------------》查找子串第一次出现的位置
print(s.find('world'))
print(s.find('www'))   #若子串不存在，则返回-1


#4、rfind()-----------------》查找子串最后一次出现的位置
print(s.rfind('world'))
print(s.rfind('www'))   #若子串不存在，则返回-1