#  @Function:merge合并
# 　＠Time:2020/6/2 下午3:55
#  @Author:Flank
import numpy as np
import pandas as pd
# 数据库表的左,右连接,内连接,外连接,全连接
left = pd.DataFrame({
    'key': ['k0', 'k1', 'k2', 'k3'],
    'A':['a0','a1','a2','a3']   ,
    'B':['b0','b1','b2','b3']
})
right = pd.DataFrame({
    'key': ['k0', 'k1', 'k2', 'k3'],
    'C':['c0','c1','c2','c3'],
    'D':['d0','d1','d2','d3']
})
print(left)
print(right)
res=pd.merge(left,right,on='key')#on表示合并哪一列
print(res)
