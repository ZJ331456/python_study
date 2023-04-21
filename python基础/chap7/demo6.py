# 作者：立志成为大神的小白

# 开发时间：2023/3/17 22:25
items=['Fruits','Books','Others']
prices=[30,66,23]

d={item:price for item,price in zip(items,prices)}
print(d)
d={item.upper():price for item,price in zip(items,prices)}
print(d)