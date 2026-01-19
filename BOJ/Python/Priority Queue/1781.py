import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    data = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    data.sort()

    heap = []
    for deadline, n_cup_ramens in data:
        heapq.heappush(heap, n_cup_ramens)

        if len(heap) > deadline:
            heapq.heappop(heap)

    max_cup_ramens = sum(heap)
    print(max_cup_ramens)


if __name__ == '__main__':
    main()
