#  @Function:  Series对象的增删改查
# 　＠Time:2020/6/2 下午1:57
#  @Author:Flank
import numpy as np
import pandas as pd

# 1. Series
s = pd.Series(data=np.arange(3), index=np.array(list('abc')))
print(s)
# 1查-使用[]查看(基于索引)
print(s['b'])
print(s['a':'c'])  # 利用标签切片的时候左右都是闭区间
print(s[0:2])  # 范围，左闭右开，返回Series切片
print('*' * 20)
print(s[[0, 2, 1]])  # 获取多个值
print(s[['a', 'b']])
print(s[[False, True, False]])  # 使用掩码,只是长度必须和Series相同

# 2.改
# 改值
s1 = s.copy()  # 深copy,拷贝数据结构包含的所有信息
s1['a'] = 10
s1['b'] = 10
print(s1)
print(s.replace(to_replace=[0, 1], value=[100, 100], inplace=False))  # to_replace表示要修改的值,value表示改成什么值,inplace是否在原地修改

# 3.增
s1['d'] = 4  # 增加一行
print(s1)
s2 = pd.Series([12, 32], index=['e', 'f'])
s3 = s.append(to_append=s2, ignore_index=False)  # 增加多行,to_append:另一个series或多个Series构成的列表
print(s3)

# 4.删
s3.drop('f',inplace=True)
print(s3)