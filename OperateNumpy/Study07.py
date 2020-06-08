#  @Function:  形状变换
#　＠Time:2020/6/1 下午4:01
#  @Author:Flank
import  numpy as np
'''
数组形状变换
    重塑
    扁平化处理
    数组合并
    数组拆分
    数组扩充
    数组转置和轴对换
'''
# 1.重塑
# reshape和resize的区别前者不会修改自身返回一个新对象,后者会修改自身
a=np.arange(10)
a1=a.reshape((2,5),order='F')#order表示按行还是按列读
print(a)
print(a1)
a.resize(5,2)
print(a)
# 1.2 多为数组重塑
a2=np.arange(24).reshape(3,4,2)
print(a2)

#2. 扁平化处理
b1=np.arange(12).reshape(3,4)
print("*"*20)
print("b1:",b1)
b2=b1.flatten()#order='C'按列
b3=b1.flatten(order='F')#order='F'按行
print("b2:C:",b2)
print("b3:F:",b3)
#3.数组合并

