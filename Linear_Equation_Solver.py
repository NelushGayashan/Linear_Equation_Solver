import numpy as np

# Coefficient matrix
A = np.array([[76, -25, -50],
              [-25, 56, -1],
              [-50, -1, 81]])

# Right-hand side vector
B = np.array([10, 0, 0])

# Inverse Matrix Method
A_inv = np.linalg.inv(A)
solution_inv = np.dot(A_inv, B)
x_inv, y_inv, z_inv = solution_inv
print("Using Inverse Matrix Method:")
print(f"x = {x_inv}")
print(f"y = {y_inv}")
print(f"z = {z_inv}")

# Gaussian Elimination Method
A_aug = np.array([[76, -25, -50, 10],
                  [-25, 56, -1, 0],
                  [-50, -1, 81, 0]], dtype=float)  # Ensure dtype is float for precision

n = A_aug.shape[0]

# Forward elimination
for i in range(n):
    # Divide the current row by the diagonal element to make it 1
    divisor = A_aug[i, i]
    A_aug[i] /= divisor
    # Eliminate below the diagonal
    for j in range(i + 1, n):
        multiplier = A_aug[j, i]
        A_aug[j] -= multiplier * A_aug[i]

# Backward substitution
sol = np.zeros(n)
for i in range(n - 1, -1, -1):
    sol[i] = A_aug[i, -1] - np.dot(A_aug[i, :-1], sol)

x_gauss, y_gauss, z_gauss = sol
print("\nUsing Gaussian Elimination Method:")
print(f"x = {x_gauss}")
print(f"y = {y_gauss}")
print(f"z = {z_gauss}")
