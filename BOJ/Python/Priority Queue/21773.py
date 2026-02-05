import sys
import heapq


input = sys.stdin.readline


def main():
    T, n = map(int, input().split())

    heap = []
    for _ in range(n):
        a, b, c = map(int, input().split())

        heapq.heappush(heap, (-c, a, b))

    i = 0
    while i < T:
        c, a, b = heapq.heappop(heap)

        print(a)

        c += 1

        b -= 1
        if b >= 1:
            heapq.heappush(heap, (c, a, b))

        i += 1


if __name__ == '__main__':
    main()
