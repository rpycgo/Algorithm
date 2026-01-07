import sys


def calculate_total_people(total_time, times):
    total_people = 0
    for time in times:
        total_people += total_time // time

    return total_people


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    times = [int(input()) for _ in range(N)]

    left = 1
    right = max(times) * M

    answer = right
    while left <= right:
        mid = (left+right) // 2

        total_people = calculate_total_people(mid, times)
        if total_people >= M:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
