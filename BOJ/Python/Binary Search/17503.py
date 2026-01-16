import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())
    items = [
        list(map(int, input().split()))
        for _
        in range(K)
    ]

    left = 1
    right = max((c for _, c in items))
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        available_v = [v for v, c in items if c <= mid]

        if len(available_v) < N:
            left = mid + 1
            continue

        available_v.sort(reverse=True)

        if sum(available_v[:N]) >= M:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
