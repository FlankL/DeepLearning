# @Function:多层感知机进行识别-手写数字识别Demon,
# @Time: 2020/6/17 上午11:41
# @Authon: flank
import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

# 创建1~10的手写数字数据,会自动的从网上下载数据包
mnist = read_data_sets("MNIST_data/", one_hot=True)


def add_layer(inputs, inSize, outSize, activation_function=None):
    '''
    添加神经层
    :param inputs:输入数据
    :param inSize:权重的size
    :param outSize:权重的size
    :param activation_function:是否有激励函数
    :return:返回该层的运算结果
    '''
    Weights = tf.Variable(tf.random_normal([inSize, outSize]))  # 定义一个insize行，outSize列的矩阵
    biases = tf.Variable(tf.zeros([1, outSize]) + 0.1)  # 权重和偏移在每一次训练中会修改
    Wx_plus_b = tf.matmul(inputs, Weights) + biases  # 预测出来的值
    # 预测出来的值是否过激励函数
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def computeAccuracy(v_xs, v_ys):
    global prediction
    y_pre = session.run(prediction, feed_dict={xs: v_xs})  # 生成预测值
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))  # 对比预测值和真实值的差别
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = session.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result


xs = tf.placeholder(tf.float32, [None, 784])  # 不规定有多少张图片,但规定每张图片784个像素(28*28)
ys = tf.placeholder(tf.float32, [None, 10])  # 10表示10个输出
# 添加输出层
prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)  # 表示输入是784,输出是10

crossEnropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))  # loss

train = tf.train.GradientDescentOptimizer(0.89).minimize(crossEnropy)

session = tf.Session()
session.run(tf.initialize_all_variables())

for i in range(1000):
    # 数据分为训练数据,和测试数据
    batch_xs, batch_ys = mnist.train.next_batch(100)  # 从整套数据中提取100份,全部数据学习太慢了
    session.run(train, feed_dict={xs: batch_xs, ys: batch_ys})
    if i % 50 == 0:
        # 输出精确度
        print(computeAccuracy(mnist.test.images, mnist.test.labels))
