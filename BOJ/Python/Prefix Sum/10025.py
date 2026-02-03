import sys


input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    ices = [0] * (1_000_001)
    for _ in range(N):
        g, x = map(int, input().split())
        ices[x] = g

    prefix_sums = [0] * (1_000_002)
    for i in range(1_000_001):
        prefix_sums[i+1] = prefix_sums[i] + ices[i]

    max_ice = float('-inf')
    for i in range(1_000_001):
        start = max(0, i-K)
        end = min(1_000_000, i+K)

        curr_sum = prefix_sums[end+1] - prefix_sums[start]
        max_ice = max(max_ice, curr_sum)

    print(max_ice)


if __name__ == '__main__':
    main()
