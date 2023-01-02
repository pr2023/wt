#Import the library
import pandas as pd
#Create an empty data frame with column names
df = pd.DataFrame(columns = ['name','age','Per'])
#Add records
df.loc[0] = ['Rohit', 5, 85]
df.loc[1] = ['Ajinkya',10, 75]
df.loc[2] = ['XYZ', 20, 2019]
df.loc[3] = ['PQR', 30, 2015]
#Print the dataframe
print(df)   
