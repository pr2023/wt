
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
plt.figure(figsize = (10, 7))
new_data = data[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm","PetalWidthCm"]]
new_data.boxplot()
plt.show()
