#  @Function: 普通神经网络：抛物线权重训练
# 　＠Time:2020/6/7 21:11
#  @Author:Flank
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


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
    xData=np.linspace(-1,1,300).reshape(300,1)
    noise=np.random.normal(0,0.05,xData.shape)#0表示中心点，0.05表示方差,
    yData=np.square(xData)-0.5+noise# 加一些噪声点，让他不是完全的抛物线来模拟真实情况

    xs=tf.placeholder(tf.float32,[None,1])#用来接收运行时输入的数据
    ys=tf.placeholder(tf.float32,[None,1])#用来接收运行时输入的数据

    #输入层一个神经元，隐藏层10个，输出层一个神经元的神经网络模型
    l1=add_layer(xs,1,10,activation_function=tf.nn.relu)#隐藏层
    prediction=add_layer(l1,10,1,activation_function=None)#输出层

    loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
    optimizer=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    init =tf.initialize_all_variables()
    session=tf.Session()
    session.run(init)#训练前将变量初始化

    #结果可视化
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(xData,yData)
    plt.ion()#因为plt.show之后程序会停住，这句话的作用就是，让主程序继续往下走
    plt.show()

    # 开始训练
    for i in range(1000):
        session.run(optimizer,feed_dict={xs:xData,ys:yData})
        if i % 50 ==0:
            try:#第一次的时候没有线，防止报错
               ax.lines.remove(lines[0]) # 每次生成完一条线后就要，删除掉，不然会有很多条线叠在一起
            except Exception as e:
                print(e)
            print(session.run(loss,feed_dict={xs:xData,ys:yData}))#只要是跟placholer所定义的参数参与的计算，都要用feed_dict传入参数
            predictionValue=session.run(prediction,feed_dict={xs:xData})
            lines=ax.plot(xData,predictionValue,'r-',lw=5,label='预测抛物线') #画线，r-表示红色虚线
            plt.pause(0.5)#停上0.1秒

