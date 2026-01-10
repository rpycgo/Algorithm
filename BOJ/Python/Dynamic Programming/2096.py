import sys


def main():
    input = sys.stdin.readline

    N = int(input())

    first_line = list(map(int, input().split()))

    max_dp = first_line.copy()
    min_dp = first_line.copy()

    for _ in range(N-1):
        current = list(map(int, input().split()))

        max_0 = current[0] + max(max_dp[0], max_dp[1])
        max_1 = current[1] + max(max_dp[0], max_dp[1], max_dp[2])
        max_2 = current[2] + max(max_dp[1], max_dp[2])
        max_dp = [max_0, max_1, max_2]

        min_0 = current[0] + min(min_dp[0], min_dp[1])
        min_1 = current[1] + min(min_dp[0], min_dp[1], min_dp[2])
        min_2 = current[2] + min(min_dp[1], min_dp[2])
        min_dp = [min_0, min_1, min_2]

    print(max(max_dp), min(min_dp))


if __name__ == '__main__':
    main()
