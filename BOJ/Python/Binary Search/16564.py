import sys


def calculate_total_max_level(target_level, levels):
    total_level = 0
    for level in levels:
        if level < target_level:
            total_level += (target_level - level)

    return total_level


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    levels = [int(input()) for _ in range(N)]

    left = min(levels)
    right = max(levels) + K

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_total_max_level(mid, levels) <= K:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
