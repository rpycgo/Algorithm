import sys


input = sys.stdin.readline


def main():
    N = int(input())

    events = []
    for i in range(N):
       x, r = map(int, input().split())

       events.append((x-r, i, 0))
       events.append((x+r, i, 1))

    events.sort()

    for i in range(len(events)-1):
        if events[i][0] == events[i+1][0]:
            print('NO')
            return

    stack = []
    for pos, circle_id, type in events:
        if type == 0:
            stack.append(circle_id)
        else:
            if stack and stack[-1] == circle_id:
                stack.pop()
            else:
                print('NO')
                return

    print('YES')


if __name__ == '__main__':
    main()
   