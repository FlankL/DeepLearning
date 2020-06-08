#  @Function:  设置图例
#　＠Time:2020/5/27 下午5:05
#  @Author:Flank

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1
y1 = x ** 2
plt.plot(x, y,label='up')
plt.plot(x, y1, color='red', linestyle='--',label='down')

plt.xlim((-1, 2))  # 限制x轴的取值范围
plt.xlabel(r'$I\ am\ x$') # 对x轴进行描述,$表示显示数学字体,r表示正则表达式
newTicks=np.linspace(-1,2,5)#替换x轴的坐标
plt.xticks(newTicks)


plt.ylim((-2, 3))  # 限制y轴的取值范围
plt.ylabel(r'$I\ am\ y$')  # 对y轴进行描述
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$','$bad$','$normal$','$good$','$rellay\ good$'])


plt.legend()#打印图例
plt.show()

