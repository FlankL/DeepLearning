# @Function:保存和读取
# @Time: 2020/6/18 下午3:44
# @Authon: flank
import tensorflow as tf
import numpy as np


# 1.存数据
# 会保存数据类型,形状
# W=tf.Variable([[1,2,3],[4,5,6]],dtype=tf.float32,name='Weights')
# b=tf.Variable([1,2,3],dtype=tf.float32,name='biases')
# init=tf.initialize_all_variables()
# #用来存储各种变量
# saver=tf.train.Saver()
# with tf.Session() as session:
#     session.run(init)
#     save_path=saver.save(session,"my_net/save_net.ckpt")


# 2.取数据
#取数据要先建立空的网络结构,数据类型和形状都要和文件中的一致
W=tf.Variable(np.arange(6).reshape(2,3),dtype=tf.float32,name='Weights')
b=tf.Variable(np.arange(3).reshape(1,3).flatten(),dtype=tf.float32,name='biases')
saver=tf.train.Saver()
with tf.Session() as session:
    saver.restore(session,"my_net/save_net.ckpt")
    print('weights',session.run(W))
    print('biases',session.run(b))