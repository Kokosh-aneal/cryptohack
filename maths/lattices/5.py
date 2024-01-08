import numpy as np

# Given vectors
v = np.array([846835985, 9834798552], dtype=np.int64)
u = np.array([87502093, 123094980], dtype=np.int64)

# Gauss's algorithm for lattice reduction
while True:
    if np.linalg.norm(u) < np.linalg.norm(v):
        v, u = u, v  # Swap v and u if ||u|| < ||v||

    m = int(np.dot(v, u) / np.dot(v, v))  # Compute m = floor(v · u / v · v)

    if m == 0:
        break  # If m = 0, the basis is optimal

    u -= m * v  # Update u by subtracting m * v

# Calculate the inner product of the new basis vectors
inner_product = int(np.dot(v, u))

# print("Optimal Basis Vectors:")
# print("v =", v)
# print("u =", u)
print("Inner product of the new basis vectors:", inner_product)
