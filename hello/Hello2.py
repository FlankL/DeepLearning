a,b,c=tuple(range(0,3))
print(a,b,c)
# 变量前加＊，这样变量会获取元组中所有剩余的元素
a,*b=tuple(range(0,3))
print(a,b)
# 解包的应用，两个变量互换值
d=20
e=30
d,e=e,d
print(d,e)
# scope=locals()
# print(scope)
def jiCheng(a):
    if a==1:return 1
    return jiCheng(a-1)*a
print(jiCheng(5))
