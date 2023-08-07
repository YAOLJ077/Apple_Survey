import pandas as pd
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
import statsmodels.formula.api as smf
from openpyxl.utils.cell import col
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999
def cal_all_target():
    dfall=pd.DataFrame()
    for target in ['FB','FE','PU','RS','ST']:
        df=linear(target)
        dfall=dfall.append(df)
    dfall=dfall.pivot(index='Variable', columns='Target',values='coef(std)').reset_index()
    dfall=dfall[dfall.Variable.apply(lambda x:x in ['MM' ,'FC' ,'ATESC' ,'ACD' ,'EXP' ,'FP' ,'PE'])]
    print (df.Variable.unique())
    dfall.to_excel('../fig/table4.xlsx',index=False)
    
def linear(target):
    df = pd.read_csv("../data/Linear_gross_margin_%s.csv"%target)
    
    for col in df.columns:
        if col.find(' ')>-1 or col.find('-')>-1:
            df=df.rename(columns={col:col.replace(' ','_').replace('-','_')})
    df.columns=[col[col.find('_')+1:] if col.find(target)>-1 else col  for col in df.columns]
    IS = df.iloc[:311, 1:16]
    IS = sm.add_constant(IS)
    GM = df.iloc[:311, 0]
    # IS=information source and GM = gross margin
    # coefficient
    model = sm.OLS(GM,IS)
    ret1 = model.fit()
    # standardized coefficients beta
    std_err = df.select_dtypes(include=[np.number]).dropna().apply(stats.zscore)
    formula=df.columns[0]+' ~ '+'+'.join(df.columns[1:])


#     formula = 'y ~ x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 + x14  + x15'
    ret2 = smf.ols(formula, data=std_err).fit()
#     print (dir(ret1.summary()))
#     return ret1.summary(),ret2.summary()
    results_as_html = ret1.summary().tables[1].as_html()
    re1=pd.read_html(results_as_html, header=0, index_col=0)[0]
    results_as_html = ret2.summary().tables[1].as_html()
    re2=pd.read_html(results_as_html, header=0, index_col=0)[0] 
    df1=re1.join(re2,rsuffix='_standard')[['coef','coef_standard','P>|t|']]
    df1=df1[df1.coef!='const']
    df1['coef(std)']=df1.apply(lambda row: significant(row.coef,row.coef_standard,row['P>|t|']),axis=1)
    df1=df1.reset_index()[['index','coef(std)']]
    df1.columns=['Variable','coef(std)']
    df1=df1[df1.Variable!='const']
    df1['Target']=target
    return df1
#     df1.to_excel('../fig/table4.xlsx',index=False)
#     print (df1)
    
def significant(coef,coef_standard,p):
    if p<0.01:
        return '%.3f***(%.3f)'%(coef,coef_standard)
    elif p<0.05:
        return '%.3f**(%.3f)'%(coef,coef_standard)
    elif p<0.1:
        return '%.3f*(%.3f)'%(coef,coef_standard)
    else:
        return '%.3f(%.3f)'%(coef,coef_standard)
if __name__ == '__main__':
    print(cal_all_target())



