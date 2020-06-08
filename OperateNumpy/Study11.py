#  @Function: 文件输入和输出
# 　＠Time:2020/6/2 上午10:56
#  @Author:Flank

import numpy as np

a1 = np.arange(12, dtype=np.uint8).reshape(3, 4)
# 保存为二进制文件
# 保存为通用的二进制格式
a1.tofile('file/normal_a1.bin')
b = np.fromfile('file/normal_a1.bin', dtype=np.uint8)  # 按照uint8的类型读入数据
print(b)
print(b.dtype)
print(b.shape)  # 一维数组
# 保存为numpy格式的二进制文件
b = np.arange(12, dtype=np.uint8).reshape(4, 3)
np.save('file/np_a1', a1)
a2 = np.load('file/np_a1.npy')
print(a2)
print(a2.dtype)
np.savez('file/np_a2', a1, b)
result = np.load('file/np_a2.npz')  # 返回的多个数组保存为字典类型,键值为arr_0,arr_1,arr_2..
print(result['arr_0'])
print(result['arr_1'])

# 保存为文本文件
np.savetxt('file/a1.txt', a1, fmt='%d', delimiter=',')  # 保存为整数(默认保存为%.18e格式,以空格分分隔),用逗号分隔
a3 = np.loadtxt('file/a1.txt', delimiter=',', dtype=np.uint8)  # 读入的时候也需要指定逗号分隔
print(a3)
print(a3.dtype)

# 文件对象file
f = open('file/a2.bin', 'wb+')
a1.tofile(f)
b.tofile(f)
f.close()
