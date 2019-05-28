{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 과거부터 프로그램이 진행이 되었다.\n",
    "# 기계어 -> 어셈블리언어 -> 포트란, 코블 \n",
    "# -> C언어(절차적 언어의 대표격인 프로그래밍 언어)\n",
    "# 절차적 언어 ( 프로그램을 만드는 방식 )\n",
    "# 기능을 기준으로 큰 문제를 작은 문제로 세분화\n",
    "# 예) 은행 프로그램을 작성\n",
    "# -외환업무, -대출업무, -예금업무, -보험업무,... \n",
    "# 각각의 기능을 다시 세분화\n",
    "# 예금업무 => 입금업무, 출금업무, 무통장입금업무...\n",
    "# 더이상 세분화 시킬 수 없을 때까지 기능을 세분화 시키고 \n",
    "# 이렇게 세분화된 기능을 코드로 구현 -> 구현된 코드를 하나로 합친다.\n",
    "# 이런 프로그램 방식의 장점 : 프로그래밍의 설계가 쉽다. ->빨리 쉽게 만들 수 있다 -> 비용절감의 장점\n",
    "# 단점 : 프로그램을 유지보수 하는 게 어렵다.\n",
    "# 1990년대에 프로그래밍의 패러다임이 바뀌게 된다.\n",
    "# 객체지향 방식이 대두!! (유지보수에 강점)\n",
    "# 객체지향 프로그램 방식\n",
    "# 현실 세계의 해결해야 하는 문제를 프로그램적으로 modeling하는 프로그램 기법이 객체지향 방식'\n",
    "# 객체지향 방식은 프로그램을 기능으로 세분화하지 않는다.\n",
    "# 내가 해결해야 하는 문제를 구성하고 있는 구성 요소를 파악하고(개체)\n",
    "# 이 구성요소들 간의 상호관계(정보전달관계)를 파악\n",
    "# 프로그램 설계가 어렵다. \n",
    "# 하지만 일단 잘 만든면 프로그램의 유지보수에 강점이 있다.\n",
    "# 현실 세계의 구성요소를 파악하고 프로그램으로 옯기는 작업을 해야 한다.\n",
    "# 현실 세계의 개체가 가니는 굉장히 많은 기능과 특성 중 프로그램에서 필요한 것들만 추린다.(abstraction)\n",
    "# 개체를 프로그램으로 표현하기 위한 '객체 모델링 수단'\n",
    "# class\n",
    "# ADT(abstract data type , 추상 데이터 타입)\n",
    "# class가 가지는 기능 중 하나는 encapsulation(캡슐화)\n",
    "# 관련이 있는 특성(filed)과 기능(method)을 class라는 하나의 단위로 묶는 역할"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "3.1415926563\n"
     ]
    }
   ],
   "source": [
    "# python의 module\n",
    "# python의 변수, 함수, 클래스를 모아놓은 파일.(라이브러리 개념)\n",
    "# 다른 python program에서 불러다 사용할 수 있는 파일\n",
    "# import : module을 사용할 수 있도록 만들어 주는 keyword\n",
    "# import 모듈이름(파일명)\n",
    "# import 모듈이름 as 별명\n",
    "import module1 as m1     #내가 만들어 놓은 module1이라는 파일을 사용하겠다. 축약형 as m1\n",
    "print(m1.PI)   #module1에 있는 PI를 사용하겠다.\n",
    "# from 모듈이름 import 함수, 변수, 클래스\n",
    "from module1 import my_sum     #해당 모듈로부터 my_sum이라는 함수를 불러다 쓰겠다. (해당 함수 1개만)\n",
    "print(my_sum(10,20))            #여기서는 PI 사용 x, my_sum 함수만 불러왔기 때문\n",
    "\n",
    "from module1 import PI\n",
    "print(PI)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\python35.zip',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\DLLs',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\lib',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\lib\\\\site-packages',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\lib\\\\site-packages\\\\win32',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\lib\\\\site-packages\\\\win32\\\\lib',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\lib\\\\site-packages\\\\Pythonwin',\n",
       " 'C:\\\\Users\\\\msm03\\\\Anaconda3\\\\envs\\\\asus_env\\\\lib\\\\site-packages\\\\IPython\\\\extensions',\n",
       " 'C:\\\\Users\\\\msm03\\\\.ipython',\n",
       " 'c;/python_lib']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# module을 불러올 수 있는 폴더들이 있다. (아무데나 놓고 불러올 수는 없다.)\n",
    "import sys\n",
    "sys.path       #list\n",
    "#sys.path.append(\"c;/python_lib\")   #list.append 마지막 요소에 추가하는 것\n",
    "#sys.path\n",
    "# 환경변수 PYTHONPATH를 생성해서 여기에 폴더를 지정해도 module을 사용할 수 있는 폴더가 된다.\n",
    "#sys.path.pop()\n",
    "#sys.path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "300\n",
      "300\n",
      "300\n"
     ]
    }
   ],
   "source": [
    "# python module을 관리하기 위한 방안\n",
    "# 가장 일반적으로 쉽게 생각할 수 있는 방안\n",
    "# 관련있는 module끼리 폴더구조로 저장\n",
    "# package : 관련있는 module을 묶어놓은 논리적인 집합\n",
    "# package : 결국 폴더로 표현\n",
    "# import할 때 module이 package안에 포함되어 있으면 package이름을 명시해야 한다.\n",
    "import myPackage.inner.myModule #package 모두 명시해야 한다 (package : myPackage.inner / module: myModule)\n",
    "print(myPackage.inner.myModule.my_variable)\n",
    "\n",
    "import myPackage.inner.myModule as haha # haha라는 별명으로 접근\n",
    "print(haha.my_variable)\n",
    "\n",
    "from myPackage.inner import myModule   #from (package이름) import (module이름)\n",
    "print(myModule.my_variable)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
