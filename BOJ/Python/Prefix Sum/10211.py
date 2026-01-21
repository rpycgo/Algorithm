import sys


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = tuple(map(int, input().split()))

        prefix_sum = 0
        min_prefix_sum = 0
        max_subarray_sum = float('-inf')

        for num in nums:
            prefix_sum += num
            max_subarray_sum = max(max_subarray_sum, prefix_sum-min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        print(max_subarray_sum)


if __name__ == '__main__':
    main()
