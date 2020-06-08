# @Function:  数组运算
# ＠Time:2020/6/1 下午2:10
#  @Author:Flank
import numpy as np

a1 = np.arange(6).reshape(2, 3)
a2 = np.arange(6).reshape(3, 2)
print("原始a1:", a1)
print("原始a2:", a2)
# 1.数组与标量的运算(会产生一个新的数组,不影响到原来的)
print("a1*2:", a1 * 2)
print("a1+2:", a1 + 2)
# 2. 数组与数组的运算(会产生一个新的数组,不影响到原来的)
print("a1+a1:", a1 + a1)  # 对应元素相加
print("a1*a2:", a1 * a1)  # 对应元素相乘,等同于a1**2
# 3.*=,+=会修改原数组,不会创建新数组
a1 *= 2
print("a1*=2", a1)
a1 += 2
print("a1+=2", a1)
# 4.shape相同的数组可以产生布尔值,逐元素比较,不同shape不能比较
a3 = a1 + 1
print("a3:", a3)
print("compare a1, a3:", a3 > a1)
