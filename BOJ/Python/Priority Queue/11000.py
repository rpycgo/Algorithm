import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    times = list(
        tuple(map(int, input().split()))
        for _
        in range(N)
    )

    times.sort()

    heap = []
    heapq.heappush(heap, times[0][1])

    for i in range(1, N):
        s, t = times[i]

        if heap[0] <= s:
            heapq.heappop(heap)

        heapq.heappush(heap, t)

    min_rooms = len(heap)
    print(min_rooms)


if __name__ == '__main__':
    main()
