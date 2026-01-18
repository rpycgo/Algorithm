import sys
import math


input = sys.stdin.readline


def cal_dist(t, ax, ay, az, bx, by, bz, cx, cy, cz):
    x = ax + (bx - ax)*t
    y = ay + (by - ay)*t
    z = az + (bz - az)*t

    dist = math.sqrt((x - cx)**2 + (y - cy)**2 + (z - cz)**2)

    return dist


def main():
    Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())

    low = 0
    high = 1

    for _ in range(100):
        p1 = low + (high - low)/3
        p2 = high - (high - low)/3

        if cal_dist(p1, Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz) > cal_dist(p2, Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
            low = p1
        else:
            high = p2

    answer = cal_dist(low, Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz)
    print(f'{answer:.10f}')


if __name__ == '__main__':
    main()
