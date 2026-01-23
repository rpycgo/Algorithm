import sys
import heapq


input = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    W, H = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(H)]

    lazer_coords = []
    for x in range(H):
        for y in range(W):
            if board[x][y] == 'C':
                lazer_coords.append((x, y))

    start, end = lazer_coords[0], lazer_coords[1]

    dists = [
        [
            [float('inf')] * W for _ in range(H)
        ] for _ in range(4)
    ]

    heap = []
    for i in range(4):
        nx = start[0] + dx[i]
        ny = start[1] + dy[i]

        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*':
            dists[i][nx][ny] = 0
            heapq.heappush(heap, (0, nx, ny, i))

    while heap:
        n_mirrors, curr_x, curr_y, curr_direction = heapq.heappop(heap)

        if dists[curr_direction][curr_x][curr_y] < n_mirrors:
            continue

        if curr_x == end[0] and curr_y == end[1]:
            print(n_mirrors)
            return

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*':
                new_n_mirrors = n_mirrors if curr_direction == i else n_mirrors+1

                if new_n_mirrors < dists[i][nx][ny]:
                    dists[i][nx][ny] = new_n_mirrors
                    heapq.heappush(heap, (new_n_mirrors, nx, ny, i))


if __name__ == '__main__':
    main()
