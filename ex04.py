import numpy as np

# Create Matrix
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix Multiplication
res_multp = np.matmul(matrix_a, matrix_b)

# Matrix Dot Product
res_dot = np.dot(matrix_a, matrix_b)

# Display Result
print("Matrix A: ")
print(matrix_a)

print(" ")
print("Matrix B: ")
print(matrix_b)

print(" ")
print("Matrix Multiplication: ")
print(res_multp)

print(" ")
print("Matrix Dot Product: ")
print(res_dot)
