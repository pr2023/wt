import pandas as pd
import matplotlib.pyplot as plt
iris=pd.read_csv("iris.csv")
plt.hist('species',data=iris)
plt.show()
