import sys
import heapq


input = sys.stdin.readline


def main():
    N, k = map(int, input().split())

    checkout_heap = []
    for i in range(1, k+1):
        heapq.heappush(checkout_heap, (0, i))

    completed = []
    for _ in range(N):
        customer_id, w = map(int, input().split())
        end_time, counter_id = heapq.heappop(checkout_heap)
        new_end_time = end_time + w

        completed.append((new_end_time, counter_id, customer_id))
        heapq.heappush(checkout_heap, (new_end_time, counter_id))

    completed.sort(key=lambda x: (x[0], -x[1]))

    total_sum = 0
    for i in range(N):
        total_sum += (i+1) * completed[i][2]

    print(total_sum)


if __name__ == '__main__':
    main()
