import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    S.sort()

    answer = 0
    for _ in range(M):
        query = input().strip()

        idx = bisect_left(S, query)

        if idx < N and S[idx].startswith(query):
            answer += 1

    print(answer)


if __name__ == '__main__':
    main()
