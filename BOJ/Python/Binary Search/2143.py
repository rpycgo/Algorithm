import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline

    T = int(input())
    n = int(input())
    sequence1 = list(map(int, input().split()))
    m = int(input())
    sequence2 = list(map(int, input().split()))

    prefix_sequence1 = [0] * (n+1)
    for i, num in enumerate(sequence1, start=1):
        prefix_sequence1[i] = prefix_sequence1[i-1] + num

    prefix_sequence2 = [0] * (m+1)
    for i, num in enumerate(sequence2, start=1):
        prefix_sequence2[i] = prefix_sequence2[i-1] + num

    subarray_sums1 = []
    for i in range(n):
        for j in range(i+1, n+1):
            subarray_sums1.append(prefix_sequence1[j] - prefix_sequence1[i])

    subarray_sum2 = []
    for i in range(m):
        for j in range(i+1, m+1):
            subarray_sum2.append(prefix_sequence2[j] - prefix_sequence2[i])

    subarray_sum2.sort()

    answer = 0
    for subarray_sum in subarray_sums1:
        target = T - subarray_sum

        left_index = bisect_left(subarray_sum2, target)
        right_index = bisect_right(subarray_sum2, target)

        answer += (right_index - left_index)

    print(answer)


if __name__ == '__main__':
    main()
