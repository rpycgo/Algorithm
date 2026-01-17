import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    heap = []

    for _ in range(N):
        row = map(int, input().split())

        for num in row:
            if len(heap) < N:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heappushpop(heap, num)

    print(heap[0])


if __name__ == '__main__':
    main()
