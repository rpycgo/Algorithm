import sys
import heapq


input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    heapq.heapify(A)

    cnt = 0
    while cnt < m:
        num1 = heapq.heappop(A)
        num2 = heapq.heappop(A)

        combined = num1 + num2
        heapq.heappush(A, combined)
        heapq.heappush(A, combined)

        cnt += 1

    min_score = sum(A)
    print(min_score)


if __name__ == '__main__':
    main()
