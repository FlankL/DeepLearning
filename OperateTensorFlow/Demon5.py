# @Function:卷积神经网络的-手写数字图像识别 (keras版本的实现:http://blog.nodetopo.com/2020/03/23/tensorflow2%e5%ad%a6%e4%b9%a0%e5%9b%9b/)
# @Time: 2020/6/18 上午10:33
# @Authon: flank
import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


def computeAccuracy(v_xs, v_ys):
    '''
    计算准确度
    让学习训练好的模型去跑测试的数据,然后让预测数据和正确的输出结果进行对比计算准确率
    :param v_xs: 用来测试的输入数据
    :param v_ys: 用来测试的输出数据
    :return:
    '''
    global prediction
    y_pre = session.run(prediction, feed_dict={xs: v_xs})  # 生成预测值
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))  # 对比预测值和真实值的差别
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = session.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

def weightVariable(shape):
    '''
    输入形状返回该形状的权重参数
    :param shape:权重的形状
    :return:
    '''
    initial = tf.truncated_normal(shape, stddev=0.1)  # 用来产生随机变量
    return tf.Variable(initial)

def biasVariable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    '''
    卷积函数
    :param x: 输入图片数据
    :param W: 输入权重
    :return:
    '''
    # strides=[1,x_movement,y_movement,1]有四个元素,前后两个元素必须为1,中间两个表示width方向的步长,height方向的步长
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def maxPooling2x2(x):
    '''
    对输入进行maxpooling
    :param x: 需要pooling的数据
    :return:
    '''
    # kszie:表示需要pooling的块的大小
    # stides:表示块之间移动的步长
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


if __name__ == '__main__':
    # 1.定义输入和输出
    # 2.定义获取权重和biase函数
    # 3.添加卷积层
    # 4.添加全连接分类函数
    # 5.初始化变量,计算loss,构建优化方法
    # 6.开始训练,计算精度

    # 1.构建输入数据
    # 创建1~10的手写数字数据,会自动的从网上下载数据包
    mnist = read_data_sets("MNIST_data/", one_hot=True)
    xs = tf.placeholder(tf.float32, [None, 784])  # 不规定有多少张图片,但规定每张图片784个像素(28*28)
    ys = tf.placeholder(tf.float32, [None, 10])  # 10表示10个输出
    keep_prob = 0.1
    x_image = tf.reshape(xs, [-1, 28, 28, 1])  # [-1,28,28,1]表示n_samples(多少个样本数据),h w, c(1说明只有一个通道,黑白)

    # 2.添加中间层
    # conv1 layer 卷积层
    W_conv1 = weightVariable([5, 5, 1, 32])  # kernel 5x5,insize 1,outsize 32,表示一个输入一个点,然后32个通道
    b_conv1 = biasVariable([32])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)  # 加上非线性的处理,output size: 28*28*32(hwc)
    h_pool1 = maxPooling2x2(h_conv1)  # output size:14*14*32
    # conv2 layer
    W_conv2 = weightVariable([5, 5, 32, 64])  # 表示 w,h,c,k
    b_conv2 = biasVariable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)  # 加上非线性的处理,output size: 14*14*64(hwc)
    h_pool2 = maxPooling2x2(h_conv2)  # output size:7*7*64

    # func1 layer 卷积层
    W_func1 = weightVariable([7 * 7 * 64, 1024])  # 1024表示更高,通道数1024
    b_func1 = biasVariable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])  # [n_samples,7,7,64]--->[n_samples,7*7*64],-1表示自动扩展
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_func1)) + b_func1
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob=1 - keep_prob)  # 使用dropout避免ouverfitting

    # func2 layer 函数层
    W_func2 = weightVariable([1024, 10])  # 传入1024,传出10
    b_func2 = biasVariable([10])
    prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_func2) + b_func2)  # 使用softmax进行激活分类

    # 计算loss(真实数据和预测数据)
    crossEnropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
    train = tf.train.AdamOptimizer(1e-4).minimize(crossEnropy)

    session = tf.Session()
    session.run(tf.initialize_all_variables())

    for i in range(1000):
        # 这种方式是静态构图,session.run()以后才能动起来
        # 数据分为训练数据,和测试数据
        batch_xs, batch_ys = mnist.train.next_batch(100)  # 从整套数据中提取100份,全部数据学习太慢了
        session.run(train, feed_dict={xs: batch_xs, ys: batch_ys})
        if i % 50 == 0:
            # 输出精确度
            print(computeAccuracy(mnist.test.images, mnist.test.labels))
