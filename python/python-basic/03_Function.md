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
      "30\n"
     ]
    }
   ],
   "source": [
    "#python은 독립적인 함수를 사용자가 정의해서\n",
    "#사용할 수 있다\n",
    "#함수의 정의 ( 일반적인 형해 )\n",
    "def my_sum(a,b):\n",
    "    result = a+b\n",
    "    return result\n",
    "\n",
    "print(my_sum(10,20))\n",
    "# pritn(result) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 아무런 일도 하지 않는 함수를 선언하는 경우\n",
    "def do_nothing():\n",
    "    pass\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# python 함수는 내장함수와 사용자 정의 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "True\n",
      "13\n",
      "2927415132936\n",
      "(3, 1)\n",
      "Hello World !!\n",
      "None\n",
      "[1, 3, 4, 5, 8]\n",
      "[1, 3, 4, 5, 8]\n"
     ]
    }
   ],
   "source": [
    "# python의 내장함수\n",
    "# abs(x) : x의 절대값을 구하는 함수\n",
    "print(abs(-100))\n",
    "# all(x) : '반복 가능한 대상'에 대해 모든 것이 True면 True\n",
    "print(all([1,2,3,4,5]))   # 0은 False  / list는 반복 가능 \n",
    "# any(x) :반복 가능한 대상에 대해 True가 한 개라도 있으면 True\n",
    "any([0,\"\",False,\"hello world\"])\n",
    "# eval(x) : 문자열로 입력된 수식을 직접 계산\n",
    "print(eval(\"1+3*4\"))\n",
    "# int(x) : 입력 값을 정수로 변환시키는 함수\n",
    "# str(x) : 입력 값을 문자열로 변환시키는 함수\n",
    "# len(x) : 입력 parameter에 대한 길이를 구하는 함수\n",
    "# list(x) : list를 생성하거나 list로 변환시키는 함수\n",
    "# tuple(x) : tuple로 변환시키는 함수\n",
    "# type(x) : x의 데이터 타입을 알아내는 함수 \n",
    "# dir(x) : 사용 가능한 변수와 함수를 list로 반환시키는 함수\n",
    "#print(dir(\"hello\"))\n",
    "# id(x) : 입력 객체의 고유 주소값(reference)을 return\n",
    "print(id(\"hello\"))\n",
    "# divmod(a,b) : a를 b로 나누어서 몫과 나머지를 tuple로 리턴\n",
    "print(divmod(10,3))\n",
    "# join() :리스트를 문자열로 변환할 때 많이 사용\n",
    "my_list = [\"Hello\", \"World\",\"!!\"]\n",
    "print(\" \".join(my_list))\n",
    "# max(), min(), pow() : 최대값, 최소값, 제곱값\n",
    "\n",
    "my_list =[5,3,8,1,4]\n",
    "result = my_list.sort()      #원본이 변한다\n",
    "print(result)                # None      \n",
    "print(my_list)               # [1, 3, 4, 5, 8]\n",
    "\n",
    "my_list =[5,3,8,1,4]\n",
    "result = sorted(my_list)   #sorted라는 내장함수 사용 / 원본 변환시키지 않고 정렬하여 리턴\n",
    "print(result)              #[1, 3, 4, 5, 8]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 사용자 정의 함수( user-define function )\n",
    "# 1, 가장 일반적인 형태\n",
    "def my_calc(a,b):\n",
    "    result = a + b\n",
    "    return result\n",
    "my_calc(100,200)\n",
    "\n",
    "# 2. 인자의 개수에 영향을 받지 않도록 지정\n",
    "def my_calc(*args):      #'*' 인자 여러개 받을 거라는 의미 / tuple 형태로 \n",
    "    result = 0\n",
    "    for tmp in args:\n",
    "        result += tmp\n",
    "    return result\n",
    "\n",
    "my_calc(1,2,3,4,5)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30 200\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3. python은 두 개 이상의 값을 리턴할 수 있어요.( 여러개의 값을 리턴하는 것처럼 보이지만, \n",
    "#                                                  본래 튜플의 특성을 이용한 방법이다)\n",
    "def my_calc(a,b):\n",
    "    result1 = a+b\n",
    "    result2 = a*b\n",
    "    return result1, result2\n",
    "\n",
    "a , b = my_calc(10,20)\n",
    "print(a,b)\n",
    "\n",
    "# 4. default값을 이용할 수 있다.(파라미터 마지막 값에만 사용가능)   \n",
    "def my_calc(a,b,c=False): # 마지막 값은 default처리 되었기 때문에 값을 넣어도 되고 안 넣어도 됨\n",
    "    if c :   #c가 True면\n",
    "        return a\n",
    "    else:\n",
    "        return b\n",
    "\n",
    "my_calc(10,20)          #10\n",
    "my_calc(10,20,True)    #20\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5. 외부변수를 사용할 수 있다.\n",
    "\"\"\"\n",
    "result = 0\n",
    "\n",
    "def my_calc(a,b):\n",
    "    result += (a+b)\n",
    "    return result\n",
    "my_calc(10,20)   # 에러 발생 \n",
    "#                 => result 이름은 같지만, 위에서 사용한 것과 함수 안의 것은 다른 result이기 때문에(scope가 다름) \"\"\"\n",
    "\n",
    "result = 0\n",
    "\n",
    "def my_calc(a,b):\n",
    "    global result \n",
    "    result += (a+b)   #global을 쓰면 전역변수를 사용하겠다는 말\n",
    "    return result    #코드가 서로 연결되기 때문에 유지보수에 문제점이 있다(지양!!!)\n",
    "my_calc(10,20)   "
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
