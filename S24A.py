import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris =pd.read_csv('/home/pc256/Iris.csv')
ax=plt.subplots(1,1,figsize=(10,8))
sns.countplot('Species',data=iris)
plt.title("Iris Species Count")
plt.show()
 
