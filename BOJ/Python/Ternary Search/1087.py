import sys


input = sys.stdin.readline


def calculate_dist(time, data):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')

    for px, py, vx, vy in data:
        curr_x = px + vx*time
        curr_y = py + vy*time

        if curr_x < min_x:
            min_x = curr_x
        if curr_y < min_y:
            min_y = curr_y

        if curr_x > max_x:
            max_x = curr_x
        if curr_y > max_y:
            max_y = curr_y

    return max(max_x-min_x, max_y-min_y)


def main():
    N = int(input())
    data = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    left = 0
    right = 2000

    for _ in range(200):
        p1 = left + (right-left) / 3
        p2 = right - (right-left) / 3

        if calculate_dist(p1, data) < calculate_dist(p2, data):
            right = p2
        else:
            left = p1

    answer = calculate_dist(left, data)
    print(f'{answer:.10f}')


if __name__ == '__main__':
    main()
