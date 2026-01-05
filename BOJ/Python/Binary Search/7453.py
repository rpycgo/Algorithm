import sys
from bisect import bisect_left, bisect_right


def main():
    input = sys.stdin.readline

    n = int(input())

    A = [0] * n
    B = [0] * n
    C = [0] * n
    D = [0] * n

    for i in range(n):
        a,b,c,d = map(int, input().split())
        A[i], B[i], C[i], D[i] = a,b,c,d

    AB = [a + b for a in A for b in B]
    CD = [c + d for c in C for d in D]

    CD.sort()

    answer = 0
    for ab_sum in AB:
        target = -ab_sum

        idx_left = bisect_left(CD, target)
        idx_right = bisect_right(CD, target)

        answer += (idx_right - idx_left)

    print(answer)


if __name__ == '__main__':
    main()
