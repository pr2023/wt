import numpy as np
a = np.arange(4).reshape((2,2))
print("Original flattened array:")
print(a)
print("Maximum value of the above flattened array:")
print(np.amax(a))
print("Minimum value of the above flattened array:")
print(np.amin(a))
