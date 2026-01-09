import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    while True:
        N, M = map(int, input().split())

        if N == 0 and M == 0:
            break

        CDs_sangguen = [int(input()) for _ in range(N)]
        CDs_sunyoung = [int(input()) for _ in range(M)]

        answer = 0
        for cd in CDs_sunyoung:
            idx = bisect_left(CDs_sangguen, cd)

            if idx < N and CDs_sangguen[idx] == cd:
                answer += 1

        print(answer)


if __name__ == '__main__':
    main()
