import sys
from collections import deque


input = sys.stdin.readline


def main():
    N = int(input())

    dq = deque()
    history = []

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == '1':
            dq.append(cmd[1])
            history.append(1)
        elif cmd[0] == '2':
            dq.appendleft(cmd[1])
            history.append(2)
        else:
            if history:
                last_operation = history.pop()

                if last_operation == 1:
                    dq.pop()
                else:
                    dq.popleft()

    answer = ''.join(dq) if dq else '0'
    print(answer)


if __name__ == '__main__':
    main()
