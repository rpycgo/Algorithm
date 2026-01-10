import sys
from collections import deque


def bfs(M, N, H, matrix, queue):
    dh = [1, -1, 0, 0, 0, 0]
    dn = [0, 0, 1, -1, 0, 0]
    dm = [0, 0, 0, 0, 1, -1]

    days = -1

    while queue:
        days += 1

        for _ in range(len(queue)):
            ch, cn, cm = queue.popleft()

            for i in range(6):
                nh = ch + dh[i]
                nn = cn + dn[i]
                nm = cm + dm[i]

                if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                    if matrix[nh][nn][nm] == 0:
                        matrix[nh][nn][nm] = 1
                        queue.append((nh, nn, nm))

    return days


def main():
    input = sys.stdin.readline

    M, N, H = map(int, input().split())

    queue = deque()
    tomatoes = []

    for h in range(H):
        layer = []

        for n in range(N):
            row = list(map(int, input().split()))

            for m in range(M):
                if row[m] == 1:
                    queue.append((h, n, m))

            layer.append(row)
        tomatoes.append(layer)

    answer = bfs(M, N, H, tomatoes, queue)

    for h in range(H):
        for n in range(N):
            if 0 in tomatoes[h][n]:
                print(-1)
                return

    print(answer)


if __name__ == '__main__':
    main()
