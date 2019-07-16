import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0,5001,20000).reshape(1000,20)

# Average of the values in each column of X
ave_cols = X.mean(axis=0)

# Standard Deviation of the values in each column of X
std_cols = X.std(axis=0)

# Mean normalize X
X_norm = (X-ave_cols)/std_cols
