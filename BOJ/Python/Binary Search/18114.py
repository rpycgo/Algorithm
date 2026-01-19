import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    N, C = map(int, input().split())
    weights = list(map(int, input().split()))

    weights.sort()

    idx = bisect_left(weights, C)
    if idx < N and weights[idx] == C:
        print(1)
        return

    for i in range(N):
        target = C - weights[i]

        idx = bisect_left(weights, target, i+1)
        if idx < N and weights[idx] == target:
            print(1)
            return

    for i in range(N):
        if weights[i] > C:
            break

        for j in range(i+1, N):
            s = weights[i] + weights[j]
            if s >= C:
                break

            target = C - s
            if target > weights[j]:
                idx = bisect_left(weights, target, j+1)
                if idx < N and weights[idx] == target:
                    print(1)
                    return

    print(0)


if __name__ == '__main__':
    main()
