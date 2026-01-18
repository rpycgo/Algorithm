import sys


input = sys.stdin.readline


def cal_dist(t, ax, ay, bx, by, cx, cy, dx, dy):
    mx = ax + (bx - ax) * t
    my = ay + (by - ay) * t

    kx = cx + (dx - cx) * t
    ky = cy + (dy - cy) * t

    dist = ((mx - kx)**2 + (my - ky)**2) ** 0.5

    return dist


def main():
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())

    low = 0
    high = 1

    for _ in range(100):
        p1 = low + (high - low) / 3
        p2 = high - (high - low) / 3

        if cal_dist(p1, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy) > cal_dist(p2, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
            low = p1
        else:
            high = p2

    answer = cal_dist(low, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy)
    print(f'{answer:.10f}')


if __name__ == '__main__':
    main()
