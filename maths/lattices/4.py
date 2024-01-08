import numpy as np

# Given basis vectors
v1 = np.array([6, 2, -3])
v2 = np.array([5, 1, 4])
v3 = np.array([2, 7, 1])

# Create the matrix A with rows corresponding to the basis vectors
A = np.vstack((v1, v2, v3))

# Calculate the determinant of A
det_A = np.linalg.det(A)

# Calculate the volume of the fundamental domain (take the absolute value of the determinant)
volume = abs(det_A)

# Print the result
print("Volume of the fundamental domain:", volume)