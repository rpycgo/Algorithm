import sys


input = sys.stdin.readline


def main():
    N = int(input())


    queue = []
    for _ in range(N):
        line = input().split()
        for ticket in line:
            alpha, num = ticket.split('-')
            queue.append((alpha, int(num)))

    target = sorted(queue)

    stack = []
    target_idx = 0

    for person in queue:
        stack.append(person)

        while stack and stack[-1] == target[target_idx]:
            stack.pop()
            target_idx += 1

    answer = 'GOOD' if not stack else 'BAD'
    print(answer)


if __name__ == '__main__':
    main()
