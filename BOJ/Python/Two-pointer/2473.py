import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    solutions = list(map(int, input().split()))
    solutions.sort()

    answer = (0, 0, 0)
    best = float('inf')

    for i in range(N-2):
        left = i+1
        right = N-1

        while left < right:
            total = solutions[i] + solutions[left] + solutions[right]

            if abs(total) < best:
                best = abs(total)
                answer = (solutions[i], solutions[left], solutions[right])

            if total < 0:
                left += 1
            else:
                right -= 1

    print(*answer)


if __name__ == '__main__':
    main()
