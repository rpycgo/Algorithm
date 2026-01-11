import sys


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    candies = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    for j in range(1, M):
        candies[0][j] += candies[0][j-1]
    for i in range(1, N):
        candies[i][0] += candies[i-1][0]

    for i in range(1, N):
        for j in range(1, M):
            candies[i][j] += max(candies[i-1][j], candies[i][j-1], candies[i-1][j-1])

    answer = candies[N-1][M-1]

    print(answer)


if __name__ == '__main__':
    main()
