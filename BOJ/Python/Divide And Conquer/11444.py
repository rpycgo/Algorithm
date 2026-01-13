import sys


def multiply_matrix(A, B, MOD=1_000_000_007):
    matrix = [
        [0, 0],
        [0, 0],
    ]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix[i][j] += A[i][k] * B[k][j]
            matrix[i][j] %= MOD

    return matrix


def power_matrix(matrix, n):
    if n == 1:
        return matrix

    half = power_matrix(matrix, n // 2)
    square = multiply_matrix(half, half)

    if n % 2 == 0:
        return square
    else:
        return multiply_matrix(square, matrix)


def main():
    input = sys.stdin.readline

    n = int(input())

    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return

    base = [
        [1, 1],
        [1, 0],
    ]

    result = power_matrix(base, n)
    answer = result[0][1]

    print(answer)

    
if __name__ == '__main__':
    main()
