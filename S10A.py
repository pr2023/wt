
import pandas as pd
data=pd.read_csv(“/home/pc Ds/ weight-height.csv”)
mean_data=data[“sepalLengthCm’].mean()
median_data=data[“sepalLengthCm”].median()
print(“\n Mean of sepal length: ”,mean_data.”\n Median of sepal length: 
“,median_data)
mean_data=data[“sepalwidthCm”].median()
print(“\n Mean of sepal width: ”,mean_data.”\n Median of sepal width: 
“,median_data)
mean_data=data[“petalLengthCm’].mean()
median_data=data[“petalLengthCm’].median()
print(“\n Mean of petal length: ”,mean_data.”\n Median of petal length: 
“,median_data)
mean_data=data[“petalwidthCm’].mean()
mean_data=data[“petalwidthCm’].median()
print(“\n Mean of petal _width: ”,mean_data.”\n Median of petal_width: 
",Median_data)