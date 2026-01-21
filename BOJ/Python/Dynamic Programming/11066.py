import sys


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        file_sizes = list(map(int, input().split()))

        pre_sum = [0] * (K+1)
        for i in range(K):
            pre_sum[i+1] = pre_sum[i] + file_sizes[i]

        dp = [[0] * K for _ in range(K)]

        for length in range(1, K):
            for i in range(K-length):
                j = i + length

                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + (pre_sum[j+1] - pre_sum[i])

                    if dp[i][j] > cost:
                        dp[i][j] = cost

        answer = dp[0][K-1]
        print(answer)


if __name__ == '__main__':
    main()
