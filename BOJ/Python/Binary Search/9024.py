import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        n, K = map(int, input().split())
        S = list(map(int, input().split()))

        S.sort()

        min_diff = float('inf')
        answer = 0

        for i, num in enumerate(S):
            target = K - num

            idx = bisect_left(S, target, i+1)

            for j in (idx-1, idx):
                if j <= i or j >= n:
                    continue

                curr_sum = num + S[j]
                curr_diff = abs(K - curr_sum)

                if curr_diff < min_diff:
                    min_diff = curr_diff
                    answer = 1
                elif curr_diff == min_diff:
                    answer += 1

        print(answer)


if __name__ == '__main__':
    main()
