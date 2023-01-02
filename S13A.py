import pandas as pd
import numy as np
import matplotlib.pyplot as plt
iris=pd.read_csv(“/home/pc256/tybcfig=iris[iris.species=’Iris 
setosa’].plot.scatter(x=’PetalLengthCm’,y=’PetalWidthCm’,color=’orange’,label
=’setosa’)
iris[iris.species==’Iris 
versicolor’].plot.scatter(x=’PetalLengthCm’,y=’PetalWidthCm’,color=’blue’,labe
l=’versicolor’,ax=fig)
iris[iris.species==’Iris 
virginica’].plot.scatter(x=’PetalLengthCm’,y=’PetalWidthCm’,color=’green’,label
=’virginica’,ax=fig)
fig.set_xlabel(“Petal Length”)
fig.set_ylabel(“Petal width”)
fig.set_title(“petal Length vs Width”)
fig.=plt.gcf()
fig.set_size_inches(12,8)
plt.show()