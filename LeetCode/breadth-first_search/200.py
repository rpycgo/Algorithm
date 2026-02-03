class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(start_r, start_c):
            visited[start_r][start_c] = True

            queue = deque([(start_r, start_c)])
            while queue:
                curr_r, curr_c = queue.popleft()

                for i in range(4):
                    nr = curr_r + dr[i]
                    nc = curr_c + dc[i]

                    if 0 <= nr < n_row and 0 <= nc < n_col:
                        if not visited[nr][nc] and grid[nr][nc] == '1':
                            visited[nr][nc] = True
                            grid[nr][nc] = '0'
                            queue.append((nr, nc))

        dr = (-1, 1, 0, 0)
        dc = (0, 0, -1, 1)

        n_row, n_col = len(grid), len(grid[0])

        visited = [[False] * n_col for _ in range(n_row)]

        n_islands = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '1':
                    bfs(i, j)
                    n_islands += 1

        return n_islands
