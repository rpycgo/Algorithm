import sys


input = sys.stdin.readline


def get_paths(h, w):
    dp = [[1] * w for _ in range(h)]
    for i in range(1, h):
        for j in range(1, w):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[h-1][w-1]


def main():
    N, M, K = map(int, input().split())

    if K == 0:
        answer = get_paths(N, M)
        print(answer)
        return

    n_row, n_col = (K-1)//M, (K-1)%M

    path1 = get_paths(n_row+1, n_col+1)
    path2 = get_paths(N-n_row, M-n_col)

    answer = path1*path2
    print(answer)


if __name__ == '__main__':
    main()
