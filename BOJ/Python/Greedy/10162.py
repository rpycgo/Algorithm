import sys


input = sys.stdin.readline


def main():
    T = int(input())

    times = (300, 60, 10)
    cnts = [0, 0, 0]

    for i, time in enumerate(times):
        cnts[i] = T // time

        T %= time

    if T == 0:
        print(*cnts)
    else:
        print(-1)


if __name__ == '__main__':
    main()
