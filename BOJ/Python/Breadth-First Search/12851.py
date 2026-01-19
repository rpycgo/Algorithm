import sys
from collections import deque


input = sys.stdin.readline


def main():
    MAX = 100_000

    N, K = map(int, input().split())

    dists = [-1] * (MAX+1)
    dists[N] = 0

    min_time = 0
    n_ways = 0

    queue = deque([N])
    while queue:
        curr_pos = queue.popleft()

        if curr_pos == K:
            min_time = dists[curr_pos]
            n_ways += 1
            continue

        for next_pos in (curr_pos-1, curr_pos+1, curr_pos*2):
            if 0 <= next_pos <= MAX:
                if (dists[next_pos] == -1) or (dists[next_pos] == dists[curr_pos]+1):
                    dists[next_pos] = dists[curr_pos] + 1
                    queue.append(next_pos)

    print(min_time)
    print(n_ways)


if __name__ == '__main__':
    main()
