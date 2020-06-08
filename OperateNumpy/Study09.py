#  @Function: 排序
# 　＠Time:2020/6/2 上午10:18
#  @Author:Flank
import numpy as np

a1 = np.arange(10)
np.random.shuffle(a1)
print("a1排序前", a1)
a2 = np.sort(a1)  # 返回一个新的数组 a1.sort()#修改原数组
print(a2)
# 多维数组排序
a1.shape = (2, 5)
print("按列排序", np.sort(a1, axis=1))
print("按行排序", np.sort(a1, axis=0))
