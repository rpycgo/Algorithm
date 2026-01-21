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

        dp = [[0] * (K+1) for _ in range(K+1)]
        optimizations = [[0] * (K+1) for _ in range(K+1)]

        for i in range(1, K+1):
            optimizations[i][i] = i

        for length in range(1, K):
            for i in range(1, K-length+1):
                j = i + length

                dp[i][j] = float('inf')
                for k in range(optimizations[i][j-1], optimizations[i+1][j]+1):
                    if k < j:
                        cost = dp[i][k] + dp[k+1][j] + (pre_sum[j] - pre_sum[i-1])

                        if dp[i][j] > cost:
                            dp[i][j] = cost
                            optimizations[i][j] = k

        answer = dp[1][K]
        print(answer)


if __name__ == '__main__':
    main()
