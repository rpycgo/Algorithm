import sys


input = sys.stdin.readline


def main():
    N, P = map(int, input().split())

    stacks = [[] for _ in range(7)]
    cnt = 0

    for _ in range(N):
        line_num, fret = map(int, input().split())
        curr_stack = stacks[line_num]

        while curr_stack and (curr_stack[-1] > fret):
            curr_stack.pop()
            cnt += 1

        if curr_stack and curr_stack[-1] == fret:
            continue

        curr_stack.append(fret)
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
