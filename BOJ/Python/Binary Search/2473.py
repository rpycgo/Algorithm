import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N = int(input())
    solutions = list(map(int, input().split()))
    solutions.sort()

    best = float('inf')
    answer = (0, 0, 0)

    for i in range(N-2):
        for j in range(i+1, N-1):
            target = -(solutions[i] + solutions[j])
            idx = bisect_left(solutions, target, j+1)

            if idx < N:
                total = solutions[i] + solutions[j] + solutions[idx]

                if abs(total) < best:
                    best = abs(total)
                    answer = (solutions[i], solutions[j], solutions[idx])

            if idx-1 > j:
                total = solutions[i] + solutions[j] + solutions[idx-1]

                if abs(total) < best:
                    best = abs(total)
                    answer = (solutions[i], solutions[j], solutions[idx-1])

    print(*answer)


if __name__ == '__main__':
    main()
