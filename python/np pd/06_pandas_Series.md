{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pandas : python의 data analysis의 핵심 라이브러리\n",
    "# pandas는 고유하게 정의된 두 개의 자료구조를 이용\n",
    "# Series : numpy의 1차원 배열과 유사\n",
    "#          같은 데이터 타입을 가진다.\n",
    "# DataFrame : numpy의 2차원 배열과 유사"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1,  5, 10, 24])"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==============================\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0    -1.0\n",
       "1     5.0\n",
       "2    10.0\n",
       "3    99.0\n",
       "dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RangeIndex(start=0, stop=4, step=1)\n",
      "[-1.  5. 10. 99.]\n",
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "# Series의 생성\n",
    "import numpy as np    # pandas를 사용할 때 numpy도 함께 import\n",
    "import pandas as pd   # pandas설치 conda install pandas\n",
    "\n",
    "# numpy 배열 ( list를 가지고 만든다.)\n",
    "arr = np.array([-1,5,10,24])\n",
    "display(arr)    # out값 형태로 결과 값 찍힘  array([-1,  5, 10, 24])\n",
    "#print(arr)      #[-1  5 10 24]\n",
    "\n",
    "# numpy array의 data type확인\n",
    "arr.dtype\n",
    "\n",
    "# numpy 배열을 생설할 때 data type을 지정 (모두 같은 데이터 타입을 가짐!)\n",
    "arr = np.array([-1,5,10,24], np.float64)\n",
    "arr = np.array([-1,5,10,24], np.str)\n",
    "\n",
    "# numpy 배열을 다음과 같이 생성하고 싶다.\n",
    "arr = np.array([-1,3.14,\"Hello\",True], np.object)   # 각 요소가 다른 데이터타입\n",
    "arr                                      # data type을 객체로 지정\n",
    "\n",
    "print(\"=\"*30)\n",
    "\n",
    "s = pd.Series([-1,5,10,99], dtype=np.float64)\n",
    "display(s)    # list와 dictionary를 합쳐놓은 형태 같음( index를 같이 들고있다. )\n",
    "print(s.index)       # Series에서 index정보만 따로 출력\n",
    "print(s.values)      # Series에서 값만 출력 ( 1차원 numpy array 리턴 )\n",
    "print(type(s.values))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Series에 대한 indexing과 slicing\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "s = pd.Series([-1,5,10,99], index=[\"c\",\"d\",\"a\",\"b\"])   # index 지정\n",
    "#                                                      dict처럼 key값처럼 사용\n",
    "s                                                   # 숫자 인덱스 여전히 사용 가능\n",
    "print(\"s[0]의 값 : {}\".format(s[0]))\n",
    "print(\"s['a']의 값 : {}\".format(s[\"a\"]))\n",
    "print(\"=\"*40)\n",
    "print(\"s[0:-1]의 값 : \\n{}\".format(s[:-1]))\n",
    "s[\"c\":\"b\"]   #c부터 b까지를 의미\n",
    "s[\"c\":\"a\"]   #c부터 a까지\n",
    "# 숫자 인덱스를 사용하는 것과 내가 지정한 인덱스를 사용하는 것의 차이\n",
    "\n",
    "# Series안의 데이터를 모두 합해서 출력(지양)\n",
    "result = 0.0\n",
    "for tmp in s:\n",
    "    result+=tmp\n",
    "print(result)\n",
    "\n",
    "# 집계함수 이용 !!! 이 방법을 많이 사용합시다!\n",
    "print(\"Series안의 데이터 총합 : {}\".format(s.sum()))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A공장의 2019-01-01부터 10일간 생상량을 Series로 저장\n",
    "# 생산량은 평균이 50이고 표준편차가 5인 정규분포에서 \n",
    "# random하게 추출(생산량은 정수로 처리)\n",
    "# 예) 2019-01-10 54\n",
    "#     2019-01-02 49\n",
    "#        .....\n",
    "# B공장의 2019-01-01부터 10일간의 생산량을 Series로저장\n",
    "# 생산량은 평균이 70이고 표준편차가 8인 정규분포에서 \n",
    "# random하게 추출(생산량은 정수로 처리)\n",
    "\n",
    "# 이렇게 두 개의 Series를 생성하고 모든 공장의 생산량을 출력하세요\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "# from datetime as datetime, timedelta\n",
    "\n",
    "arr1 = np.random.normal(50,5,(10,)).astype(np.int32)\n",
    "print(arr1)\n",
    "arr2 = np.random.normal(70,8,(10,)).astype(np.int32)\n",
    "_date=pd.date_range(start='2019-01-01', periods=10)\n",
    "# 2019-01-01부터 시작해서 10개를 list로 생성\n",
    "s1 =pd.Series(arr1,index=[_date])\n",
    "s2 =pd.Series(arr2, index=[_date])\n",
    "\n",
    "print(s1)\n",
    "print(\"=\"*30)\n",
    "print(s2)\n",
    "print(\"=\"*30)\n",
    "print(\"두 공장의 총 생산량 : \\n{}\".format(s1+s2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 강사님 풀이\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from datetime import datetime, timedelta\n",
    "start_day = datetime(2019,1,1)\n",
    "s1_value=[int(x) for x in np.random.normal(50,5,(10,))]\n",
    "# for문과 list 접목해서 한 번에 list 만드는 것 연습!!!!!!\n",
    "# s1_value =np.random.normal(50,5,(10,)).astype(np.int32)\n",
    "\n",
    "s2_value=[int(x) for x in np.random.normal(70,8,(10,))]\n",
    "s_date=[start_day + timedelta(days=x) for x in range(10)]\n",
    "s1=pd.Series(s1_value, index=s_date)\n",
    "s2=pd.Series(s2_value, index=s_date)\n",
    "s1+s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Series를 생성하는 방법 중에 list를 이용하는 방법\n",
    "# s = pd.Series([1,2,3,4,5])\n",
    "# Series를 dictionary를 이용해서 만들 수 있다.\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "my_dict = { \"서울\" : 3000 , \"인천\" : 5000, \"제주\" : 2000 }\n",
    "s = pd.Series(my_dict)\n",
    "\n",
    "# Series의 이름을 부여할 수 있다.\n",
    "s.name = \"지역별 가격 데이터\"\n",
    "# Series index의 이름을 부여할 수 있다.\n",
    "s.index.name=\"지역명\"\n",
    "\n",
    "# index를 수정할 수 있다.\n",
    "idx =[\"seoul\",\"incheon\",\"jeju\"]\n",
    "s.index = idx\n",
    "s"
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
