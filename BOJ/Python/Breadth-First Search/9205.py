import sys
from collections import deque


input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        coords = [
            list(map(int, input().split()))
            for _
            in range(n+2)
        ]

        visited = [False] * (n+2)
        visited[0] = False

        answer = 'sad'

        queue = deque([0])
        while queue:
            curr_idx = queue.popleft()
            curr_x, curr_y = coords[curr_idx]

            if curr_idx == n+1:
                answer = 'happy'
                break

            for new_idx in range(n+2):
                if not visited[new_idx]:
                    nx, ny = coords[new_idx]
                    dist = abs(curr_x - nx) + abs(curr_y - ny)

                    if dist <= 1000:
                        visited[new_idx] = True
                        queue.append(new_idx)

        print(answer)


if __name__ == '__main__':
    main()
