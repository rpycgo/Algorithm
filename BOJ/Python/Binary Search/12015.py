import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N = int(input())
    sequence = list(map(int, input().split()))

    answer = []
    for num in sequence:
        idx = bisect_left(answer, num)

        if idx == len(answer):
            answer.append(num)
        else:
            answer[idx] = num

    answer = len(answer)

    print(answer)


if __name__ == '__main__':
    main()
