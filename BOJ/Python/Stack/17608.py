import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    heights = [int(input()) for _ in range(N)]

    max_val = float('-inf')

    result = []
    while heights:
        val = heights.pop()

        if val > max_val:
            max_val = val

            result.append(max_val)

    answer = len(result)

    print(answer)


if __name__ == '__main__':
    main()
