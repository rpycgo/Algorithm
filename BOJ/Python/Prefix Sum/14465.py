import sys


input = sys.stdin.readline


def main():
    N, K, B = map(int, input().split())

    broken_light_nums = [int(input()) for _ in range(B)]

    broken_lights = [0] * (N+1)
    for broken_light_num in broken_light_nums:
        broken_lights[broken_light_num] = 1

    prefix_sums = [0] * (N+1)
    for i in range(1, N+1):
        prefix_sums[i] = prefix_sums[i-1] + broken_lights[i]

    min_repairs = float('inf')
    for i in range(1, N-K+2):
        curr_broken = prefix_sums[i+K-1] - prefix_sums[i-1]

        min_repairs = min(min_repairs, curr_broken)

    print(min_repairs)


if __name__ == '__main__':
    main()
