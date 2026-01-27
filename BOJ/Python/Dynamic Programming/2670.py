import sys


input = sys.stdin.readline


def main():
    N = int(input())
    nums = [float(input()) for _ in range(N)]

    dp = nums[:]
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i]*dp[i-1])

    answer = max(dp)
    print(f'{answer:.3f}')


if __name__ == '__main__':
    main()
