import sys


class Pooling:
    def __init__(self):
        input = sys.stdin.readline

        self.N = int(input())
        self.grid = [
            list(map(int, input().split()))
            for _
            in range(self.N)
        ]

        self.answer = 0

    def pool(self, x, y, n):
        if n == 2:
            candidates = [
                self.grid[x][y], self.grid[x][y+1],
                self.grid[x+1][y], self.grid[x+1][y+1],
            ]
            candidates.sort()

            return candidates[2]

        half = n // 2

        top_left = self.pool(x, y, half)
        top_right = self.pool(x, y+half, half)
        bottom_left = self.pool(x+half, y, half)
        bottom_right = self.pool(x+half, y+half, half)

        final_candidates= [top_left, top_right, bottom_left, bottom_right]
        final_candidates.sort()

        return final_candidates[2]


    def run(self):
        answer = self.pool(0, 0, self.N)

        print(answer)


if __name__ == '__main__':
    Pooling().run()
