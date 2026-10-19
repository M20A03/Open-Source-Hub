"""
Matrix Operations Library
Author: Mayank Raj (M20A03)
Co-Author: mayankrajdhn5-prog
"""

from typing import List

Matrix = List[List[float]]

def matrix_multiply(A: Matrix, B: Matrix) -> Matrix:
    """Multiplies two matrices A (m x k) and B (k x n) returning matrix (m x n)."""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Incompatible matrix dimensions for multiplication")

    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_transpose(A: Matrix) -> Matrix:
    """Returns the transpose of matrix A."""
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
