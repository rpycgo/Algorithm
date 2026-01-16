import sys


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    matrix = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    prefix = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + matrix[i-1][j-1]

    K = int(input())
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())

        answer = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
        print(answer)


if __name__ == '__main__':
    main()
