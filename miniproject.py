import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0,5001,20000).reshape(1000,20)
