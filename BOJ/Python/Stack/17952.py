import sys


input = sys.stdin.readline


def main():
    stack = []
    total_score = 0

    N = int(input())
    for _ in range(N):
        row = tuple(map(int, input().split()))

        if row[0] == 1:
            score, T = row[1:]
            T -= 1

            if T == 0:
                total_score += score
            else:
                stack.append((score, T))

        else:
            if stack:
                score, T = stack.pop()
                T -= 1

                if T == 0:
                    total_score += score
                else:
                    stack.append((score, T))

    print(total_score)


if __name__ == '__main__':
    main()
