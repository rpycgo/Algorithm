import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    times = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    times.sort(key=lambda x: x[0])

    heap = [times[0][1]]
    for i in range(1, N):
        start, end = times[i]

        if start >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    answer = len(heap)
    print(answer)


if __name__ == '__main__':
    main()
