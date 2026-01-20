import sys


input = sys.stdin.readline


def calculate_dist(interval, coords):
    total_dist = 0
    for i, coord in enumerate(coords):
        total_dist += abs(interval*i - coord)

    return total_dist


def main():
    N = int(input())
    x_coords = list(map(int, input().split()))

    left = 0
    right = x_coords[-1]

    while right-left >= 3:
        p1 = left + (right-left) // 3
        p2 = right - (right-left) // 3

        if calculate_dist(p1, x_coords) < calculate_dist(p2, x_coords):
            right = p2
        else:
            left = p1

    min_n_switch = float('inf')
    for i in range(left, right+1):
        min_n_switch = min(min_n_switch, calculate_dist(i, x_coords))

    print(min_n_switch)


if __name__ == '__main__':
    main()
