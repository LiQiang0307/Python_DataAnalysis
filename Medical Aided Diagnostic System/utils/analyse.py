import numpy as np
import pandas as pd

# 添加列名
header_row = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', \
              'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# 载入数据
heart = pd.read_csv('data/processed.cleveland.data.csv', names=header_row)

# heart = pd.read_csv('../data/processed.cleveland.data.csv', names=header_row)

# 心脏病（0=否，1=是）
heart["target"] = np.where(heart["target"] != 0, 1, 0)

data = heart
countNoDisease = len(data[data.target == 0])
countHaveDisease = len(data[data.target == 1])
countfemale = len(data[data.sex == 0])
countmale = len(data[data.sex == 1])

female=data[data.sex==0]
male=data[data.sex==1]
#患病女性
have_countfemale=len(female[female.target==1])
#患病男性
have_countmale= len(male[male.target == 1])
#未患病女性
no_countfemale=countfemale-have_countfemale
#未患病男性
no_countmale=countmale-have_countmale


# print(f'没患病人数:{countNoDisease}', end=' ,')
# print("没有得心脏病比率: {:.2f}%".format((countNoDisease / (len(data.target)) * 100)))
# print(f'有患病人数:{countHaveDisease}', end=' ,')
# print("患有心脏病比率: {:.2f}%".format((countHaveDisease / (len(data.target)) * 100)))
# print(f'女性人数:{countfemale}', end=' ,')
# print("女性比例: {:.2f}%".format((countfemale / (len(data.sex)) * 100)))
# print(f'男性人数:{countmale}', end=' ,')
# print("男性比例: {:.2f}%".format((countmale / (len(data.sex)) * 100)))

def get_ratio():
    """
    获取患病比率
    :return:
    """
    count = {'countNoDisease': countNoDisease, 'countHaveDisease': countHaveDisease, 'have_countfemal': have_countfemale,
             'have_countmale': have_countmale,'no_countfemale':no_countfemale,'no_countmale':no_countmale
             }
    ratio = {
        'ratioNoDisease': countNoDisease / (len(data.target)),
        'ratioHaveDisease': countHaveDisease / (len(data.target)),
        'ratiomale': countmale / (len(data.sex)), 'ratiofemale': countfemale / (len(data.sex))
    }
    return count, ratio


def age_thalach():
    """
    年龄心率分布
    :return:
    """
    x0=data.age[data.target == 1]
    y0=data.thalach[(data.target == 1)]
    x1=data.age[data.target == 0]
    y1=data.thalach[(data.target == 0)]

    return {'have':[x0.to_list(), y0.to_list()],'no':[x1.to_list(),y1.to_list()]}


def age_trestbps():
    """
    年龄血压分布
    :return:
    """
    x0=data.age[data.target == 1]
    y0=data.trestbps[data.target == 1]
    x1=data.age[data.target == 0]
    y1=data.trestbps[data.target == 0]

    return {'have':[x0.to_list(),y0.to_list()],'no':[x1.to_list(),y1.to_list()]}

def trestbps_thalach():
    """
    心率和血压
    :return:
    """
    x0 = data.thalach[data.target == 1]
    y0 = data.trestbps[data.target == 1]
    x1=data.thalach[data.target == 0]
    y1=data.trestbps[data.target == 0]

    return {'have':[x0.to_list(),y0.to_list()],'no':[x1.to_list(),y1.to_list()]}


def cp():
    """
    胸痛类型
    :return:
    """
    res0=data.cp.value_counts()
    y0=res0.to_list()
    res1=data.cp[data.target==1].value_counts()
    y1=res1.to_list()
    have=y1
    no= list(map(lambda x: x[0] - x[1], zip(y0, have)))
    return have,no


def correlation():
    """
    相关性分析
    :return:
    """
    data_list=[]
    res=data.corr().values # 将pd格式转化为矩阵
    for i in range(len(res)):
        for j in range(len(res)):
            a=[i,j,round(res[i][j],2)]
            data_list.append(a)
    return data_list





if __name__ == '__main__':
    print(correlation())