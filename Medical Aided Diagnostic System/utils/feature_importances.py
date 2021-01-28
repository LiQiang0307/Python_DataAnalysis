import numpy as np
import pandas as pd

# 添加列名
header_row = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', \
              'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# 载入数据
heart = pd.read_csv('data/processed.cleveland.data.csv', names=header_row)
# heart = pd.read_csv('../data/processed.cleveland.data.csv', names=header_row)

# 数据预处理
features = heart[['age','sex','cp','trestbps','chol','fbs',\
                'restecg','thalach','exang','oldpeak','slope','ca','thal']]
targets = heart['target']

# 将离散型数据，从普通的0,1,2这些，转换成真正的字符串表示

# sex
features.loc[features['sex']==0,'sex'] = 'female'
features.loc[features['sex']==1,'sex'] = 'male'

# cp
features.loc[features['cp'] == 1,'cp'] = 'typical'
features.loc[features['cp'] == 2,'cp'] = 'atypical'
features.loc[features['cp'] == 3,'cp'] = 'non-anginal'
features.loc[features['cp'] == 4,'cp'] = 'asymptomatic'

# fbs
features.loc[features['fbs'] == 1,'fbs'] = 'true'
features.loc[features['fbs'] == 0,'fbs'] = 'false'

# exang
features.loc[features['exang'] == 1,'exang'] = 'true'
features.loc[features['exang'] == 0,'exang'] = 'false'

# slope
features.loc[features['slope'] == 1,'slope'] = 'true'
features.loc[features['slope'] == 2,'slope'] = 'true'
features.loc[features['slope'] == 3,'slope'] = 'true'

# thal
features.loc[features['thal'] == 3,'thal'] = 'normal'
features.loc[features['thal'] == 3,'thal'] = 'fixed'
features.loc[features['thal'] == 3,'thal'] = 'reversable'

# restecg
# 0：普通，1：ST-T波异常，2：可能左心室肥大
features.loc[features['restecg'] == 0,'restecg'] = 'normal'
features.loc[features['restecg'] == 1,'restecg'] = 'ST-T abnormal'
features.loc[features['restecg'] == 2,'restecg'] = 'Left ventricular hypertrophy'

# ca
features['ca'].astype("object")

# thal
features.thal.astype("object")

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

features = pd.get_dummies(features)
features_temp = StandardScaler().fit_transform(features)
# features_temp = StandardScaler().fit_transform(pd.get_dummies(features))

X_train,X_test,y_train,y_test = train_test_split(features_temp,targets,test_size=0.25)

# 随机森林
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train,y_train)


importances = pd.Series(data=rf.feature_importances_,index=features.columns).sort_values(ascending=True)

def get_feature_importance():
    """
    获取不同特征的重要性
    :return:
    """
    x=[round(i,3) for i in importances.values.tolist()]
    y=importances.index.tolist()

    return x,y

if __name__ == '__main__':
    print(get_feature_importance())