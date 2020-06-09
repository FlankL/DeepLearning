#  @Function:  
# 　＠Time:2020/6/8 23:16
#  @Author:Flank
import tensorflow as tf
import numpy as np


def stduyConstant():
    '''
    常量不会变的量，需要通过session接口去调用
    '''
    v1 = tf.constant(1)
    v2 = tf.constant(list(range(10)))
    v3 = tf.constant(np.arange(9), shape=[3, 3], dtype=tf.float32)
    v4 = tf.constant(np.random.randn(9).reshape(3, 3).astype(np.float32))
    with tf.Session() as session:
        print(session.run(v3))
        print("*" * 20)
        print(session.run(v4))
        print("matmul:", session.run(tf.matmul(v3, v4)))
        # 这个是常量，不能定义成变量
        print(session.run(tf.random_uniform(shape=(3, 3), minval=-1)))  # np.random.uniform(size=[3,4])生成3*4的矩阵


def studyVariable():
    '''
    声明变量之后必须对所有的变量，进行初始化
    '''
    v1 = tf.Variable(tf.random_uniform(shape=[4, 4], minval=-1, maxval=1))
    v2 = tf.Variable(tf.zeros([3, 3]))
    init = tf.initialize_all_variables()  # 获得初始化变量的指向
    with tf.Session() as session:
        session.run(init)  # 运行初始化变量
        print(session.run(v1))
        print(session.run(v2))


def studyPlaceHolder():
    '''
    作用在session.run运行的时候传入参数
    '''
    v1 = tf.placeholder(tf.float32)  # 表示传入参数的数据类型
    v2 = tf.placeholder(tf.float32)
    result = tf.multiply(v1, v2)
    with tf.Session() as session:
        print(session.run(result, feed_dict={v1: 10, v2: 20}))


if __name__ == '__main__':
    # stduyConstant()
    # studyVariable()
    studyPlaceHolder()
