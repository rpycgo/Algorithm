import sys


def main():
    input = sys.stdin.readline

    count = [0] * 10001

    n = int(input())
    for _ in range(n):
        num = int(input())
        count[num] += 1

    for i in range(1, 10001):
        if count[i] != 0:
            for _ in range(count[i]):
                print(i)


if __name__ == '__main__':
    main()
