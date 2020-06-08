#  @Function:  session会话控制 和 Variable 变量，placeholder
# 　＠Time:2020/6/7 19:24
#  @Author:Flank
import tensorflow as tf

'''
1.tensorflow 中定义变量后初始化一下，
其他的结构，需要每一次都需要使用session来run一下才会运行。
2.tensorflow 中的数据类型通常用float32
3.矩阵的变量名大写开头
'''


def matrixTest():
    # 1.矩阵相乘
    matrix1 = tf.constant([[3, 3]])  # 一行两列
    matrix2 = tf.constant([[2], [2]])  # 两行一列矩阵
    product = tf.matmul(matrix1, matrix2)  # 矩阵乘法 np.dot(m1,m2) numpy中的矩阵乘法,product相当于这个表达式的指针
    with tf.Session() as session:
        result = session.run(product)  # 每run一下tensorflow才会执行一次定义的结构
        print(result)


def variableTest():
    # 2. 定义变量
    v1 = tf.Variable(100, name='counter')
    # print(v1.name)
    one = tf.constant(1)  # 定义常量1
    newValue = tf.add(v1, one)
    update = tf.assign(v1, newValue)  # assign :分配也就是v1=newValue
    init = tf.initialize_all_variables()  # tensorflow中如果定义了变量，必须初始化

    with tf.Session() as session:
        session.run(init)
        for step in range(3):
            session.run(update)
            print(session.run(v1))


def placeholderTest(
        # 3. placeholder
    input1=tf.placeholder(tf.float32)):
    input2 = tf.placeholder(tf.float32)
    output = tf.multiply(input1, input2)
    with tf.Session() as session:
        print(session.run(output,feed_dict={input1:20,input2:10}))


if __name__=='__main__':
    placeholderTest()