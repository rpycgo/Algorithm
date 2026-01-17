import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())

    if N == 1:
        print(0)
        return

    heap = []
    for _ in range(N):
        amount = int(input())
        heapq.heappush(heap, amount)


    total = 0
    while len(heap) >= 2:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)

        sum_val = num1 + num2
        total += sum_val

        heapq.heappush(heap, sum_val)

    print(total)


if __name__ == '__main__':
    main()
