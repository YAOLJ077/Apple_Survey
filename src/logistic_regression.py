{\rtf1\ansi\ansicpg936\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
import pandas as pd\
import statsmodels.api as sm\
\
RS = pd.read_csv("../data/Binary_Technology_RS.csv")\
RS['intercept']=1.0\
\
dummy_1=pd.get_dummies(RS['Gender'],prefix='Gender')\
dummy_2=pd.get_dummies(RS['Training'],prefix='Training')\
dummy_3=pd.get_dummies(RS['Identity'],prefix='Identity')\
dummy_4=pd.get_dummies(RS['Farm Cooperative'],prefix='Farm Cooperative')\
dummy_5=pd.get_dummies(RS['RS_MM'],prefix='RS_MM')\
dummy_6=pd.get_dummies(RS['RS_FC'],prefix='RS_FC')\
dummy_7=pd.get_dummies(RS['RS_ATESC'],prefix='RS_ATESC')\
dummy_8=pd.get_dummies(RS['RS_ACD'],prefix='RS_ACD')\
dummy_9=pd.get_dummies(RS['RS_EXP'],prefix='RS_EXP')\
dummy_10=pd.get_dummies(RS['RS_FP'],prefix='RS_FP')\
dummy_11=pd.get_dummies(RS['RS_PE'],prefix='RS_PE')\
dummy_12=pd.get_dummies(RS['Rootstock'],prefix='Rootstock')\
\
cols_to_keeps=[ 'Age', 'Edu', 'Area', 'T-Age','intercept']\
\
data_1=RS[cols_to_keeps].join(dummy_1.loc[:,'Gender_0'])\
data_2=data_1.join(dummy_2.loc[:,'Training_0'])\
data_3=data_2.join(dummy_3.loc[:,'Identity_0'])\
data_4=data_3.join(dummy_4.loc[:,'Farm Cooperative_0'])\
data_5=data_4.join(dummy_5.loc[:,'RS_MM_0'])\
data_6=data_5.join(dummy_6.loc[:,'RS_FC_0'])\
data_7=data_6.join(dummy_7.loc[:,'RS_ATESC_0'])\
data_8=data_7.join(dummy_8.loc[:,'RS_ACD_0'])\
data_9=data_8.join(dummy_9.loc[:,'RS_EXP_0'])\
data_10=data_9.join(dummy_10.loc[:,'RS_FP_0'])\
data_11=data_10.join(dummy_11.loc[:,'RS_PE_0'])\
data_12=data_11.join(dummy_12.loc[:,'Rootstock_1'])\
\
dd=data_12\
dd_Columns=dd.columns[0:16]\
logit_RS=sm.Logit(dd['Rootstock_1'],dd[dd_Columns])\
result_RS=logit_RS.fit()\
print(result_RS.summary())\
\
#OR
\f1 \'ba\'cd\'d6\'c3\'d0\'c5\'c7\'f8\'bc\'e4\
params = np.exp (result_RS.params))\
conf = result_RS.conf_int()\
conf['OR'] = params\
conf.columns = ['5%','95%','OR']\
print(np.exp(conf))\
}