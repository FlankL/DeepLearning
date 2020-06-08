# 使用Ｆilter进行过滤
myList=list(range(0,20))
def fun2(arg):
        return arg % 2==0
# lambda arg : arg%2==0
tmp=filter(fun2,myList)#函数fun2是作为参数传进去，不要加括号（加括号是调用），不然传进去的是函数的返回值
print(list(tmp))
# 如果一个函数是会被调用一次，可以将函数写成匿名函数
def fun3(a,b):
    return a+b
fn4=lambda a,b:a+b
print(fn4(2,3))
print(list(filter(lambda arg : arg%2==0,myList)))
print(list(map(lambda i:i+1,myList)))
# sort()
myList2=["bbb","aa","ccc","dddd"]
print(myList2)
myList2.sort(key=len)
print(myList2)
myList3=[1,'3',2]#直接排序不能排，可以使用ｓｏｒｔ时进行强制类型转换，这只是在比较的时候类型转换，并不影响原ｌｉｓｔ
myList3.sort(key=int)
print(myList3)

# sorted()
myList4=[1,'3',2]
print(sorted(myList4,key=int))
