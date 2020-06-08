#  @Function:  索引和切片
#　＠Time:2020/6/1 下午2:48
#  @Author:Flank
import  numpy as np

# 1.切片[i:j:k]i:起始下标,j:结束下标,k步长
#取值
a1=np.arange(10)
print("a1:",a1)
print("a1[1:9:2]:",a1[1:9:2])
# print("a1[9:1:-2]:",a1[1:9-2])#错误的
print("a1[9:1:-2]:",a1[9:1:-2])
print("a1[4:-3]",a1[4:-2])
print("[::2]",a1[::2])
#赋值
a1[::2]=0
print(a1)
a2=np.arange(10)
a2[:6]=0
print(a2)
a3=np.arange(10)
a3[:]=10
print(a3)
#1.2.多维切片[i:j,m:n]i,j表示起始结束行,m,n表示列
b1=np.arange(16).reshape(4,4)
print("b1:",b1)
print("b1[:2]",b1[:2])#获取两行
print("b1[:2,:2]",b1[:2,:2])#获取前两行的前两列

#2.索引[i:j]表示行,j表示列
c1=np.arange(10).reshape(2,5)
print("c1",c1)
print("c1[1]",c1[1])
print("c1[:3,[0,1]]",c1[:3,[0,1]])#前3行第0,1列元素


