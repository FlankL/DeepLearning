#  @Function:  
#　＠Time:2020/5/27 下午3:29
#  @Author:Flank
import  matplotlib.pyplot as plt

# 只传入一个数组作为参数,会默认数组的值为y轴坐标
# x:1,3,5,7 y:2,4,6,8
plt.plot([1,3,5,7],[2,4,6,8])
plt.ylabel("some numbers")
plt.show()
