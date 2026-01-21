import sys


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        candidates = [
            tuple(map(int, input().split()))
            for _
            in range(N)
        ]

        candidates.sort()

        min_interview_score = candidates[0][1]
        max_n_candidates = 1

        for i in range(1, N):
            interview_score = candidates[i][1]

            if interview_score < min_interview_score:
                max_n_candidates += 1
                min_interview_score = interview_score

        print(max_n_candidates)


if __name__ == '__main__':
    main()
