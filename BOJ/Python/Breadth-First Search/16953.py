import sys
from collections import deque


def main():
    A, B = map(int, input().split())

    queue = deque([(A, 1)])

    while queue:
        curr, cnt = queue.popleft()

        if curr == B:
            print(cnt)
            return

        next_val_1 = curr * 2
        if next_val_1 <= B:
            queue.append((next_val_1, cnt+1))

        next_val_2 = curr*10 + 1
        if next_val_2 <= B:
            queue.append((next_val_2, cnt+1))

    print(-1)


if __name__ == '__main__':
    main()
