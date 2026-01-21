import sys


input = sys.stdin.readline


def flip(r, c, matrix):
    for i in range(r, r+3):
        for j in range(c, c+3):
            matrix[i][j] = 1 - matrix[i][j]


def main():
    N, M = map(int, input().split())
    matrix = list(
        list(map(int, list(input().rstrip())))
        for _
        in range(N)
    )
    target_matrix = list(
        list(map(int, list(input().rstrip())))
        for _
        in range(N)
    )

    cnt = 0
    for i in range(N-2):
        for j in range(M-2):
            if matrix[i][j] != target_matrix[i][j]:
                flip(i, j, matrix)
                cnt += 1

    answer = cnt if matrix == target_matrix else -1
    print(answer)


if __name__ == '__main__':
    main()
 