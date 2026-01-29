import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    times = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    times.sort()

    using_rooms = []
    empty_rooms = []

    room_cnt = 0
    usage_stats = []

    for start, end in times:
        while using_rooms and using_rooms[0][0] <= start:
            _, room_idx = heapq.heappop(using_rooms)
            heapq.heappush(empty_rooms, room_idx)

        if not empty_rooms:
            target_room = room_cnt
            usage_stats.append(1)
            room_cnt += 1
        else:
            target_room = heapq.heappop(empty_rooms)
            usage_stats[target_room] += 1

        heapq.heappush(using_rooms, (end, target_room))

    print(room_cnt)
    print(*usage_stats)


if __name__ == '__main__':
    main()
