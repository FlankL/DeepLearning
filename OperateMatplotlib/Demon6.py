#  @Function:  散点图
#　＠Time:2020/5/27 21:01
#  @Author:Flank
import matplotlib.pyplot as plt
import numpy as np


n=1024
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X) # 给相同值添加颜色

plt.figure("1")
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(())#隐藏所有标尺
plt.yticks(())

plt.figure("2")
plt.scatter(np.arange(10),np.arange(10))
plt.show()

plt.show()

