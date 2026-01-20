import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class LevelHamburger:
    def __init__(self, N, X):
        self.N = N
        self.X = X

        self.length = [0] * (N + 1)
        self.patty = [0] * (N + 1)

        self.length[0] = 1
        self.patty[0] = 1

        for i in range(1, N + 1):
            self.length[i] = 1 + self.length[i-1] + 1 + self.length[i-1] + 1
            self.patty[i] = self.patty[i-1] + 1 + self.patty[i-1]


    def find_patty(self, n, x):
        if n == 0:
            return 1 if x > 0 else 0

        if x == 1:
            return 0

        elif x <= 1 + self.length[n-1]:
            return self.find_patty(n-1, x-1)

        elif x == 1 + self.length[n-1] + 1:
            return self.patty[n-1] + 1

        elif x <= 1 + self.length[n-1] + 1 + self.length[n-1]:
            return self.patty[n-1] + 1 + self.find_patty(n-1, x-1-self.length[n-1]-1)

        else:
            return self.patty[n]

    def run(self):
        answer = self.find_patty(self.N, self.X)
        print(answer)


if __name__ == '__main__':
    N, X = map(int, input().split())

    level_hamburger = LevelHamburger(N, X)
    level_hamburger.run()
