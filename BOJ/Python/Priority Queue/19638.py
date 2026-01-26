import sys
import heapq


input = sys.stdin.readline


def main():
    N, H, T = map(int, input().split())

    heap = []
    for _ in range(N):
        height = int(input())
        heapq.heappush(heap, -height)

    cnt = 0
    for _ in range(T):
        max_height = -heap[0]

        if max_height < H or max_height == 1:
            break

        max_height = -heapq.heappop(heap)
        heapq.heappush(heap, -(max_height//2))

        cnt += 1

    max_height = -heap[0]
    if max_height < H:
        print('YES')
        print(cnt)
    else:
        print('NO')
        print(max_height)


if __name__ == '__main__':
    main()
