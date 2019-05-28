{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cost : 0.14201930165290833\n",
      "Cost : 0.04031349718570709\n",
      "Cost : 0.01966295950114727\n",
      "Cost : 0.03418554738163948\n",
      "Cost : 0.012416670098900795\n",
      "Cost : 0.0026706429198384285\n",
      "Cost : 0.01826443150639534\n",
      "Cost : 0.018171926960349083\n",
      "Cost : 0.005761802662163973\n",
      "Cost : 0.004348637070506811\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "import warnings\n",
    "\n",
    "tf.reset_default_graph()\n",
    "\n",
    "warnings.filterwarnings(action=\"ignore\")\n",
    "\n",
    "data = pd.read_csv(\"./data/Digit/train.csv\")\n",
    "\n",
    "# train data / test data로 나눔\n",
    "num_of_train = int(data.shape[0] * 0.7)\n",
    "data_70p = data[:num_of_train+1]\n",
    "data_30p = data[num_of_train : ]\n",
    "\n",
    "# data set을 x와 y로 나누는 처리\n",
    "train_x = data_70p.drop(\"label\", axis=1, inplace=False)\n",
    "train_y = data_70p[\"label\"]\n",
    "train_y\n",
    "\n",
    "test_x = data_30p.drop(\"label\", axis = 1, inplace=False)\n",
    "# new_idx = range(0, test_x.shape[0])\n",
    "# test_x.index = new_idx\n",
    "\n",
    "test_y = data_30p[\"label\"]\n",
    "\n",
    "# multinomial regression - y가 n개 => one_hot encoding 처리 해주기\n",
    "### one_hot encoding ###\n",
    "sess = tf.Session()\n",
    "train_y = tf.one_hot(train_y, 10).eval(session=sess)  # 현재 2차원 nparray 형태이다.\n",
    "test_y = tf.one_hot(test_y, 10).eval(session=sess)\n",
    "########################################################\n",
    "\n",
    "# placeholder\n",
    "X = tf.placeholder(shape=[None, 784], dtype = tf.float32)\n",
    "Y = tf.placeholder(shape=[None, 10], dtype = tf.float32)\n",
    "keep = tf.placeholder(dtype=tf.float32)\n",
    "\n",
    "###########################################################\n",
    "\n",
    "# Convolution Layer\n",
    "\n",
    "X_img = tf.reshape(X, shape=[-1,28,28,1])  # 입력데이터를 convolution 하도록 4차원배열로 만듦\n",
    "\n",
    "## filter\n",
    "W1 = tf.Variable(tf.random_normal([2,2,1,32], stddev = 0.01))\n",
    "## convolution\n",
    "L1 = tf.nn.conv2d(X_img, W1, strides=[1,1,1,1], padding=\"SAME\")\n",
    "## relu\n",
    "L1 = tf.nn.relu(L1)\n",
    "## max pooling\n",
    "L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1], strides=[1,2,2,1], padding=\"SAME\")\n",
    "\n",
    "\n",
    "# convolution layer2\n",
    "L2 = tf.layers.conv2d(inputs=L1, filters=64, kernel_size=[3,3], padding=\"SAME\", strides=1, activation=tf.nn.relu)\n",
    "## max pooling\n",
    "L2 = tf.layers.max_pooling2d(inputs=L2, pool_size=[2,2], padding=\"SAME\", strides=2)\n",
    "\n",
    "################################################################\n",
    "\n",
    "# FC ( neural network)\n",
    "L2 = tf.reshape(L2, shape=[-1,7*7*64])\n",
    "\n",
    "W2 = tf.get_variable(\"weight2\", shape =[7*7*64,256], \\\n",
    "                           initializer=tf.contrib.layers.xavier_initializer() )\n",
    "\n",
    "b2 = tf.Variable(tf.random_normal([256]), name = \"bias2\")\n",
    "_layer1 = tf.nn.relu(tf.matmul(L2, W2) + b2)\n",
    "layer1 = tf.nn.dropout(_layer1, keep_prob=keep)\n",
    "\n",
    "W3 = tf.get_variable(\"weight3\", shape =[256,256], \\\n",
    "                           initializer=tf.contrib.layers.xavier_initializer() )\n",
    "\n",
    "b3 = tf.Variable(tf.random_normal([256]), name = \"bias3\")\n",
    "_layer2 = tf.nn.relu(tf.matmul(layer1, W3) + b2)\n",
    "layer2 = tf.nn.dropout(_layer2, keep_prob=keep)\n",
    "\n",
    "\n",
    "W4 = tf.get_variable(\"weight4\", shape =[256,10], \\\n",
    "                           initializer=tf.contrib.layers.xavier_initializer() )\n",
    "\n",
    "b4 = tf.Variable(tf.random_normal([10]), name = \"bias4\")\n",
    "\n",
    "################################################################\n",
    "\n",
    "# Hypothesis\n",
    "logit = tf.matmul(layer2, W4) + b4\n",
    "H = logit\n",
    "cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=Y))\n",
    "\n",
    "train = tf.train.AdamOptimizer(learning_rate=0.0005).minimize(cost)\n",
    "\n",
    "sess= tf.Session()\n",
    "sess.run(tf.global_variables_initializer())\n",
    "\n",
    "####################################################################\n",
    "\n",
    "# 학습\n",
    "\n",
    "num_of_epoch = 10   # 전체 데이터 한 번 학습을 10번 반복하겠다\n",
    "batch_size = 100    # 전체 데이터가 너무 많으니 100개씩 잘라서 학습 시키겠다\n",
    "\n",
    "for step in range(num_of_epoch):\n",
    "    num_of_iter = int(train_x.shape[0] / batch_size)\n",
    "    \n",
    "    for i in range(num_of_iter):\n",
    "        batch_x = train_x[batch_size*i : batch_size*i + batch_size]\n",
    "        batch_y = train_y[batch_size*i : batch_size*i + batch_size]\n",
    "        _, cost_val = sess.run([train,cost], feed_dict={X:batch_x, Y:batch_y, keep:0.7})\n",
    "\n",
    "        \n",
    "    print(\"Cost : {}\".format(cost_val))\n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정확도 : 0.9873025950321404\n"
     ]
    }
   ],
   "source": [
    "# 나머지 30% 데이터로 정확도 구하기\n",
    "\n",
    "batch_size = 100\n",
    "num_of_iter2 = int(test_x.shape[0] / batch_size)\n",
    "result_sum=0\n",
    "\n",
    "predict = tf.argmax(H,1)\n",
    "correct = tf.equal(predict, tf.argmax(Y,1))\n",
    "accuracy = tf.reduce_sum(tf.cast(correct, dtype=tf.float32))\n",
    "             # correct가 1이 나오는 개수를 더해라\n",
    "\n",
    "\n",
    "for i in range(num_of_iter2):\n",
    "    batch_x = test_x.iloc[batch_size*i : batch_size*i + batch_size ]\n",
    "    batch_y = test_y[batch_size*i : batch_size*i + batch_size ]\n",
    "# test_y는 one_hot encoding을 해서 index가 0부터 시작하는데, \n",
    "# test_x는 하위 30%를 잘라왔기 때문에 index가 28400부터 시작했다.\n",
    "# index가 맞지 않아서 위에서 test_x의 index를 0부터 시작하도록 재설정했다.\n",
    "# 그런데 batch_x를 만들 때 test_X.iloc[] 형태로 하면 index가 0부터 설정된다!!!!!!!!!\n",
    "    correct_num = sess.run(accuracy, feed_dict={X:batch_x, Y:batch_y, keep:1})\n",
    "    result_sum+= correct_num\n",
    "    # 100개씩 batch_x와 batch_y가 만들어 지고 이것을 정확도 측정하는데\n",
    "    # 100개 단위로 accuracy한 개수를 reduce_sum으로 구하고 128번의 모든 개수 더하기 위해\n",
    "\n",
    "print(\"정확도 : {}\".format(result_sum / test_x.shape[0]))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# test파일로 예측하기 \n",
    "\n",
    "test_data = pd.read_csv(\"./data/Digit/test.csv\")\n",
    "\n",
    "batch_size = 100\n",
    "num_of_iter3 = int(test_data.shape[0] / batch_size)\n",
    "final =[]\n",
    "for i in range(num_of_iter3):\n",
    "    batch_x = test_data[batch_size*i : batch_size*i + batch_size]\n",
    "    result = sess.run(predict, feed_dict={X:batch_x, keep:1})\n",
    "    final.append(result.tolist())\n",
    "\n",
    "final = np.array(final)\n",
    "final = np.ravel(final)\n",
    "\n",
    "data = {\"ImageId\": range(1, test_data.shape[0]+1), \"Label\": final}\n",
    "submission = pd.DataFrame(data)\n",
    "submission.set_index(\"ImageId\", inplace=True)\n",
    "submission.to_csv(\"./data/Digit/submission2.csv\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "[GPU_ENV]",
   "language": "python",
   "name": "gpu_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}