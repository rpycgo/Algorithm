import sys
import heapq


input = sys.stdin.readline


def main():
    lines = input().split()

    T = int(lines[0])
    for _ in range(T):
        M = int(input())

        seq = []
        while len(seq) < M:
            seq.extend(map(int, input().split()))

        min_heap = []
        max_heap = []
        results = []

        for i, val in enumerate(seq, start=1):
            if len(max_heap) == len(min_heap):
                heapq.heappush(max_heap, -val)
            else:
                heapq.heappush(min_heap, val)

            if min_heap and (-max_heap[0] > min_heap[0]):
                max_val = -heapq.heappop(max_heap)
                min_val = heapq.heappop(min_heap)

                heapq.heappush(max_heap, -min_val)
                heapq.heappush(min_heap, max_val)

            if i%2 == 1:
                results.append(str(-max_heap[0]))


        mid = (M+1) // 2
        print(mid)

        for i in range(0, len(results), 10):
            print(' '.join(results[i:i+10]))


if __name__ == '__main__':
    main()
