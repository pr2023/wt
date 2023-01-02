import pandas as pd
data=pd.read_csv("/home/pc256/TYBCS-(sem-I)DS/Data1.csv")
print("des the dataset")
print(data.describe())
print("shape of the data")
print(data.shape)
print("first 3 rows ")
print(data.head(3))
print("Last 3 rows:")
print(data.tail(3))
print("random records ")
print(data.sample(3))
                    
