import sys
import heapq


input = sys.stdin.readline


def main():
    n = int(input())

    heap = []
    for _ in range(n):
        a = tuple(map(int, input().split()))

        if a[0] == 0:
            if not heap:
                print(-1)
            else:
                val = -heapq.heappop(heap)
                print(val)
        else:
            for i in range(1, len(a)):
                heapq.heappush(heap, -a[i])


if __name__ == '__main__':
    main()
