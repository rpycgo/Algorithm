class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])

        for j in range(1, n_col):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        for i in range(1, n_row):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        for i in range(1, n_row):
            for j in range(1, n_col):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])

        answer = grid[n_row-1][n_col-1]

        return answer
