import sys
from bisect import bisect_right


def get_subset_sums(arr, limit):
    sums = [0]
    for x in arr:
        new_sums = []

        for sum in sums:
            if sum + x <= limit:
                new_sums.append(sum + x)
        sums.extend(new_sums)

    return sums


def main():
    input = sys.stdin.readline

    N, C = map(int, input().split())
    weights = list(map(int, input().split()))

    half_left = weights[:N//2]
    half_right = weights[N//2:]

    left_sums = get_subset_sums(half_left, C)
    right_sums = get_subset_sums(half_right, C)
    right_sums.sort()

    answer = 0
    for sum in left_sums:
        if sum <= C:
            idx = bisect_right(right_sums, C - sum)

            answer += idx

    print(answer)


if __name__ == '__main__':
    main()
