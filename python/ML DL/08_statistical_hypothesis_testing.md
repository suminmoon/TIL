{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 통계의 목적에 따른 분류\n",
    "# 1. 기술통계( Descriptive statistics )\n",
    "#   -우리에게 주어진 데이터를 요약, 설명, 분석하는 통계기법을 의미\n",
    "#   -Pandas ( EDA - 탐색적 데이터 분석 )\n",
    "#   -평균(대표값), 분산(데이터의 분포)\n",
    "# 2. 추리(추론)통계( Inferential statistics )\n",
    "#   -수집한 데이터를 기반으로 어떠한 사실을 예측하고 검정하는 통계기법을 의미 \n",
    "#   -통계적 가설 검증\n",
    "#    표본으로 부터 얻은 어떠한 사실을 근간으로 가설이 맞는지를 통계적으로 검증하는 방법\n",
    "#    가자 먼저 할 일은 가설을 정의하는 것.\n",
    "#     -귀무가설( null hypothesis ) => H0\n",
    "#      관계가 없다. 영향력이 없다. 관련이 없다.\n",
    "#      채택되기를 원하는 가설이 아니고, reject가 되는 것을 기대하는 가설.\n",
    "#     -대립가설( alternative hypothesis ) => H1\n",
    "#      관계가 있다. 영향력이 있다. 관계가 있다.\n",
    "#      통계에 근거해서 채택되기는 원하는 가설`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "기각 되었습니다.\n",
      "수명이 75세 이상이다.\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "# np.sqrt : numpy에서 제곱근 구하는 것!\n",
    "\n",
    "Ho = \"수명이 75세다.\"\n",
    "H1 = \"수명이 75세 이상이다.\"    \n",
    "u0 = (79 - 75) / (10 / 30**0.5)\n",
    "if u0 > 1.28:\n",
    "    print(\"기각 되었습니다.\")\n",
    "    print(H1)\n",
    "else:\n",
    "    print(H0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 통계적 가설 검증\n",
    "# 1. 표본을 통해서 모집단의 특성을 유추\n",
    "# 2. 머신러닝을 할 때 필요한 parameter를 분류해서 사용할 필요가 있다. \n",
    "#    필요 없는 건 버리고 서로 연관성이 있는 parameter만 머신러닝의 입력으로 사용.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14.338"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "total = 500\n",
    "df = pd.DataFrame({\"1갑 이상\" : [23,31,13], \"1갑 이하\" : [21,48,23],\\\n",
    "                \"안피움\" : [63,159,119]})\n",
    "df.index=[\"반병 이상\", \"반병 이하\", \"못 마심\"]\n",
    "(df[\"1갑 이상\"].sum()/total) *(df.loc[\"반병 이상\"].sum()/ total) * 500\n",
    "(df[\"1갑 이하\"].sum()/total) *(df.loc[\"반병 이상\"].sum()/ total) * 500\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "                                        \n"
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
      "카이제곱값: 12.826630603041854\n",
      "pvalue : 0.012154721873148373\n",
      "자유도 : 4\n",
      "대립가설 accept\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import stats\n",
    "\n",
    "arr = np.array([[23,21,63],\n",
    "              [31,48,159],\n",
    "              [13,23,119]])\n",
    "\n",
    "chi2, pvalue, free, _table = stats.chi2_contingency(arr)\n",
    "print(\"카이제곱값: {}\".format(chi2))\n",
    "print(\"pvalue : {}\".format(pvalue))\n",
    "print(\"자유도 : {}\".format(free))\n",
    "\n",
    "if pvalue < 0.05:\n",
    "    print(\"대립가설 accept\")\n",
    "    \n",
    "else:\n",
    "    print(\"귀무가설 accept\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##### matplotlib을 이용한 그래프 그리기\n",
    "## data간의 관계, 방향성 등을 눈으로 파악하기 위해서 사용\n",
    "\n",
    "### 통계\n",
    "## 통계는 목적에 따라서 크게 두 가지 분류로 구분\n",
    "## 1. 가지고 있는 데이터를 분석해서 해당 데이터를 요약, 특정한 사실을 이끌어내는 통계 기법\n",
    "##    기술통계 ( 데이터를 기술 (내용을 기술하다 할 때 기술) )\n",
    "## 2. 수집한 데이터를 기반으로 모집단의 특성을 유추\n",
    "##    독립변수에 따른 종속변수의 변화를 예측하기 위해서 사용하는 통계기법\n",
    "##    추론(추론)통계 \n",
    "##     ==> 통계적 가설 검정\n",
    "##         표본에 대한 내용을 근거로 모집단의 특성을 유추\n",
    "##         가설 : 귀무가설, 대립가설\n",
    "\n",
    "##     또 다른 목적으로 통계적 가설 검정을 이용한다.\n",
    "##     머신러닝을 위해 여러가지 입력 parameter들이 들어간다.\n",
    "##     특정 parameter는 머신러닝을 위해 필요하고, 또 어떤 parameter는 그닥 필요가 없다.\n",
    "##     parameter간의 관계성을 고려해서 입력 parameter를 설정해주는 작업이 필요\n",
    "##     parameter간의 관련성을 검증하기 위해서 통계적 가설검증이 사용된다.\n",
    "##     ==> 음주량과 흡연량의 관계를 통계적 가설검증 기법으로 알아보자!!\n",
    "##         범주형으로 되어있고 밀도 값이 데이터로 사용되는 검증에 '카이제곱'검증을 이용\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Group1의 평균 : 171.9028591091939\n",
      "Group2의 평균 : 173.4912348536539\n",
      "0.15685018595907008\n",
      "귀무가설 선택 : 평균키의 차이는 의미가 없다.\n"
     ]
    }
   ],
   "source": [
    "# 독립표본 t검정   stats.ttest_ind\n",
    "# 두 집단의 평균을 이용해서 두 집단이 서로 차이가 있는지를 판단하는 검정방법\n",
    "# 그룹 1과 그룹 2의 평균 키를 조사해서 그 차이가 있는지 혹은 차이는 무시할 정도인지 판별\n",
    "# 귀무가설 : 두 그룹 간의 평균 키의 차이가 없다.\n",
    "# 대립가설 : 두 그룹 간의 평균 키의 차이는 의미가 있다.\n",
    "\n",
    "import numpy as np\n",
    "from scipy import stats \n",
    "np.random.seed(1)\n",
    "group1 = [170 + np.random.normal(2, 1) for _ in range(10)]  \n",
    "# 170을 기준으로 랜덤으로 10개 난수 뽑기 /    일반적으로 사용하지 않는 변수는 _ 로 잡는다!!\n",
    "group2 = [174 + np.random.normal(0,3) for _ in range(10)]\n",
    "print(\"Group1의 평균 : {}\".format(np.mean(group1)))\n",
    "print(\"Group2의 평균 : {}\".format(np.mean(group2)))\n",
    "\n",
    "_, pvalue = stats.ttest_ind(group1, group2)   #결과값 두 개 인자 중 pvalue만 사용\n",
    "print(pvalue)\n",
    "if pvalue < 0.05:\n",
    "    print(\"대립가설 선택 : 평균키의 차이는 의미가 있다.\")\n",
    "else:\n",
    "    print(\"귀무가설 선택 : 평균키의 차이는 의미가 없다.\")\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.1810898292540683e-13\n",
      "대립가설 채택 : 다이어트 약이 효과가 있다.\n"
     ]
    }
   ],
   "source": [
    "# 대응표본 t검정   stats.ttest_rel\n",
    "# 다이어트약의 복용 전과 복용 후의 값을 통계적으로 약의 효과를 알아보기 위해서 사용.\n",
    "# 귀무가설 : 복용 전후의 체중의 차이가 없다.\n",
    "# 대립가설 : 복용 전후의 체중의 차이가 있다.\n",
    "import numpy as np\n",
    "from scipy import stats\n",
    "\n",
    "before = [60 + np.random.normal(0,5) for _ in range(20)]\n",
    "after = [w - np.random.normal(2,1) for w in before]\n",
    "_, pvalue = stats.ttest_rel(before, after)\n",
    "print(pvalue)\n",
    "if pvalue < 0.05:\n",
    "    print(\"대립가설 채택 : 다이어트 약이 효과가 있다.\")\n",
    "else:\n",
    "    print(\"귀무가설 채택 : 다이어트 약이 효과가 없다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.04743795427394179"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# ANOVA 검정\n",
    "# 비교대상이 3개 이상일 경우 ttest 대신 사용\n",
    "from scipy import stats\n",
    "\n",
    "# 교육 훈련 데이터\n",
    "a = [67,45,98,41,22,50]\n",
    "b = [93,68,85,77,53,92]\n",
    "c = [73,50,79,60,50,85]\n",
    "d = [57,55,68,47,24,32]\n",
    "\n",
    "_, pvalue = stats.f_oneway(a, b, c, d)\n",
    "pvalue"
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
