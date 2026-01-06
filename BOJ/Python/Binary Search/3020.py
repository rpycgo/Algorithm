import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N, H = map(int, input().split())

    stalagmites = []
    stalactites = []

    for i in range(N):
        size = int(input())
        if i%2 == 0:
            stalagmites.append(size)
        else:
            stalactites.append(size)

    stalagmites.sort()
    stalactites.sort()

    min_obstacles = N
    count = 0

    for i in range(1, H+1):
        idx_stalagmite = bisect_left(stalagmites, i)
        idx_stalactite = bisect_left(stalactites, H-i+1)

        obstacles = (len(stalagmites)-idx_stalagmite) + (len(stalactites)-idx_stalactite)

        if obstacles < min_obstacles:
            min_obstacles = obstacles
            count = 1
        elif obstacles == min_obstacles:
            count += 1

    print(min_obstacles, count)


if __name__ == '__main__':
    main()
