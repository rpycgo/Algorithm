import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    n = int(input())
    port_nums = list(map(int, input().split()))

    longest_increasing_subsequence = []
    for port_num in port_nums:
        idx = bisect_left(longest_increasing_subsequence, port_num)

        if not longest_increasing_subsequence or idx == len(longest_increasing_subsequence):
            longest_increasing_subsequence.append(port_num)
        else:
            longest_increasing_subsequence[idx] = port_num

    answer = len(longest_increasing_subsequence)

    print(answer)


if __name__ == '__main__':
    main()
