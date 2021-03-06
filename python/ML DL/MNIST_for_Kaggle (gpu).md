{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cost : 0.15869945287704468\n",
      "Cost : 0.019224340096116066\n",
      "Cost : 0.03470276668667793\n",
      "Cost : 0.003677507396787405\n",
      "Cost : 0.00574610335752368\n",
      "Cost : 0.03974410146474838\n",
      "Cost : 0.04596129432320595\n",
      "Cost : 0.0037466955836862326\n",
      "Cost : 0.001529334462247789\n",
      "Cost : 0.03732401505112648\n"
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
    "train = pd.read_csv(\"./data/digit/train.csv\")\n",
    "test = pd.read_csv(\"./data/digit/test.csv\")\n",
    "a = np.array(test.values, dtype=np.float32)\n",
    "# data loading\n",
    "num_of_train = int(train.shape[0] * 0.7)  # 데이터의 70%를 train data로 30%를 test로\n",
    "data_train = train.loc[ : num_of_train,:]\n",
    "data_test = train.loc[num_of_train+1 : ,:]\n",
    "\n",
    "train_x_data = data_train.drop(\"label\", axis = 1, inplace= False)\n",
    "train_y = data_train[\"label\"]   # Series\n",
    "\n",
    "test_x_data = data_test.drop(\"label\", axis=1, inplace=False)\n",
    "test_y = data_test[\"label\"]\n",
    "\n",
    "### one-hot encoding ###\n",
    "sess = tf.Session()\n",
    "train_y_ = tf.one_hot(train_y, 10).eval(session=sess)\n",
    "test_y_ = tf.one_hot(test_y, 10).eval(session=sess)\n",
    "train_y_data = pd.DataFrame(train_y_)   # one hot encoding을 dataframe으로 바꾸기\n",
    "test_y_data = pd.DataFrame(test_y_)     # one hot encoding을 dataframe으로 바꾸기\n",
    "#######################\n",
    "\n",
    "# placeholder\n",
    "X = tf.placeholder(shape=[None, 784], dtype=tf.float32)\n",
    "Y = tf.placeholder(shape=[None, 10], dtype=tf.float32)\n",
    "keep = tf.placeholder(dtype = tf.float32)\n",
    "\n",
    "# 3. Convolution Layer\n",
    "# 3.1 Convolution Layer 1 (conv, relu, pool)\n",
    "#     입력데이터의 형태를 Convolution 할 수 있도록 4차배열로 reshape (None, 784) => \n",
    "X_img = tf.reshape(X, shape=[ -1 ,28 ,28, 1]) \n",
    "\n",
    "# Filter를 생성\n",
    "W1 = tf.Variable(tf.random_normal([2,2,1,32], stddev=0.01))\n",
    "# 3*3의 흑백 필터 32개 / 표준편차를 적게 줘서 난수 값의 차이가 많이 나지 않도록 설정\n",
    "\n",
    "# Convolution\n",
    "L1 = tf.nn.conv2d(X_img, W1, strides=[1,1,1,1], padding=\"SAME\")\n",
    "# relu\n",
    "L1 = tf.nn.relu(L1)\n",
    "# max pooling\n",
    "L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1], strides=[1,2,2,1], padding=\"SAME\")\n",
    "\n",
    "# Convolution Layer 2   (위에 L1을 만드는 것과 같은 건데 한 줄에 합쳐서 만든 것.)\n",
    "#     Filter, Convolution, ReLU  \n",
    "L2 = tf.layers.conv2d(inputs=L1, filters=64,\\\n",
    "                kernel_size=[3,3], padding=\"SAME\", strides=1, activation=tf.nn.relu)\n",
    "# Max Pooling\n",
    "L2 = tf.layers.max_pooling2d(inputs=L2, pool_size=[2,2], padding=\"SAME\", strides=2)\n",
    "\n",
    "#### Convolution Layer 끝\n",
    "\n",
    "# 4. FC ( Neural Network )\n",
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
    "#################################\n",
    "\n",
    "# hypothesis\n",
    "\n",
    "logit = tf.matmul(layer2,W4) + b4\n",
    "# H = tf.nn.softmax(logit)\n",
    "H = logit\n",
    "\n",
    "# Cost\n",
    "cost = \\\n",
    "tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=Y))\n",
    "\n",
    "# train\n",
    "train = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)\n",
    "\n",
    "# Session, 초기화\n",
    "sess = tf.Session()\n",
    "sess.run(tf.global_variables_initializer())\n",
    "\n",
    "# 학습\n",
    "\n",
    "num_of_epoch = 10\n",
    "batch_size = 100\n",
    "\n",
    "for step in range(num_of_epoch):\n",
    "    num_of_iter = int(train_x_data.shape[0]/ batch_size)   #29400 / 100 = 294\n",
    "    \n",
    "    for i in range(num_of_iter):\n",
    "        batch_x = train_x_data.loc[(batch_size*i):(batch_size*i)+batch_size-1, : ]\n",
    "        batch_y = train_y_data.loc[(batch_size*i):(batch_size*i)+batch_size-1, : ]\n",
    "        _, cost_val = sess.run([train, cost], feed_dict={X:batch_x, Y:batch_y, keep:0.7})\n",
    "    \n",
    "    print(\"Cost : {}\".format(cost_val))\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정확도 : 0.9889682539682539\n"
     ]
    }
   ],
   "source": [
    "num_of_iter2= int(test_x_data.shape[0]/batch_size)\n",
    "result_sum=0\n",
    "start = train_x_data.shape[0]    \n",
    "\n",
    "# 정확도 측정\n",
    "# predict = tf.cast(H > 0.5, dtype = tf.float32)\n",
    "# correct = tf.equal(predict, Y)\n",
    "# accuracy = tf.reduce_mean(tf.cast(correct, dtype=tf.float32))\n",
    "predict = tf.argmax(H,1)\n",
    "correct = tf.equal(predict, tf.argmax(Y,1))\n",
    "accuracy = tf.reduce_sum(tf.cast(correct, dtype=tf.float32))\n",
    "\n",
    "\n",
    "for i in range(num_of_iter2):\n",
    "    batch_x = test_x_data.loc[(start+batch_size*i):(start+batch_size*i)+batch_size-1,:]\n",
    "    batch_y = test_y_data.loc[(batch_size*i):(batch_size*i)+batch_size-1,:]\n",
    "    \n",
    "    correct_num = sess.run(accuracy, feed_dict={X:batch_x, Y:batch_y, keep:1})\n",
    "    result_sum += correct_num\n",
    "\n",
    "print(\"정확도 : {}\".format(result_sum / data_test.shape[0]))\n",
    "\n",
    "## 예측 ##\n",
    "\n",
    "# result = sess.run(predict,feed_dict={X:x_test})\n",
    "# test[\"Survived\"]=result.astype(np.int32)\n",
    "# file = test[[\"PassengerId\",\"Survived\"]]\n",
    "# file.set_index(\"PassengerId\", inplace=True)\n",
    "\n",
    "# file.to_csv(\"./data/titanic/submission.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 예측 ##\n",
    "\n",
    "batch_size = 100\n",
    "num_of_iter3 = int(a.shape[0] / batch_size)  # 28000 / 100 = 280\n",
    "final =[]\n",
    "\n",
    "for i in range(num_of_iter3):\n",
    "    batch_x = a[(batch_size*i):(batch_size*i)+batch_size]\n",
    "    result = sess.run(predict, feed_dict={X:batch_x, keep:1})\n",
    "    final.append(result.tolist())\n",
    "final = np.array(final)\n",
    "final = np.ravel(final)\n",
    "result = {\"ImageId\":range(1,a.shape[0]+1), \"Label\": final}\n",
    "\n",
    "file = pd.DataFrame(result)\n",
    "file.set_index(\"ImageId\", inplace=True)\n",
    "file\n",
    "file.to_csv(\"./data/digit/submission.csv\")"
   ]
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
