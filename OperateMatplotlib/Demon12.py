#  @Function:  制作动画
#　＠Time:2020/5/28 上午10:44
#  @Author:Flank

import  numpy as np
import  matplotlib.pyplot as plt
from matplotlib import animation


fig,ax=plt.subplots()

x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,

#生成动画
ani=animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=10,blit=False)

plt.show()