import sys


def main():
    def can_divide(durations, M, max_durations):
        count = 1
        current_sum = 0

        for duration in durations:
            if current_sum + duration <= max_durations:
                current_sum += duration
            else:
                count += 1
                current_sum = duration

                if count > M:
                    return False

        return True

    input = sys.stdin.readline

    N, M = map(int, input().split())
    durations = list(map(int, input().split()))

    left = max(durations)
    right = sum(durations)
    answer = right

    while left <= right:
        mid = (left+right) // 2

        if can_divide(durations, M, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
