import pandas as pd
data=pd.read_csv("/home/pc256/TYBCS-(sem-I)DS/weight-height.csv")
print("\n first 10 rows")
print(data.head(10))
print("\n last  10 rows")
print(data.tail(10))
print("\n random 20 rows ")
print(data.sample(20))
