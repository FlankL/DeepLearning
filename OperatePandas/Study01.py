#  @Function:创建Series和DataFrame对象
#　＠Time:2020/6/2 下午1:28
#  @Author:Flank
import numpy as np
import  pandas as pd
from pandas import Series
from  pandas import DataFrame
#1.创建Series
data=np.arange(5)+1
index=np.array(list("abcde"))
s=Series(data=data,index=index)#如果提供index,则必须和data长度相同,不提供则默认数值索引
print(s)
print(s.index)
print(s.values)
print(s.shape)
print('*'*30)
#2.创建DataFrame
data1=np.arange(6).reshape(2,3)
index=['a','b']
columns=['A','B',"c"]
df=DataFrame(data=data1,index=index,columns=columns)
data3 = { 'A' : { 'a':1, 'b':4}, 'B': {'a':2,'b':5}, 'C':{'a':3, 'c':6} }
df1 = pd.DataFrame(data3)
print(df)
print(df.index)
print(df.columns)
print(df.values)
print(df.shape)
print(df.dtypes)
print(df1)
# 3.由Excel文件创建
excelDf=pd.read_excel('file/TestExcel.xlsx')
print(excelDf)
