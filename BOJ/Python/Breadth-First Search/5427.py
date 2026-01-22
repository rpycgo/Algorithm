import sys
from collections import deque


input = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        grid = [list(input().rstrip()) for _ in range(h)]

        fire_dist = [[float('inf')] * w for _ in range(h)]
        person_dist = [[-1] * w for _ in range(h)]

        fire_queue = deque()
        person_queue = deque()

        for x in range(h):
            for y in range(w):
                if grid[x][y] == '*':
                    fire_queue.append((x, y))
                    fire_dist[x][y] = 0
                elif grid[x][y] == '@':
                    person_queue.append((x, y))
                    person_dist[x][y] = 0

        while fire_queue:
            curr_x, curr_y = fire_queue.popleft()

            for i in range(4):
                nx = curr_x + dx[i]
                ny = curr_y + dy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if grid[nx][ny] != '#' and fire_dist[nx][ny] == float('inf'):
                        fire_dist[nx][ny] = fire_dist[curr_x][curr_y] + 1
                        fire_queue.append((nx, ny))

        answer = 'IMPOSSIBLE'
        is_found = False
        while person_queue:
            curr_x, curr_y = person_queue.popleft()

            for i in range(4):
                nx = curr_x + dx[i]
                ny = curr_y + dy[i]

                if not (0 <= nx < h and 0 <= ny < w):
                    answer = person_dist[curr_x][curr_y] + 1
                    is_found = True
                    break

                if grid[nx][ny] == '.' and person_dist[nx][ny] == -1:
                    if person_dist[curr_x][curr_y] + 1 < fire_dist[nx][ny]:
                        person_dist[nx][ny] = person_dist[curr_x][curr_y] + 1
                        person_queue.append((nx, ny))

            if is_found:
                break

        print(answer)


if __name__ == '__main__':
    main()
