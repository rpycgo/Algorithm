import sys
from collections import defaultdict


input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    sums = defaultdict(int)
    sums[0] = 1

    curr_sum = 0
    answer = 0

    for num in A:
        curr_sum += num

        target = curr_sum - K
        if target in sums:
            answer += sums[target]

        sums[curr_sum] += 1

    print(answer)


if __name__ == '__main__':
    main()
