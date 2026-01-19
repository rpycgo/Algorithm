import sys
import heapq


input = sys.stdin.readline


def main():
    max_heap = []
    min_heap = []
    problems = {}

    N = int(input())
    for _ in range(N):
        P, L = map(int, input().split())

        heapq.heappush(max_heap, (-L, -P))
        heapq.heappush(min_heap, (L, P))
        problems[P] = L

    M = int(input())
    for _ in range(M):
        command, *val = input().split()

        if command == 'add':
            P, L = val
            P, L = int(P), int(L)

            heapq.heappush(max_heap, (-L, -P))
            heapq.heappush(min_heap, (L, P))
            problems[P] = L
        elif command == 'recommend':
            category = int(val[0])

            if category == 1:
                while max_heap:
                    L, P = max_heap[0]
                    L, P = -L, -P

                    if P in problems and problems[P] == L:
                        print(P)
                        break

                    heapq.heappop(max_heap)
            elif category == -1:
                while min_heap:
                    L, P = min_heap[0]

                    if P in problems and problems[P] == L:
                        print(P)
                        break

                    heapq.heappop(min_heap)
        elif command == 'solved':
            P = int(val[0])

            if P in problems:
                del problems[P]


if __name__ == '__main__':
    main()
