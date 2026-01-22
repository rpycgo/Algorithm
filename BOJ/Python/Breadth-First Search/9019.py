import sys
from collections import deque


input = sys.stdin.readline


def main():
    cmds = ('D', 'S', 'L', 'R')

    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())

        parent = [-1] * 10000
        command = [''] * 10000

        queue = deque([(A)])
        while queue:
            curr_num = queue.popleft()

            if curr_num == B:
                break

            for cmd in cmds:
                if cmd == 'D':
                    new_num = (curr_num*2) % 10000
                elif cmd == 'S':
                    new_num = 9999 if curr_num == 0 else curr_num-1
                elif cmd == 'L':
                    new_num = (curr_num*10)%10000 + curr_num//1000
                elif cmd == 'R':
                    new_num = (curr_num%10)*1000 + curr_num//10

                if parent[new_num] == -1:
                    parent[new_num] = curr_num
                    command[new_num] = cmd
                    queue.append((new_num))

        path = []
        while curr_num != A:
            path.append(command[curr_num])
            curr_num = parent[curr_num]

        print(''.join(path[::-1]))


if __name__ == '__main__':
    main()
