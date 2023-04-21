# 作者：立志成为大神的小白

# 开发时间：2023/3/19 21:34
#字符串的其他操作方法
'''1、replace()----------->字符串替换，第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串
替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数'''
s='hello world python'
print(s.replace('python','java'))
s='hello python python python'
print(s.replace('python','java',2))
print(s.replace('py','xx',2))
'''2、join()-------------->字符串合并，将列表或元组中的字符串合并成一个字符串'''
lst=['hello','world','python']
print(''.join(lst))
print('&'.join(lst))

t=('hello','world','python')
print('+'.join(t))