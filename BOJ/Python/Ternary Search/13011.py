import sys


input = sys.stdin.readline


def calculate_cost(d, n, C, W):
    total_cost = 0
    for i in range(n):
        actual_w = C[i] * d
        total_cost += abs(W[i] - actual_w)

    return total_cost


def main():
    N = int(input())
    C = tuple(map(int, input().split()))
    W = tuple(map(int, input().split()))

    left = 0
    right = 1_000_000

    for _ in range(200):
        m1 = (left*2 + right) / 3
        m2 = (left + right*2) / 3

        if calculate_cost(m1, N, C, W) < calculate_cost(m2, N, C, W):
            right = m2
        else:
            left = m1

    answer = calculate_cost(left, N, C, W)
    print(f'{answer:.10f}')


if __name__ == '__main__':
    main()
