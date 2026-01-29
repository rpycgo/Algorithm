import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())

    coords = []
    for _ in range(N):
        L, H ,R = map(int, input().split())

        coords.append((L, -H, R))
        coords.append((R, 0, 0))

    coords.sort()

    max_heap = [(0, float('inf'))]
    results = []
    max_h = 0

    for L, H, R in coords:
        if H < 0:
            heapq.heappush(max_heap, (H, R))

        while max_heap[0][1] <= L:
            heapq.heappop(max_heap)

        curr_max_h = -max_heap[0][0]

        if max_h !=  curr_max_h:
            results.append((L, curr_max_h))
            max_h = curr_max_h

    for L, H in results:
        print(f'{L} {H}', end=' ')


if __name__ == '__main__':
    main()
