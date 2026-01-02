class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        idx_row = 0
        idx_col = n-1

        while idx_row < m and 0 <= idx_col:
            value = matrix[idx_row][idx_col]

            if target == value:
                return True
            elif target > value:
                idx_row += 1
            else:
                idx_col -= 1

        return False
