import heapq
import sys


def solution(N: int):
    input = sys.stdin.readline

    min_heap = []
    max_heap = []
    answer = []

    for i in range(N):
        temp = int(input())

        if i%2 == 0:
            heapq.heappush(max_heap, -temp)
        else:
            heapq.heappush(min_heap, temp)

        if all([max_heap, min_heap]) and -max_heap[0] > min_heap[0]:
            value_of_max_heap = -heapq.heappop(max_heap)
            value_of_min_heap = heapq.heappop(min_heap)

            heapq.heappush(max_heap, -value_of_min_heap)
            heapq.heappush(min_heap, value_of_max_heap)

        answer.append(-max_heap[0])

    for item in answer:
        print(item)


if __name__ == '__main__':
    N = int(input())

    solution(N)
