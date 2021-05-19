#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve, validation_curve


plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# In[2]:


from sklearn import neighbors

knn = neighbors.KNeighborsClassifier()

# In[31]:


# 添加列名
header_row = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age','Outcome']

# 载入数据
heart = pd.read_csv('diabetes1.csv', names=header_row)

# In[32]:


x = heart[
    ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]

# In[46]:


# 心脏病（0=否，1=是）
heart["Outcome"] = np.where(heart["Outcome"] != 0, 1, 0)
label = heart.Outcome
print(label)
# In[47]:
# label=label.astype(float)
#
# print(label)
# In[48]:
print(x)

score = []
krange = range(1, 10)
for i in krange:
    clf = neighbors.KNeighborsClassifier(n_neighbors=i, metric="euclidean")
    clf = clf.fit(x[:200], label[:200])
    score.append(clf.score(x[200:], label[200:]))
bestK = krange[score.index(max(score))]
print(bestK)
print(score)
print(max(score))

# In[49]:
clf = neighbors.KNeighborsClassifier(n_neighbors=5, metric="euclidean")
clf = clf.fit(x, label)

# 绘制学习曲线
plt.figure(figsize=(6, 4), dpi=80)
plt.plot(krange, score)
plt.title('K值学习曲线', fontsize=15)
plt.xlabel('K值', fontsize=12)
plt.ylabel('预测准确率', fontsize=12)
plt.xticks(krange[::2])
plt.show()

# In[50]:


clf.predict(x[100:200])

# In[51]:



# In[52]:

import joblib
# 保存模型
joblib.dump(clf, '糖尿病KNN.m')

# In[53]:


# 提取算法
knn_digits = joblib.load("糖尿病KNN.m")

# In[54]:


# 使用模型
knn_digits.predict(x[:20])

# In[22]:


# a3=pd.DataFrame({'一卡通消费':[60],'上网情况得分':[60],'获奖情况得分':[74],'图书馆得分':[70],'网络空间状态得分':[70],'成绩得分':[60],'社交得分':[60],'心理健康调查问卷得分':[60]})


# In[23]:


# a3.dtypes


# In[56]:


#####20201023
train_size, train_scores, test_scores = learning_curve(clf, x, label, cv=10, scoring='accuracy',  # 10折交叉验证
                                                       train_sizes=np.linspace(0.1, 1.0, 5))  # 5次的训练数量占比
mean_train = np.mean(train_scores, 1)  # (5,)
# 得到得分范围的上下界
upper_train = np.clip(mean_train + np.std(train_scores, 1), 0, 1)
lower_train = np.clip(mean_train - np.std(train_scores, 1), 0, 1)

mean_test = np.mean(test_scores, 1)
# 得到得分范围的上下界
upper_test = np.clip(mean_test + np.std(test_scores, 1), 0, 1)
lower_test = np.clip(mean_test - np.std(test_scores, 1), 0, 1)

plt.figure('Fig1')
plt.plot(train_size, mean_train, 'ro-', label='train score')
plt.plot(train_size, mean_test, 'go-', label='test score')
##填充上下界的范围
plt.fill_between(train_size, upper_train, lower_train, alpha=0.2,  # alpha：覆盖区域的透明度[0,1],其值越大，表示越不透明
                 color='r')
plt.fill_between(train_size, upper_test, lower_test, alpha=0.2,  # alpha：覆盖区域的透明度[0,1],其值越大，表示越不透明
                 color='g')
plt.grid()
plt.xlabel('train size')
plt.ylabel('score')
plt.legend(loc='lower right')
plt.title('KNN')
plt.savefig('train number-size.png')
plt.show()

######20201023knn_digits.predict(a3)


# In[57]:


from sklearn.metrics import accuracy_score

# In[59]:


y_predict = clf.predict(x[:200])

# In[61]:


print(accuracy_score(label[:200], y_predict))

# In[63]:


clf.score(x[:200], label[:200])

# In[ ]:




