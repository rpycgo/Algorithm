import sys


input = sys.stdin.readline


def main():
    N = int(input())
    rgbs = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    total_min = float('inf')

    for start_color in range(3):
        dp = [[float('inf')] * 3 for _ in range(N)]

        dp[0][start_color] = rgbs[0][start_color]

        for i in range(1, N):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgbs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgbs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgbs[i][2]

        for last_color in range(3):
            if start_color == last_color:
                continue

            if dp[N-1][last_color] < total_min:
                total_min = dp[N-1][last_color]

    print(total_min)


if __name__ == '__main__':
    main()
