import sys


input = sys.stdin.readline


def main():
    n = int(input())
    sequences = tuple(map(int, input().split()))

    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = sequences[0]
    dp[0][1] = sequences[0]

    answer = sequences[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0]+sequences[i], sequences[i])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]+sequences[i])

        answer = max(answer, dp[i][0], dp[i][1])

    print(answer)


if __name__ == '__main__':
    main()
