#!/usr/bin/python3
"""Defines a function of pascal triangle"""


def pascal_triangle(n):
    """
    Pascal triangle

    Args:
        n (int): number provided
    Returns:
        list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        temp = [1]
        for i in range(1, len(triangle)):
            temp.append(triangle[i - 1] + triangle[i])
        temp.append(1)
        triangles.append(temp)
    return triangles
