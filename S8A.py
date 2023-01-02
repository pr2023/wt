 

import pandas as pd
from sklearn.preprocessing 
data=pd.read_csv("/home/pc256/TYBCS-(sem-I)DS/winequality-red.csv")
data_scaler=preprocessing.StandardScaler()
data_scaled=data_scaler.fit_transform(df)
print(data_scaled)
