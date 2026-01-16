import sys


class StarPainter:
    def __init__(self):
        input = sys.stdin.readline

        self.N = int(input())
        self.grid = [
            [' ' for _ in range(self.N)]
            for _
            in range(self.N)
        ]

    def draw_stars(self, x, y, n):
        if n == 1:
            self.grid[x][y] = '*'
            return

        next_size = n // 3
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    self.draw_stars(x+i*next_size, y+j*next_size, next_size)

    def run(self):
        self.draw_stars(0, 0, self.N)

        for row in self.grid:
            print(''.join(row))


if __name__ == '__main__':
    StarPainter().run()
