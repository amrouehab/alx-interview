#!/usr/bin/python3
"""
Module for Pascal's Triangle implementation
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    
    Args:
        n (int): The number of rows in Pascal's triangle
        
    Returns:
        list: A list of lists representing Pascal's triangle
              Returns empty list if n <= 0
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Start each row with 1
        row = [1]
        
        # Calculate the middle values of the row
        if i > 0:
            for j in range(1, i):
                # Each element is the sum of the two elements above it
                value = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(value)
            # End each row (except the first) with 1
            row.append(1)
        
        triangle.append(row)
    
    return triangle

