import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    answer = 0
    for i in range(N):
        for j in range(i+1, N-1):
            target = -(A[i] + A[j])

            idx_left = bisect_left(A, target, j+1, N)

            if idx_left < N and A[idx_left] == target:
                idx_right = bisect_right(A, target, j+1, N)

                n_target = idx_right - idx_left
                answer += n_target

    print(answer)


if __name__ == '__main__':
    main()
