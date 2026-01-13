import sys


class Origami:
    def __init__(self):
        input = sys.stdin.readline

        self.N = int(input())
        self.grid = [
            list(map(int, input().split()))
            for _
            in range(self.N)
        ]

        self.white = 0
        self.blue = 0

    def divide(self, x, y, n):
        color = self.grid[x][y]

        for i in range(x, x+n):
            for j in range(y, y+n):
                if self.grid[i][j] != color:
                    half = n //2

                    self.divide(x, y, half)
                    self.divide(x, y+half, half)
                    self.divide(x+half, y, half)
                    self.divide(x+half, y+half, half)

                    return

        if color == 0:
            self.white += 1
        else:
            self.blue += 1

    def run(self):
        self.divide(0, 0, self.N)

        print(self.white)
        print(self.blue)


if __name__ == '__main__':
    origami = Origami().run()
