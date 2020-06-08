#  @Function: 最基本的画图
#　＠Time:2020/5/27 下午3:49
#  @Author:Flank

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50)
y=2*x+1
y2=x**2

plt.figure()#创建一个图像
plt.plot(x,y)#横坐标,纵坐标

plt.figure()#创建第二个图像,下面的图都属于这张图像
#将两条线放在同一个图像中
plt.plot(x,y2)
plt.plot(x,y,color='red',linewidth=1.0,linestyle='--')
plt.show()