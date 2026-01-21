import sys


input = sys.stdin.readline


def main():
    N = int(input())
    dates = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    dp = [0] * (N+2)
    for i in range(N, 0, -1):
        if i + dates[i-1][0] <= N+1:
            dp[i] = max(dp[i+1], dates[i-1][1] + dp[i + dates[i-1][0]])
        else:
            dp[i] = dp[i+1]

    print(dp[1])


if __name__ == '__main__':
    main()
