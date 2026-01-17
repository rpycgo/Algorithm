import sys


input = sys.stdin.readline


class Fractal:
    def __init__(self, s, N, K, R1, R2, C1, C2):
        self.s = s
        self.N = N
        self.K = K
        self.R1 = R1
        self.R2 = R2
        self.C1 = C1
        self.C2 = C2

        self.size = N ** s

    def divide(self, size, r, c):
        if size == 1:
            return 0

        unit = size // self.N

        start = unit * (self.N - self.K) // 2
        end = unit * (self.N + self.K) // 2

        if start <= r < end and start <= c < end:
            return 1

        return self.divide(unit, r%unit, c%unit)

    def run(self):
        for r in range(self.R1, self.R2+1):
            row = [self.divide(self.size, r, c) for c in range(C1, C2+1)]
            row = map(str, row)
            print(''.join(row))


if __name__ == '__main__':
    s, N, K, R1, R2, C1, C2 = map(int, input().split())

    if s == 0:
        print(0)
    else:
        fractal = Fractal(s, N, K, R1, R2, C1, C2)
        fractal.run()
