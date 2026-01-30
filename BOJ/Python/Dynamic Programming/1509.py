import sys


input = sys.stdin.readline


def main():
    string = input().rstrip()

    n = len(string)

    string = ' ' + string

    is_palindrom = [[False] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        is_palindrom[i][i] = True

    for i in range(1, n):
        if string[i] == string[i+1]:
            is_palindrom[i][i+1] = True

    for length in range(3, n+1):
        for start in range(1, n-length+2):
            end = start + length - 1

            if string[start] == string[end] and is_palindrom[start+1][end-1]:
                is_palindrom[start][end] = True

    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for i in range(1, n+1):
        for j in range(1, i+1):
            if is_palindrom[j][i]:
                dp[i] = min(dp[i], dp[j-1]+1)

    print(dp[n])


if __name__ == '__main__':
    main()
