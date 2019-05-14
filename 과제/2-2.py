import tensorflow as tf

cost=tf.reduce_mean(tf.square(hypothesis-Y))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op=optimizer.minimize(cost)