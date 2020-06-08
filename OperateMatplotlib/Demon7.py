#  @Function:  柱状图
#　＠Time:2020/5/27 21:14
#  @Author:Flank
import matplotlib.pyplot as plt
import numpy as np

n=12 #规定12个柱状图，也就是12个数字
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
# 画柱状图
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')#向上
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')#向下

for x,y in zip(X,Y1):
    # ha :horzontal alignment
    plt.text(x+0.1,y+0.05,'%.2f'%y,ha='center',va='bottom')# 位置坐标，显示的值保留两位小数，水平对齐方式 纵向对齐方式

for x,y in zip(X,Y2):
    # ha :horzontal alignment
    plt.text(x+0.1,-y-0.05,'%.2f'%y,ha='center',va='top')# 位置坐标，显示的值保留两位小数，水平对齐方式 纵向对齐

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()

