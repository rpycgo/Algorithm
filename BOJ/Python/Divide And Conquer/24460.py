import sys


class SpecialPrize:
    def __init__(self, N, grid):
        self.N = N
        self.grid = grid

    def find(self, r, c, n):
        if n == 1:
            return self.grid[r][c]

        half = n // 2
        candidates = []

        candidates.append(self.find(r, c, half))
        candidates.append(self.find(r, c+half, half))
        candidates.append(self.find(r+half, c, half))
        candidates.append(self.find(r+half, c+half, half))

        candidates.sort()

        return candidates[1]

    def run(self):
        answer = self.find(0, 0, self.N)
        print(answer)


if __name__ == '__main__':
    N = int(input())
    numbers = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    special_prize = SpecialPrize(N, numbers)
    special_prize.run()
