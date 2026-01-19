import sys
import heapq


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        pages = list(map(int, input().split()))

        heapq.heapify(pages)

        total_cost = 0
        while len(pages) > 1:
            page1 = heapq.heappop(pages)
            page2 = heapq.heappop(pages)

            cost = page1 + page2
            total_cost += cost

            heapq.heappush(pages, cost)

        print(total_cost)


if __name__ == '__main__':
    main()
