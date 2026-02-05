import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    curr_max = max(A)
    init_max = curr_max

    heap = []
    for a in A:
        heapq.heappush(heap, a)

    answer = curr_max - heap[0]
    while heap:
        curr_min = heapq.heappop(heap)

        answer = min(answer, curr_max-curr_min)

        if init_max < curr_min:
            break

        next_val = 2 * curr_min
        heapq.heappush(heap, next_val)

        if curr_max < next_val:
            curr_max = next_val

    print(answer)


if __name__ == '__main__':
    main()
