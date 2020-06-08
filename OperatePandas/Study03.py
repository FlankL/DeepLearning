#  @Function:  DataFrame对象的增删改查
# 　＠Time:2020/6/2 下午2:53
#  @Author:Flank
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list('ABCD'))
print(df)
# 1.查
print(df[['A', 'C']])  # 列操作
print(df[0:1])
print("*" * 20)

# 2.改
df1 = df.replace(to_replace=0, value=100, inplace=False)  # 改值
# 该索引:直接改或rename
print(df1)

# 3.增
df1.loc[3] = [3, 2, 3, 4]  # 增加一行
print(df1)
df2 = pd.concat([df, df1], axis=0)  # 增加多行
print(df2)
df1['E'] = [1, 1, 1, 1]  # 增加一列
print("*" * 20)
print(df1)
df2 = pd.concat([df, df1], axis=1)  # 增加多列

# 4.删
df4 = df1.drop([3], axis=0)  # 删除多行
print("*" * 20)
print(df4)
del df4['E']
print(df4)  # 删除一列
df5 = df4.drop(['C', 'D'], axis=1)  # 删除多列
print(df5)
