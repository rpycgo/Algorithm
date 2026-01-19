import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    assignments = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    assignments.sort()

    heap = []
    for d, w in assignments:
        heapq.heappush(heap, w)

        if len(heap) > d:
            heapq.heappop(heap)

    total_score = sum(heap)
    print(total_score)



if __name__ == '__main__':
    main()
