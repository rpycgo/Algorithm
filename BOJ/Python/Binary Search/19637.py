import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    titles = []
    standards = []
    for _ in range(N):
        title, standard = input().split()
        standard = int(standard)

        titles.append(title)
        standards.append(standard)

    for _ in range(M):
        power = int(input())

        idx = bisect_left(standards, power)

        print(titles[idx])


if __name__ == '__main__':
    main()
