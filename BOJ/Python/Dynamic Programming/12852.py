import sys


def main():
    input = sys.stdin.readline

    N = int(input())

    dp = [0] * (N+1)
    path = [0] * (N+1)

    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        path[i] = i - 1

        if i%2 == 0:
            if dp[i//2]+1 < dp[i]:
                dp[i] = dp[i//2] + 1
                path[i] = i // 2

        if i%3 == 0:
            if dp[i//3]+1 < dp[i]:
                dp[i] = dp[i//3] + 1
                path[i] = i // 3

    curr = N
    answer = []

    while curr != 0:
        answer.append(str(curr))
        curr = path[curr]

    print(dp[N])
    print(' '.join(answer))


if __name__ == '__main__':
    main()
