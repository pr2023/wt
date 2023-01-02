import pandas as pd
data=pd.read_csv("/home/pc256/TYBCS-(sem-I)DS/Assignment3/Data1.csv")
print(data.fillna(data.mean()))

