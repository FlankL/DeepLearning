#  @Function:  修改坐标轴,文字,标尺,位置
# 　＠Time:2020/5/27 下午4:11
#  @Author:Flank
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1
y1 = x ** 2
plt.plot(x, y)
plt.plot(x, y1, color='red', linestyle='--')

plt.xlim((-1, 2))  # 限制x轴的取值范围
plt.xlabel(r'$I\ am\ x$') # 对x轴进行描述,$表示显示数学字体,r表示正则表达式
newTicks=np.linspace(-1,2,5)#替换x轴的坐标
plt.xticks(newTicks)


plt.ylim((-2, 3))  # 限制y轴的取值范围
plt.ylabel(r'$I\ am\ y$')  # 对y轴进行描述
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$','$bad$','$normal$','$good$','$rellay\ good$'])

#修改坐标轴的位置
# gca = "get current axis"
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#设置x轴
ax.yaxis.set_ticks_position('left')#设置y轴

ax.spines['bottom'].set_position(('data',0))#设置x轴是从y轴-1的位置开始
ax.spines['left'].set_position(('data',0))







plt.show()

