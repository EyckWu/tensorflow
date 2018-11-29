#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
# 进入一个交互式 TensorFlow 会话.
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])
# 使用初始化器 initializer op 的 run() 方法初始化 'x'
x.initializer.run()
# 增加一个减法 sub op, 从 'x' 减去 'a'. 运行减法 op, 输出结果
sub = tf.subtract(x, a)

print(sub.eval())
# ==> [-2. -1.]