import sys


class QuadTree:
    def __init__(self):
        input = sys.stdin.readline

        self.N = int(input())
        self.video = [
            list(map(int, list(input().rstrip())))
            for _
            in range(self.N)
        ]

    def compress(self, x, y, n):
        color = self.video[x][y]

        for i in range(x, x+n):
            for j in range(y, y+n):
                if self.video[i][j] != color:
                    print('(', end='')

                    half = n // 2

                    self.compress(x, y, half)
                    self.compress(x, y+half, half)
                    self.compress(x+half, y, half)
                    self.compress(x+half, y+half, half)

                    print(')', end='')

                    return

        print(color, end='')

    def run(self):
        self.compress(0, 0, self.N)


if __name__ == '__main__':
    origami = QuadTree().run()
