from sklearn.externals import joblib
import pandas as pd
#提取算法



def predict(path,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
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

if __name__ == '__main__':
    res=predict('./心脏病预测KNN.m',63,1,1,145,233,1,2,150,0,2.3,3,0,6)
    res2=predict('./心脏病预测KNN.m',67,1,4,120,229,0,2,129,1,2.6,2,2,7)
    print(res)