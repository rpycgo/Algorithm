import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())

        left = 1
        right = N

        answer = right
        while left <= right:
            mid = (left + right) // 2

            if mid * (mid+1) // 2 <= N:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        print(answer)


if __name__ == '__main__':
    main()
