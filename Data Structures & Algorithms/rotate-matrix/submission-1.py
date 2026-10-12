class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new_matrix = [[0] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                # new row = old col
                # new col = n - 1 - row
                # row, col --> col, n - 1 - row
                new_matrix[col][n - 1 - row] = matrix[row][col]
        matrix[:] = new_matrix