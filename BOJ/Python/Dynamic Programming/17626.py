import sys


def main():
    input = sys.stdin.readline

    n = int(input())

    dp = [0] * (n+1)
    dp[1] = 1

    squares = [i*i for i in range(1, int(n**0.5)+1)]
    for i in range(2, n+1):
        min_val = 4

        for square in squares:
            if i < square:
                break

            if dp[i-square] < min_val:
                min_val = dp[i-square]

        dp[i] = min_val + 1

    answer = dp[n]

    print(answer)


if __name__ == '__main__':
    main()
