# @Function:firstDemon
# @Time: 2020/6/9 下午4:05
# @Authon: flank
import numpy as np
import tensorflow as tf

# 1. 创建input和output
xData = np.random.rand(100).astype(np.float32)
yData = xData * 0.1 + 0.3
# 2. 创建weights和ｂias,和预测数据
Weights = tf.Variable(tf.random_uniform([1, ], -1.0, 1.0))  # [1,]表示输出一个数
bias = tf.Variable(tf.ones([1, ]))
predY = xData * Weights + bias
# 3. 创建损失函数，优化策略，指定学习效率
loss = tf.reduce_mean(tf.square(predY - yData))  # 均方误差损失函数
optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
# 4. 初始化变量，生成session接口
init = tf.initialize_all_variables()
session = tf.Session()
session.run(init)
# 5. 训练，反向传播不断修正weight,bias
for step in range(201):
    session.run(optimizer)  # 每训练一次优化一次
    if step % 20 == 0:
        print(step, session.run(loss), session.run(Weights), session.run(bias))
