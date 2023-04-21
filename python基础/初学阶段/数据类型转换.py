# 作者：立志成为大神的小白

# 开发时间：2023/3/8 16:22

name='张三'
age=20
print(type(name),type(age))
#print('我叫'+name,'今年'+age+'岁')  当str类型与int类型连用时会报错，解决方法：类型转换
print('我叫'+name,',今年'+str(age)+'岁') #str()就是将别的数据类型强制转换成str类型
                                        #还有int()和float()
                                        #注意 若字符串里面并非数字串则转换不了
