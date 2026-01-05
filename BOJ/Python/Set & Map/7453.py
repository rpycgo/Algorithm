import sys
from collections import Counter


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

    count_CD = Counter(CD)

    answer = 0
    for target in AB:
        answer += count_CD.get(-target, 0)

    print(answer)


if __name__ == '__main__':
    main()
