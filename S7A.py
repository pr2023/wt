 
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data=pd.read_csv("/home/pc256/TYBCS-(sem-I)DS/Assignment3/Data1.csv")
df2=pd.DataFrame(data)
enc = OneHotEncoder(handle_unknown='ignore')
enc_df = pd.DataFrame(enc.fit_transform(df2[['Country']]).toarray())
print(enc_df)
