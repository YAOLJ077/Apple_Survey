{\rtf1\ansi\ansicpg936\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import matplotlib\
import matplotlib.pyplot as plt\
import numpy as np\
\
df = pd.read_excel("/Users/yaolinjia/Desktop/apple/Apple-survey.com/data/data_final.xlsx")\
\
Age = df["Age"].value_counts()\
Area = df["Area"].value_counts()\
Edu = df["Edu"].value_counts()\
\
Gender = df["Sex"].value_counts()\
Identity = df["Identity"].value_counts()\
Training = df["Training"].value_counts()\
FC = df["Farm Cooperative"].value_counts()\
PK = df["Pesticide Knowledge"].value_counts()\
PA = df["Prevention Awareness"].value_counts()\
\
\
# print(len(list(pd.DataFrame(Area).iloc[:,0])))\
# print(len(list(pd.DataFrame(Area).index)))\
\
plt.figure(figsize=(24,24), dpi = 400)\
\
plt.subplot(4,1,3)\
# plt.style.use('_mpl-gallery')\
plt.bar(list(pd.DataFrame(Age).index),list(pd.DataFrame(Age).iloc[:,0]), edgecolor = 'black', linewidth = 1.5)\
# plt.stem(list(pd.DataFrame(Age).index),list(pd.DataFrame(Age).iloc[:,0]),linefmt='-.',markerfmt='C3o',basefmt='-')\
# plt.title('Age', fontsize=23)\
plt.xlabel('age', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=22)\
\
plt.subplot(4,2,7)\
x_lab = ['2.5','7.5','15','25','40','75','350','400','900','1500','2000']\
y_val = [132,109,34,6,4,4,2,2,3,7,8]\
# plt.stem(x_lab,y_val,linefmt='-.',markerfmt='C3o',basefmt='-')\
plt.bar(x_lab,y_val,edgecolor = 'black', linewidth = 1.5)\
# plt.plot(list(pd.DataFrame(Area).index),list(pd.DataFrame(Area).iloc[:,0]))\
# plt.title('Area', fontsize=23)\
plt.xlabel('area', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=22)\
\
plt.subplot(4,2,8)\
plt.bar(list(pd.DataFrame(Edu).index),list(pd.DataFrame(Edu).iloc[:,0]),width = 1.0,edgecolor = 'black', linewidth = 1.5)\
# plt.stem(list(pd.DataFrame(Edu).index),list(pd.DataFrame(Edu).iloc[:,0]),linefmt='-.',markerfmt='C3o',basefmt='-')\
# plt.title('Edu', fontsize=23)\
plt.xlabel('edu', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=22)\
\
plt.subplot(4,3,1)\
gender = ['male','female']\
counts = list(pd.DataFrame(Gender).iloc[:,0])\
bar_labels=['orange','blue']\
bar_colors=['tab:orange','tab:blue']\
plt.bar(gender,counts,width=0.6,label=bar_labels,color=bar_colors, edgecolor = 'black', linewidth = 2.0)\
# plt.bar(list(pd.DataFrame(Gender).index),list(pd.DataFrame(Gender).iloc[:,0]))\
# plt.title('Gender', fontsize=23)\
plt.xlabel('gender', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=23)\
\
\
plt.subplot(4,3,2)\
iden = ['full-time','part-time']\
counts = list(pd.DataFrame(Identity).iloc[:,0])\
bar_labels=['orange','blue']\
bar_colors=['tab:orange','tab:blue']\
plt.bar(iden,counts,width=0.6,label=bar_labels,color=bar_colors, edgecolor = 'black', linewidth = 2.0)\
# plt.bar(list(pd.DataFrame(Identity).index),list(pd.DataFrame(Identity).iloc[:,0]))\
# plt.title('Identity', fontsize=23)\
plt.xlabel('identity', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=23)\
\
plt.subplot(4,3,3)\
train = ['not-joined','joined']\
counts = list(pd.DataFrame(Training).iloc[:,0])\
bar_labels=['orange','blue']\
bar_colors=['tab:orange','tab:blue']\
plt.bar(train,counts,width=0.6,label=bar_labels,color=bar_colors, edgecolor = 'black', linewidth = 2.0)\
# plt.bar(list(pd.DataFrame(Training).index),list(pd.DataFrame(Training).iloc[:,0]))\
# plt.title('Training', fontsize=23)\
plt.xlabel('training', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=23)\
\
plt.subplot(4,3,4)\
fc = ['not-joined','joined']\
counts = list(pd.DataFrame(FC).iloc[:,0])\
bar_labels=['orange','blue']\
bar_colors=['tab:orange','tab:blue']\
plt.bar(fc,counts,width=0.6,label=bar_labels,color=bar_colors, edgecolor = 'black', linewidth = 2.0)\
# plt.bar(list(pd.DataFrame(FC).index),list(pd.DataFrame(FC).iloc[:,0]))\
# plt.title('Farm cooperative', fontsize=23)\
plt.xlabel('Farm cooperative', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=23)\
\
plt.subplot(4,3,5)\
pk = ['knowed','non-knowed']\
counts = list(pd.DataFrame(PK).iloc[:,0])\
bar_labels=['orange','blue']\
bar_colors=['tab:orange','tab:blue']\
plt.bar(pk,counts,width=0.6,label=bar_labels,color=bar_colors, edgecolor = 'black', linewidth = 2.0)\
# plt.bar(list(pd.DataFrame(PK).index),list(pd.DataFrame(PK).iloc[:,0]))\
# plt.title('Pesticide Knowledge', fontsize=23)\
plt.xlabel('Pesticide Knowledge', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=23)\
\
plt.subplot(4,3,6)\
pa = ['yes', 'no']\
counts = list(pd.DataFrame(PA).iloc[:,0])\
bar_labels=['orange','blue']\
bar_colors=['tab:orange','tab:blue']\
plt.bar(pa,counts,width=0.6,label=bar_labels,color=bar_colors, edgecolor = 'black', linewidth = 2.0)\
# plt.bar(list(pd.DataFrame(PA).index),list(pd.DataFrame(PA).iloc[:,0]))\
# plt.title('Prevention Awareaness', fontsize=23)\
plt.xlabel('Prevention Awareaness', fontsize=24)\
plt.ylabel('No.farmers', fontsize=24)\
plt.tick_params(labelsize=23)\
\
\
plt.savefig('result1_subplot.png', bbox_inches='tight',dpi=300)}