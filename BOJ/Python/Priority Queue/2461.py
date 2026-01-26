import sys
import heapq


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    students = [
        sorted(list(map(int, input().split())))
        for _
        in range(N)
    ]

    heap = []
    curr_max = 0

    for i in range(N):
        val = students[i][0]
        heapq.heappush(heap, (val, i, 0))
        curr_max = max(curr_max, val)

    answer = float('inf')
    while heap:
        min_val, idx_class, idx_student = heapq.heappop(heap)

        answer = min(answer, curr_max-min_val)

        if idx_student+1 < M:
            next_val = students[idx_class][idx_student+1]
            heapq.heappush(heap, (next_val, idx_class, idx_student+1))
            curr_max = max(curr_max, next_val)
        else:
            break

    print(answer)


if __name__ == '__main__':
    main()
