import sys
import heapq


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        operators = [tuple(input().split()) for _ in range(k)]

        min_heap = []
        max_heap = []
        visited = [False] * k

        for i, (operator, val) in enumerate(operators):
            val = int(val)

            if operator == 'I':
                heapq.heappush(min_heap, (val, i))
                heapq.heappush(max_heap, (-val, i))

                visited[i] = True
            elif operator == 'D':
                if val == 1:
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)

                    if max_heap:
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                elif val == -1:
                    while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)

                    if min_heap:
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)

        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)

        if not min_heap or not max_heap:
            print('EMPTY')
        else:
            max_val = -max_heap[0][0]
            min_val = min_heap[0][0]

            print(max_val, min_val)


if __name__ == '__main__':
    main()
