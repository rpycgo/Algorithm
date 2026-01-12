import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    coordinates = list(map(int, input().split()))

    coordinates.sort()

    for _ in range(M):
        start, end = map(int, input().split())

        idx_start = bisect_left(coordinates, start)
        idx_end = bisect_right(coordinates, end)

        answer = idx_end - idx_start

        print(answer)


if __name__ == '__main__':
    main()
