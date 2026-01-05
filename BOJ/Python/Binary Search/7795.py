import sys
from bisect import bisect_right


def main():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        A.sort()

        answer = 0
        for num in B:
            idx = bisect_right(A, num)
            answer += (N - idx)

        print(answer)


if __name__ == '__main__':
    main()
