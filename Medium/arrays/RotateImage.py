from typing import List


"""
Input: [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        lenght = len(matrix)

        top, bottom = 0, lenght-1

        while top < bottom:
            for col in range(lenght):
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
            top += 1
            bottom -= 1

        for row in range(lenght):
            for col in range(row+1, lenght):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        return matrix


sol = Solution()
print(sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
