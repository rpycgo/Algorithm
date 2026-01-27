import sys
import heapq


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    presents = list(map(int, input().split()))
    children = tuple(map(int, input().split()))

    presents = [-n_present for n_present in presents]
    heapq.heapify(presents)

    for n_wishes in children:
        n_presents = -heapq.heappop(presents)

        if n_presents >= n_wishes:
            remaining = n_presents - n_wishes

            if remaining > 0:
                heapq.heappush(presents, -remaining)
        else:
            print(0)
            return

    print(1)


if __name__ == '__main__':
    main()
