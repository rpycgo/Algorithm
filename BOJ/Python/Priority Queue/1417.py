import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())

    if N == 1:
        print('0')
        return

    n_votes_dasom = int(input())

    heap = []
    for _ in range(N-1):
        n_votes = int(input())
        heapq.heappush(heap, -n_votes)

    n_buy_votes = 0
    while True:
        max_n_votes = -heapq.heappop(heap)

        if n_votes_dasom > max_n_votes:
            break

        n_buy_votes += 1
        n_votes_dasom += 1
        max_n_votes -= 1

        heapq.heappush(heap, -max_n_votes)

    print(n_buy_votes)


if __name__ == '__main__':
    main()
