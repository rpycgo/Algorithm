import sys


input = sys.stdin.readline


class Origami:
    def __init__(self, string):
        self.string = string

    def can_fold(self, paper):
        if len(paper) == 1:
            return True

        mid = len(paper) // 2
        for i in range(mid):
            if paper[i] == paper[len(paper)-1-i]:
                return False

        return self.can_fold(paper[:mid])

    def run(self):
        if self.can_fold(self.string):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        info = input().rstrip()

        origami = Origami(info)
        origami.run()
