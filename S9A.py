import numpy as np
import matplotlib.pyplot as plt
x=np.random.randn(50)
y=np.random.randn(50)
plt.plot(x,y)
plt.scatter(x,y)
plt.hist(x)
plt.boxplot(x, vert=True)
#plt.show()
plt.scatter(x, y, s=110, c = 'red', marker ='*')
plt.hist(x, facecolor ='y',linewidth=2,edgecolor='k')
plt.show()
 

