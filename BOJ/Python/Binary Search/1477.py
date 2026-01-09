import sys


def calculate_required_rest_area(positions, distance):
    count = 0
    for x, y in zip(positions[:-1], positions[1:]):
        n_rest_area = (y-x-1) // distance
        count += n_rest_area

    return count


def main():
    input = sys.stdin.readline

    N, M, L = map(int, input().split())
    positions = [0] + list(map(int, input().split())) + [L]
    positions.sort()

    left = 1
    right = L - 1

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_required_rest_area(positions, mid) <= M:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
