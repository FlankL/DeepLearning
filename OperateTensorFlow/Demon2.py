#  @Function: 添加层
# 　＠Time:2020/6/7 21:11
#  @Author:Flank
import tensorflow as tf
import numpy as np


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

if __name__=='__main__':
    xData=np.linspace(-1,1,10).reshape(10,1)
    noise=np.random.normal(0,0.05,)#0表示中心点，0.05表示方差
    yData=np.square(xData)-0.5+noise# 加一些噪声点，让他不是完全的抛物线来模拟真实情况
    print(xData)

