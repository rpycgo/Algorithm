import sys


def main():
    input = sys.stdin.readline

    x, y, c = map(float, input().split())

    left = 0
    right = min(x, y)

    while (right - left) > 1e-6:
        mid = (left+right) / 2

        h_x = (x**2 - mid**2) ** 0.5
        h_y = (y**2 - mid**2) ** 0.5

        c_star = (h_x * h_y) / (h_x + h_y)

        if c_star >= c:
            left = mid
        else:
            right = mid

    print(f'{left: .3f}')


if __name__ == '__main__':
    main()
