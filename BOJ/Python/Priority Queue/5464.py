import sys
import heapq
from collections import deque


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    Rs = [int(input()) for _ in range(N)]
    Wk = [int(input()) for _ in range(M)]

    empty_slots = []
    for i in range(N):
        heapq.heappush(empty_slots, i)

    waiting_queue = deque()
    car_pos = {}

    revenue = 0

    for _ in range(2*M):
        car_idx = int(input())

        if car_idx > 0:
            if empty_slots:
                idx_slot = heapq.heappop(empty_slots)
                car_pos[car_idx] = idx_slot
            else:
                waiting_queue.append(car_idx)
        else:
            car_idx = abs(car_idx)
            slot = car_pos[car_idx]

            revenue += (Rs[slot] * Wk[car_idx-1])

            del car_pos[car_idx]

            if waiting_queue:
                next_car = waiting_queue.popleft()
                car_pos[next_car] = slot
            else:
                heapq.heappush(empty_slots, slot)

    print(revenue)


if __name__ == '__main__':
    main()
