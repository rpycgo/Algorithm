import sys
import heapq


input = sys.stdin.readline


def main():
    C, N = map(int, input().split())
    T = sorted([int(input()) for _ in range(C)])
    cows = sorted([
        tuple(map(int, input().split()))
        for _
        in range(N)
    ])

    heap = []
    cow_idx = 0
    n_helped = 0

    for t in T:
        while cow_idx < N and cows[cow_idx][0] <= t:
            heapq.heappush(heap, cows[cow_idx][1])
            cow_idx += 1

        while heap and heap[0] < t:
            heapq.heappop(heap)

        if heap:
            heapq.heappop(heap)
            n_helped += 1

    print(n_helped)


if __name__ == '__main__':
    main()
