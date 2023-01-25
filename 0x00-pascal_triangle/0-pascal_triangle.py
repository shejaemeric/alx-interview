#!/usr/bin/python3
"""module to display pascal triangle"""


def pascal_triangle(n):

    """display pascal triangle of n

    Args:
        n (integer): pascal number to stop on.
    """

    if n <= 0:
        return []
    else:
        results = [[1]]
        pascal_list = [1]
        for n in range(1, n):
            new_pascal_list = [1]
            for n in range(0, len(pascal_list) - 1):
                new_pascal_list.append(
                    pascal_list[n] + pascal_list[n+1])
            new_pascal_list.append(1)
            pascal_list = new_pascal_list
            results.append(pascal_list)
        return results
