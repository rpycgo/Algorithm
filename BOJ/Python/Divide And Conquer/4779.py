import sys


input = sys.stdin.readline


class CountourSet:
    def __init__(self, N):
        self.size = 3 ** N

        self.grid = [' ' for _ in range(self.size)]

    def draw_line(self, x, n):
        if n == 1:
            self.grid[x] = '-'
            return

        next_size = n // 3
        for i in range(3):
            if not i == 1:
                self.draw_line(x + i*next_size, next_size)

    def run(self):
        self.draw_line(0, self.size)

        print(''.join(self.grid))


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.strip()

        if line:
            N = int(line)
            CountourSet(N).run()
