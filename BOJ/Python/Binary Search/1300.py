import sys


def main():
    def count_less_equal(x, n):
        cnt = 0
        for i in range(1, n+1):
            cnt += min(n, x // i)

        return cnt

    input = sys.stdin.readline

    N = int(input())
    k = int(input())

    left = 1
    right = N * N
    answer = 0

    while left <= right:
        mid = (left+right) // 2
        cnt = count_less_equal(mid, N)

        if cnt >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
