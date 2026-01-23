import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = list(map(int, input().split()))

        X.sort()

        cnt = 0
        for i in range(N-2):
            for j in range(i+1, N-1):
                diff = X[j] - X[i]
                target = X[j] + diff

                idx = bisect_left(X, target)
                if idx < N and X[idx] == target:
                    cnt += 1

        print(cnt)


if __name__ == '__main__':
    main()
