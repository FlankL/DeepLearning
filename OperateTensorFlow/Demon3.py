#  @Function:  tensorboard网络可视化
# 　＠Time:2020/6/9 23:16
#  @Author:Flank
import tensorflow as tf
import numpy as np


def add_layer(inputs, inSize, outSize, n_layer, activation_function=None):
    '''
    添加神经层
    :param inputs:输入数据
    :param inSize:权重的size
    :param outSize:权重的size
    :param activation_function:是否有激励函数
    :return:返回该层的运算结果
    '''
    layer_name = 'layer%s' % n_layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([inSize, outSize]), name='Weight')  # 定义一个insize行，outSize列的矩阵
            tf.summary.histogram(layer_name + "/weights", Weights)
        with tf.name_scope('bias'):
            biases = tf.Variable(tf.zeros([1, outSize]) + 0.1, name='b')  # 权重和偏移在每一次训练中会修改
            tf.summary.histogram(layer_name + "/bias", biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases  # 预测出来的值
        # 预测出来的值是否过激励函数
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + "/outputs", outputs)
        return outputs


if __name__ == '__main__':
    xData = np.linspace(-1, 1, 300).reshape(300, 1)
    noise = np.random.normal(0, 0.05, xData.shape)  # 0表示中心点，0.05表示方差,
    yData = np.square(xData) - 0.5 + noise  # 加一些噪声点，让他不是完全的抛物线来模拟真实情况
    # 定义网络的input
    with tf.name_scope('inputs'):
        xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
        ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

    # 输入层一个神经元，隐藏层10个，输出层一个神经元的神经网络模型
    l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)  # 隐藏层
    prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)  # 输出层
    # 构建损失函数
    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
        tf.summary.scalar('loss', loss)  # 是一个量的变化
    with tf.name_scope('optimizer'):
        optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    init = tf.initialize_all_variables()
    session = tf.Session()
    session.run(init)
    merged = tf.summary.merge_all()  # 合并所有的summary放到writer文件中
    writer = tf.summary.FileWriter("logs/", session.graph)  # 将模型写到一个文件中
    # 开始训练
    for i in range(1000):
        session.run(optimizer, feed_dict={xs: xData, ys: yData})
        if i % 50 == 0:
            # 在writer文件中添加summary
            result = session.run(merged, feed_dict={xs: xData, ys: yData})
            writer.add_summary(result, i)  # i表示记录的步数,每50步记一个点.
            print(session.run(loss, feed_dict={xs: xData, ys: yData}))  # 只要是跟placholer所定义的参数参与的计算，都要用feed_dict传入参数
