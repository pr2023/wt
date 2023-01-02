
import pandas as pd
from sklearn.preprocessing
df=pd.read_csv(‘/home/pc256/tybcs-(sem-1)DS/winequality-red.csv’)
dn=preprocessing.normalize(df,norm=’l1’)
print(“\n L1 Normalized Data”)
print(“--------------------------“)
print(dn.round(2))