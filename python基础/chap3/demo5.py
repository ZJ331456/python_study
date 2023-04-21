# 作者：立志成为大神的小白

# 开发时间：2023/3/8 21:50
#赋值运算
i=3+4
print(i)

a=b=c=66
print(a,id(a))
print(b,id(b))
print(c,id(c))

print('--------------支持参数赋值----------')
a=10
print(a)
a+=10
print(a,type(a))
a/=3
print(a,type(a))
a*=6
print(a,type(a))
a//=6
print(a,type(a))

print('---------支持系列解包赋值--------')
a,b,c=1,2,3
print(a,b,c)

# a,b=1,2,3   错误----》因为复制储存变量不够

print('-------交换两个变量值---------')
a,b=1,2
print('交换赋值前：',a,b)
a,b=b,a
print('交换赋值后：',a,b)