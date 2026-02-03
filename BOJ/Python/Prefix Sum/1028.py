import sys


input = sys.stdin.readline


class DiamondMine:
    def __init__(self, R, C, grid):
        self.R = R
        self.C = C
        self.grid = grid

        self.bottom_right = [[0] * (C+2) for _ in range(R+2)]
        self.bottom_left = [[0] * (C+2) for _ in range(R+2)]

        self._build()

    def _build(self):
        for r in range(1, self.R+1):
            for c in range(1, self.C+1):
                if self.grid[r-1][c-1] == '1':
                    self.bottom_right[r][c] = self.bottom_right[r-1][c-1] + 1
                    self.bottom_left[r][c] = self.bottom_left[r-1][c+1] + 1

    def check_bottom_right(self, r, c, k):
        return self.bottom_right[r-k+1][c+k-1] >= k

    def check_bottom_left(self, r, c, k):
        return self.bottom_left[r-k+1][c-k+1] >= k

    def find(self):
        answer = 0
        for r in range(1, self.R+1):
            for c in range(1, self.C+1):
                if self.grid[r-1][c-1] == '0':
                    continue

                max_k = min(self.bottom_right[r][c], self.bottom_left[r][c])
                for k in range(max_k, answer, -1):
                    if self.check_bottom_right(r, c, k) and self.check_bottom_left(r, c, k):
                        answer = k
                        break

        return answer


def main():
    R, C = map(int, input().split())
    grid = [
        list(input().rstrip())
        for _
        in range(R)
    ]

    diamond_mine = DiamondMine(R, C, grid)
    answer = diamond_mine.find()
    print(answer)


if __name__ == '__main__':
    main()
