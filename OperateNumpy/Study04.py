#  @Function:  数组拷贝
#　＠Time:2020/6/1 下午2:32
#  @Author:Flank
import  numpy as np
'''
拷贝
NumPy中拷贝分为三种情况：

完全不拷贝

一个数组的任何变化都反映在另一个数组上，包括值变化和形状变化

浅拷贝

一个数组值会变化会反映在另一个数组上，但是形状不变化

深拷贝

创建原数组的副本，副本的任何变化都不会反映在原数组上
'''
# 完全不拷贝
a=np.arange(12)
b=a#指向的是相同的地址
b.shape=(3,4)
print(b is a )
print(a)
print(b)
# 浅拷贝
a=np.arange(12)
c=a.view()
c.shape=(3,4)
print(c is a )
print(a)
print(c)
# 深拷贝
a=np.arange(12)
d=a.copy()
d[0]=100
d.shape=(2,6)
print(a)
print(d)
