import sys
import heapq


input = sys.stdin.readline


def main():
    N = int(input())

    lectures = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]
    lectures.sort(key=lambda x: x[1])

    queue = [lectures[0][2]]
    for i in range(1, N):
        _, start, end = lectures[i]

        if start >= queue[0]:
            heapq.heappop(queue)

        heapq.heappush(queue, end)

    answer = len(queue)
    print(answer)


if __name__ == '__main__':
    main()
    