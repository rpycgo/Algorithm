import sys


class Z:
    def __init__(self):
        input = sys.stdin.readline

        self.N, self.r, self.c = map(int, input().split())

        self.answer = 0

    def calculate_tour(self, x, y, n):
        if n == 1:
            return

        half = n // 2

        if self.r < x+half and self.c < y+half:
            self.calculate_tour(x, y, half)
        elif self.r < x+half and self.c >= y+half:
            self.answer += half*half
            self.calculate_tour(x, y+half, half)
        elif self.r >= x+half and self.c < y+half:
            self.answer += (half*half) * 2
            self.calculate_tour(x+half, y, half)
        else:
            self.answer += (half*half) * 3
            self.calculate_tour(x+half, y+half, half)


    def run(self):
        self.calculate_tour(0, 0, 2**self.N)

        print(self.answer)


if __name__ == '__main__':
    Z().run()
