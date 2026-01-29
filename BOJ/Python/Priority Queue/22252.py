import sys
import heapq
from collections import defaultdict


input = sys.stdin.readline


def main():
    Q = int(input())

    names = defaultdict(list)

    total_info_val = 0
    for _ in range(Q):
        cmd, k, n, *C = input().split()

        C = tuple(map(int, C))

        if cmd == '1':
            for c in C:
                heapq.heappush(names[k], -c)
        elif cmd == '2':
            n = int(n)

            if k in names:
                cnt = 0
                while names[k] and cnt < n:
                    info_val = -heapq.heappop(names[k])
                    total_info_val += info_val

                    cnt += 1

    print(total_info_val)



if __name__ == '__main__':
    main()
