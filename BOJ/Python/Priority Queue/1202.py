import sys
import heapq


input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    jewels = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]
    jewels.sort()

    bags = [int(input()) for _ in range(K)]
    bags.sort()

    total_value = 0
    candidates_jewels = []

    i = 0
    for bag_cap in bags:
        while i < N and jewels[i][0] <= bag_cap:
            heapq.heappush(candidates_jewels, -jewels[i][1])
            i += 1

        if candidates_jewels:
            total_value -= heapq.heappop(candidates_jewels)

    print(total_value)


if __name__ == '__main__':
    main()
