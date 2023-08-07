from pylab import *
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import rcParams

config = {"font.family":"Times New Roman"}
rcParams.update(config)

def fig3():
#     sns.set()
    df=pd.read_excel("F:\YAO_2023\Apple\workspace\data\data_final.xlsx")[['PP-MM', 'PP-FC',
       'PP-ATESC', 'PP-ACD', 'PP-Experts', 'PP-FFF', 'PP-PPE','ST-MM', 'ST-FC',
       'ST-ATESC', 'ST-ACD', 'ST-Experts', 'ST-FFF', 'ST-PPE', 
       'Pe-MM', 'Pe-FC',
       'Pe-ATESC', 'Pe-ACD', 'Pe-Experts', 'Pe-FFF', 'Pe-PPE',
       'Fe-MM', 'Fe-FC',
       'Fe-ATESC', 'Fe-ACD', 'Fe-Experts', 'Fe-FFF', 'Fe-PPE', 
       'FB-MM', 'FB-FC',
       'FB-ATESC', 'FB-ACD', 'FB-Experts', 'FB-FFF', 'FB-PPE']].sum().reset_index()
    df.columns=['Cat','Count']
    df['Management']=df.Cat.apply(lambda x:x.split('-')[0])
    df['IS']=df.Cat.apply(lambda x:x.split('-')[1])

    df=df.replace({'Management':{'PP':'Rootstock','Pe':'Pesticide use','Fe':'Fertilization','FB':'Fruit bagging','ST':'Seedling treatments'}})
    df=df.replace({'IS':{'Experts':'Local expert','FFF':'Farmer peers','PPE':'Personal experience','MM':'Mass media','FC':'Farmer cooperatives'}})
    fig,ax=plt.subplots(figsize=(8,4),nrows=1,ncols=1)
    df=df.pivot(index='IS', columns='Management', values='Count').reset_index()
    df.set_index('IS').plot(kind='bar', stacked=True,ax=ax)
    ax.set_ylabel('Count',fontsize=10,fontweight='bold')
    ax.set_xlabel('Communication channel',fontsize=10, fontweight='bold')
    plt.tight_layout(pad=0)
    ax.tick_params(axis='both', which='major', rotation=0,labelsize=10)
    # fig.savefig('../fig/fig3.png',dpi=300,pad_inches=0.0)
if __name__=='__main__':
    fig3()
    plt.show()

