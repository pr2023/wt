import pandas as pd
from sklearn.preprocessing
df=pd.read_csv(‘/home/pc256/tybcs-(sem-1)DS/winequality-red.csv’)
data_sacler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_sacled=data_scalar.fit_transform(df)
print(data_scaled.round(2))