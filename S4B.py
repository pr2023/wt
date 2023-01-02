import numpy as np
import pandas as pd
df = pd.read_csv('/home/pc256/TYBCS-(sem-I)DS/Iris.csv')
#print(df.head(6))
print('shape of CSV')
print(df.shape)
print('Data types')
print(df.dtypes)
print('Description of CSV')
print(df.describe())
