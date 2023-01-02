
import pandas as pd
df=pd.DataFrame(column=[‘Name’,’Salary’,’Department’])
df.loc[0]=[‘mansi’,None,’IT’]
df.loc[1]=[‘harshal’,60000’IT’]
df.loc[2]=[‘deva’,60000’IT’]
df.loc[3]=[‘mansi’,60000,None]
df.loc[4]=[‘mansi’,60000’IT’]
df.loc[5]=[‘mansi’,60000’IT’]
df.loc[6]=[‘viraj’,60000’IT’]
df.loc[7]=[‘dadu’,60000’IT’]
df.loc[8]=[‘mau’,60000’IT’]
df.loc[9]=[‘TAU’,60000’IT’]
print(df.dropna())