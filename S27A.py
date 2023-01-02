import numy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv(“/home/pc256/TYBCS(sem1)Ds/Assignment 3/Data1.csv”)
df2=pd.DataFrame(data)
onc=OneHotEncoder(handel_unknown=’ignore’)
enc_df=pd.DataFrame(enc.fit transform(df2[[‘country’]]).toarray())
print(enc_df)