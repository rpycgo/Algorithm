import sys


def multiply(A, B, N):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += (A[i][k] * B[k][j])
            result[i][j] %= 1000

    return result


def power(A, B, N):
    if B == 1:
        for r in range(N):
            for c in range(N):
                A[r][c] %= 1000

        return A

    temp = power(A, B//2, N)
    if B%2 == 0:
        return multiply(temp, temp, N)
    else:
        square = multiply(temp, temp, N)

        return multiply(square, A, N)


def main():
    input = sys.stdin.readline

    N, B = map(int, input().split())
    matrix = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    answer = power(matrix, B, N)

    for row in answer:
        print(*row)


if __name__ == '__main__':
    main()
