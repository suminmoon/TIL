{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "리스트의 총 합은: 29\n"
     ]
    }
   ],
   "source": [
    "my_list =[5,8,2,4,10]\n",
    "\n",
    "sum=0\n",
    "for tmp in my_list:     #my_list값을 하니씩 뽑아서 tmp에 넣어라\n",
    "    sum +=tmp\n",
    "\n",
    "print(\"리스트의 총 합은: {}\".format(sum))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "리스트의 총 합은: 29\n"
     ]
    }
   ],
   "source": [
    "my_list = [5,8,2,4,10]\n",
    "sum=0\n",
    "for idx in range(len(my_list)):\n",
    "    sum+= my_list[idx]\n",
    "print(\"리스트의 총 합은: {}\".format(sum))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 8, 12, 16]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list=[1,2,3,4,5,6,7,8,9]\n",
    "\n",
    "score1 = [ tmp *2 for tmp in my_list]  #list값들을 하나씩 tmp에 넣어서 2를 곱해라\n",
    "score2 = [ tmp *2 for tmp in my_list if tmp %2 ==0]   #짝수인 list만 tmp에 넣어서 2 곱해라\n",
    "score2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:asus_env]",
   "language": "python",
   "name": "conda-env-asus_env-py"
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
