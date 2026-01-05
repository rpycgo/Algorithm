import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    longest_increasing_subsequence = []
    for num in A:
        idx = bisect_left(longest_increasing_subsequence, num)

        if idx == len(longest_increasing_subsequence):
            longest_increasing_subsequence.append(num)
        else:
            longest_increasing_subsequence[idx] = num

    answer = len(longest_increasing_subsequence)

    print(answer)


if __name__ == '__main__':
    main()
