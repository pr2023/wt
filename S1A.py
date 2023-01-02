import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
ax=plt.subplots(1,1,figsize=(10,8))
iris['species'].value_counts().plot.pie(explode=[0.1,0.1,0.1],autopct='%5.1f%%',shadow=True,figsize=(5,8))
plt.title("Iris Species %")
plt.show()
