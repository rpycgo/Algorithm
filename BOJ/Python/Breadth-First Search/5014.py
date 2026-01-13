import sys
from collections import deque


def main():
    input = sys.stdin.readline

    F, S, G, U, D = map(int, input().split())

    distances = [-1] * (F+1)

    queue = deque([S])
    distances[S] = 0

    while queue:
        curr_floor = queue.popleft()

        if curr_floor == G:
            print(distances[curr_floor])
            return

        for next_floor in (curr_floor+U, curr_floor-D):
            if 1 <= next_floor <= F and distances[next_floor] == -1:
                distances[next_floor] = distances[curr_floor] + 1
                queue.append(next_floor)

    print('use the stairs')


if __name__ == '__main__':
    main()
