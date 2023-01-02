
import pandas as pd 
df=pd.DataFrame({‘Name’:[‘pratham’,’ganesh’,’deepak’,’mansi’],
 ‘Per’:[98,85,92,72],
 ‘Age’:[21,20,23,20]})
print(“ Average of graduation percentage:”,df[‘per’].mean())
print(“Average of age of student:”,df[‘Age’].mean())