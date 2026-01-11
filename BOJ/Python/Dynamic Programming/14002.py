import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j]+1)

    max_len = max(dp)

    result = []
    curr_len = max_len

    for i in range(N-1, -1, -1):
        if dp[i] == curr_len:
            result.append(A[i])
            curr_len -= 1


    answer = result[::-1]

    print(max_len)
    print(*answer)


if __name__ == '__main__':
    main()
