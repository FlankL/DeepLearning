#  @Function:  3D图像
#　＠Time:2020/5/27 21:52
#  @Author:Flank

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # 添加3D坐标轴的显示

fig=plt.figure()
ax=Axes3D(fig)#添加一个3D坐标轴
#X,Y vlaue
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
#height value
Z=np.sin(R)

#画3D图
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))#rstide,cstride表示行，列颜色跨度
#画等高线图
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)



plt.show()