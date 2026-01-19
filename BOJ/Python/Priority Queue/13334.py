import sys
import heapq


input = sys.stdin.readline


def main():
    n = int(input())
    coords = [
        sorted(list(map(int, input().split())))
        for _
        in range(n)
    ]
    d = int(input())

    coords.sort(key=lambda x: x[1])

    max_overlap = float('-inf')
    heap = []

    for start, end in coords:
        if (end - start) <= d:
            heapq.heappush(heap, start)

        while heap and heap[0] < end - d:
            heapq.heappop(heap)

        if len(heap) > max_overlap:
            max_overlap = len(heap)

    print(max_overlap)


if __name__ == '__main__':
    main()
