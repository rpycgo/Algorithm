import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    numbers = list(map(int, input().split()))
    M = int(input())
    questions = [
        list(map(int, input().split()))
        for _
        in range(M)
    ]

    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1

    for i in range(N-1):
        if numbers[i] == numbers[i+1]:
            dp[i][i+1] = 1

    for term in range(2, N):
        for start in range(N-term):
            end = start + term

            if numbers[start] == numbers[end] and dp[start+1][end-1] == 1:
                dp[start][end] = 1

    for question in questions:
        S, E = question

        print(dp[S-1][E-1])


if __name__ == '__main__':
    main()
