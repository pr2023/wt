import numpy as np
import matplotlib.pyplot as plt
x=np.random.randn(50)
y=np.random.randn(50)
plt.plot(x,y)
plt.scatter(x,y)
plt.hist(x)
plt.boxplot(x, vert=False)
plt.show()
plt.scatter(x, y, s=110, c = 'red', marker ='*', alpha=0.7)
plt.hist(x, facecolor ='y',linewidth=2,edgecolor='k', bins=30, alpha=0.6)
 
