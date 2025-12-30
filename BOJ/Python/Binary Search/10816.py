import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline

    N = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    M = int(input())
    numbers_to_check = list(map(int, input().split()))

    answer = []
    for number_to_check in numbers_to_check:
        idx_left = bisect_left(cards, number_to_check)
        idx_right = bisect_right(cards, number_to_check)

        answer.append(idx_right - idx_left)

    print(*answer)


if __name__ == '__main__':
    main()
