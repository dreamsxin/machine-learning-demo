import tensorflow as tf

def my_loss_function(var, data):
	return tf.abs(tf.sub(var, data))

def my_other_loss_function(var, data):
	return tf.square(tf.sub(var, data))

data = tf.placeholder(tf.float32)
var = tf.Variable(1.)
loss = my_loss_function(var, data)
var_grad = tf.gradients(loss, [var])[0]

with tf.Session() as sess:
	sess.run(tf.initialize_all_variables())
	var_grad_val = sess.run(var_grad, feed_dict={data: 4})
	print(var_grad_val)