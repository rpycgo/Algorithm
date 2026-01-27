import sys
from collections import deque


input = sys.stdin.readline



def main():
    max_capacities = tuple(map(int, input().split()))

    visited = [[False] * 201 for _ in range(201)]
    visited[0][0] = True

    answer = []

    queue = deque([(0, 0, max_capacities[-1])])
    while queue:
        curr_a, curr_b, curr_c = queue.popleft()

        if curr_a == 0:
            answer.append(curr_c)

        cases = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        for next_src, next_tgt in cases:
            next_amount = [curr_a, curr_b, curr_c]

            amount = min(next_amount[next_src], max_capacities[next_tgt]-next_amount[next_tgt])
            next_amount[next_src] -= amount
            next_amount[next_tgt] += amount

            if not visited[next_amount[1]][next_amount[0]]:
                visited[next_amount[1]][next_amount[0]] = True
                queue.append(next_amount)

    answer = sorted(set(answer))
    print(*answer)


if __name__ == '__main__':
    main()
