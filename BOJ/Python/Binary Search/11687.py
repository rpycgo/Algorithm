import sys


input = sys.stdin.readline


def calculate_n_fives(num):
    cnt = 0
    while num >= 5:
        cnt += (num // 5)
        num //= 5

    return cnt


def main():
    M = int(input())

    left = 1
    right = 5 * M

    answer = -1
    while left <= right:
        mid = (left + right) // 2

        n_zeros = calculate_n_fives(mid)
        if n_zeros >= M:
            if n_zeros == M:
                answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
