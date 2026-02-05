import sys
import heapq


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    
    heap = []
    for i in range(M):
        heapq.heappush(heap, (-B[i], A[i]))

    total_score = sum(A)

    T = 24 * N
    while T > 0 and heap:
        b, a = heapq.heappop(heap)
        b = -b

        needed_score = 100 - a
        study_time = needed_score // b

        if study_time > 0:
            actual_study = min(study_time, T)
            total_score += actual_study*b
            T -= actual_study
            a += actual_study * b

        if a < 100 and T > 0:
            new_b = 100 - a
            heapq.heappush(heap, (-new_b, a))

    print(total_score)


if __name__ == '__main__':
    main()
