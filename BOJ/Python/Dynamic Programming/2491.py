import sys


input = sys.stdin.readline


def main():
    N = int(input())
    sequences = tuple(map(int, input().split()))

    increasing_dp = [1] * N
    decreasing_dp = [1] * N

    for i in range(1, N):
        if sequences[i] >= sequences[i-1]:
            increasing_dp[i] = increasing_dp[i-1] + 1

        if sequences[i] <= sequences[i-1]:
            decreasing_dp[i] = decreasing_dp[i-1] + 1

    answer = max(max(increasing_dp), max(decreasing_dp))
    print(answer)


if __name__ == '__main__':
    main()
