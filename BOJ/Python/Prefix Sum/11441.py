import sys


input = sys.stdin.readline


def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    prefix = [0] * (N + 1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + A[i-1]

    M = int(input())
    for _ in range(M):
        i, j = map(int, input().split())

        result = prefix[j] - prefix[i-1]
        print(result)


if __name__ == '__main__':
    main()
