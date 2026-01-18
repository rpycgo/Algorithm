import sys


input = sys.stdin.readline


class Moo:
    def __init__(self, N):
        self.N = N

        self.length = 3
        self.k = 0
        while self.length < N:
            self.k += 1
            self.length = self.length*2 + (self.k + 3)

    def find(self, total_len, mid_len, n):
        if n <= 3:
            return 'm' if n == 1 else 'o'

        left_len = (total_len - mid_len) // 2

        if n <= left_len:
            return self.find(left_len, mid_len-1, n)
        elif n <= left_len + mid_len:
            return 'm' if n - left_len == 1 else 'o'
        else:
            return self.find(left_len, mid_len-1, n - (left_len+mid_len))

    def run(self):
        return self.find(self.length, self.k+3, self.N)


if __name__ == '__main__':
    N = int(input())

    moo = Moo(N)
    result = moo.run()

    print(result)
