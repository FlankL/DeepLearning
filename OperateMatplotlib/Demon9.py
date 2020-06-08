#  @Function:  打印图像
#　＠Time:2020/5/27 21:37
#  @Author:Flank
import matplotlib.pyplot as plt
import numpy as np

a =np.array(list(np.arange(9))).reshape(3,3)#创建一个3*3的矩阵
plt.imshow(a,interpolation='nearest',cmap=plt.cm.bone,origin='upper')
plt.colorbar(shrink=0.9)#shrink表示压缩到原来的90%
print(a)
plt.xticks(())
plt.yticks(())
plt.show()