import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())
    stations = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]
    L, P = map(int, input().split())

    stations.sort()

    heap = []
    cnt = 0
    idx = 0
    curr_fuel = P

    while curr_fuel < L:
        while idx < N and stations[idx][0] <= curr_fuel:
            heapq.heappush(heap, -stations[idx][1])
            idx += 1

        if not heap:
            print(-1)
            return

        curr_fuel += -heapq.heappop(heap)
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
