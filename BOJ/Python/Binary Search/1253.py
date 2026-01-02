import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    sequence = list(map(int, input().split()))
    sequence.sort()

    answer = 0
    for i in range(N):
        target = sequence[i]
        left = 0
        right = N - 1

        while left < right:
            if left == i:
                left += 1
                continue

            if right == i:
                right -= 1
                continue

            sum_ = sequence[left] + sequence[right]

            if sum_ == target:
                answer += 1
                break
            elif sum_ < target:
                left += 1
            else:
                right -= 1

    print(answer)


if __name__ == '__main__':
    main()
