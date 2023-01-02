import numy as np
import matplotlib.pyplot as plt
iris=pd.read_csv(“Iris.csv”)
plt.hist(‘species’,data=iris)
plt.show()
