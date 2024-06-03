import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

added_matrix = np.add(matrix1, matrix2)
subtracted_matrix = np.subtract(matrix1, matrix2)

print("Added matrix:\n", added_matrix)
print("Subtracted matrix:\n", subtracted_matrix)
