import sys


input = sys.stdin.readline


def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(N):
        if dp[i] == float('inf'):
            continue

        jump_range = A[i]
        for step in range(1, jump_range+1):
            if i + step < N:
                dp[i+step] = min(dp[i+step], dp[i]+1)

    answer = dp[N-1] if dp[N-1] != float('inf') else -1
    print(answer)


if __name__ == '__main__':
    main()
