import sys


input = sys.stdin.readline


def main():
    n, k = map(int, input().split())

    row = [1]
    for _ in range(n-1):
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]

    print(row[k-1])


if __name__ == '__main__':
    main()
