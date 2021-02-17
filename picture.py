'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-02-17 14:01:04
LastEditTime: 2021-02-17 14:29:06
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial']  # 如果要显示中文字体,则在此处设为：SimHei
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

x = np.array([1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14])

a5=np.array([30.20, 31.65, 31.80, 31.80, 31.80,31.80,31.80,31.80,31.80,31.80,31.80,31.80,31.80,31.80])
a10=np.array([30.40, 31.70, 31.98, 32.10, 32.10, 32.10,32.10,32.10,32.10,32.10,32.10,32.10,32.10,32.10])
a15=np.array([30.10, 32.20, 32.40, 32.50, 32.53, 32.55, 32.58,32.60,32.60,32.60,32.60,32.60,32.60,32.60])
a20=np.array([29.70, 31.9, 32.25, 32.35, 32.42, 32.50, 32.55,32.58,32.60,32.60,32.60,32.64,32.64,32.64])
a25=np.array([29.50, 31.50, 32.10, 32.20, 32.30, 32.35, 32.40,32.45,32.50,32.55,32.60,32.62,32.65,32.70])

# VGG_supervised = np.array([2.9749694, 3.9357018, 4.7440844, 6.482254, 8.720203, 13.687582])
# VGG_unsupervised = np.array([2.1044724, 2.9757383, 3.7754183, 5.686206, 8.367847, 14.144531])
# ourNetwork = np.array([2.0205495, 2.6509762, 3.1876223, 4.380781, 6.004548, 9.9298])



# label在图示(legend)中显示。若为数学公式,则最好在字符串前后添加"$"符号
# color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
# 线型：-  --   -.  :    ,
# marker：.  ,   o   v    <    *    +    1
plt.figure(figsize=(10, 5))
plt.grid(linestyle="--")  # 设置背景网格线为虚线
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 去掉上边框
ax.spines['right'].set_visible(False)  # 去掉右边框


plt.plot(x, a5, marker='o', color="blue", label="n=5", linewidth=1.5)
plt.plot(x, a10, marker='o', color="green", label="n=10", linewidth=1.5)
plt.plot(x, a15, marker='x', color="red", label="n=15(ours)", linewidth=1.5)
plt.plot(x, a20, marker='o', color="yellow", label="n=20", linewidth=1.5)
plt.plot(x, a25, marker='o', color="pink", label="n=25", linewidth=1.5)


group_labels = ['300', '350', '400', '450', '500', '550', '600','650','700','750','800','950','1000','1050']  # x轴刻度的标识
plt.xticks(x, group_labels, fontsize=12, fontweight='bold')  # 默认字体大小为10
plt.yticks(fontsize=12, fontweight='bold')
# plt.title("example", fontsize=12, fontweight='bold')  # 默认字体大小为12
plt.xlabel("Epoch", fontsize=13, fontweight='bold')
plt.ylabel("PSNR", fontsize=13, fontweight='bold')
plt.xlim(0.9, 14.1)  # 设置x轴的范围
plt.ylim(29.0, 33.0)

# plt.legend()          #显示各曲线的图例
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=12, fontweight='bold')  # 设置图例字体的大小和粗细

plt.savefig('./filename.svg', format='svg')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
plt.show()