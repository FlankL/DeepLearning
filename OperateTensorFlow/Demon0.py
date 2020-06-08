#  @Function:  
# 　＠Time:2020/6/3 下午2:56
#  @Author:Flank
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# create x data
xData = np.random.rand(100).astype(np.float32)
# weight:0.1,bias:0.3
yData = xData * 0.1 + 0.3
plt.plot(xData, yData)
plt.show()
# 开始创建tensorflow结构
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 创建一些变量,[1]:表示一维,-1.0:表示起始位置,1.0:表示结束位置
Biases = tf.Variable(tf.zeros([1]))
predictY = Weights * xData + Biases  # 不断学习y表示预测后的结果值
loss = tf.reduce_mean(tf.square(predictY - yData))
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 创建一个梯度下降的优化器,0.5表示学习效率(通常<1)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()  # 初始化上面创建的变量,初始化上面创建的网络结构
# 结束tensorflow结构

session = tf.Session()
session.run(init)  # 创建一个会话,来运行创建的网络结构

for step in range(201):  # 一步一步的训练,训练201次
    session.run(train)
    if step % 20 == 0:
        print(step, session.run(Weights), session.run(Biases))
