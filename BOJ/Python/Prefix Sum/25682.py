import sys


input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())
    board = [
        tuple(input().rstrip())
        for _
        in range(N)
    ]

    start_color = 'W'
    diff = [[0] * (M+1) for _ in range(N+1)]

    for r in range(N):
        for c in range(M):
            if (r+c)%2 == 0:
                expected = start_color
            else:
                expected = 'B' if start_color == 'W' else 'W'

            if board[r][c] != expected:
                diff[r+1][c+1] = 1

    prefix_sums = [[0] * (M+1) for _ in range(N+1)]
    for r in range(1, N+1):
        for c in range(1, M+1):
            prefix_sums[r][c] = (
                diff[r][c]
                + prefix_sums[r-1][c]
                + prefix_sums[r][c-1]
                - prefix_sums[r-1][c-1]
            )

    min_cnt = K * K
    for r in range(K, N+1):
        for c in range(K, M+1):
            cnt = (
                prefix_sums[r][c]
                - prefix_sums[r-K][c]
                - prefix_sums[r][c-K]
                + prefix_sums[r-K][c-K]
            )
            min_cnt = min(min_cnt, cnt, K*K - cnt)

    print(min_cnt)


if __name__ == '__main__':
    main()
