import sys
from bisect import bisect_left, bisect_right


def get_subset_sums(arr):
    sums = [0]
    for x in arr:
        new_sums = []

        for s in sums:
            new_sums.append(s + x)
        sums.extend(new_sums)

    return sums


def count_target(arr, target):
    return bisect_right(arr, target) - bisect_left(arr, target)


def main():
    input = sys.stdin.readline

    N, S = map(int, input().split())
    nums = list(map(int, input().split()))

    mid = N // 2
    left_side = nums[:mid]
    right_side = nums[mid:]

    left_sums = get_subset_sums(left_side)
    right_sums = get_subset_sums(right_side)
    right_sums.sort()

    answer = 0
    for left_sum in left_sums:
        target = S - left_sum
        answer += count_target(right_sums, target)

    if S == 0:
        answer -= 1

    print(answer)


if __name__ == '__main__':
    main()
