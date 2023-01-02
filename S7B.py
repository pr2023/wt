import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
data=pd.read_csv("/home/pc256/TYBCS-(sem-I)DS/Assignment3/Data1.csv")
df2=pd.DataFrame(data)
labelencoder = LabelEncoder()
df2['Purchased'] = labelencoder.fit_transform(df2['Purchased'])
print(df2)
