import sys
from collections import deque


class PopulationMovement:
    def __init__(self):
        input = sys.stdin.readline

        self.N, self.L, self.R = map(int, input().split())
        self.grid = [
            list(map(int, input().split()))
            for _
            in range(self.N)
        ]

        self.dr = [1, -1, 0, 0]
        self.dc = [0, 0, 1, -1]

    def _bfs(self, r, c, visited):
        queue = deque([(r, c)])
        visited[r][c] = True
        union = [(r, c)]
        total_population = self.grid[r][c]

        while queue:
            curr_r, curr_c = queue.popleft()

            for i in range(4):
                nr = curr_r + self.dr[i]
                nc = curr_c + self.dc[i]

                if 0 <= nr < self.N and 0 <= nc < self.N and not visited[nr][nc]:
                    if self.L <= abs(self.grid[curr_r][curr_c] - self.grid[nr][nc]) <= self.R:
                        visited[nr][nc] = True

                        queue.append((nr, nc))
                        union.append((nr, nc))

                        total_population += self.grid[nr][nc]

        if len(union) > 1:
            avg = total_population // len(union)

            for curr_r, curr_c in union:
                self.grid[curr_r][curr_c] = avg
            return True

        return False

    def run(self):
        days = 0
        while True:
            visited = [[False] * self.N for _ in range(self.N)]
            is_moved = False

            for i in range(self.N):
                for j in range(self.N):
                    if not visited[i][j]:
                        if self._bfs(i, j, visited):
                            is_moved = True

            if not is_moved:
                break

            days += 1

        print(days)


if __name__ == '__main__':
    PopulationMovement().run()
