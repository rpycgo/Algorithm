import sys
import heapq


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    times = list(map(int, input().split()))

    times.sort(reverse=True)

    outlets = []
    for i in range(min(N, M)):
        heapq.heappush(outlets, times[i])

    for i in range(M, N):
        finished = heapq.heappop(outlets)
        heapq.heappush(outlets, finished+times[i])

    answer = max(outlets) if outlets else 0
    print(answer)


if __name__ == '__main__':
    main()
