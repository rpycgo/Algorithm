from collections import deque


def main():
    N, K = map(int, input().split())

    MAX = 100_001
    visited = [0] * MAX

    queue = deque([N])

    while queue:
        current = queue.popleft()

        if current == K:
            print(visited[current])
            return

        for next_pos in (current-1, current+1, current*2):
            if 0 <= next_pos < MAX and not visited[next_pos]:
                visited[next_pos] = visited[current] + 1

                queue.append(next_pos)


if __name__ == '__main__':
    main()
