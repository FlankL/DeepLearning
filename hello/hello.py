# 乘方
import math
import time

a = 2 ** 3

print(a)
if (a > 3):
    print("a大于3")
b = "hello,world"
for letter in b:
    print(letter)
tmpList = ["apple", "banana", "mango"]
for list in tmpList:
    print(list)
for index in range(len(tmpList)):
    print(tmpList[index], len(tmpList))
print(id(a))  # 显示变量在内存中的地址
print(dir(math))  # 显示类中的方法
print(time.time())  # 输出时间戳
print(time.localtime()) #输出时间元组
print(time.asctime()) # 输出格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  #输出自定义格式化时间
#定义函数
"""
 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""
def fun1(name):
    print(name)
    return 3
print(fun1("小明"))
#可变形参个数函数
def fun2(arg1,*tupple):
    print(arg1)
    for var in tupple:
        print(var)
fun2(10,[2,3])
fun2(10,2,3)
#定义匿名函数
sum=lambda arg1,arg2:arg1+arg2
print(sum(1,2))
#读取键盘输入
# str=input()
# print(str)
fo=open("./foo.txt","w")
print("文件名:",fo.name)
print("是否已经关闭",fo.close())
print("访问模式",fo.mode)
print("末尾是否强制加空格",fo.softspace)

fo.close()