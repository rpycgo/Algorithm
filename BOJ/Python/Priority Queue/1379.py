import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())

    times = []
    for _ in range(N):
        lecture_num, start, end = map(int, input().split())
        times.append((start, end, lecture_num))

    times.sort()

    heap_for_end = []
    available_rooms = []
    results = [0] * (N+1)
    room_cnt = 0

    for start, end, lecture_num in times:
        while heap_for_end and heap_for_end[0][0] <= start:
            _, room_idx = heapq.heappop(heap_for_end)
            heapq.heappush(available_rooms, room_idx)

        if not available_rooms:
            room_cnt += 1
            target_room = room_cnt
        else:
            target_room = heapq.heappop(available_rooms)

        results[lecture_num] = target_room
        heapq.heappush(heap_for_end, (end, target_room))

    print(room_cnt)
    for i in range(1, N+1):
        print(results[i])


if __name__ == '__main__':
    main()
