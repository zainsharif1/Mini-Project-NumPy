import numpy as np

# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0,5001,20000).reshape(1000,20)

# Average of the values in each column of X
ave_cols = X.mean(axis=0)

# Standard Deviation of the values in each column of X
std_cols = X.std(axis=0)

# Mean normalize X
X_norm = (X-ave_cols)/std_cols

# Create a rank 1 ndarray that contains a random permutation of the row indices of `X_norm`
row_indices = np.random.permutation(X_norm.shape[0])

train_row_indices = row_indices[:600]
crossVal_row_indices = row_indices[600:800]
test_row_indices=row_indices[800:]

# Create a Training Set
X_train = X_norm[train_row_indices,:]

# Create a Cross Validation Set
X_crossVal =X_norm[crossVal_row_indices,:]

# Create a Test Set
X_test =X_norm[test_row_indices,:]
