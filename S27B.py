import pandas as pd
from sklearn.preprocessing import label Encoder
import numy as np
data=pd.read_csv(“/home/pc256/TYBCS(sem1)Ds/Assignment 3/Data1.csv”)
df2=pd.DataFrame(data)
labelencoder=LabelEncoder()
df2[‘purchased']=labelencoder.fit_transform(df2[“purchased”])
print(enc_df2)