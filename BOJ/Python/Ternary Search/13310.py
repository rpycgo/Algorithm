import sys


input = sys.stdin.readline


def calculate_dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def counter_clockwise(a, b, c):
    val = (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])

    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0


def calculate_max_dist(t, stars):
    points = []
    for x, y, vx, vy in stars:
        points.append((x + vx*t, y + vy*t))

    points.sort()
    if len(points) <= 2:
        return calculate_dist(points[0], points[-1])

    lower = []
    for p in points:
        while len(lower) >= 2 and counter_clockwise(lower[-2], lower[-1], p) <= 0:
            lower.pop()

        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and counter_clockwise(upper[-2], upper[-1], p) <= 0:
            upper.pop()

        upper.append(p)

    hull = lower[:-1] + upper[:-1]

    m = len(hull)
    if m == 2:
        return calculate_dist(hull[0], hull[1])

    max_dist = 0
    k = 1
    for i in range(m):
        while True:
            ni = (i+1) % m
            nk = (k+1) % m

            v1 = (hull[ni][0]-hull[i][0], hull[ni][1]-hull[i][1])
            v2 = (hull[nk][0]-hull[k][0], hull[nk][1]-hull[k][1])

            if (v1[0]*v2[1] - v1[1]*v2[0]) > 0:
                k = nk
            else:
                break

        curr_dist1 = calculate_dist(hull[i], hull[k])
        curr_dist2 = calculate_dist(hull[ni], hull[k])
        max_dist = max(max_dist, curr_dist1, curr_dist2)

    return max_dist


def main():
    N, T = map(int, input().split())
    coords = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    left, right = 0, T

    while right - left >= 3:
        p1 = (left*2 + right) // 3
        p2 = (left+right * 2) // 3

        if calculate_max_dist(p1, coords) <= calculate_max_dist(p2, coords):
            right = p2
        else:
            left = p1

    min_t = left
    min_dist = calculate_max_dist(left, coords)

    for t in range(max(0, left-5), min(T, right+5)+1):
        dist = calculate_max_dist(t, coords)

        if dist < min_dist:
            min_dist = dist
            min_t = t

    print(min_t)
    print(min_dist)


if __name__ == '__main__':
    main()
