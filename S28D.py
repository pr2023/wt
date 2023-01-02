import numpy as np
import pandas as pd

df = pd.DataFrame(columns = ['name','age','Per'])
#Add records
df.loc[0] = ['Rohit', 5, 85]
df.loc[1] = ['Ajinkya',10, 75]
df.loc[5]= [None, None, None]
df.loc[3] = ['PQR', 30, 2015]
#Print the dataframe
print(df)
df["remark"] = None 
print(df)
