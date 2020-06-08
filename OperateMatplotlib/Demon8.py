#  @Function:  等高线图
#　＠Time:2020/5/27 21:25
#  @Author:Flank
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # calc hetight
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)

X,Y=np.meshgrid(x,y)
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)#画等高线：坐标，高度，8表示等高线分成8部分
#.5就表示0.5
C=plt.contour(X,Y,f(X,Y),8,colors='black')#画等高线的线

plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()