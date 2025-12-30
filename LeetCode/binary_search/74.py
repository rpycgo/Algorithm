class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n - 1

        while left <= right:
            mid = (left+right) // 2

            idx_row = mid // n
            idx_col = mid % n

            if matrix[idx_row][idx_col] == target:
                return True
            if matrix[idx_row][idx_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
