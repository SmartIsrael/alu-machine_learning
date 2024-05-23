#!/usr/bin/env python3
def determinant(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0:  # Handle empty matrix case
        return 1

    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            submatrix = [row[:i] + row[i+1:] for row in (matrix[:j] + matrix[j+1:]
                         for j in range(1, n))]
            det += ((-1)**i) * matrix[0][i] * determinant(submatrix)
        return det
