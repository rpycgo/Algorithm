import sys


def calculate_n_intervals(limit, numbers):
    count = 1
    min_val = numbers[0]
    max_val = numbers[0]

    for number in numbers[1:]:
        min_val = min(min_val, number)
        max_val = max(max_val, number)

        if max_val - min_val > limit:
            count += 1

            min_val = number
            max_val = number

    return count


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    left = 0
    right = max(numbers) - min(numbers)
    answer = right

    while left <= right:
        mid = (left+right) // 2

        if calculate_n_intervals(mid, numbers) <= M:
            answer = mid
            right = mid - 1
        else:
            left = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
