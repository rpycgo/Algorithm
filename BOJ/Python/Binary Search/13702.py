import sys


def calculate_n_people(standard, capacities):
    count = 0
    for capacity in capacities:
        count += (capacity // standard)

    return count


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    capacities = [int(input()) for _ in range(N)]

    left = 1
    right = max(capacities)

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_n_people(mid, capacities) >= K:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
