import numpy as np

def create_random_matrix():
    matrix = np.random.randint(1, 10, (3, 3))
    while np.linalg.det(matrix) == 0:
        matrix = np.random.randint(1, 10, (3, 3))
    return matrix

def determinant(matrix):
    return np.linalg.det(matrix)

def inverse(matrix):
    return np.linalg.inv(matrix)
