
import pandas as pd
from sklearn.preprocessing
df=pd.read_csv(‘/home/pc256/tybcs-(sem-1)DS/winequality-red.csv’)
data_binarized=preprocessing.Binarizer(threshold=s).transform(df)
dn=preprocessing.normalize(df,norm=’l1’)
print(“\n Binarized Data”)
print(“--------------------------“)
print(data_binarized)