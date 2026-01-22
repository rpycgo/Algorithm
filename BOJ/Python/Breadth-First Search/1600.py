import sys
from collections import deque


input = sys.stdin.readline


def main():
    mdx = (-1, 1, 0, 0)
    mdy = (0, 0, -1, 1)

    hdx = (-2, -1, 1, 2, 2, 1, -1, -2)
    hdy = (1, 2, 2, 1, -1, -2, -2, -1)

    K = int(input())
    W, H = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _
        in range(H)
    ]

    visited = [
        [
            [False] * (K + 1) for _ in range(W)
        ]
        for _ in range(H)
    ]
    visited[0][0][0] = True

    queue = deque([(0, 0, 0, 0)])
    while queue:
        curr_x, curr_y, cnt, dist = queue.popleft()

        if curr_x == H-1 and curr_y == W-1:
            print(dist)
            return

        for i in range(4):
            mnx = curr_x + mdx[i]
            mny = curr_y + mdy[i]

            if 0 <= mnx < H and 0 <= mny < W:
                if grid[mnx][mny] == 0 and not visited[mnx][mny][cnt]:
                    visited[mnx][mny][cnt] = True
                    queue.append((mnx, mny, cnt, dist+1))

        if cnt < K:
            for i in range(8):
                hnx = curr_x + hdx[i]
                hny = curr_y + hdy[i]

                if 0 <= hnx < H and 0 <= hny < W:
                    if not visited[hnx][hny][cnt+1] and grid[hnx][hny] == 0:
                        visited[hnx][hny][cnt+1] = True
                        queue.append((hnx, hny, cnt+1, dist+1))

    print(-1)


if __name__ == '__main__':
    main()
