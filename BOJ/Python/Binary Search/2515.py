import sys
from bisect import bisect_right


input = sys.stdin.readline


def main():
    N, S = map(int, input().split())
    items = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    items.sort()

    heights = [item[0] for item in items]
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        height, price = items[i-1]

        target_height = height - S
        idx = bisect_right(heights, target_height)

        dp[i] = max(dp[i-1], dp[idx] + price)

    answer = dp[N]
    print(answer)


if __name__ == '__main__':
    main()
