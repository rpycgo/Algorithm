import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N = int(input())
    sequence = list(map(int, input().split()))

    longest_increasing_subsequence = []
    pos = [0] * N

    for i, num in enumerate(sequence):
        idx = bisect_left(longest_increasing_subsequence, num)

        if idx == len(longest_increasing_subsequence):
            longest_increasing_subsequence.append(num)
        else:
            longest_increasing_subsequence[idx] = num

        pos[i] = idx

    print(len(longest_increasing_subsequence))

    length = len(longest_increasing_subsequence) - 1
    answer = []

    for i in range(N-1, -1, -1):
        if pos[i] == length:
            answer.append(sequence[i])
            length -= 1

    answer.reverse()
    print(*answer)


if __name__ == '__main__':
    main()
