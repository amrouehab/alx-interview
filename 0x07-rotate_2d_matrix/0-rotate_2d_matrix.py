#!/usr/bin/python3
"""
Rotates an n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): A 2D n x n matrix to rotate.
    """
    n = len(matrix)

    # First transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then reverse each row
    for row in matrix:
        row.reverse()

