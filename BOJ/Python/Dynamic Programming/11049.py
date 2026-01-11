import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    dims = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    dp = [[0]*N for _ in range(N)]

    for term in range(1, N):
        for start in range(N-term):
            end = start + term
            dp[start][end] = float('inf')

            for mid in range(start, end):
                cost = dp[start][mid] + dp[mid+1][end] + \
                     (dims[start][0] * dims[mid][1] * dims[end][1])

                if cost < dp[start][end]:
                    dp[start][end] = cost

    print(dp[0][N-1])


if __name__ == '__main__':
    main()
