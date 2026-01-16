import sys


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    count = 0
    curr_prefix_sum = 0

    prefix_sums = {0: 1}

    for num in A:
        curr_prefix_sum += num

        target = curr_prefix_sum - M
        if target in prefix_sums:
            count += prefix_sums[target]

        prefix_sums[curr_prefix_sum] = prefix_sums.get(curr_prefix_sum, 0) + 1

    print(count)


if __name__ == '__main__':
    main()
