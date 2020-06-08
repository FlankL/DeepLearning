#  @Function: 统计方法
#　＠Time:2020/6/1 下午3:50
#  @Author:Flank
import  numpy as np
#布尔值True和False会被转为1和0参与计算
a1=np.arange(10).reshape(2,5)
print(np.amin(a1))#或a1.min()
print(np.amax(a1))#或a1.max()
print("平均值:",np.mean(a1))
print("中位数:",np.median(a1))
print("标准差:",np.std(a1))
print("方差:",np.var(a1))