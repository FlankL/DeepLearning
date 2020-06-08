#  @Function:  可见度
#　＠Time:2020/5/27 20:54
#  @Author:Flank
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=2*x+1

plt.figure(num=1,figsize=(8,5))
plt.plot(x,y,lw=10)
plt.ylim(-2,2)

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='red',edgecolor='None',alpha=1))

plt.show()

