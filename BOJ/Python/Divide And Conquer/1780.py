import sys


class PaperCount:
    def __init__(self):
        input = sys.stdin.readline

        self.N = int(input())
        self.grid = [
            list(map(int, input().split()))
            for _
            in range(self.N)
        ]

        self.negative = 0
        self.zero = 0
        self.positive = 0

    def divide(self, x, y, n):
        number = self.grid[x][y]

        for i in range(x, x+n):
            for j in range(y, y+n):
                if number != self.grid[i][j]:
                    one_third = n // 3

                    for r in range(3):
                        for c in range(3):
                            self.divide(x + r*one_third, y + c*one_third, one_third)

                    return

        if self.grid[x][y] == -1:
            self.negative += 1
        elif self.grid[x][y] == 0:
            self.zero += 1
        elif self.grid[x][y] == 1:
            self.positive += 1

    def run(self):
        self.divide(0, 0, self.N)

        print(self.negative)
        print(self.zero)
        print(self.positive)


if __name__ == '__main__':
    PaperCount().run()
