import pandas as pd
import scipy.stats as stats
import numpy as np
# the difference of gross margin of adopt dwarfing cultivation or non-adopt

df = pd.read_csv("F:/YAO_2023/Apple/workspace/data/adoption_difference.csv")
adop=list(df['Gross_Margin'].iloc[np.where(df['Seedlings_Treatment'] == 1)])
non_adop=list(df['Gross_Margin'].iloc[np.where(df['Seedlings_Treatment'] == 0)])

print(np.mean(adop))
print(np.mean(non_adop))

def difference(A, B):

    var_test = stats.levene(A, B)
    if var_test[1] > 0.05:
        return stats.ttest_ind(A, B, equal_var=True)
    else:
        return stats.ttest_ind(A, B, equal_var=False)

if __name__=='__main__':
    print(difference(adop, non_adop))



