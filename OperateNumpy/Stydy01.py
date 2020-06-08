#  @Function:  数组的创建
#　＠Time:2020/6/1 上午11:26
#  @Author:Flank
import numpy as np
import matplotlib.pyplot as plt

#1.直接赋值,并指定元素的数据类型
array1=np.array([[1,2],[3,4]],dtype=np.uint8)
print(array1,array1.dtype)
#2.产生指定步长的随机数
array2=np.arange(0,15,1).reshape(3,5)#arrage(起始,结束不包括,步长),创建3行5列的矩阵
array2.dtype=np.uint8
print("数组的维度",array2.ndim)
print("数组的形状",array2.shape)
print("数组的元素个数",array2.size)
print("数组中元素的数据类型:",array2.dtype)
print("数组中元素的字节数",array2.itemsize)
#3.产生指定元素个数的随机数
array3=np.linspace(0,10,10)#linespace(开始,结束包括,元素个数)
print(array3)
#4.产生指定常量填充的矩阵
a4=np.zeros([3,4])#根据指定形状创建一个全为0的ndarray对象
a5=np.zeros_like(array1)#传入一个数组作为参数，根据该数组的形状和dtype创建一个全0的ndaray对象
a6=np.ones([3,4])#根据指定形状创建一个全为1的ndarray对象
a7=np.ones_like(array1)
a8=np.empty([3,4])#根据指定形状创建ndarray对象，只分配内存但是不填充任何值
a9=np.full([3,4],fill_value=10)#根据指定形状传建一个ndarray对象，并用fill_value的值进行填充
a10=np.eye(3)#传入一个整数N，创建一个N * N的单位矩阵
a11=np.identity(3)#传入一个整数N，创建一个N * N的单位矩阵
print(a4)
print(a5)
print(a6)
print(a7)
print(a9)
print(a10)
print(a11)
print('#'*18)
#5.产生复杂的随机数
a12=np.random.rand(2)#产生0,1之间的随机数,2表示个数
a13=np.random.randn(10)#产生符合标准正态分布的随机数,10表示个数
a14=np.random.randint(1,10,size=(2,4))#产生1:low,hight:10,size:表示输出2*4矩阵
a15=np.random.normal(1,2,2)#产生符合正态分布的随机数
#uniform:产生符合均匀分布的随机数
#seed:产生随机种子数
# choice: 从指定的样本中随机选择数据
# shuffle:将指定的样本的元素顺序打乱
print(a12)
print("a13",a13)
print("a14",a14)