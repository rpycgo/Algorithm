import sys


input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    visitors = list(map(int, input().split()))

    prefix = [0] * (N + 1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + visitors[i-1]

    max_visitor = float('-inf')
    count = 0

    for i in range(X, N+1):
        visitor = prefix[i] - prefix[i-X]

        if visitor > max_visitor:
            max_visitor = visitor
            count = 1
        elif visitor == max_visitor:
            count += 1

    if max_visitor == 0:
        print('SAD')
        return

    print(max_visitor)
    print(count)


if __name__ == '__main__':
    main()
