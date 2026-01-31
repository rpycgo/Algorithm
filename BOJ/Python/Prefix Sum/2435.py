import sys


input = sys.stdin.readline


def main():
    N, K = map(int, sys.stdin.readline().split())
    temps = tuple(map(int, sys.stdin.readline().split()))

    prefix_sum = [0] * (N+1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + temps[i]

    max_sum = float('-inf')
    for i in range(N-K+1):
        current_sum = prefix_sum[i + K] - prefix_sum[i]

        max_sum = max(max_sum, current_sum)

    print(max_sum)


if __name__ == '__main__':
    main()
