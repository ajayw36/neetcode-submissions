class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = -1

        while left <= right:
            m = (left + right) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                row = m
                break
            elif target < matrix[m][0]:
                right = m - 1
            else:
                left = m + 1
        
        if row == -1:
            return False
        
        new_list = matrix[row]
        left = 0
        right = len(new_list) - 1

        while left <= right:
            m = (left + right) // 2
            if new_list[m] == target:
                return True
            elif target < new_list[m]:
                right = m - 1
            else:
                left = m + 1
        return False
                