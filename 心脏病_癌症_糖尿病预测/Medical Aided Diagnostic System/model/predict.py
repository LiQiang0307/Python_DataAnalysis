# from sklearn.externals import joblib
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')  # 过滤掉警告信息

def predict(path,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    """
    预测心脏病的模型
    :param path:
    :param age:
    :param sex:
    :param cp:
    :param trestbps:
    :param chol:
    :param fbs:
    :param restecg:
    :param thalach:
    :param exang:
    :param oldpeak:
    :param slope:
    :param ca:
    :param thal:
    :return:
    """
    knn_digits = joblib.load(path)
    # 构造数据格式
    res = pd.DataFrame(
        {'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps],
         'chol': [chol], 'fbs': [fbs], 'restecg': [restecg],
         'thalach': [thalach],'exang':[exang],'oldpeak':[oldpeak],'slope':[slope],'ca':[ca],'thal':[thal]
         }
    )
    #使用模型
    pre_res=knn_digits.predict(res)[0]
    return pre_res


# 预测糖尿病的模型
def predict_Tang(path,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    knn_digits = joblib.load(path)
    """
    #Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
    #'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
    #dtype='object')
    #特征（怀孕次数，血糖，血压，皮脂厚度，胰岛素，BMI身体质量指数，糖尿病遗传函数，年龄，结果）
    # 构造数据格式
    """
    res = pd.DataFrame(
        {'Pregnancies': [Pregnancies], 'Glucose': [Glucose], 'BloodPressure': [BloodPressure], 'SkinThickness': [SkinThickness],
         'Insulin': [Insulin], 'BMI': [BMI], 'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
         'Age': [Age]}
    )
    #使用模型
    pre_res=knn_digits.predict(res)[0]
    return pre_res


# 预测癌症
def predict_A(path,radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension):
    knn_digits = joblib.load(path)

    res = pd.DataFrame(
        {'radius': [radius], 'texture': [texture], 'perimeter': [perimeter], 'area': [area],
         'smoothness': [smoothness], 'compactness': [compactness], 'symmetry': [symmetry],
         'fractal_dimension': [fractal_dimension]}
    )
    #使用模型
    pre_res=knn_digits.predict(res)[0]
    return pre_res


if __name__ == '__main__':
    res=predict('./心脏病预测KNN.m',63,1,1,145,233,1,2,150,0,2.3,3,0,6)
    res2=predict('./心脏病预测KNN.m',67,1,4,120,229,0,2,129,1,2.6,2,2,7)
    # print(res)
    # 用sklearn0.24.1训练一下模型。
    result=predict_Tang('./糖尿病KNN.m',6,148,72,35,0,33.6,0.627,50)
    result2=predict_A('癌症KNN.m',23,12,151,954,0.143,0.278,0.242,0.079)

    print(result2)