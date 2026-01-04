import sys


def main():
    input = sys.stdin.readline
    N, S = map(int, input().split())
    sequence = list(map(int, input().split()))

    prefix_sum = [0] * (N+1)
    for i in range(1, N+1):
        prefix_sum[i] = prefix_sum[i-1] + sequence[i-1]

    min_length = N + 1
    start = 0
    end = 1

    while start < end and end <= N:
        current_sum = prefix_sum[end] - prefix_sum[start]

        if current_sum >= S:
            min_length = min(min_length, end-start)
            start += 1
        else:
            end += 1

    if min_length == N+1:
        print(0)
    else:
        print(min_length)


if __name__ == '__main__':
    main()
