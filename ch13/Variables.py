#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# 创建一个变量，初始化为标量0
state = tf.Variable(0, name='counter')
# 创建一个op， 其作用是使state增加1
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 启动图后，变量必须经过'初始化'(init) op初始化，
# 首先必须增加一个'初始化'op到图中
init_op = tf.initialize_all_variables()
# 启动图，运行op
with tf.Session() as sess:
    sess.run(init_op)
    print( sess.run(state))
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))