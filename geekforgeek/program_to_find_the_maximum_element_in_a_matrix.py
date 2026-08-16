"""
Given an NxM matrix. The task is to find the maximum element in this matrix.

Examples: 

Input: mat[4][4] = {{1, 2, 3, 4},
                    {25, 6, 7, 8},
                    {9, 10, 11, 12},
                    {13, 14, 15, 16}};
Output: 25

Input: mat[3][4] = {{9, 8, 7, 6},
                    {5, 4, 3, 2},
                    {1, 0, 12, 45}};
Output: 45
"""
def find_maximum_number(matrix):
    max_number = float('-inf')
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if max_number < matrix[row][col]:
                max_number = matrix[row][col]
    return max_number
