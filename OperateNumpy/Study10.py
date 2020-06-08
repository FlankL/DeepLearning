#  @Function:  搜索计数
# 　＠Time:2020/6/2 上午10:34
#  @Author:Flank
import numpy as np

a1 = np.arange(10).reshape(2, 5)
print(np.argmax(a1))  # 返回flatten之后的索引
print(np.argmax(a1, axis=0))  # 返回沿轴最大值索引
print(np.argmin(a1, axis=0))  # 返回沿轴最小值
print(np.argwhere(a1 < 6))  # 返回符合条件的元素索引
print(np.nonzero(a1))  # 返回非零元素的索引
print(np.where(a1 > 3, -3, a1))  # 将arr1中大于3的全部变为-3
print(np.where(a1 > 3, -a1, a1))  # 将arr1中大于3的全部变为该值的相反数
print(np.searchsorted([1, 2, 3, 4, 5], 3))
print(np.extract(a1 > 10, a1))
print(a1)
