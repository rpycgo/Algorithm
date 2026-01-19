import sys
import heapq


input = sys.stdin.readline


def main():
    n = int(input())
    data = [
        tuple(map(int, input().split()))
        for _
        in range(n)
    ]

    data.sort(key=lambda x: x[1])

    heap = []
    for p, d in data:
        heapq.heappush(heap, p)

        if len(heap) > d:
            heapq.heappop(heap)

    max_lecture_fee = sum(heap)
    print(max_lecture_fee)


if __name__ == '__main__':
    main()
