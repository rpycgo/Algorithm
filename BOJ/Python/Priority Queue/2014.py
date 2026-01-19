import sys
import heapq


input = sys.stdin.readline


def main():
    K, N = map(int, input().split())
    primes = list(map(int, input().split()))

    heap = primes[:]
    heapq.heapify(heap)

    for i in range(N):
        curr_num = heapq.heappop(heap)

        if i == N-1:
            print(curr_num)
            break

        for prime in primes:
            new_num = curr_num * prime
            heapq.heappush(heap, new_num)

            if curr_num%prime == 0:
                break


if __name__ == '__main__':
    main()
