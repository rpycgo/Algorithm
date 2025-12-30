import sys


def main():
    input = sys.stdin.readline

    X, Y = map(int, input().split())
    current_rate = (Y * 100) // X

    if current_rate >= 99:
        print(-1)
        return

    left = 1
    right = 1_000_000_000
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        new_rate = ((Y + mid) * 100) // (X + mid)

        if new_rate > current_rate:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
