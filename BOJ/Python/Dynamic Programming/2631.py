import sys


input = sys.stdin.readline


def main():
    N = int(input())
    orders = [int(input()) for _ in range(N)]

    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if orders[j] < orders[i]:
                dp[i] = max(dp[i], dp[j]+1)

    answer = N - max(dp)
    print(answer)


if __name__ == '__main__':
    main()
