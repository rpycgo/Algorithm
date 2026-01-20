import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class ThueMorseSequence:
    def __init__(self, k):
        self.k = k

    def find(self, k):
        if k == 0:
            return 0

        n = 1
        while n*2 <= k:
            n *= 2

        answer = 1 - self.find(k - n)

        return answer

    def run(self):
        answer = self.find(self.k)
        print(answer)


if __name__ == '__main__':
    k = int(input())
    thue_morse_sequence = ThueMorseSequence(k-1)
    thue_morse_sequence.run()
